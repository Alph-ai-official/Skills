---
name: alphai-market
description: Alph.ai 行情数据 API - 币种详情、实时行情、热门币种、市场数据、WS推送、收藏、扫链等。当用户询问价格、行情、币种信息、市场数据时使用。
argument-hint: [查询内容/币种名称]
---

# Alph.ai 行情模块 API

本模块包含 **42 个行情相关 API**，涵盖：
- 币种详情 (18个) ⭐ **新增：代币完整详情接口**
- 实时行情 (5个)
- 热门币种 (10个)
- WS 实时推送 (3个)
- 收藏功能 (3个)
- 扫链数据 (7个)
- Gas 费查询 (1个)
- 链信息 (1个)

## ⭐ 推荐接口：代币完整详情

当用户查询**代币详情**时，优先推荐使用：

**`GET /smart-web-gateway/token/token-detail`**

**为什么推荐这个接口？**
- ✅ **一站式查询**：一次调用获取所有信息，无需多次请求
- ✅ **包含市值**：直接返回市值数据（marketCap）
- ✅ **信息最全**：价格、市值、供应量、持有者、流动性、安全信息、社交媒体等
- ✅ **单位明确**：同时提供 BNB 和 USDT 计价

**请求示例：**
```
GET https://b.alph.ai/smart-web-gateway/token/token-detail?chain=bsc&token=0x924fa68a0fc644485b8df8abfa0a41c2e7744444
Header: Cookie: dex_cookie=<your_cookie>
```

**包含的关键数据：**
- 💰 价格（BNB 和 USDT）、市值
- 📊 总供应量、持有者数量
- 💧 流动性信息（池地址、流动性值、交易平台）
- 🔒 安全信息（开源、锁定、蜜罐、税率）
- 📱 社交媒体（Twitter、Telegram、Website、KOL提及）
- 🤖 AI 生成的代币描述和叙述

## 使用方式

### 1. 查询 API
```
查找币种详情接口
查询实时行情的 API
我想获取热门币种
```

### 2. 查看 API 详情
```
显示获取币价接口的详细信息
这个行情接口返回什么数据？
```

### 3. 生成调用代码
```
生成调用行情接口的 Python 代码
用 TypeScript 调用 WebSocket 推送
```

## WebSocket 实时推送

行情数据支持通过 WebSocket 实时推送。连接前需要先获取 listenKey。

### 连接流程

```
1. POST https://b.alph.ai/smart-web-gateway/ws/listenkey
   Header: Cookie: dex_cookie=<value>
   Body: {}
   → 获取 listenKey（1小时过期，需自动续期）

2. 连接 wss://ws.alph.ai/stream/ws?listenKey=<listen_key>

3. 发送订阅消息获取行情推送
```

> 完整的认证和连接说明见 `/alphai` 主导航的 [auth-guide.md](../alphai/auth-guide.md)

## 工作流程

当你询问行情、价格、币种相关问题时，我会：
1. **识别查询类型**：
   - 📊 **代币详情查询**（合约地址、代币名称） → 优先推荐 `/token/token-detail` 接口
   - 💰 **实时价格查询** → 使用 `/ticker/currentPrice` 或 `/ticker/24h` 接口
   - 🔥 **热门币种列表** → 使用 `/sherlock/popular_token/tokenPage` 接口
   - 📈 **K线数据** → 使用 `/kline/new/history` 接口
2. 从 `apis.json` 中搜索相关 API
3. 展示 API 的路径、方法、参数、响应格式
4. 根据需要生成调用代码示例
5. 提供 WebSocket 连接示例（如果需要），包含 listenKey 获取和自动续期
6. 提供使用建议和注意事项

## 💡 价格单位说明

**重要**：Alph.ai 的价格数据使用**链原生代币**作为计价单位：
- BSC 链：价格以 **BNB** 计价
- 以太坊链：价格以 **ETH** 计价
- Solana 链：价格以 **SOL** 计价

但 `token-detail` 接口同时提供：
- `tokenPriceSol`: 链原生代币计价（字段名是 Sol 但实际是链原生币）
- `tokenPriceUsdt`: **USDT 计价**（推荐使用，直观）
- `marketCap`: **市值（USD）**

## API 数据来源

按功能分类存储在 `apis/` 目录，按需查阅：

| 功能 | 文件 | 包含 |
|------|------|------|
| 币种详情 | `apis/token-detail.json` | CoinDetailController (11个) |
| 热门币种 | `apis/popular.json` | 热门、美股、PopularPage (11个) |
| 实时行情 | `apis/ticker.json` | 行情接口 (5个) |
| WS推送 | `apis/websocket.json` | WebSocket 推送 (3个) |
| 扫链数据 | `apis/scan.json` | 扫链三栏 (7个) |
| 其他 | `apis/misc.json` | 收藏、Gas费、链信息 (5个) |

> 查找 API 时请直接读取对应的分类文件，不要读取 apis.json 全量文件。

---

**参数占位符**: $ARGUMENTS
