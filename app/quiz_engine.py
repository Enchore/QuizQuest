"""
答题引擎核心模块。

负责题目加载、答案校验、分数计算与答题进度管理。
支持流式对话式答题模式和单元测试模式。
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum


class QuestionType(Enum):
    """题目类型枚举。"""
    SINGLE_CHOICE = "single_choice"
    MULTIPLE_CHOICE = "multiple_choice"
    TRUE_FALSE = "true_false"
    FILL_IN_BLANK = "fill_blank"
    SHORT_ANSWER = "short_answer"


@dataclass
class Question:
    """题目数据类。"""
    id: str
    text: str
    question_type: QuestionType
    options: Optional[List[str]] = None
    correct_answer: Optional[str] = None
    explanation: str = ""
    course_id: Optional[str] = None
    unit_id: Optional[str] = None
    difficulty: int = 1  # 1-5 难度等级


@dataclass
class QuizSession:
    """答题会话数据类。"""
    session_id: str
    course_id: str
    questions: List[Question] = field(default_factory=list)
    current_index: int = 0
    score: int = 0
    answers: Dict[str, str] = field(default_factory=dict)
    completed: bool = False


class QuizEngine:
    """答题引擎，管理答题流程。"""

    def __init__(self):
        """初始化答题引擎。"""
        self._sessions: Dict[str, QuizSession] = {}

    def create_session(self, session_id: str, course_id: str,
                       questions: List[Question]) -> QuizSession:
        """创建新的答题会话。"""
        session = QuizSession(
            session_id=session_id,
            course_id=course_id,
            questions=questions
        )
        self._sessions[session_id] = session
        return session

    def submit_answer(self, session_id: str, question_id: str,
                      answer: str) -> bool:
        """
        提交答案并判断正误。

        Args:
            session_id: 会话 ID
            question_id: 题目 ID
            answer: 用户答案

        Returns:
            是否回答正确
        """
        session = self._sessions.get(session_id)
        if not session:
            return False

        # 查找对应题目
        for q in session.questions:
            if q.id == question_id:
                is_correct = (answer.strip() == q.correct_answer.strip())
                session.answers[question_id] = answer
                if is_correct:
                    session.score += 1
                return is_correct

        return False

    def get_next_question(self, session_id: str) -> Optional[Question]:
        """获取下一道题目。"""
        session = self._sessions.get(session_id)
        if not session:
            return None

        if session.current_index < len(session.questions):
            q = session.questions[session.current_index]
            session.current_index += 1
            return q
        else:
            session.completed = True
            return None
