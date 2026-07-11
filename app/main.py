"""
QuizQuest 应用入口文件。

初始化数据库、创建主窗口并启动 Tkinter 事件循环。
"""

import tkinter as tk
from app.course_manager import CourseManager
from app.ui.main_window import MainWindow


def main():
    """应用主入口函数。"""
    root = tk.Tk()
    root.title("QuizQuest — 交互式课程学习闯关")

    # 初始化课程管理器
    course_mgr = CourseManager()

    # 创建并显示主窗口
    app = MainWindow(root, course_mgr)
    app.pack(fill=tk.BOTH, expand=True)

    # 设置窗口大小和居中
    root.geometry("1200x800")
    root.update_idletasks()
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) // 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) // 2
    root.geometry(f"+{x}+{y}")

    root.mainloop()


if __name__ == "__main__":
    main()
