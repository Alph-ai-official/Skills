---
name: alphai-twitter
description: Alph.ai 社媒推特(X) API - X 账户监控、推文抓取（发推/转发/回复/引用）、热门监控列表、关注管理、监控配置、WebSocket 实时推送、翻译等。当用户询问推特、X、社媒监控、KOL追踪、推文内容分析相关问题时使用。
argument-hint: [查询内容/功能名称]
---

# Alph.ai 社媒推特(X) 模块 API

本模块包含 **7 个 HTTP API** + **WebSocket 实时推送**，支持完整的推特监控链路：
关注 KOL → 配置监控项 → 拉取历史推文 / WebSocket 实时接收 → 翻译 → 分析

## API 列表

| 方法 | 路径 | 功能 |
|------|------|------|
| POST | `/smart-web-gateway/tracker/x/follow` | 关注/取消关注 X 账户 |
| POST | `/smart-web-gateway/tracker/x/config` | 配置监控项（发推/转发/回复/引用/头像/昵称等） |
| GET  | `/smart-web-gateway/tracker/x/configList` | 获取当前监控配置 |
| POST | `/smart-web-gateway/tracker/x/monitorList` | 获取监控推文列表（含推文正文，支持分页） |
| POST | `/smart-web-gateway/tracker/x/myList` | 我的监控列表（支持按用户名筛选和排序） |
| POST | `/smart-web-gateway/tracker/x/hotList` | 热门监控列表 |
| POST | `/smart-web-gateway/tracker/x/transTexts` | 翻译推文内容 |

---

## 推文数据格式（重要）

### 推文类型

通过 `config` 接口可配置监控以下类型：

| type 值 | 含义 | 说明 |
|---------|------|------|
| `send` | 直接发推 | KOL 发布原创推文 |
| `retweeted` | 转发 | KOL 转发他人推文 |
| `replied_to` | 回复 | KOL 回复他人推文 |
| `quoted` | 引用 | KOL 引用他人推文并评论 |
| `follow` | 关注 | KOL 关注了新账户 |
| `profile` | 个人资料变更 | KOL 修改了个人资料 |
| `icon` | 头像变更 | KOL 更换了头像 |
| `nick` | 昵称变更 | KOL 修改了昵称 |
| `banner` | 横幅变更 | KOL 更换了横幅图片 |
| `account` | 账号变更 | KOL 修改了账号信息 |

### 推文数据结构

monitorList / WebSocket 返回的每条推文数据：

```json
{
    "type": "replied_to",
    "id": "2026538218787893548",
    "created_at": "2026-02-25T06:02:17.000Z",
    "text": "@frankyluan 基座模型与工程化还是两回事...",
    "tweets": {
        "text": "True",
        "id": "2026558347798004185",
        "media": []
    },
    "referenced": {
        "text": "If we based our sentencing on recidivism data...",
        "id": "2026365444282851690",
        "media": []
    }
}
```

**字段说明：**

| 字段 | 类型 | 说明 |
|------|------|------|
| `type` | string | 推文类型（见上表） |
| `id` | string | 推文 ID |
| `created_at` | string | 发布时间（ISO 8601 格式） |
| `text` | string | 推文正文内容 |
| `tweets` | object | 该用户发出的推文（原创内容） |
| `tweets.text` | string | 原创推文正文 |
| `tweets.id` | string | 原创推文 ID |
| `tweets.media` | array | 原创推文的媒体附件（图片/视频） |
| `referenced` | object | 被引用/回复/转发的原始推文 |
| `referenced.text` | string | 原始推文正文 |
| `referenced.id` | string | 原始推文 ID |
| `referenced.media` | array | 原始推文的媒体附件 |

### 不同推文类型的数据示例

**直接发推（send）：**
```json
{
    "type": "send",
    "id": "2026558347798004185",
    "created_at": "2026-02-25T07:22:00.000Z",
    "text": "BTC 突破新高！",
    "tweets": {
        "text": "BTC 突破新高！",
        "id": "2026558347798004185",
        "media": []
    }
}
```

**回复（replied_to）：**
```json
{
    "type": "replied_to",
    "id": "2026558009577714113",
    "created_at": "2026-02-25T07:20:55.000Z",
    "text": "@someone 🎯",
    "tweets": {
        "text": "@someone 🎯",
        "id": "2026558009577714113",
        "media": []
    },
    "referenced": {
        "text": "原始推文内容...",
        "id": "2026365444282851690",
        "media": []
    }
}
```

**引用转发（quoted）：**
```json
{
    "type": "quoted",
    "id": "2026560000000000000",
    "created_at": "2026-02-25T07:30:00.000Z",
    "text": "说得对！基座模型与工程化还是两回事",
    "tweets": {
        "text": "说得对！基座模型与工程化还是两回事",
        "id": "2026560000000000000",
        "media": []
    },
    "referenced": {
        "text": "If we based our sentencing on recidivism data...",
        "id": "2026365444282851690",
        "media": []
    }
}
```

**转发（retweeted）：**
```json
{
    "type": "retweeted",
    "id": "2026561000000000000",
    "created_at": "2026-02-25T07:35:00.000Z",
    "text": "",
    "referenced": {
        "text": "被转发的原始推文内容...",
        "id": "2026300000000000000",
        "media": []
    }
}
```

---

## 数据获取方式

### 方式 1：HTTP 拉取历史推文

通过 `monitorList` 接口拉取已关注 KOL 的历史推文列表：

```
POST https://b.alph.ai/smart-web-gateway/tracker/x/monitorList
Header: Cookie: dex_cookie=<value>
Body: { "pageNum": 1, "pageSize": 20 }
```

通过 `myList` 可按用户名筛选特定 KOL 的推文：

```
POST https://b.alph.ai/smart-web-gateway/tracker/x/myList
Header: Cookie: dex_cookie=<value>
Body: { "username": "cz_binance", "pageNum": 1, "pageSize": 20, "sort": "desc" }
```

### 方式 2：WebSocket 实时推送

```
1. POST /smart-web-gateway/ws/listenkey → 获取 listenKey（1小时过期，需自动续期）
2. 连接 wss://ws.alph.ai/stream/ws?listenKey=<listen_key>
3. 发送订阅：
   {
     "id": "0c1bfd5cb47fb8051e62d333b99916e72c695203fa9d94b171eed267486efb0c",
     "event": "SUBSCRIBE",
     "params": [{"type": "user_tracker_x"}]
   }
4. 实时接收已关注 KOL 的推文推送（数据格式同上）
```

> 完整的 dex_cookie 获取、listenKey 认证、自动续期说明见 [auth-guide.md](../alphai/auth-guide.md)
> 完整的代码示例（Python/JavaScript）见 [examples.md](examples.md)

---

## 典型使用场景

### 场景 1：监控 KOL 发帖并通知
```
flow: follow(KOL) → config(send/retweeted/replied_to/quoted)
      → WebSocket 订阅 user_tracker_x → 收到推文 → 推送到 Telegram
```

### 场景 2：抓取某 KOL 最新 N 条推文并分析
```
flow: follow(KOL) → myList(username=xx, pageSize=20)
      → 拿到推文 text → Claude 分析总结
```

### 场景 3：监控推文中的 CA（合约地址）并报警
```
flow: WebSocket 收到推文 → 从 text 和 referenced.text 中提取 CA
      → 查询行情/流动性 → 推送报警
```

### 场景 4：批量分析 KOL 推文内容
```
flow: 批量 follow KOL 列表 → 逐个 myList 拉取推文
      → Claude 分析推文内容 → 打分/分类
```

---

## 配置接口详情

### follow - 关注/取消关注

```json
POST /smart-web-gateway/tracker/x/follow
{
    "username": "cz_binance",
    "operationType": 1
}
```
- `operationType`: 1=关注, 0=取消关注

### config - 监控配置

```json
POST /smart-web-gateway/tracker/x/config
{
    "send": true,
    "retweeted": true,
    "replied_to": true,
    "quoted": true,
    "follow": false,
    "profile": false,
    "icon": false,
    "nick": false,
    "banner": false,
    "account": false
}
```

### transTexts - 翻译

```json
POST /smart-web-gateway/tracker/x/transTexts
{
    "from": "en",
    "to": "cn",
    "text": "GM! BTC to the moon!"
}
// 返回: { "data": { "result": "早上好！BTC 冲！" } }
```

---

## 工作流程

当你询问推特(X)/社媒相关问题时，我会：
1. 理解需求（监控/拉取/分析/翻译）
2. 推荐合适的接口和获取方式（HTTP 拉取 or WebSocket 实时推送）
3. 说明推文数据格式，包括不同类型（发推/转发/回复/引用）的区别
4. 生成完整的调用代码（含 dex_cookie 认证和 listenKey 续期）
5. 提供监控策略和最佳实践建议

## API 数据来源

完整的 API 定义存储在同目录下的 `apis.json` 文件中。

---

**参数占位符**: $ARGUMENTS
