# 元素周期表查询工具 (Periodic Table Query Tool)

一个功能完整的化学元素周期表查询工具，支持通过元素符号或中文名称快速查找元素信息。

A comprehensive chemical periodic table query tool that supports quick element lookup by symbol or Chinese name.

## 🌟 功能特点 (Features)

- **多语言支持**: 支持中文和英文界面
- **智能搜索**: 支持元素符号、中文名称、英文名称搜索
- **完整信息**: 包含118种已知化学元素的详细信息
- **分类展示**: 信息按类别分页显示，便于查看
- **美观界面**: 现代化GUI设计，用户体验友好
- **跨平台**: 支持Windows、macOS和Linux系统
- **自动化构建**: GitHub Actions自动构建和发布

## 🚀 快速开始 (Quick Start)

### 环境要求 (Requirements)
- Python 3.7+
- tkinter (Python标准库，通常已预装)

### 安装步骤 (Installation)

1. 克隆仓库 (Clone the repository)
```bash
git clone https://github.com/yourusername/PeriodicTableApp.git
cd PeriodicTableApp
```

2. 运行应用程序 (Run the application)
```bash
python periodic_table_app.py
```

## 📖 使用说明 (Usage)

### 搜索元素 (Search Elements)

1. **通过元素符号搜索**: 输入如 `H`、`Fe`、`Au` 等
2. **通过中文名称搜索**: 输入如 `氢`、`铁`、`金` 等
3. **通过英文名称搜索**: 输入如 `Hydrogen`、`Iron`、`Gold` 等

### 查看信息 (View Information)

搜索结果分为三个标签页：

- **基本信息**: 元素符号、名称、原子序数等核心信息
- **详细信息**: 发现历史、外观特征、电子性质等
- **物理化学性质**: 密度、熔点、沸点、电子构型等

## 🛠️ 开发信息 (Development)

### 项目结构 (Project Structure)
```
PeriodicTableApp/
├── periodic_table_app.py    # 主应用程序
├── PeriodicTableJSON.json   # 元素数据文件
├── requirements.txt         # Python依赖
├── README.md               # 项目说明
├── QUICKSTART.md           # 快速启动指南
├── RELEASE_GUIDE.md        # 发布指南
├── .github/                # GitHub配置
│   └── workflows/         # GitHub Actions
│       ├── build-macos.yml
│       └── build-windows.yml
└── dist/                  # 构建输出目录
```

### 技术栈 (Tech Stack)
- **GUI框架**: tkinter (Python标准库)
- **数据处理**: JSON
- **打包工具**: PyInstaller
- **CI/CD**: GitHub Actions

## 🔄 自动化构建 (Automated Build)

本项目配置了完整的CI/CD流程，支持自动构建和发布：

### 触发条件
- **推送到main分支**: 自动构建测试版本
- **创建Pull Request**: 自动构建测试版本  
- **发布Release**: 自动构建正式版本并上传到Release页面

### 版本命名规则
- **测试版本**: 项目名称（如：`元素周期表查询工具.exe`）
- **正式版本**: 项目名称 + 版本号（如：`元素周期表查询工具-v1.0.0.exe`）

### 使用方法
1. 创建以`v`开头的Git标签（如：`v1.0.0`）
2. 在GitHub上发布Release
3. GitHub Actions自动构建并上传构建产物
4. 用户可在Release页面下载对应版本

详细说明请查看 [RELEASE_GUIDE.md](RELEASE_GUIDE.md)

## 📦 构建可执行文件 (Build Executable)

### 使用构建脚本
```bash
python build.py
```

### 使用auto-py-to-exe (Using auto-py-to-exe)

1. 安装auto-py-to-exe
```bash
pip install auto-py-to-exe
```

2. 启动图形界面
```bash
auto-py-to-exe
```

3. 选择文件并配置选项，然后构建

## 📊 数据来源 (Data Source)

元素数据来源于公开的化学数据库，包含：
- 原子序数、质量、电子构型
- 物理化学性质
- 发现历史和命名信息
- 元素分类和周期表位置

## 🤝 贡献指南 (Contributing)

欢迎提交Issue和Pull Request！

### 贡献方式 (Ways to Contribute)
1. 报告Bug
2. 提出新功能建议
3. 改进代码质量
4. 完善文档
5. 翻译界面文本

### 开发环境设置 (Development Setup)
1. Fork项目
2. 创建功能分支
3. 提交更改
4. 创建Pull Request

## 📄 许可证 (License)

本项目采用MIT许可证 - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢 (Acknowledgments)

- 感谢所有为化学元素发现做出贡献的科学家
- 感谢开源社区提供的工具和库
- 感谢用户提供的反馈和建议

## 📞 联系方式 (Contact)

- 项目主页: [GitHub Repository](https://github.com/yourusername/PeriodicTableApp)
- 问题反馈: [Issues](https://github.com/yourusername/PeriodicTableApp/issues)
- 邮箱: your.email@example.com

---

⭐ 如果这个项目对您有帮助，请给它一个星标！  
⭐ If this project helps you, please give it a star!
