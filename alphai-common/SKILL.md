---
name: alphai-common
description: Alph.ai 公共功能 API - 代币黑名单查询、发币平台信息、盈亏分享卡片、SEO 数据等通用功能。当用户询问代币是否在黑名单、查询发币平台、生成分享卡片、PnL 分享、SSR/SEO 数据时使用。
argument-hint: [查询内容/功能名称]
---

# Alph.ai 公共模块 API

本模块包含 **8 个公共功能 API**，涵盖：
- 黑名单查询 (1个)
- 发币平台信息 (1个)
- SEO 数据 (3个)
- PnL 分享 (3个)

---

## 核心接口速查

### 1. 代币黑名单查询

```
GET /smart-web-gateway/data-center/blacklist/data
  ?chain=bsc&token=0xabc...,0xdef...
```

- `chain`：链名（bsc、sol、eth 等）
- `token`：合约地址，**逗号分隔，支持批量查询**

返回字段：`chain`、`tokenAddress`、`holderNum`（持有人数）、`liquidity`（流动性）、`marketcap`（市值）

### 2. 发币平台信息

```
GET /smart-web-gateway/common/platform/{chain}?language=zh_CN
```

返回该链上所有发币平台的 `id`、`code`（平台名）、`icon`、`color`。
这是 `alphai-market` 扫链接口中 `platform` 参数的数据来源。

---

## PnL 分享卡片

用于生成代币盈亏分享卡片（用于社交媒体分享）。

### 查询代币分享详情

```
GET /smart-web-gateway/share/token-pnl
  ?walletAddress=<钱包地址>&chain=sol&token=<代币名>&language=zh_CN
```

返回字段：
| 字段 | 说明 |
|------|------|
| `tokenCode` | 代币名 |
| `iconUrl` | 代币图标 |
| `allProfit` | 总盈亏（USD） |
| `totalProfitPercent` | 总盈亏占比 |
| `holdingBalance` | 当前持仓价值 |
| `totalBuy` / `totalSell` | 总买入 / 总卖出 |
| `twitterName` | 关联 X 账号名称 |
| `backgroundImage` | 默认背景图列表 |

### 查询钱包分享详情

```
GET /smart-web-gateway/share/wallet-pnl
  ?walletAddress=<钱包地址>&chain=sol&language=en_US
```

返回字段：`realizedPnl7d`（7D已实现利润）、`realizedPnl30d`（30D已实现利润）、`unrealizedPnl`（未实现利润）、`totalPnl`（总利润）、`tradeBuyNum7d`/`tradeSellNum7d`（7D交易笔数）

### 查询是否可分享

```
GET /smart-web-gateway/share/display
  ?walletAddress=<钱包地址>&chain=sol&token=<代币名>
```

返回 `data: true/false`，判断该钱包/代币组合是否有分享数据。

---

## SEO 数据接口

| 方法 | 路径 | 功能 |
|------|------|------|
| GET | `/smart-web-gateway/token/seo/list` | 分页获取代币 SEO 列表（token 地址列表） |
| GET | `/seo-web-gateway/token/token-seo` | 代币 SSR 数据（价格、市值、涨跌等） |
| GET | `/seo-web-gateway/token/token-seo-sitemap` | Sitemap 数据（链 + 合约地址） |

`token-seo` 接口参数：`chain`、`token`（合约地址）

---

## 工作流程

当你询问公共功能相关问题时，我会：
1. 从 `apis.json` 中搜索相关 API
2. 展示 API 的路径、方法、参数、响应格式
3. 根据需要生成调用代码示例
4. 提供使用建议和注意事项

## API 数据来源

完整的 API 定义存储在同目录下的 `apis.json` 文件中。

---

**参数占位符**: $ARGUMENTS
