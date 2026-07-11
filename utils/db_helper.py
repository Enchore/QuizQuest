"""
数据库操作辅助模块。

封装 SQLite 数据库的初始化、增删改查操作，提供用户进度与答题记录的持久化存储。
"""

import sqlite3
from typing import Optional, List, Dict, Any
from contextlib import contextmanager


class DBHelper:
    """SQLite 数据库操作辅助类。"""

    def __init__(self, db_path: str = "quizquest.db"):
        """
        初始化数据库辅助类。

        Args:
            db_path: 数据库文件路径
        """
        self._db_path = db_path
        self._init_tables()

    @contextmanager
    def _get_connection(self):
        """获取数据库连接上下文管理器。"""
        conn = sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def _init_tables(self):
        """初始化数据库表结构。"""
        with self._get_connection() as conn:
            cursor = conn.cursor()

            # 用户表
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            # 答题记录表
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS quiz_records (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    course_id TEXT NOT NULL,
                    score INTEGER DEFAULT 0,
                    total INTEGER DEFAULT 0,
                    completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            """)

    def save_quiz_record(self, user_id: int, course_id: str,
                         score: int, total: int) -> int:
        """
        保存答题记录。

        Args:
            user_id: 用户 ID
            course_id: 课程 ID
            score: 得分
            total: 总题数

        Returns:
            记录 ID
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO quiz_records (user_id, course_id, score, total) "
                "VALUES (?, ?, ?, ?)",
                (user_id, course_id, score, total)
            )
            return cursor.lastrowid

    def get_user_records(self, user_id: int) -> List[Dict[str, Any]]:
        """获取用户的所有答题记录。"""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM quiz_records WHERE user_id = ? ORDER BY completed_at DESC",
                (user_id,)
            )
            return [dict(row) for row in cursor.fetchall()]
