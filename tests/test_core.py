"""答题引擎核心逻辑测试。

app/quiz_engine.py 只依赖标准库（dataclasses / typing / enum），
不碰 tkinter，所以能在无显示环境的 CI 里直接跑。
GUI 部分由 app/ui/ 负责，不在测试范围内。
"""
import os

from app.course_manager import CourseManager
from app.quiz_engine import QuizEngine, Question, QuestionType

QUESTIONS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "questions"
)


def _question(qid, answer="A"):
    return Question(
        id=qid,
        text=f"题目 {qid}",
        question_type=QuestionType.SINGLE_CHOICE,
        options=["A. 选项一", "B. 选项二"],
        correct_answer=answer,
        difficulty=1,
    )


def test_create_session_has_clean_initial_state():
    engine = QuizEngine()
    questions = [_question("q1"), _question("q2")]
    session = engine.create_session("s1", "cs_data_structures", questions)

    assert session.session_id == "s1"
    assert session.course_id == "cs_data_structures"
    assert session.score == 0
    assert session.answers == {}
    assert session.completed is False
    assert session.current_index == 0


def test_submit_answer_scores_correct_and_rejects_wrong():
    engine = QuizEngine()
    questions = [_question("q1", "A"), _question("q2", "B")]
    session = engine.create_session("s1", "cs", questions)

    assert engine.submit_answer("s1", "q2", "B") is True
    assert engine.submit_answer("s1", "q1", "B") is False  # 正确答案应为 A

    assert session.score == 1
    assert session.answers == {"q2": "B", "q1": "B"}


def test_submit_answer_ignores_whitespace():
    engine = QuizEngine()
    engine.create_session("s1", "cs", [_question("q1", "A")])

    assert engine.submit_answer("s1", "q1", "  A  ") is True
    assert engine.submit_answer("s1", "q1", "a") is False  # 大小写敏感是有意设计


def test_submit_answer_on_unknown_session_returns_false():
    engine = QuizEngine()

    assert engine.submit_answer("不存在", "q1", "A") is False
    engine.create_session("s1", "cs", [_question("q1")])
    assert engine.submit_answer("s1", "不存在的题目", "A") is False


def test_get_next_question_walks_all_then_marks_completed():
    engine = QuizEngine()
    questions = [_question("q1"), _question("q2")]
    session = engine.create_session("s1", "cs", questions)

    assert engine.get_next_question("s1").id == "q1"
    assert engine.get_next_question("s1").id == "q2"
    assert session.current_index == 2

    assert engine.get_next_question("s1") is None
    assert session.completed is True


def test_get_next_question_on_unknown_session_returns_none():
    engine = QuizEngine()

    assert engine.get_next_question("不存在") is None


def test_course_manager_loads_bundled_question_banks():
    manager = CourseManager(data_dir=QUESTIONS_DIR)
    courses = manager.get_all_courses()

    assert len(courses) >= 2, "questions/ 下至少应有示例题库 sample_cs / sample_politics"
    for course in courses:
        assert course.id
        assert course.name
        assert course.question_count > 0
        assert course.units, "每个课程都应带 units 分组"


def test_course_manager_lookup_roundtrip():
    manager = CourseManager(data_dir=QUESTIONS_DIR)
    first = manager.get_all_courses()[0]

    assert manager.get_course(first.id) is first
    assert manager.get_course("__不存在的课程__") is None
