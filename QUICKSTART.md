# 🚀 快速启动指南 (Quick Start Guide)

## 📋 系统要求 (System Requirements)

- **操作系统**: Windows 10+, macOS 10.13+, Linux (Ubuntu 18.04+)
- **Python版本**: 3.7 或更高版本
- **内存**: 至少 100MB 可用内存
- **磁盘空间**: 至少 50MB 可用空间

## ⚡ 快速启动 (Quick Launch)

### Windows 用户
1. 双击 `run.bat` 文件
2. 或在命令提示符中运行：
   ```cmd
   python periodic_table_app.py
   ```

### macOS/Linux 用户
1. 在终端中运行：
   ```bash
   ./run.sh
   ```
2. 或直接运行：
   ```bash
   python3 periodic_table_app.py
   ```

### 通用方法
```bash
python periodic_table_app.py
```

## 🔍 使用说明 (Usage Instructions)

### 搜索元素
1. **元素符号**: 输入 `H`、`Fe`、`Au` 等
2. **中文名称**: 输入 `氢`、`铁`、`金` 等
3. **英文名称**: 输入 `Hydrogen`、`Iron`、`Gold` 等

### 查看信息
- **基本信息**: 元素符号、名称、原子序数等
- **详细信息**: 发现历史、外观特征、电子性质等
- **物理化学性质**: 密度、熔点、沸点、电子构型等

## 🛠️ 故障排除 (Troubleshooting)

### 常见问题

#### 1. Python未安装
**错误**: `python: command not found`
**解决方案**: 
- Windows: 从 [python.org](https://www.python.org/downloads/) 下载安装
- macOS: `brew install python3`
- Linux: `sudo apt-get install python3` (Ubuntu/Debian)

#### 2. tkinter模块缺失
**错误**: `ModuleNotFoundError: No module named 'tkinter'`
**解决方案**:
- Windows: 重新安装Python，确保勾选"tcl/tk and IDLE"
- macOS: `brew install python-tk`
- Linux: `sudo apt-get install python3-tk` (Ubuntu/Debian)

#### 3. 文件缺失
**错误**: 缺少必需文件
**解决方案**: 确保以下文件在同一目录中：
- `periodic_table_app.py`
- `PeriodicTableJSON.json`

#### 4. 权限问题 (Linux/macOS)
**错误**: `Permission denied`
**解决方案**: 
```bash
chmod +x run.sh
```

## 📱 界面预览 (Interface Preview)

应用程序包含以下主要区域：

```
┌─────────────────────────────────────────────────────────┐
│                元素周期表查询工具                        │
│              Periodic Table Query Tool                  │
├─────────────────────────────────────────────────────────┤
│ 请输入元素符号或中文名称: [搜索框] [搜索] [清空]        │
├─────────────────────────────────────────────────────────┤
│ [基本信息] [详细信息] [物理化学性质]                     │
│                                                         │
│                    H                                   │
│              英文名称: Hydrogen                        │
│              中文名称: 氢                              │
│                                                         │
│  ┌─────────────┬─────────────────────────────────────┐ │
│  │ 属性        │ 值                                   │ │
│  ├─────────────┼─────────────────────────────────────┤ │
│  │ 原子序数    │ 1                                    │ │
│  │ 周期        │ 1                                    │ │
│  │ 族          │ 1                                    │ │
│  │ 元素类别    │ diatomic nonmetal                    │ │
│  └─────────────┴─────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

## 🔧 高级功能 (Advanced Features)

### 键盘快捷键
- **Enter**: 执行搜索
- **Ctrl+Q**: 退出应用程序 (macOS: Cmd+Q)

### 搜索技巧
- 不区分大小写
- 支持部分匹配
- 自动补全建议

## 📦 构建可执行文件 (Build Executable)

### 使用构建脚本
```bash
python build.py
```

### 手动构建
```bash
# 安装PyInstaller
pip install pyinstaller

# 构建
pyinstaller --onefile --windowed periodic_table_app.py
```

## 📞 获取帮助 (Get Help)

- **GitHub Issues**: [提交问题](https://github.com/yourusername/PeriodicTableApp/issues)
- **文档**: 查看 [README.md](README.md)
- **测试**: 运行 `python test_app.py` 检查系统兼容性

## 🎯 下一步 (Next Steps)

1. **熟悉界面**: 尝试搜索不同的元素
2. **探索功能**: 查看各种标签页中的信息
3. **自定义**: 根据需要修改代码
4. **贡献**: 提交改进建议或代码

---

**享受探索元素周期表的乐趣！** 🧪⚗️🔬
