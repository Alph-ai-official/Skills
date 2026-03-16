---
name: alphai-smart
description: Alph.ai 智能功能 API - 聪明钱包（Smart Money）分析、Tracker 链上地址追踪、信号源涨幅榜、Bot 自动交易机器人等高级功能。当用户询问聪明钱包、Smart Money、链上大户追踪、地址监控、信号推送、涨幅排行、自动交易机器人、copy trading 相关问题时使用。
argument-hint: [查询内容/功能名称]
---

# Alph.ai 智能功能模块 API

本模块包含 **31 个智能功能 API**，涵盖：
- 聪明钱包 (14个) - 大户地址分析、持仓、交易记录、盈亏
- Tracker 追踪 (8个) - 关注/取消关注钱包，实时监控链上地址
- 信号源 (7个) - 涨幅榜、信号列表、推送记录
- Bot 机器人 (2个) - 查询可用 Bot 列表

---

## 核心接口速查

### 聪明钱包

| 方法 | 路径 | 功能 |
|------|------|------|
| GET  | `/smart-web-gateway/smart/smart-wallet` | 聪明钱包列表（按链/标签筛选） |
| GET  | `/smart-web-gateway/smart/wallet` | 单个钱包详情 |
| GET  | `/smart-web-gateway/smart/search` | 按地址搜索聪明钱包 |
| GET  | `/smart-web-gateway/smart/holding-tokens` | 钱包持有代币列表 |
| GET  | `/smart-web-gateway/smart/wallet-activity` | 钱包交易记录 |
| GET  | `/smart-web-gateway/smart/wallet-profit-loss` | 钱包盈亏列表 |
| GET  | `/smart-web-gateway/smart/hot-tokens` | 1h 热门代币（聪明钱买入） |
| GET  | `/smart-web-gateway/smart/tags` | 标签列表 |
| POST | `/smart-web-gateway/smart/wallet-refresh` | 刷新钱包数据 |

### Tracker 追踪

| 方法 | 路径 | 功能 |
|------|------|------|
| POST | `/smart-web-gateway/user/tracker/follow/wallet/create` | 关注钱包（添加到追踪） |
| POST | `/smart-web-gateway/user/tracker/follow/wallet/cancel` | 取消关注钱包 |
| POST | `/smart-web-gateway/user/tracker/follow/wallet/query/page` | 分页查询已关注钱包 |
| POST | `/smart-web-gateway/user/tracker/follow/wallet/updateTradeRemind` | 开启/关闭交易提醒 |
| POST | `/smart-web-gateway/user/tracker/follow/wallet/import` | 批量导入关注地址 |
| POST | `/smart-web-gateway/user/tracker/query/hotTokenPage` | 热门币种钱包列表 |
| POST | `/smart-web-gateway/user/tracker/wallet/activity/query/page` | 活跃钱包分页 |

### 信号源

| 方法 | 路径 | 功能 |
|------|------|------|
| GET  | `/smart-web-gateway/signal/rank-list` | 24h 涨幅榜（金/银/铜） |
| GET  | `/smart-web-gateway/signal/list/latest` | 最新信号（前5个） |
| GET  | `/smart-web-gateway/signal/list` | 信号分页列表 |
| GET  | `/smart-web-gateway/signal/list-by-token` | 指定代币信号批量查询 |
| GET  | `/smart-web-gateway/signal/push-history` | 代币推送记录 |
| GET  | `/smart-web-gateway/signal/time-axis` | 信号时间轴 |
| GET  | `/smart-web-gateway/signal/smart-view-all` | 聪明钱买卖记录 ViewAll |

### Bot 机器人

| 方法 | 路径 | 功能 |
|------|------|------|
| GET  | `/smart-web-gateway/bot/get-bot-list` | 获取 Bot 列表 |
| GET  | `/smart-web-gateway/bot/get-bot` | 获取指定类型 Bot |

---

## 典型使用场景

### 场景 1：查询聪明钱包持仓
```
GET /smart-web-gateway/smart/holding-tokens
  ?wallet=<地址>&chain=sol&language=zh_CN&sort=profit&asc=desc&pageNum=1&pageSize=20
```

### 场景 2：关注一个链上地址并开启交易提醒
```
1. POST /user/tracker/follow/wallet/create  { "walletAddress": "0x...", "chain": "bsc" }
2. POST /user/tracker/follow/wallet/updateTradeRemind  { "walletAddress": "0x...", "remind": true }
```

### 场景 3：查看今日信号涨幅榜
```
GET /smart-web-gateway/signal/rank-list?chain=sol&level=Gold
```

### 场景 4：Copy Trading - 监控聪明钱包交易
```
1. 获取聪明钱包列表: GET /smart/smart-wallet?chain=sol
2. 订阅 WebSocket user_tracker，实时接收追踪地址的交易事件
3. 收到买入信号 → 调用 /alphai-trading 下单接口跟单
```

---

## 信号数据说明

信号源会对代币按聪明钱行为和 KOL 提及进行评级：

| 级别 | 说明 |
|------|------|
| `Gold` | 金牌信号，最高置信度 |
| `Silver` | 银牌信号 |
| `Copper` | 铜牌信号 |

信号列表中每条数据包含：
- `tokenInfo`：代币信息（价格、市值、流动性、AI描述）
- `smartInfo`：聪明钱持币数、买卖记录
- `kolInfo`：KOL 提及（用户名、粉丝数、等级）
- `multiple`：首推以来涨幅倍数
- `pushType`：推送类型 `[SMART, KOL_CALL]`

---

## 工作流程

当你询问智能功能相关问题时，我会：
1. 从 `apis.json` 中搜索相关 API
2. 展示 API 的路径、方法、参数、响应格式
3. 解释聪明钱/信号/追踪的工作原理
4. 根据需要生成调用代码示例
5. 提供集成建议和最佳实践

## API 数据来源

完整的 API 定义存储在同目录下的 `apis.json` 文件中。

---

**参数占位符**: $ARGUMENTS
