#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
元素周期表查询工具
Periodic Table Query Tool

支持通过化学元素符号或中文名称查询元素信息
Supports querying element information by chemical symbol or Chinese name
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import re
from typing import Dict, List, Optional, Any
from elements_data import get_elements_data, get_element_by_symbol, get_element_by_name, search_elements

class PeriodicTableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("元素周期表查询工具 - Periodic Table Query Tool")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f0f0')
        
        # 加载元素数据
        self.elements_data = self.load_elements_data()
        
        # 创建中文名称映射
        self.chinese_names = self.create_chinese_names_mapping()
        
        # 创建主界面
        self.create_widgets()
        
        # 设置样式
        self.setup_styles()
        
    def load_elements_data(self) -> Dict[str, Any]:
        """加载元素周期表数据"""
        try:
            data = get_elements_data()
            return data
        except Exception as e:
            messagebox.showerror("错误", f"无法加载元素数据: {str(e)}")
            return {"elements": []}
    
    def create_chinese_names_mapping(self) -> Dict[str, str]:
        """创建中文名称映射表"""
        chinese_names = {
            # 第1周期
            "H": "氢", "He": "氦",
            # 第2周期
            "Li": "锂", "Be": "铍", "B": "硼", "C": "碳", "N": "氮", "O": "氧", "F": "氟", "Ne": "氖",
            # 第3周期
            "Na": "钠", "Mg": "镁", "Al": "铝", "Si": "硅", "P": "磷", "S": "硫", "Cl": "氯", "Ar": "氩",
            # 第4周期
            "K": "钾", "Ca": "钙", "Sc": "钪", "Ti": "钛", "V": "钒", "Cr": "铬", "Mn": "锰", "Fe": "铁",
            "Co": "钴", "Ni": "镍", "Cu": "铜", "Zn": "锌", "Ga": "镓", "Ge": "锗", "As": "砷", "Se": "硒",
            "Br": "溴", "Kr": "氪",
            # 第5周期
            "Rb": "铷", "Sr": "锶", "Y": "钇", "Zr": "锆", "Nb": "铌", "Mo": "钼", "Tc": "锝", "Ru": "钌",
            "Rh": "铑", "Pd": "钯", "Ag": "银", "Cd": "镉", "In": "铟", "Sn": "锡", "Sb": "锑", "Te": "碲",
            "I": "碘", "Xe": "氙",
            # 第6周期
            "Cs": "铯", "Ba": "钡", "La": "镧", "Ce": "铈", "Pr": "镨", "Nd": "钕", "Pm": "钷", "Sm": "钐",
            "Eu": "铕", "Gd": "钆", "Tb": "铽", "Dy": "镝", "Ho": "钬", "Er": "铒", "Tm": "铥", "Yb": "镱",
            "Lu": "镥", "Hf": "铪", "Ta": "钽", "W": "钨", "Re": "铼", "Os": "锇", "Ir": "铱", "Pt": "铂",
            "Au": "金", "Hg": "汞", "Tl": "铊", "Pb": "铅", "Bi": "铋", "Po": "钋", "At": "砹", "Rn": "氡",
            # 第7周期
            "Fr": "钫", "Ra": "镭", "Ac": "锕", "Th": "钍", "Pa": "镤", "U": "铀", "Np": "镎", "Pu": "钚",
            "Am": "镅", "Cm": "锔", "Bk": "锫", "Cf": "锎", "Es": "锿", "Fm": "镄", "Md": "钔", "No": "锘",
            "Lr": "铹", "Rf": "鑪", "Db": "𨧀", "Sg": "𨭎", "Bh": "𨨏", "Hs": "𨭆", "Mt": "鿏", "Ds": "𨧻",
            "Rg": "𨭊", "Cn": "鿔", "Nh": "鉨", "Fl": "鉝", "Mc": "镆", "Lv": "鉝", "Ts": "鿭", "Og": "鿬"
        }
        return chinese_names
    
    def create_widgets(self):
        """创建主界面组件"""
        # 主标题
        title_frame = tk.Frame(self.root, bg='#2c3e50')
        title_frame.pack(fill='x', padx=10, pady=10)
        
        title_label = tk.Label(
            title_frame, 
            text="元素周期表查询工具", 
            font=('Microsoft YaHei', 24, 'bold'),
            fg='white',
            bg='#2c3e50'
        )
        title_label.pack(pady=10)
        
        subtitle_label = tk.Label(
            title_frame,
            text="Periodic Table Query Tool",
            font=('Arial', 14),
            fg='#ecf0f1',
            bg='#2c3e50'
        )
        subtitle_label.pack(pady=5)
        
        # 搜索框架
        search_frame = tk.Frame(self.root, bg='#f0f0f0')
        search_frame.pack(fill='x', padx=20, pady=10)
        
        # 搜索标签
        search_label = tk.Label(
            search_frame,
            text="请输入元素符号或中文名称:",
            font=('Microsoft YaHei', 12),
            bg='#f0f0f0'
        )
        search_label.pack(side='left', padx=(0, 10))
        
        # 搜索输入框
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(
            search_frame,
            textvariable=self.search_var,
            font=('Arial', 14),
            width=20
        )
        self.search_entry.pack(side='left', padx=(0, 10))
        self.search_entry.bind('<Return>', self.search_element)
        
        # 搜索按钮
        search_button = tk.Button(
            search_frame,
            text="搜索",
            command=self.search_element,
            font=('Microsoft YaHei', 12),
            bg='#3498db',
            fg='black',
            relief='flat',
            padx=20
        )
        search_button.pack(side='left')
        
        # 清空按钮
        clear_button = tk.Button(
            search_frame,
            text="清空",
            command=self.clear_search,
            font=('Microsoft YaHei', 12),
            bg='#e74c3c',
            fg='black',
            relief='flat',
            padx=20
        )
        clear_button.pack(side='left', padx=(10, 0))
        
        # 结果显示区域
        result_frame = tk.Frame(self.root, bg='#f0f0f0')
        result_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # 创建Notebook用于分页显示
        self.notebook = ttk.Notebook(result_frame)
        self.notebook.pack(fill='both', expand=True)
        
        # 基本信息页面
        self.basic_info_frame = tk.Frame(self.notebook, bg='white')
        self.notebook.add(self.basic_info_frame, text="基本信息")
        
        # 详细信息页面
        self.detailed_info_frame = tk.Frame(self.notebook, bg='white')
        self.notebook.add(self.detailed_info_frame, text="详细信息")
        
        # 物理化学性质页面
        self.properties_frame = tk.Frame(self.notebook, bg='white')
        self.notebook.add(self.properties_frame, text="物理化学性质")
        
        # 初始化显示欢迎信息
        self.show_welcome_message()
    
    def setup_styles(self):
        """设置界面样式"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # 配置Notebook样式
        style.configure('TNotebook', background='#f0f0f0')
        style.configure('TNotebook.Tab', padding=[10, 5], font=('Microsoft YaHei', 10))
    
    def show_welcome_message(self):
        """显示欢迎信息"""
        welcome_text = """
欢迎使用元素周期表查询工具！

使用方法：
1. 在搜索框中输入化学元素符号（如：H、Fe、Au）
2. 或输入中文名称（如：氢、铁、金）
3. 按回车键或点击搜索按钮
4. 查看元素的详细信息

支持的元素：
• 所有118种已知化学元素
• 包括最新的超重元素
• 提供完整的物理化学性质数据

开始搜索您感兴趣的元素吧！
        """
        
        self.clear_all_frames()
        
        welcome_label = tk.Label(
            self.basic_info_frame,
            text=welcome_text,
            font=('Microsoft YaHei', 12),
            bg='white',
            justify='left',
            wraplength=800
        )
        welcome_label.pack(expand=True, fill='both', padx=20, pady=20)
    
    def search_element(self, event=None):
        """搜索元素"""
        query = self.search_var.get().strip()
        if not query:
            messagebox.showwarning("警告", "请输入搜索内容")
            return
        
        # 查找元素
        element = self.find_element(query)
        
        if element:
            self.display_element_info(element)
        else:
            messagebox.showinfo("搜索结果", f"未找到元素: {query}\n\n请尝试：\n• 检查拼写\n• 使用元素符号（如H、Fe）\n• 使用中文名称（如氢、铁）")
    
    def find_element(self, query: str) -> Optional[Dict[str, Any]]:
        """查找元素"""
        query = query.strip()
        
        # 首先尝试通过符号查找
        element = get_element_by_symbol(query)
        if element:
            return element
        
        # 然后尝试通过中文名称查找
        for symbol, chinese_name in self.chinese_names.items():
            if chinese_name.lower() == query.lower():
                element = get_element_by_symbol(symbol)
                if element:
                    return element
        
        # 最后尝试通过英文名称查找
        element = get_element_by_name(query)
        if element:
            return element
        
        return None
    
    def display_element_info(self, element: Dict[str, Any]):
        """显示元素信息"""
        self.clear_all_frames()
        
        # 基本信息页面
        self.create_basic_info_page(element)
        
        # 详细信息页面
        self.create_detailed_info_page(element)
        
        # 物理化学性质页面
        self.create_properties_page(element)
    
    def create_basic_info_page(self, element: Dict[str, Any]):
        """创建基本信息页面"""
        # 元素符号（大字体加粗）
        symbol_label = tk.Label(
            self.basic_info_frame,
            text=element.get("symbol", ""),
            font=('Arial', 72, 'bold'),
            fg='#2c3e50',
            bg='white'
        )
        symbol_label.pack(pady=(20, 10))
        
        # 元素名称
        name_frame = tk.Frame(self.basic_info_frame, bg='white')
        name_frame.pack(fill='x', padx=20)
        
        name_label = tk.Label(
            name_frame,
            text=f"英文名称: {element.get('name', 'N/A')}",
            font=('Arial', 14),
            bg='white'
        )
        name_label.pack(anchor='w')
        
        chinese_name = self.chinese_names.get(element.get("symbol", ""), "未知")
        chinese_label = tk.Label(
            name_frame,
            text=f"中文名称: {chinese_name}",
            font=('Microsoft YaHei', 14),
            bg='white'
        )
        chinese_label.pack(anchor='w', pady=(5, 0))
        
        # 基本信息表格
        info_frame = tk.Frame(self.basic_info_frame, bg='white')
        info_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # 创建表格
        tree = ttk.Treeview(info_frame, columns=('属性', '值'), show='headings', height=8)
        tree.heading('属性', text='属性')
        tree.heading('值', text='值')
        tree.column('属性', width=200)
        tree.column('值', width=400)
        
        # 添加数据
        basic_info = [
            ("原子序数", str(element.get("number", "N/A"))),
            ("周期", str(element.get("period", "N/A"))),
            ("族", str(element.get("group", "N/A"))),
            ("元素类别", element.get("category", "N/A")),
            ("物态", element.get("phase", "N/A")),
            ("发现者", element.get("discovered_by", "N/A")),
            ("命名者", element.get("named_by", "N/A")),
            ("电子构型", element.get("electron_configuration", "N/A")),
            ("电子构型语义", element.get("electron_configuration_semantic", "N/A")),
            ("电子层", str(element.get("shells", "N/A"))),
        ]
        
        for info in basic_info:
            tree.insert('', 'end', values=info)
        
        tree.pack(fill='both', expand=True)
    
    def create_detailed_info_page(self, element: Dict[str, Any]):
        """创建详细信息页面"""
        # 创建滚动文本框
        text_widget = scrolledtext.ScrolledText(
            self.detailed_info_frame,
            wrap=tk.WORD,
            font=('Microsoft YaHei', 11),
            bg='white'
        )
        text_widget.pack(fill='both', expand=True, padx=20, pady=20)
        
        # 插入详细信息
        info_text = f"""
元素详细信息 - {element.get('name', 'N/A')} ({element.get('symbol', 'N/A')})

基本信息:
• 原子序数: {element.get('number', 'N/A')}
• 周期: {element.get('period', 'N/A')}
• 族: {element.get('group', 'N/A')}
• 元素类别: {element.get('category', 'N/A')}
• 物态: {element.get('phase', 'N/A')}
• 电子构型: {element.get('electron_configuration', 'N/A')}
• 电子构型语义: {element.get('electron_configuration_semantic', 'N/A')}
• 电子层: {element.get('shells', 'N/A')}

发现历史:
• 发现者: {element.get('discovered_by', 'N/A')}
• 命名者: {element.get('named_by', 'N/A')}

外观特征:
• 外观: {element.get('appearance', 'N/A')}

电子性质:
• 电子亲和能: {element.get('electron_affinity', 'N/A')} kJ/mol
• 电负性(鲍林标度): {element.get('electronegativity_pauling', 'N/A')}
• 电离能: {element.get('ionization_energies', 'N/A')} kJ/mol

元素描述:
{element.get('summary', 'N/A')}

更多信息请访问: {element.get('source', 'N/A')}
        """
        
        text_widget.insert('1.0', info_text)
        text_widget.config(state='disabled')  # 设置为只读
    
    def create_properties_page(self, element: Dict[str, Any]):
        """创建物理化学性质页面"""
        # 创建滚动文本框
        text_widget = scrolledtext.ScrolledText(
            self.properties_frame,
            wrap=tk.WORD,
            font=('Microsoft YaHei', 11),
            bg='white'
        )
        text_widget.pack(fill='both', expand=True, padx=20, pady=20)
        
        # 插入物理化学性质信息
        properties_text = f"""
物理化学性质 - {element.get('name', 'N/A')} ({element.get('symbol', 'N/A')})

原子性质:
• 原子质量: {element.get('atomic_mass', 'N/A')} u
• 原子序数: {element.get('number', 'N/A')}

物理性质:
• 密度: {element.get('density', 'N/A')} g/cm³
• 熔点: {element.get('melt', 'N/A')} K
• 沸点: {element.get('boil', 'N/A')} K
• 摩尔热容: {element.get('molar_heat', 'N/A')} J/(mol·K)

电子性质:
• 电子构型: {element.get('electron_configuration', 'N/A')}
• 电子构型语义: {element.get('electron_configuration_semantic', 'N/A')}
• 电子层: {element.get('shells', 'N/A')}
• 电子亲和能: {element.get('electron_affinity', 'N/A')} kJ/mol
• 电负性(鲍林标度): {element.get('electronegativity_pauling', 'N/A')}

电离能数据:
{element.get('ionization_energies', 'N/A')}

元素分类:
• 元素类别: {element.get('category', 'N/A')}
• 元素块: {element.get('block', 'N/A')}
• 周期: {element.get('period', 'N/A')}
• 族: {element.get('group', 'N/A')}

物态信息:
• 标准状态: {element.get('phase', 'N/A')}

颜色信息:
• CPK颜色代码: #{element.get('cpk-hex', 'N/A')}

注意: 某些数据可能为N/A，表示该信息不可用或尚未测定。
        """
        
        text_widget.insert('1.0', properties_text)
        text_widget.config(state='disabled')  # 设置为只读
    
    def clear_search(self):
        """清空搜索"""
        self.search_var.set("")
        self.show_welcome_message()
    
    def clear_all_frames(self):
        """清空所有框架内容"""
        for widget in self.basic_info_frame.winfo_children():
            widget.destroy()
        
        for widget in self.detailed_info_frame.winfo_children():
            widget.destroy()
        
        for widget in self.properties_frame.winfo_children():
            widget.destroy()

def main():
    """主函数"""
    root = tk.Tk()
    app = PeriodicTableApp(root)
    
    # 设置窗口图标（如果有的话）
    try:
        root.iconbitmap('icon.ico')
    except:
        pass
    
    # 启动应用程序
    root.mainloop()

if __name__ == "__main__":
    main()
