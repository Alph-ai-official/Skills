#!/usr/bin/env python3
"""
Alph.ai 交易脚本 - 支持买入和卖出

用法：
  python trade.py buy --chain bsc --contract 0x360a... --amount 0.001 --cookie <dex_cookie>
  python trade.py sell --chain bsc --contract 0x360a... --coin 黑马 --amount 16710 --cookie <dex_cookie>

也可以设置环境变量 DEX_COOKIE 代替 --cookie 参数：
  export DEX_COOKIE="你的dex_cookie"
  python trade.py buy --chain sol --contract <addr> --amount 0.1
"""

import argparse
import json
import os
import sys
import time
import uuid

try:
    import requests
except ImportError:
    print("需要安装 requests: pip install requests")
    sys.exit(1)

BASE_URL = "https://b.alph.ai/smart-web-gateway"

NATIVE_COINS = {
    "sol": ("sol", "SOL"),
    "bsc": ("bnb", "BNB"),
    "eth": ("eth", "ETH"),
}

EXPLORERS = {
    "bsc": "https://bscscan.com/tx/",
    "eth": "https://etherscan.io/tx/",
    "sol": "https://solscan.io/tx/",
}


def make_headers(cookie):
    return {
        "Cookie": f"dex_cookie={cookie}",
        "Content-Type": "application/json;charset=UTF-8",
    }


def create_order(cookie, chain, side, buy_coin, buy_contract, sell_coin, sell_contract, volume, slippage=0.275, priority_fee=0.2, anti_mev=True):
    """创建订单"""
    order = {
        "chain": chain,
        "side": side,
        "type": "MARKET",
        "buyCoin": buy_coin,
        "buyContract": buy_contract,
        "sellCoin": sell_coin,
        "sellContract": sell_contract,
        "volume": str(volume),
        "slippage": slippage,
        "priorityFee": priority_fee,
        "antiMev": anti_mev,
        "sniper": False,
        "source": "api",
        "clientOrderId": f"cli-{int(time.time() * 1000)}-{uuid.uuid4().hex[:8]}",
        "waitTime": 10,
    }

    resp = requests.post(
        f"{BASE_URL}/order/create",
        headers=make_headers(cookie),
        json=order,
        timeout=30,
    )
    return resp.json()


def buy(args):
    """执行买入"""
    chain = args.chain
    if chain not in NATIVE_COINS:
        print(f"不支持的链: {chain}，支持: {', '.join(NATIVE_COINS.keys())}")
        sys.exit(1)

    sell_coin, sell_contract = NATIVE_COINS[chain]
    coin_name = args.coin or "TOKEN"

    print(f"\n即将执行买入：")
    print(f"  链：{chain.upper()}")
    print(f"  买入：{coin_name}（{args.contract}）")
    print(f"  花费：{args.amount} {sell_coin.upper()}")
    print(f"  滑点：{args.slippage * 100}%")
    print(f"  防夹子：{'开启' if args.anti_mev else '关闭'}")

    if not args.yes:
        confirm = input("\n确认下单？(y/n): ").strip().lower()
        if confirm != "y":
            print("已取消")
            return

    print("\n下单中...")
    result = create_order(
        cookie=args.cookie,
        chain=chain,
        side="BUY",
        buy_coin=coin_name,
        buy_contract=args.contract,
        sell_coin=sell_coin,
        sell_contract=sell_contract,
        volume=args.amount,
        slippage=args.slippage,
        priority_fee=args.priority_fee,
        anti_mev=args.anti_mev,
    )

    if result.get("code") == "200" and result.get("data", {}).get("success"):
        vo = result["data"]["orderVo"]
        explorer = EXPLORERS.get(chain, "")
        print(f"\n买入成功！")
        print(f"  订单ID：{result['data']['orderId']}")
        print(f"  买入：{vo['buyVolume']} {vo['buyCoin']}")
        print(f"  花费：{vo['sellVolume']} {vo['sellCoin']}")
        print(f"  成交价：{vo['price']}")
        print(f"  Gas 费：{vo['gasFee']} {vo['gasFeeCoin']}")
        print(f"  手续费：{vo['platformFee']}（{vo['platformFeeRate'] * 100}%）")
        print(f"  交易哈希：{vo['hash']}")
        if explorer:
            print(f"  查看交易：{explorer}{vo['hash']}")
    else:
        print(f"\n买入失败")
        print(f"  返回：{json.dumps(result, ensure_ascii=False, indent=2)}")
        sys.exit(1)


def sell(args):
    """执行卖出"""
    chain = args.chain
    if chain not in NATIVE_COINS:
        print(f"不支持的链: {chain}，支持: {', '.join(NATIVE_COINS.keys())}")
        sys.exit(1)

    buy_coin, buy_contract = NATIVE_COINS[chain]
    coin_name = args.coin or "TOKEN"

    print(f"\n即将执行卖出：")
    print(f"  链：{chain.upper()}")
    print(f"  卖出：{args.amount} {coin_name}（{args.contract}）")
    print(f"  换回：{buy_coin.upper()}")
    print(f"  滑点：{args.slippage * 100}%")
    print(f"  防夹子：{'开启' if args.anti_mev else '关闭'}")

    if not args.yes:
        confirm = input("\n确认下单？(y/n): ").strip().lower()
        if confirm != "y":
            print("已取消")
            return

    print("\n下单中...")
    result = create_order(
        cookie=args.cookie,
        chain=chain,
        side="SELL",
        buy_coin=buy_coin,
        buy_contract=buy_contract,
        sell_coin=coin_name,
        sell_contract=args.contract,
        volume=args.amount,
        slippage=args.slippage,
        priority_fee=args.priority_fee,
        anti_mev=args.anti_mev,
    )

    if result.get("code") == "200" and result.get("data", {}).get("success"):
        vo = result["data"]["orderVo"]
        explorer = EXPLORERS.get(chain, "")
        print(f"\n卖出成功！")
        print(f"  订单ID：{result['data']['orderId']}")
        print(f"  卖出：{vo['sellVolume']} {vo['sellCoin']}")
        print(f"  获得：{vo['buyVolume']} {vo['buyCoin']}")
        print(f"  成交价：{vo['price']}")
        print(f"  Gas 费：{vo['gasFee']} {vo['gasFeeCoin']}")
        print(f"  手续费：{vo['platformFee']}（{vo['platformFeeRate'] * 100}%）")
        print(f"  交易哈希：{vo['hash']}")
        if explorer:
            print(f"  查看交易：{explorer}{vo['hash']}")
    else:
        print(f"\n卖出失败")
        print(f"  返回：{json.dumps(result, ensure_ascii=False, indent=2)}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Alph.ai 交易工具")
    parser.add_argument(
        "--cookie",
        default=os.environ.get("DEX_COOKIE", ""),
        help="dex_cookie 值（也可通过 DEX_COOKIE 环境变量设置）",
    )
    subparsers = parser.add_subparsers(dest="action", help="操作类型")

    # buy 子命令
    buy_parser = subparsers.add_parser("buy", help="买入代币")
    buy_parser.add_argument("--chain", required=True, choices=["sol", "bsc", "eth"], help="链")
    buy_parser.add_argument("--contract", required=True, help="代币合约地址")
    buy_parser.add_argument("--amount", required=True, type=float, help="花费主链币数量")
    buy_parser.add_argument("--coin", default="", help="代币名称（可选）")
    buy_parser.add_argument("--slippage", type=float, default=0.275, help="滑点（默认 0.275 = 27.5%%）")
    buy_parser.add_argument("--priority-fee", type=float, default=0.2, help="优先费（默认 0.2）")
    buy_parser.add_argument("--anti-mev", action="store_true", default=True, help="开启防夹子（默认开启）")
    buy_parser.add_argument("--no-anti-mev", dest="anti_mev", action="store_false", help="关闭防夹子")
    buy_parser.add_argument("-y", "--yes", action="store_true", help="跳过确认")

    # sell 子命令
    sell_parser = subparsers.add_parser("sell", help="卖出代币")
    sell_parser.add_argument("--chain", required=True, choices=["sol", "bsc", "eth"], help="链")
    sell_parser.add_argument("--contract", required=True, help="代币合约地址")
    sell_parser.add_argument("--amount", required=True, type=float, help="卖出代币数量")
    sell_parser.add_argument("--coin", default="", help="代币名称（可选）")
    sell_parser.add_argument("--slippage", type=float, default=0.275, help="滑点（默认 0.275 = 27.5%%）")
    sell_parser.add_argument("--priority-fee", type=float, default=0.2, help="优先费（默认 0.2）")
    sell_parser.add_argument("--anti-mev", action="store_true", default=True, help="开启防夹子（默认开启）")
    sell_parser.add_argument("--no-anti-mev", dest="anti_mev", action="store_false", help="关闭防夹子")
    sell_parser.add_argument("-y", "--yes", action="store_true", help="跳过确认")

    args = parser.parse_args()

    if not args.action:
        parser.print_help()
        sys.exit(1)

    if not args.cookie:
        print("错误：需要提供 dex_cookie")
        print("  方式 1：--cookie <值>")
        print("  方式 2：export DEX_COOKIE=<值>")
        sys.exit(1)

    if args.action == "buy":
        buy(args)
    elif args.action == "sell":
        sell(args)


if __name__ == "__main__":
    main()
