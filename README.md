# QuizQuest — 交互式课程学习闯关

> 交互式课程学习闯关 | Interactive Course Learning & Quiz Platform

## 项目简介

QuizQuest 是针对自我课程复习而建立的项目；面向大学生各项课程答题后备考的辅助交互式测试平台。包含不同的计算机专业课程以及思政类课程，采用流式对话、自设考题、对应单元测试试题有详尽解析。可从「新建课程」处进入创建，可选内置联网语义进行语意导入和题型更新。为提升趣味性，研习了音频辅助和子系统加之 3D 视觉效果。

## 功能特性

- **多课程支持**：覆盖计算机专业课程及思政类课程
- **交互式答题**：流式对话式答题体验，支持详尽解析
- **自定义题库**：支持自设考题与单元测试
- **智能语义导入**：内置联网语义功能，支持语意导入和题型更新
- **音频辅助**：音频辅助功能提升学习体验
- **3D 视觉效果**：子系统集成 3D 视觉效果增强趣味性
- **SQLite 数据存储**：本地数据库存储题目与用户进度

## 技术栈

| 类别 | 技术 |
|------|------|
| 后端 | Python, Tkinter, SQLite |
| 前端 | HTML, CSS, JavaScript |
| 桌面 GUI | Tkinter |

## 项目结构

```
QuizQuest/
├── app/                  # 主应用程序代码
│   ├── __init__.py
│   ├── main.py           # 应用入口
│   ├── quiz_engine.py    # 答题引擎核心逻辑
│   ├── course_manager.py # 课程管理模块
│   └── ui/               # 界面相关模块
│       ├── __init__.py
│       ├── main_window.py
│       └── quiz_window.py
├── questions/            # 示例题库数据
│   ├── __init__.py
│   ├── sample_cs.json    # 计算机专业课程示例题目
│   └── sample_politics.json # 思政类课程示例题目
├── utils/                # 工具函数
│   ├── __init__.py
│   ├── db_helper.py      # 数据库操作辅助
│   └── audio_player.py   # 音频播放辅助
├── assets/               # 静态资源
│   ├── css/
│   ├── js/
│   └── audio/
├── README.md
├── .gitignore
└── LICENSE
```

## 快速开始

```bash
# 克隆项目
git clone https://github.com/Enchore/QuizQuest.git
cd QuizQuest

# 安装依赖
pip install -r requirements.txt

# 启动应用
python -m app.main
```

## 贡献

欢迎提交 Issue 和 Pull Request。

## 许可证

本项目基于 [MIT License](LICENSE) 开源。
