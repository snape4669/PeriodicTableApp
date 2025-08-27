# 🚀 Release工作流说明

## 概述

本项目配置了完整的GitHub Actions Release工作流，能够自动构建多平台应用程序并上传为Release附件。

## 工作流文件

### 1. `build-windows.yml` / `build-macos.yml`
- **触发条件**: 推送到main分支、Pull Request、Release发布
- **功能**: 构建对应平台的应用程序
- **输出**: 构建产物和Artifacts

### 2. `release.yml` (新增)
- **触发条件**: 仅Release发布时
- **功能**: 专门处理Release构建和上传
- **输出**: 自动上传到GitHub Release页面

## Release工作流流程

### 阶段1: 并行构建
```
┌─────────────────┐    ┌─────────────────┐
│   Windows构建   │    │   macOS构建     │
│                 │    │                 │
│ • 安装依赖      │    │ • 安装依赖      │
│ • PyInstaller   │    │ • PyInstaller   │
│ • 生成.exe      │    │ • 生成可执行文件│
│ • 验证构建      │    │ • 创建.app包    │
│ • 上传Artifact  │    │ • 验证构建      │
└─────────────────┘    │ • 上传Artifact  │
                       └─────────────────┘
```

### 阶段2: 统一上传
```
┌─────────────────────────────────────────┐
│            Release上传                   │
│                                         │
│ • 下载Windows Artifacts                 │
│ • 下载macOS Artifacts                   │
│ • 验证文件完整性                        │
│ • 上传到GitHub Release                  │
│ • 生成Release说明文档                   │
└─────────────────────────────────────────┘
```

## 构建产物

### Windows平台
- **文件名**: `元素周期表查询工具-v{版本号}.exe`
- **特点**: 单文件可执行程序，无需安装

### macOS平台
- **可执行文件**: `PeriodicTableApp-v{版本号}`
- **应用程序包**: `PeriodicTableApp-v{版本号}.app`
- **特点**: 标准的macOS应用程序包

## 使用方法

### 1. 创建Release标签
```bash
# 本地创建标签
git tag v1.0.0

# 推送标签到GitHub
git push origin v1.0.0
```

### 2. 在GitHub上发布Release
1. 进入GitHub仓库页面
2. 点击 "Releases" 标签
3. 点击 "Create a new release"
4. 选择刚创建的标签 `v1.0.0`
5. 填写Release标题和说明
6. 点击 "Publish release"

### 3. 自动构建和上传
- GitHub Actions自动触发Release工作流
- 并行构建Windows和macOS版本
- 自动上传构建产物到Release页面
- 用户可在Release页面下载对应平台的应用程序

## 工作流优势

### ✅ 自动化程度高
- 无需手动构建和上传
- 自动版本号识别和命名
- 自动生成Release说明文档

### ✅ 多平台支持
- Windows和macOS并行构建
- 统一的Release管理
- 一致的版本号命名规则

### ✅ 质量保证
- 构建验证步骤
- 文件完整性检查
- 详细的构建日志

### ✅ 用户体验
- 一键下载对应平台版本
- 清晰的Release说明
- 版本历史记录完整

## 故障排除

### 常见问题

1. **构建失败**
   - 检查Python依赖是否正确
   - 确认PyInstaller版本兼容性
   - 查看构建日志中的具体错误

2. **上传失败**
   - 确认GitHub权限配置
   - 检查网络连接
   - 验证Release标签格式

3. **文件缺失**
   - 检查构建产物路径
   - 确认Artifacts上传成功
   - 验证文件命名规则

### 调试方法

1. **查看工作流日志**
   - 在GitHub Actions页面查看详细日志
   - 关注每个步骤的输出信息

2. **本地测试**
   - 使用`build.py`脚本本地构建
   - 验证构建产物完整性

3. **权限检查**
   - 确认仓库的Actions权限设置
   - 检查`GITHUB_TOKEN`权限

## 配置说明

### 权限配置
```yaml
permissions:
  contents: write    # 允许创建Release和上传文件
  actions: read      # 允许读取Actions信息
```

### 触发条件
```yaml
on:
  release:
    types: [ published ]  # 仅在Release发布时触发
```

### 依赖关系
```yaml
needs: [build-windows, build-macos]  # 等待所有构建完成
```

## 更新日志

- **v1.0.0**: 初始Release工作流配置
- **v1.1.0**: 优化构建流程，添加验证步骤
- **v1.2.0**: 新增专门的Release工作流文件

---

## 📞 技术支持

如果您在使用Release工作流时遇到问题：

1. 查看GitHub Actions日志
2. 检查权限配置
3. 参考故障排除指南
4. 创建Issue寻求帮助

感谢使用我们的自动化构建系统！🎉
