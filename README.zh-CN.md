# Alph.ai API Skills

[English](README.md)

加入我们的 Telegram 群获取更多资讯、技术支持和交流：

**https://t.me/alphaiglobalchat/101011**

> 208 个 Alph.ai API 封装为 AI Agent Skills，支持代币监控、社媒监控、自动交易、代码生成和使用建议。

## 包含内容

208 个 API 分为 6 个功能模块 + 1 个主导航：

| Skill | 说明 | API 数量 |
|-------|------|----------|
| `alphai` | 主导航 + 认证指南（dex_cookie / WebSocket / listenKey） | - |
| `alphai-trading` | 交易模块（买卖、挂单、跟单等） | 54 |
| `alphai-market` | 行情模块（币价、行情、WS推送、扫链等） | 42 |
| `alphai-user` | 用户模块（注册、账户、钱包等） | 67 |
| `alphai-twitter` | 社媒推特X（KOL监控、推文抓取、WS推送等） | 7 |
| `alphai-smart` | 智能功能（聪明钱包、追踪等） | 31 |
| `alphai-common` | 公共模块（SEO、分享等） | 8 |

## 前置条件：获取 dex_cookie

所有 API 调用都需要 `dex_cookie` 认证。获取方式：

1. 浏览器登录 [alph.ai](https://alph.ai)
2. 打开 DevTools（`F12` / `Cmd+Option+I`）
3. **Application → Cookies → alph.ai → 复制 `dex_cookie`**
4. 有效期 14 天

详细说明见 `alphai/auth-guide.md`

## 兼容性

本 Skills 适用于任何支持 skills/tools 目录的 AI Agent：

| AI Agent | 安装路径 | 说明 |
|----------|---------|------|
| **Claude Code**（CLI） | `~/.claude/skills/` | 全局安装，所有项目共享 |
| **Claude Desktop** | 项目根目录 `.claude/skills/` | 按项目安装 |
| **Cursor** | `~/.cursor/skills/` | 全局安装 |
| **Windsurf** | `~/.windsurf/skills/` | 全局安装 |
| **其他 Agent** | Agent 的 skills/tools 目录 | 或直接引用 JSON 文件 |

## 安装方法

### 方式 1：运行安装脚本（推荐）

脚本支持多种 Agent，选择你的即可：

```bash
cd Alph.ai_api_skills
./install.sh
```

### 方式 2：手动复制

```bash
# Claude Code（默认）
cp -r alphai* ~/.claude/skills/

# Cursor
cp -r alphai* ~/.cursor/skills/

# Windsurf
cp -r alphai* ~/.windsurf/skills/

# 按项目安装（任意 Agent）
mkdir -p .claude/skills && cp -r alphai* .claude/skills/
```

安装后重启 AI Agent 即可使用。

## 使用方法

### 直接调用具体模块

```
/alphai-trading 查询下单接口
/alphai-market 获取 ETH 实时价格的 API
/alphai-twitter 如何监控 CZ 的推特？
/alphai-user 用户注册需要哪些接口？
```

### 使用主导航

```
/alphai 我想做交易功能
/alphai 如何获取币价？
```

### 让 Agent 自动选择

直接提问，Agent 会自动判断并调用合适的 skill：

```
帮我查询下单的 API
我想监控某个 KOL 的推特
用户注册登录怎么实现？
```

## 目录结构

```
Alph.ai_api_skills/
├── README.md                         # 英文文档
├── README.zh-CN.md                   # 中文文档
├── QUICKSTART.md                     # 快速开始（3分钟上手）
├── CHANGELOG.md                      # 版本更新日志
├── install.sh                        # 一键安装脚本
├── alphai/                           # 主导航
│   ├── SKILL.md
│   └── auth-guide.md                 # 认证与 WebSocket 连接指南
├── alphai-trading/                   # 交易模块
│   ├── SKILL.md
│   ├── apis.json                     # 完整 API 定义
│   └── apis/                         # 按分类拆分（每文件 < 2000 行）
├── alphai-market/                    # 行情模块
│   ├── SKILL.md
│   ├── apis.json
│   └── apis/
├── alphai-user/                      # 用户模块
│   ├── SKILL.md
│   ├── apis.json
│   └── apis/
├── alphai-twitter/                   # 社媒推特(X)
│   ├── SKILL.md
│   ├── examples.md                   # 完整代码示例
│   └── apis.json
├── alphai-smart/                     # 智能功能
│   ├── SKILL.md
│   └── apis.json
└── alphai-common/                    # 公共模块
    ├── SKILL.md
    └── apis.json
```

## 7 个模块速查

| 命令 | 用途 | 示例 |
|------|------|------|
| `/alphai` | 导航、认证指南 | 我想做交易 |
| `/alphai-trading` | 交易、挂单、跟单 | 查询下单接口 |
| `/alphai-market` | 行情、币价、WS推送 | 获取 ETH 价格 |
| `/alphai-user` | 注册、登录、钱包 | 用户登录流程 |
| `/alphai-twitter` | 推特监控、KOL追踪 | 监控 CZ 的推特 |
| `/alphai-smart` | 智能分析、钱包追踪 | 聪明钱包接口 |
| `/alphai-common` | 公共、SEO、分享 | 公共配置接口 |

## 常见问题

**Q: Skills 不生效？**
A: 确认安装到 `~/.claude/skills/`（或你的 Agent 的 skills 目录）并重启 Agent。输入 `/` 可查看所有可用命令。

**Q: 如何分享给团队？**
A: 克隆本仓库或打包目录发给同事，解压后运行 `./install.sh`。

**Q: 如何卸载？**
A: `rm -rf ~/.claude/skills/alphai*`

## 社区

加入我们的 Telegram 群获取更多资讯、技术支持和交流：

**https://t.me/alphaiglobalchat/101011**

---

**Alph.ai Team**
