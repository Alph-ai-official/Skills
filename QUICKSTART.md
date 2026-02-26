# 快速开始

## 3 分钟上手 Alph.ai  Skills

### 第 1 步：获取 dex_cookie

1. 浏览器登录 alph.ai
2. F12 打开 DevTools
3. **Application → Cookies → alph.ai → 复制 `dex_cookie`**

> dex_cookie 有效期 14 天，所有 API 调用都需要它

### 第 2 步：安装

```bash
cd Alph.ai_api_skills
./install.sh
```

### 第 3 步：验证

```bash
ls ~/.claude/skills/ | grep alphai
```

应该看到：
```
alphai
alphai-common
alphai-market
alphai-smart
alphai-trading
alphai-twitter
alphai-user
```

### 第 4 步：使用

重启 Claude Code，尝试以下命令：

```
/alphai-trading 查询下单接口
/alphai-twitter 如何监控 CZ 的推特？
/alphai-market 获取 ETH 实时价格的 API
```

或者直接提问，Claude 会自动选择合适的模块：
```
帮我监控某个 KOL 的推特，发帖时通知我
```

---

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

---

## 注意事项

1. **认证**：所有请求需要 dex_cookie（Cookie header），有效期 14 天
2. **WebSocket**：需要先获取 listenKey，详见 `/alphai` 主导航的认证指南
3. **首次使用**：安装后必须重启 Claude Code
4. **更新**：API 更新时需要重新安装 skills
