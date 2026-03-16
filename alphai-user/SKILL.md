---
name: alphai-user
description: Alph.ai 用户账户 API - 注册登录、账户安全、钱包管理、用户信息、空投活动、VIP、分销邀请返佣等。当用户询问注册、登录、账户安全、钱包地址、用户信息、邀请码、返佣、空投活动、VIP、Google 认证相关问题时使用。
argument-hint: [查询内容/功能名称]
---

# Alph.ai 用户模块 API

本模块包含 **67 个用户相关 API**，涵盖：
- 注册与登录 (8个)
- 账户安全 (8个) + Google 认证 (1个)
- 钱包管理 (8个)
- 用户管理 (20个)
- 空投活动 (4个) + VIP (1个) + Humidifi 活动 (2个)
- 分销系统 (6个) + 邀请码 (9个) + 返佣 (2个)

> 社媒推特(X) 相关 API 已独立为 `/alphai-twitter` 模块

---

## 核心接口速查

### 注册 & 登录（`apis/auth.json`）

| 方法 | 路径 | 功能 |
|------|------|------|
| POST | `/smart-web-gateway/user/sendEmailCode` | 发送邮箱验证码 |
| POST | `/smart-web-gateway/user/register` | 邮箱注册 |
| POST | `/smart-web-gateway/user/login` | 邮箱登录 |
| POST | `/smart-web-gateway/user/loginByWallet` | 钱包登录（Web3） |
| POST | `/smart-web-gateway/user/loginByGoogle` | Google 登录 |
| POST | `/smart-web-gateway/user/logout` | 退出登录 |
| POST | `/smart-web-gateway/user/refreshToken` | 刷新 Token |
| POST | `/smart-web-gateway/user/resetPassword` | 重置密码 |

### 账户安全（`apis/security.json`）

| 方法 | 路径 | 功能 |
|------|------|------|
| GET  | `/smart-web-gateway/user/security/info` | 安全状态（邮箱/GA/密码绑定情况） |
| POST | `/smart-web-gateway/user/security/bindEmail` | 绑定邮箱 |
| POST | `/smart-web-gateway/user/security/changePassword` | 修改密码 |
| POST | `/smart-web-gateway/user/google/bind` | 绑定 Google 认证 |
| POST | `/smart-web-gateway/user/google/verify` | Google 验证码校验 |

### 钱包管理（`apis/wallet.json`）

| 方法 | 路径 | 功能 |
|------|------|------|
| GET  | `/smart-web-gateway/user/wallet/list` | 获取钱包地址列表 |
| POST | `/smart-web-gateway/user/wallet/add` | 添加钱包地址 |
| POST | `/smart-web-gateway/user/wallet/delete` | 删除钱包地址 |
| POST | `/smart-web-gateway/user/wallet/setPrimary` | 设置主钱包 |

### 用户信息（`apis/profile.json`）

| 方法 | 路径 | 功能 |
|------|------|------|
| GET  | `/smart-web-gateway/user/info` | 获取用户信息 |
| POST | `/smart-web-gateway/user/updateInfo` | 更新用户信息 |
| GET  | `/smart-web-gateway/user/vip/info` | 查询 VIP 等级 |

### 分销 & 邀请（`apis/referral.json`）

| 方法 | 路径 | 功能 |
|------|------|------|
| GET  | `/smart-web-gateway/user/invite/code` | 获取我的邀请码 |
| GET  | `/smart-web-gateway/user/invite/list` | 邀请记录列表 |
| GET  | `/smart-web-gateway/user/rebate/record` | 返佣记录 |
| GET  | `/smart-web-gateway/user/rebate/total` | 返佣总额统计 |

### 活动相关（`apis/activity.json`）

| 方法 | 路径 | 功能 |
|------|------|------|
| GET  | `/smart-web-gateway/user/airdrop/info` | 空投活动信息 |
| POST | `/smart-web-gateway/user/airdrop/claim` | 领取空投 |

---

## 工作流程

当你询问用户、账户、钱包相关问题时，我会：
1. 从对应的分类文件中搜索相关 API
2. 展示 API 的路径、方法、参数、响应格式
3. 特别关注认证和安全相关的要求
4. 根据需要生成调用代码示例
5. 提供安全最佳实践建议

## API 数据来源

按功能分类存储在 `apis/` 目录，按需查阅：

| 功能 | 文件 | 包含 |
|------|------|------|
| 注册登录 | `apis/auth.json` | 注册流程、登录流程 (8个) |
| 账户安全 | `apis/security.json` | 账户安全、Google 认证 (9个) |
| 钱包管理 | `apis/wallet.json` | 钱包信息、用户中心 (6个) |
| 用户信息 | `apis/profile.json` | UserController 全部接口 (20个) |
| 分销邀请 | `apis/referral.json` | 分销、邀请码、返佣 (17个) |
| 活动相关 | `apis/activity.json` | 空投活动、VIP、Humidifi (7个) |

> 查找 API 时请直接读取对应的分类文件，不要读取 apis.json 全量文件。

---

**参数占位符**: $ARGUMENTS
