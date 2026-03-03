# Alph.ai API Skills 更新日志

## [v1.3.0] - 2026-03-03

### alphai-twitter 模块新增 4 个接口（7 → 11 API）

新增 4 个推特数据接口，基于 Twitter API 会员封装：

**新增接口：**

| 方法 | 路径 | 功能 |
|------|------|------|
| GET | `/token/twitter-search` | 推文 meme 代币搜索 — 根据推文 URL 提取关联的 meme 代币合约地址，返回链名和池子流动性 |
| POST | `/x/detail` | X 用户详情 — 根据用户名查询账户信息（粉丝数、简介、头像、认证状态等） |
| POST | `/x/search` | 推文关键词搜索 — 按关键词搜索推文，返回推文内容、互动数据和作者信息，支持分页 |
| POST | `/x/tweets` | 用户推文列表 — 根据用户 ID 获取最新推文，含 entities（mentions/cashtags）和互动数据，支持分页 |

**使用场景：**

- 根据推文链接一键查找所有关联 meme 代币及流动性
- 查询任意 X 用户详情（粉丝数、认证状态等）
- 按关键词搜索推文做舆情分析
- 拉取指定 KOL 最新推文并分析内容

**文档更新：**

- 更新 `alphai-twitter/SKILL.md`：API 列表、接口详情、参数说明、返回示例、新增场景 5/6/7
- 更新 `alphai-twitter/apis.json`：新增 4 个接口完整定义
- 更新 `README.md` / `README.zh-CN.md`：API 总数 208 → 212，Twitter 模块 7 → 11

---

## [v1.2.0] - 2026-03-02

### 拆分大型 apis.json 为分类子文件

alphai-user、alphai-market、alphai-trading 三个模块的 apis.json 超过 2000 行，导致 AI 读取时被截断查不到靠后的 API。按子分类拆分到 `apis/` 目录，每个文件控制在 2000 行以内。

**新增 17 个分类文件：**

- `alphai-user/apis/` — 6 个文件（auth、security、wallet、profile、referral、activity）
- `alphai-market/apis/` — 6 个文件（token-detail、popular、ticker、websocket、scan、misc）
- `alphai-trading/apis/` — 5 个文件（order、pending、follow、settings、fee）

**更新 SKILL.md：**

- 三个模块的 SKILL.md 均添加 API 索引路由表，引导优先读取分类文件
- 更新 install.sh 添加 apis/ 验证提示

> 原 apis.json 保留不动，保持向后兼容。

**文档改进：**

- README 拆分为中英文双版本（`README.md` + `README.zh-CN.md`）
- 全部文档将 "Claude Code" 改为 "AI Agent"，明确兼容多种 Agent
- 新增兼容性说明：Claude Code / Claude Desktop / 其他 AI Agent
- 更新 QUICKSTART.md、install.sh 中的措辞

---

## [v1.1.0] - 2026-03-02

### ✨ 新增功能

#### alphai-market 模块

**新增接口：代币完整详情** (`GET /smart-web-gateway/token/token-detail`)

- ⭐ **推荐使用**：查询代币详情时的首选接口
- 📊 **一站式查询**：一次调用获取所有代币信息
- 💰 **包含市值**：直接返回市值数据（marketCap）

**接口特性：**
- 价格信息（BNB 和 USDT 双计价）
- 市值数据（USD）
- 供应量和持有者信息
- 流动性池详情
- 安全检测（开源、锁定、蜜罐、税率）
- 社交媒体信息（Twitter、Telegram、Website）
- AI 生成的代币描述

**请求参数：**
```
GET /smart-web-gateway/token/token-detail
Query Parameters:
  - chain: 链名称（如 bsc, ethereum, solana）
  - token: 代币合约地址
```

**使用示例：**
```bash
curl "https://b.alph.ai/smart-web-gateway/token/token-detail?chain=bsc&token=0x924fa..." \
  -H "Cookie: dex_cookie=<your_cookie>"
```

### 📝 文档更新

- 更新 `alphai-market/SKILL.md`
  - 添加代币完整详情接口说明
  - 新增推荐接口使用指南
  - 添加价格单位说明（BNB vs USDT）
  - 优化工作流程说明

- 更新 `alphai-market/apis.json`
  - 添加 token-detail 接口完整定义
  - 包含详细的请求参数和响应结构

### 🎯 重要提示

**价格单位说明：**
- Alph.ai 在不同链上使用对应的链原生代币计价
  - BSC 链：BNB
  - 以太坊链：ETH
  - Solana 链：SOL
- `token-detail` 接口同时提供 BNB 和 USDT 计价，推荐使用 USDT 计价（更直观）

**推荐使用场景：**
- 📊 查询代币详情 → `/token/token-detail`（推荐）
- 💰 查询实时价格 → `/ticker/currentPrice` 或 `/ticker/24h`
- 🔥 热门币种列表 → `/sherlock/popular_token/tokenPage`

---

## [v1.0.0] - 2025-02-25

### 初始版本

包含 208 个 Alph.ai API，分为 7 个功能模块：
- alphai（主导航）
- alphai-trading（交易模块 - 54 API）
- alphai-market（行情模块 - 41 API → 42 API）
- alphai-user（用户模块 - 67 API）
- alphai-twitter（社媒模块 - 7 API）
- alphai-smart（智能模块 - 31 API）
- alphai-common（公共模块 - 8 API）
