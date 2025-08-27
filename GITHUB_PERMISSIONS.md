# 🔐 GitHub Actions权限配置说明

## 📋 问题描述

在运行GitHub Actions时，可能会遇到以下权限错误：

```
⚠️ Unexpected error fetching GitHub release for tag refs/tags/v0.0.1: 
HttpError: Resource not accessible by integration
Error: Resource not accessible by integration
```

这个错误通常是因为GitHub Actions没有足够的权限来访问仓库的Release资源。

## 🛠️ 解决方案

### 1. 工作流文件权限配置

在每个工作流文件中添加 `permissions` 配置：

```yaml
# 添加权限配置
permissions:
  contents: write    # 允许写入仓库内容（创建Release）
  actions: read      # 允许读取Actions信息
```

### 2. 权限说明

| 权限 | 说明 | 用途 |
|------|------|------|
| `contents: write` | 写入仓库内容 | 允许创建Release、上传文件 |
| `actions: read` | 读取Actions信息 | 允许访问工作流状态 |

## 🔧 完整配置示例

### Windows构建工作流

```yaml
name: Build Windows Executable

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
  release:
    types: [ published ]

# 添加权限配置
permissions:
  contents: write
  actions: read

jobs:
  build:
    runs-on: windows-latest
    # ... 其他配置
```

### macOS构建工作流

```yaml
name: Build macOS Application

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
  release:
    types: [ published ]

# 添加权限配置
permissions:
  contents: write
  actions: read

jobs:
  build:
    runs-on: macos-latest
    # ... 其他配置
```

## 🚨 其他可能的权限问题

### 1. 仓库设置检查

确保在GitHub仓库设置中：

1. **Actions权限**:
   - 进入仓库 → Settings → Actions → General
   - 确保 "Actions permissions" 设置为 "Allow all actions and reusable workflows"

2. **Workflow permissions**:
   - 在 "Workflow permissions" 部分
   - 勾选 "Read and write permissions"
   - 勾选 "Allow GitHub Actions to create and approve pull requests"

### 2. 组织权限检查

如果仓库属于组织，确保：

1. **组织设置**:
   - 组织管理员已启用Actions
   - 组织策略允许工作流运行

2. **成员权限**:
   - 您的账户有足够的权限运行Actions
   - 仓库访问权限设置正确

## 🔍 故障排除步骤

### 步骤1: 检查工作流文件
- 确认已添加 `permissions` 配置
- 检查YAML语法是否正确

### 步骤2: 检查仓库设置
- 验证Actions权限设置
- 确认工作流权限配置

### 步骤3: 检查组织设置
- 如果是组织仓库，联系管理员
- 确认组织策略设置

### 步骤4: 重新运行工作流
- 手动触发工作流
- 检查Actions日志中的错误信息

## 📚 相关文档

- [GitHub Actions权限文档](https://docs.github.com/en/actions/security-guides/automatic-token-authentication#permissions-for-the-github_token)
- [工作流权限配置](https://docs.github.com/en/actions/using-jobs/assigning-permissions-to-jobs)
- [仓库设置说明](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository)

## 💡 最佳实践

1. **最小权限原则**: 只授予必要的权限
2. **定期检查**: 定期审查权限设置
3. **安全更新**: 及时更新GitHub Actions版本
4. **日志监控**: 监控Actions运行日志

---

**注意**: 修改权限配置后，需要重新提交代码并推送，新的权限设置才会生效。
