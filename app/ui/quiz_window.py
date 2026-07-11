"""
答题窗口模块。

提供答题界面的题目展示、选项选择、答案提交、解析查看等功能。
支持流式对话式答题体验。
"""

import tkinter as tk
from tkinter import ttk, scrolledtext
from typing import Optional
from app.quiz_engine import QuizEngine, QuizSession


class QuizWindow(ttk.Frame):
    """答题窗口框架，展示题目并提供交互式答题。"""

    def __init__(self, parent, session: QuizSession, engine: QuizEngine):
        """
        初始化答题窗口。

        Args:
            parent: 父容器
            session: 当前答题会话
            engine: 答题引擎实例
        """
        super().__init__(parent)
        self._session = session
        self._engine = engine
        self._setup_ui()

    def _setup_ui(self):
        """构建答题界面布局。"""
        # 进度条
        progress_frame = ttk.Frame(self)
        progress_frame.pack(fill=tk.X, padx=10, pady=5)

        self._progress_var = tk.StringVar(value="进度: 0/0")
        ttk.Label(progress_frame, textvariable=self._progress_var,
                  font=("Microsoft YaHei", 10)).pack(side=tk.LEFT)

        # 进度条控件
        self._progress_bar = ttk.Progressbar(
            progress_frame, mode="determinate", length=300
        )
        self._progress_bar.pack(side=tk.LEFT, padx=10)

        # 题目区域
        question_frame = ttk.LabelFrame(self, text="题目", padding=10)
        question_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self._question_text = scrolledtext.ScrolledText(
            question_frame, height=8, font=("Microsoft YaHei", 11),
            wrap=tk.WORD, state=tk.DISABLED
        )
        self._question_text.pack(fill=tk.BOTH, expand=True)

        # 选项区域
        options_frame = ttk.LabelFrame(self, text="选项", padding=10)
        options_frame.pack(fill=tk.X, padx=10, pady=5)

        self._option_var = tk.StringVar()
        self._option_buttons = []

        # 答案提交按钮
        btn_frame = ttk.Frame(self, padding=10)
        btn_frame.pack(fill=tk.X, padx=10, pady=5)

        ttk.Button(btn_frame, text="提交答案",
                   command=self._submit_answer).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="下一题",
                   command=self._next_question).pack(side=tk.LEFT, padx=5)

        # 解析区域
        self._explanation_frame = ttk.LabelFrame(self, text="解析", padding=10)
        self._explanation_text = scrolledtext.ScrolledText(
            self._explanation_frame, height=6, font=("Microsoft YaHei", 10),
            wrap=tk.WORD, state=tk.DISABLED
        )
        self._explanation_text.pack(fill=tk.BOTH, expand=True)

    def display_question(self):
        """显示当前题目。"""
        # TODO: 从 session 中获取当前题目并显示
        pass

    def _submit_answer(self):
        """提交当前题目答案。"""
        # TODO: 调用引擎校验答案
        pass

    def _next_question(self):
        """跳转到下一题。"""
        # TODO: 加载下一道题目
        pass
