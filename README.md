# QuizQuest — 交互式课程学习闯关

[![CI](https://github.com/Enchore/QuizQuest/actions/workflows/ci.yml/badge.svg)](https://github.com/Enchore/QuizQuest/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> 面向大学生课程复习的本地答题练习工具 | Tkinter + SQLite

## 项目简介

一个用于课后自测的桌面答题工具。内置计算机专业与思政两类示例题库，支持自建课程与自定义题目，答题记录与得分持久化到本地 SQLite 数据库。

项目定位是**单机轻量练习工具**，不依赖网络，所有数据保存在本地。

## 功能特性

- **多课程管理**：新建、删除、浏览课程，课程以 JSON 文件存储
- **五种题型**：单选、多选、判断、填空、简答
- **章节划分**：题目按 unit（章节）组织，可针对章节练习
- **答题会话**：连续答题、即时判分、答错给出解析
- **成绩记录**：答题记录与得分写入 SQLite，可回溯历史成绩
- **题库导入**：从 JSON 文件导入题目扩充题库
- **音频反馈**：答对／答错可播放提示音（需自备音频文件，见下方说明）

## 技术栈

| 类别 | 技术 |
|------|------|
| 语言 | Python 3.8+ |
| 桌面 GUI | Tkinter / ttk |
| 数据存储 | SQLite3 |
| 第三方依赖 | **无**，仅使用 Python 标准库 |

## 项目结构

```
QuizQuest/
├── app/                      # 主应用
│   ├── main.py               # 入口，初始化并启动 Tkinter 主循环
│   ├── quiz_engine.py        # 答题引擎：会话管理、判分、出题
│   ├── course_manager.py     # 课程增删改查，加载 JSON 题库
│   └── ui/
│       ├── main_window.py    # 主窗口：课程列表、新建课程、导入题目
│       └── quiz_window.py    # 答题窗口：逐题作答与结果反馈
├── questions/                # 题库数据（JSON）
│   ├── sample_cs.json        # 示例：数据结构与算法
│   └── sample_politics.json  # 示例：思政课程
├── utils/
│   ├── db_helper.py          # SQLite 封装：users / quiz_records 表
│   └── audio_player.py       # 调用系统默认播放器的音频反馈
├── assets/
│   ├── css/                  # 预留的 Web 端样式（当前未使用）
│   ├── js/                   # 预留的 Web 端脚本（当前未使用）
│   └── audio/                # 音频资源目录——需自行放入音频文件
└── requirements.txt
```

## 快速开始

```bash
git clone https://github.com/Enchore/QuizQuest.git
cd QuizQuest

# 本项目零第三方依赖，无需 pip install
python -m app.main
```

> Windows 若提示 tkinter 不可用，请确认安装 Python 时勾选了 "tcl/tk and IDLE" 组件。

## 题库格式

自定义课程请在 `questions/` 下新建 JSON 文件，结构如下：

```json
{
  "course_id": "cs_data_structures",
  "course_name": "数据结构与算法",
  "description": "课程描述",
  "category": "cs",
  "units": [
    { "unit_id": "linear_list", "unit_name": "线性表" },
    { "unit_id": "tree", "unit_name": "树与二叉树" }
  ],
  "questions": [
    {
      "id": "q_001",
      "unit_id": "linear_list",
      "type": "single_choice",
      "stem": "题干",
      "options": ["选项A", "选项B", "选项C", "选项D"],
      "answer": "A",
      "explanation": "解析文本"
    }
  ]
}
```

`type` 可选值：`single_choice`、`multiple_choice`、`true_false`、`fill_blank`、`short_answer`。

## 关于音频反馈

`utils/audio_player.py` 已实现播放逻辑，通过系统默认播放器播放音频。仓库**未内置音频文件**，如需启用，请将音频放入 `assets/audio/` 目录。未放置音频时程序正常运行，仅无提示音。

## 当前边界

以下是本项目**尚未实现**的内容，列出以免误解：

- 无 3D 视觉效果
- 无联网功能，不含任何在线语义解析或题型自动更新
- 无 Web 界面（`assets/css`、`assets/js` 为预留目录，当前未接入）
- 无单元测试与 CI

## 许可证

本项目基于 [MIT License](LICENSE) 开源。
