---
name: alphai-market
description: Alph.ai 行情数据 API - 币种详情、实时行情、热门币种、市场数据、WS推送、收藏、扫链等。当用户询问价格、行情、币种信息、市场数据时使用。
argument-hint: [查询内容/币种名称]
---

# Alph.ai 行情模块 API

本模块包含 **41 个行情相关 API**，涵盖：
- 币种详情 (17个)
- 实时行情 (5个)
- 热门币种 (10个)
- WS 实时推送 (3个)
- 收藏功能 (3个)
- 扫链数据 (7个)
- Gas 费查询 (1个)
- 链信息 (1个)

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
1. 从 `apis.json` 中搜索相关 API
2. 展示 API 的路径、方法、参数、响应格式
3. 根据需要生成调用代码示例
4. 提供 WebSocket 连接示例（如果需要），包含 listenKey 获取和自动续期
5. 提供使用建议和注意事项

## API 数据来源

完整的 API 定义存储在同目录下的 `apis.json` 文件中。

---

**参数占位符**: $ARGUMENTS
