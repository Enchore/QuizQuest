"""
QuizQuest 主窗口模块。

提供主界面的布局、课程列表展示、新建课程入口等功能。
"""

import tkinter as tk
from tkinter import ttk, messagebox
from typing import Optional
from app.course_manager import CourseManager


class MainWindow(ttk.Frame):
    """主窗口框架，展示课程列表与导航。"""

    def __init__(self, parent: tk.Tk, course_mgr: CourseManager):
        """
        初始化主窗口。

        Args:
            parent: 父 Tkinter 窗口
            course_mgr: 课程管理器实例
        """
        super().__init__(parent)
        self._course_mgr = course_mgr
        self._setup_ui()

    def _setup_ui(self):
        """构建主界面布局。"""
        # 顶部标题栏
        header = ttk.LabelFrame(self, text="QuizQuest — 课程列表", padding=10)
        header.pack(fill=tk.X, padx=10, pady=5)

        ttk.Label(header, text="选择一门课程开始学习：",
                  font=("Microsoft YaHei", 12)).pack(anchor=tk.W)

        # 课程列表区域
        list_frame = ttk.Frame(self)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self._course_tree = ttk.Treeview(
            list_frame, columns=("name", "category", "count"),
            show="headings", height=15
        )
        self._course_tree.heading("name", text="课程名称")
        self._course_tree.heading("category", text="分类")
        self._course_tree.heading("count", text="题目数量")
        self._course_tree.column("name", width=300)
        self._course_tree.column("category", width=100)
        self._course_tree.column("count", width=100)

        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL,
                                  command=self._course_tree.yview)
        self._course_tree.configure(yscrollcommand=scrollbar.set)

        self._course_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # 底部按钮栏
        btn_frame = ttk.Frame(self, padding=10)
        btn_frame.pack(fill=tk.X, padx=10, pady=5)

        ttk.Button(btn_frame, text="开始答题",
                   command=self._start_quiz).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="新建课程",
                   command=self._create_course).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="导入题库",
                   command=self._import_questions).pack(side=tk.LEFT, padx=5)

        # 加载课程数据
        self._refresh_course_list()

    def _refresh_course_list(self):
        """刷新课程列表。"""
        for item in self._course_tree.get_children():
            self._course_tree.delete(item)

        courses = self._course_mgr.get_all_courses()
        for course in courses:
            self._course_tree.insert("", tk.END, iid=course.id, values=(
                course.name, course.category, course.question_count
            ))

    def _start_quiz(self):
        """开始答题。"""
        selection = self._course_tree.selection()
        if not selection:
            messagebox.showwarning("提示", "请先选择一门课程")
            return
        # TODO: 打开答题窗口
        pass

    def _create_course(self):
        """新建课程。"""
        # TODO: 打开课程创建对话框
        pass

    def _import_questions(self):
        """导入题库。"""
        # TODO: 打开文件选择对话框导入 JSON 题库
        pass
