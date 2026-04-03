---
name: alphai-websocket
description: Alph.ai WebSocket 实时推送 - 统一推送通道，覆盖行情（K线/Ticker）、交易（订单/仓位/挂单）、智能功能（聪明钱交易/Tracker钱包追踪）、社媒推特（KOL推文）、新币发现、信号等全部实时数据。当用户需要 WebSocket 连接、实时推送、listenKey、订阅行情/订单/仓位/钱包活动/推特监控时使用。
argument-hint: [订阅类型/使用场景]
---

# Alph.ai WebSocket 实时推送

本模块是 **平台级统一推送通道**，通过单一 WebSocket 连接订阅所有实时数据。

**3 个管理接口** + **15 种订阅类型**，覆盖：
- 行情数据（K线、Ticker）
- 交易数据（订单、仓位、挂单、Swap）
- 智能功能（聪明钱交易、Tracker 钱包活动）
- 社媒推特（关注账号的推文行为）
- 新币发现（新 Token 上线、信号）

---

## 连接流程

```
1. POST https://b.alph.ai/smart-web-gateway/ws/listenkey
   Header: Cookie: dex_cookie=<value>
   Body: {}
   → 返回 listenKey（1小时过期）

2. 连接 wss://ws.alph.ai/stream/ws?listenKey=<listen_key>

3. 发送订阅消息（见下方各类型示例）

4. listenKey 过期前调用续期接口（或删除后重新申请）
```

> dex_cookie 获取方式见 [auth-guide.md](../alphai/auth-guide.md)

---

## 管理接口

| 方法 | 路径 | 功能 |
|------|------|------|
| POST | `/smart-web-gateway/ws/listenkey` | 申请 / 续期 listenKey |
| POST | `/smart-web-gateway/ws/delete/listenkey` | 删除 listenKey（立即断开连接） |
| GET  | `wss://ws.alph.ai/stream/ws` | WebSocket 连接端点 |

**测试环境**：`wss://ws.alphtest.cc/stream/ws`

### listenKey 说明

- 默认有效期 **1 小时**，需在过期前续期（调用申请接口即可续期）
- 删除 listenKey 后，对应连接**立即断开**
- 连接时不带 listenKey 只能订阅**公开数据**（行情、新币等）
- 连接时带 listenKey 可订阅**所有数据**（含用户私有数据）

---

## 订阅消息格式

### 发送（订阅/取消订阅）

```json
{
  "id": "req-001",
  "event": "SUBSCRIBE",
  "params": [
    {
      "chain": "bsc",
      "token": "0x...",
      "type": "kline",
      "scale": "1m"
    }
  ]
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `id` | string | 否 | 请求 ID，原样返回，用于匹配响应 |
| `event` | string | 是 | `SUBSCRIBE` 订阅 / `UNSUBSCRIBE` 取消 |
| `params` | array | 是 | 订阅参数列表（可批量） |
| `params[].chain` | string | 是 | 链名，小写（如 `bsc`、`sol`） |
| `params[].token` | string | 部分必填 | 合约地址（见各类型说明） |
| `params[].type` | string | 是 | 订阅类型（见下方列表） |
| `params[].scale` | string | 部分必填 | 精度枚举（kline/ticker 必填） |
| `params[].scene` | string | 部分必填 | 场景（token_info 必填） |

### 服务端 Ping/Pong

服务端会定期发送 ping 帧（携带时间戳），客户端必须回复 pong 帧（带回时间戳）。多次未响应会断开连接。客户端需支持 `permessage-deflate` 扩展。

---

## 订阅类型总览

### 公开数据（无需 listenKey）

| type | token 必填 | scale 必填 | 说明 |
|------|-----------|-----------|------|
| `kline` | 是 | 是 | K 线实时更新 |
| `all_tickers` | 是 | 否 | 全部精度 Ticker |
| `single_ticker` | 是 | 是 | 单精度 Ticker |
| `token_info` | 是 | 否（scene 必填）| Token 详情页数据 |
| `token_level` | 否 | 否 | Token 等级变化 |
| `token_change` | 否 | 否 | Token 信息变化 |
| `signal` | 否 | 否 | 交易信号推送 |
| `new_token` | 否 | 否 | 新创建的 Token |
| `smart_trade` | 是 | 否 | 聪明钱交易 |
| `kol_call` | 是 | 否 | KOL 提及 |
| `tracker` | 是 | 否 | 钱包活动（Tracker 追踪） |

### 用户私有数据（需要 listenKey）

| type | token 必填 | 说明 |
|------|-----------|------|
| `order` | 否 | 订单数据 |
| `position` | 否 | 仓位余额 |
| `swap` | 否 | 交易信息 |
| `pending_order` | 否 | 挂单 |
| `user_tracker_x` | 否 | 关注的推特账号发推行为 |

---

## 各类型详细说明

### K 线（kline）

```json
{
  "event": "SUBSCRIBE",
  "params": [{"chain": "bsc", "token": "0x...", "type": "kline", "scale": "1m"}]
}
```

**scale 枚举**：`1s` `15s` `30s` `1m` `5m` `15m` `30m` `1h` `2h` `4h` `12h` `1d` `1w`

**推送数据格式**：
```json
{"e": "kline", "E": 1700000000000, "C": "bsc", "t": "0x...", "s": "1m",
 "d": [{"i": 123456, "o": "0.001", "c": "0.0012", "h": "0.0013", "l": "0.0009",
        "v": "10000", "ba": "6000", "sa": "4000", "bc": 50, "sc": 30, "cp": "300"}]}
```

| 字段 | 说明 |
|------|------|
| `e` | 事件类型（kline） |
| `E` | 推送时间（毫秒时间戳） |
| `C` | 链名 |
| `t` | Token 合约地址 |
| `s` | K 线精度 |
| `d[].i` | K 线 ID（idx） |
| `d[].o/c/h/l` | 开/收/高/低 |
| `d[].v` | 成交量 |
| `d[].ba/sa` | 买入/卖出金额 |
| `d[].bc/sc` | 买入/卖出笔数 |
| `d[].cp` | 主链汇率 |

---

### Ticker（all_tickers / single_ticker）

```json
{"event": "SUBSCRIBE", "params": [{"chain": "bsc", "token": "0x...", "type": "all_tickers"}]}
{"event": "SUBSCRIBE", "params": [{"chain": "bsc", "token": "0x...", "type": "single_ticker", "scale": "1m"}]}
```

**single_ticker scale 枚举**：`1m` `5m` `1h` `1d`

**推送数据格式**：
```json
{"e": "all_tickers", "E": 1700000000000, "C": "bsc", "t": "0x...",
 "d": {"1m": {"o": "0.001", "c": "0.0012", "h": "0.0013", "l": "0.0009",
              "v": "10000", "ba": "6000", "sa": "4000", "bc": 50, "sc": 30, "r": "0.2"}}}
```

`d` 的 key 为精度，`r` 为涨跌幅。

---

### Token 信息（token_info）

```json
{"event": "SUBSCRIBE", "params": [{"chain": "bsc", "token": "0x...", "type": "token_info", "scene": "detail_real"}]}
```

**scene 枚举**：
- `detail_real`：详情页实时数据
- `detail_schedule`：详情页定时数据
- `xtock_schedule`：美股页面数据

---

### 信号（signal）

不需要传 token，订阅后接收全链信号推送。

```json
{"event": "SUBSCRIBE", "params": [{"chain": "bsc", "type": "signal"}]}
```

**推送数据包含**：token 合约、token 信息（code、价格、市值、社交媒体、安全信息、top10 持仓、AI 描述）、信号类型等。

---

### 新 Token（new_token）

不需要传 token，订阅后实时接收新创建的代币。

```json
{"event": "SUBSCRIBE", "params": [{"chain": "bsc", "type": "new_token"}]}
```

---

### 聪明钱交易（smart_trade）

```json
{"event": "SUBSCRIBE", "params": [{"chain": "bsc", "token": "0x...", "type": "smart_trade"}]}
```

---

### KOL 提及（kol_call）

```json
{"event": "SUBSCRIBE", "params": [{"chain": "bsc", "token": "0x...", "type": "kol_call"}]}
```

---

### Tracker 钱包活动（tracker）

```json
{"event": "SUBSCRIBE", "params": [{"chain": "bsc", "token": "0x...", "type": "tracker"}]}
```

---

### 订单（order）⚠️ 需要 listenKey

```json
{"event": "SUBSCRIBE", "params": [{"chain": "bsc", "type": "order"}]}
```

---

### 仓位余额（position）⚠️ 需要 listenKey

```json
{"event": "SUBSCRIBE", "params": [{"chain": "bsc", "type": "position"}]}
```

---

### 挂单（pending_order）⚠️ 需要 listenKey

```json
{"event": "SUBSCRIBE", "params": [{"chain": "bsc", "type": "pending_order"}]}
```

---

### 交易信息（swap）⚠️ 需要 listenKey

```json
{"event": "SUBSCRIBE", "params": [{"chain": "bsc", "type": "swap"}]}
```

---

### 推特关注账号行为（user_tracker_x）⚠️ 需要 listenKey

订阅后实时接收你关注的 X 账号的推文行为（发推、转发、回复、引用）。

```json
{"event": "SUBSCRIBE", "params": [{"type": "user_tracker_x"}]}
```

---

## 完整代码示例

### Python

```python
import asyncio
import json
import aiohttp
import websockets

DEX_COOKIE = "your_dex_cookie"
WS_URL = "wss://ws.alph.ai/stream/ws"
GATEWAY = "https://b.alph.ai/smart-web-gateway"

async def get_listen_key(session):
    async with session.post(
        f"{GATEWAY}/ws/listenkey",
        json={},
        headers={"Cookie": f"dex_cookie={DEX_COOKIE}"}
    ) as resp:
        data = await resp.json()
        return data["data"]["listenKey"]

async def renew_listen_key(session, listen_key):
    await session.post(
        f"{GATEWAY}/ws/listenkey",
        json={"listenKey": listen_key},
        headers={"Cookie": f"dex_cookie={DEX_COOKIE}"}
    )

async def main():
    async with aiohttp.ClientSession() as session:
        listen_key = await get_listen_key(session)

        # 自动续期任务（每50分钟续期一次）
        async def auto_renew():
            while True:
                await asyncio.sleep(50 * 60)
                await renew_listen_key(session, listen_key)

        asyncio.create_task(auto_renew())

        url = f"{WS_URL}?listenKey={listen_key}"
        async with websockets.connect(url, compression="deflate") as ws:
            # 订阅 K 线
            await ws.send(json.dumps({
                "id": "sub-kline",
                "event": "SUBSCRIBE",
                "params": [{
                    "chain": "bsc",
                    "token": "0x...",
                    "type": "kline",
                    "scale": "1m"
                }]
            }))

            # 处理 ping/pong
            async for msg in ws:
                if isinstance(msg, bytes):
                    # ping 帧，回 pong
                    await ws.pong(msg)
                    continue
                data = json.loads(msg)
                print(data)

asyncio.run(main())
```

### JavaScript / Node.js

```javascript
const WebSocket = require('ws');
const axios = require('axios');

const DEX_COOKIE = 'your_dex_cookie';
const GATEWAY = 'https://b.alph.ai/smart-web-gateway';
const WS_URL = 'wss://ws.alph.ai/stream/ws';

async function getListenKey() {
  const res = await axios.post(`${GATEWAY}/ws/listenkey`, {}, {
    headers: { Cookie: `dex_cookie=${DEX_COOKIE}` }
  });
  return res.data.data.listenKey;
}

async function main() {
  const listenKey = await getListenKey();

  // 自动续期（每50分钟）
  setInterval(async () => {
    await axios.post(`${GATEWAY}/ws/listenkey`, { listenKey }, {
      headers: { Cookie: `dex_cookie=${DEX_COOKIE}` }
    });
  }, 50 * 60 * 1000);

  const ws = new WebSocket(`${WS_URL}?listenKey=${listenKey}`, {
    perMessageDeflate: true
  });

  ws.on('open', () => {
    ws.send(JSON.stringify({
      id: 'sub-kline',
      event: 'SUBSCRIBE',
      params: [{ chain: 'bsc', token: '0x...', type: 'kline', scale: '1m' }]
    }));
  });

  ws.on('ping', (data) => ws.pong(data));
  ws.on('message', (data) => console.log(JSON.parse(data)));
}

main();
```

---

## API 数据来源

| 文件 | 包含 |
|------|------|
| `apis/websocket.json` | listenKey 申请/续期/删除、WS 连接端点（3个 API） |

**参数占位符**: $ARGUMENTS
