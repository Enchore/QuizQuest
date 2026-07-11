"""
课程管理模块。

负责课程的创建、加载、删除以及课程内题库的管理。
支持从 JSON 文件导入题目数据。
"""

import json
import os
from typing import List, Dict, Optional
from dataclasses import dataclass, field


@dataclass
class Course:
    """课程数据类。"""
    id: str
    name: str
    description: str
    category: str  # "cs" / "politics" / "custom"
    question_count: int = 0
    units: List[Dict] = field(default_factory=list)


class CourseManager:
    """课程管理器，负责课程与题库的 CRUD 操作。"""

    def __init__(self, data_dir: str = "questions"):
        """
        初始化课程管理器。

        Args:
            data_dir: 题库数据目录路径
        """
        self._data_dir = data_dir
        self._courses: Dict[str, Course] = {}
        self._load_all_courses()

    def _load_all_courses(self):
        """从数据目录加载所有课程。"""
        if not os.path.exists(self._data_dir):
            return

        for filename in os.listdir(self._data_dir):
            if filename.endswith(".json"):
                filepath = os.path.join(self._data_dir, filename)
                self._load_course_from_file(filepath)

    def _load_course_from_file(self, filepath: str):
        """从 JSON 文件加载单个课程。"""
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        course = Course(
            id=data.get("course_id", ""),
            name=data.get("course_name", ""),
            description=data.get("description", ""),
            category=data.get("category", "custom"),
            question_count=len(data.get("questions", [])),
            units=data.get("units", [])
        )
        self._courses[course.id] = course

    def get_all_courses(self) -> List[Course]:
        """获取所有课程列表。"""
        return list(self._courses.values())

    def get_course(self, course_id: str) -> Optional[Course]:
        """根据 ID 获取课程。"""
        return self._courses.get(course_id)

    def create_course(self, course: Course) -> bool:
        """创建新课程。"""
        if course.id in self._courses:
            return False
        self._courses[course.id] = course
        return True

    def delete_course(self, course_id: str) -> bool:
        """删除课程。"""
        if course_id in self._courses:
            del self._courses[course_id]
            return True
        return False
