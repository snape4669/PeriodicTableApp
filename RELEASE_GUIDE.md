# 🚀 发布指南 (Release Guide)

## 📋 概述

本指南说明如何使用GitHub Actions自动构建和发布元素周期表查询工具的不同版本。

## 🔄 自动化构建流程

### 触发条件

GitHub Actions会在以下情况下自动触发：

1. **推送到main分支**: 自动构建测试版本
2. **创建Pull Request**: 自动构建测试版本
3. **发布Release**: 自动构建正式版本并上传到Release页面

### 版本命名规则

- **测试版本**: 项目名称（如：`元素周期表查询工具.exe`、`PeriodicTableApp`）
- **正式版本**: 项目名称 + 版本号（如：`元素周期表查询工具-v1.0.0.exe`、`PeriodicTableApp-v1.0.0`）

## 🏷️ 创建Release版本

### 步骤1: 创建Git标签

在GitHub上创建新的Release时，使用以下格式的标签：

```
v1.0.0
v1.1.0
v2.0.0
```

**重要**: 标签必须以 `v` 开头，后面跟版本号。

### 步骤2: 发布Release

1. 在GitHub仓库页面，点击 "Releases"
2. 点击 "Create a new release"
3. 选择刚才创建的标签（如：`v1.0.0`）
4. 填写Release标题和描述
5. 选择 "Publish release"

### 步骤3: 自动构建

发布Release后，GitHub Actions会自动：

1. 检测到新的Release标签
2. 提取版本号（去掉v前缀）
3. 构建对应版本的可执行文件
4. 将构建产物上传到Release页面
5. 提供下载链接

## 📦 构建产物

### Windows版本

- **文件名**: `元素周期表查询工具-v{版本号}.exe`
- **类型**: 独立的可执行文件
- **系统要求**: Windows 10+
- **特点**: 即开即用，无需安装Python

### macOS版本

- **可执行文件**: `PeriodicTableApp-v{版本号}`
- **应用程序包**: `PeriodicTableApp-v{版本号}.app`
- **系统要求**: macOS 10.13+
- **特点**: 标准的macOS应用程序

## 🔧 手动触发构建

### 通过GitHub Actions页面

1. 进入仓库的 "Actions" 标签页
2. 选择对应的工作流（Windows或macOS）
3. 点击 "Run workflow"
4. 选择分支和参数
5. 点击 "Run workflow"

### 通过API调用

```bash
# 触发Windows构建
curl -X POST \
  -H "Authorization: token YOUR_GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/OWNER/REPO/actions/workflows/build-windows.yml/dispatches \
  -d '{"ref":"main"}'

# 触发macOS构建
curl -X POST \
  -H "Authorization: token YOUR_GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/OWNER/REPO/actions/workflows/build-macos.yml/dispatches \
  -d '{"ref":"main"}'
```

## 📊 构建状态监控

### 查看构建日志

1. 进入 "Actions" 标签页
2. 点击具体的构建任务
3. 查看详细的构建日志
4. 下载构建产物（Artifacts）

### 构建失败排查

常见问题及解决方案：

1. **Python版本问题**
   - 确保使用Python 3.9+
   - 检查依赖包安装

2. **PyInstaller问题**
   - 检查requirements.txt
   - 验证Python环境

3. **权限问题**
   - 检查GitHub Actions权限设置
   - 验证仓库访问权限

## 🎯 最佳实践

### 版本管理

1. **语义化版本**: 使用 `MAJOR.MINOR.PATCH` 格式
2. **预发布版本**: 使用 `v1.0.0-alpha.1` 格式
3. **发布说明**: 详细描述新功能和修复

### 构建优化

1. **缓存依赖**: 利用GitHub Actions缓存机制
2. **并行构建**: Windows和macOS可以同时构建
3. **条件构建**: 只在必要时触发构建

### 发布流程

1. **代码审查**: 确保代码质量
2. **测试验证**: 本地测试通过后再发布
3. **文档更新**: 同步更新README和文档
4. **用户通知**: 在Release中说明重要变更

## 📞 故障排除

### 常见错误

1. **版本号解析失败**
   - 确保标签格式正确（v开头）
   - 检查GitHub Actions语法

2. **构建产物上传失败**
   - 检查文件路径
   - 验证权限设置

3. **Release创建失败**
   - 检查GitHub Token权限
   - 验证仓库设置

### 获取帮助

- **GitHub Issues**: 报告问题
- **Actions日志**: 查看详细错误信息
- **社区支持**: 寻求帮助和建议

## 🔮 未来改进

计划中的功能：

1. **多架构支持**: ARM64、x86_64等
2. **自动测试**: 构建后自动运行测试
3. **代码签名**: 数字签名验证
4. **增量更新**: 支持增量更新机制

---

**享受自动化构建的便利！** 🚀✨
