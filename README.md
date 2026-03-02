# Alph.ai API Skills for AI Agent

[中文文档](README.zh-CN.md) 

Join our Telegram group for updates, support and discussions:

**https://t.me/alphaiglobalchat/101011**

> 208 Alph.ai APIs packaged as AI Agent skills — token monitoring, social media tracking, automated trading, code generation and usage guidance.

## What's Inside

208 APIs organized into 6 functional modules + 1 navigation hub:

| Skill | Description | APIs |
|-------|-------------|------|
| `alphai` | Navigation hub + auth guide (dex_cookie / WebSocket / listenKey) | - |
| `alphai-trading` | Trading (buy/sell, limit orders, copy trading) | 54 |
| `alphai-market` | Market data (prices, tickers, WS push, on-chain scanning) | 42 |
| `alphai-user` | User management (registration, accounts, wallets) | 67 |
| `alphai-twitter` | Twitter/X monitoring (KOL tracking, tweet scraping, WS push) | 7 |
| `alphai-smart` | Smart features (smart wallets, trackers) | 31 |
| `alphai-common` | Common utilities (SEO, sharing) | 8 |

## Prerequisites: Get dex_cookie

All API calls require `dex_cookie` authentication:

1. Log in to [alph.ai](https://alph.ai) in your browser
2. Open DevTools (`F12` / `Cmd+Option+I`)
3. **Application → Cookies → alph.ai → copy `dex_cookie`**
4. Valid for 14 days

See `alphai/auth-guide.md` for details.

## Compatibility

These skills work with any AI agent that supports the skills/tools directory convention:

| AI Agent | Install Path | Notes |
|----------|-------------|-------|
| **Claude Code** (CLI) | `~/.claude/skills/` | Global install, all projects share |
| **Claude Desktop** | `.claude/skills/` in project root | Per-project |
| **Cursor** | `~/.cursor/skills/` | Global install |
| **Windsurf** | `~/.windsurf/skills/` | Global install |
| **Other Agents** | Agent's skills/tools directory | Or reference JSON files directly |

## Installation

### Option 1: Install script (recommended)

The script supports multiple agents — just pick yours:

```bash
cd Alph.ai_api_skills
./install.sh
```

### Option 2: Manual copy

```bash
# Claude Code (default)
cp -r alphai* ~/.claude/skills/

# Cursor
cp -r alphai* ~/.cursor/skills/

# Windsurf
cp -r alphai* ~/.windsurf/skills/

# Per-project (any agent)
mkdir -p .claude/skills && cp -r alphai* .claude/skills/
```

Restart your AI agent after installation.

## Usage

### Call a specific module

```
/alphai-trading find the order creation API
/alphai-market get ETH real-time price API
/alphai-twitter how to monitor CZ's tweets?
/alphai-user what APIs are needed for user registration?
```

### Use the navigation hub

```
/alphai I want to build a trading feature
/alphai how to get token prices?
```

### Let the agent decide

Just ask naturally — the agent will pick the right module:

```
Help me find the order API
I want to monitor a KOL's Twitter
How to implement user login?
```

## Directory Structure

```
Alph.ai_api_skills/
├── README.md                         # English docs
├── README.zh-CN.md                   # Chinese docs
├── QUICKSTART.md                     # Quick start (3 min)
├── CHANGELOG.md                      # Version history
├── install.sh                        # Install script
├── alphai/                           # Navigation hub
│   ├── SKILL.md
│   └── auth-guide.md                 # Auth & WebSocket guide
├── alphai-trading/                   # Trading module
│   ├── SKILL.md
│   ├── apis.json                     # Full API definitions
│   └── apis/                         # Split by category (< 2000 lines each)
├── alphai-market/                    # Market data module
│   ├── SKILL.md
│   ├── apis.json
│   └── apis/
├── alphai-user/                      # User module
│   ├── SKILL.md
│   ├── apis.json
│   └── apis/
├── alphai-twitter/                   # Twitter/X module
│   ├── SKILL.md
│   ├── examples.md                   # Code examples
│   └── apis.json
├── alphai-smart/                     # Smart features module
│   ├── SKILL.md
│   └── apis.json
└── alphai-common/                    # Common module
    ├── SKILL.md
    └── apis.json
```

## Module Quick Reference

| Command | Purpose | Example |
|---------|---------|---------|
| `/alphai` | Navigation, auth guide | I want to trade |
| `/alphai-trading` | Trading, limit orders, copy trading | Find order API |
| `/alphai-market` | Prices, tickers, WS push | Get ETH price |
| `/alphai-user` | Registration, login, wallets | User login flow |
| `/alphai-twitter` | Twitter monitoring, KOL tracking | Monitor CZ's tweets |
| `/alphai-smart` | Smart analytics, wallet tracking | Smart wallet API |
| `/alphai-common` | Common, SEO, sharing | Public config API |

## FAQ

**Q: Skills not working?**
A: Verify files are in `~/.claude/skills/` (or your agent's skills directory) and restart the agent. Type `/` to see available commands.

**Q: How to share with my team?**
A: Clone this repo or zip the directory. Teammates run `./install.sh` after extracting.

**Q: How to uninstall?**
A: `rm -rf ~/.claude/skills/alphai*`

## Community

Join our Telegram group for updates, support and discussions:

**https://t.me/alphaiglobalchat/101011**

---

**Alph.ai Team**
