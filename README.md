# Alph.ai API Skills for Claude Code

> Alph.ai Skills，包含 208 个 API，支持代币监控、社媒监控、自动交易、代码生成和使用建议。

## 包含内容

本 Skills 包将 Alph.ai 的 208 个 API 分为 6 个功能模块 + 1 个主导航：

| Skill | 说明 | API 数量 |
|-------|------|----------|
| `alphai` | 主导航 + 认证指南（dex_cookie / WebSocket / listenKey） | - |
| `alphai-trading` | 交易模块（买卖、挂单、跟单等） | 54 |
| `alphai-market` | 行情模块（币价、行情、WS推送等） | 41 |
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

## 安装方法

### 方式 1：运行安装脚本（推荐）

```bash
cd Alph.ai_api_skills
./install.sh
```

### 方式 2：手动复制

```bash
cp -r Alph.ai_api_skills/* ~/.claude/skills/
```

### 方式 3：放在项目中

```bash
mkdir -p .claude/skills
cp -r Alph.ai_api_skills/* .claude/skills/
```

安装后重启 Claude Code 即可使用。

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

### 让 Claude 自动选择

直接提问，Claude 会自动判断并调用合适的 skill：

```
帮我查询下单的 API
我想监控某个 KOL 的推特
用户注册登录怎么实现？
```

## 目录结构

```
Alph.ai_api_skills/
├── README.md                         # 本文件
├── QUICKSTART.md                     # 快速开始（3分钟上手）
├── SHARE.md                          # 分享给同事的指南
├── install.sh                        # 一键安装脚本
├── alphai/                           # 主导航
│   ├── SKILL.md
│   └── auth-guide.md                 # 认证与 WebSocket 连接指南
├── alphai-trading/                   # 交易模块
│   ├── SKILL.md
│   └── apis.json
├── alphai-market/                    # 行情模块
│   ├── SKILL.md
│   └── apis.json
├── alphai-user/                      # 用户模块
│   ├── SKILL.md
│   └── apis.json
├── alphai-twitter/                   # 社媒推特(X)
│   ├── SKILL.md                      # 含推文数据格式说明
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
A: 确认安装到 `~/.claude/skills/` 并重启 Claude Code。输入 `/` 可查看所有可用命令。

**Q: 如何分享给团队？**
A: 压缩整个目录发给同事，同事解压后运行 `./install.sh`。详见 `SHARE.md`。

**Q: 如何卸载？**
A: `rm -rf ~/.claude/skills/alphai*`

---

**Alph.ai Team 内部使用**
