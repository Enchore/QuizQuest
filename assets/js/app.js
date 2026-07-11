// QuizQuest 前端 JavaScript 模块（Web 版本辅助脚本）
// 此文件为 Web 版本的辅助脚本，桌面版主要使用 Tkinter

"use strict";

/**
 * QuizQuest Web 模块入口
 */
class QuizQuestApp {
    constructor() {
        this.currentCourse = null;
        this.currentQuestion = null;
    }

    /**
     * 初始化应用
     */
    init() {
        console.log("QuizQuest Web 初始化中...");
        // TODO: 加载课程列表
    }

    /**
     * 开始答题
     */
    startQuiz(courseId) {
        // TODO: 调用后端 API 开始答题
    }

    /**
     * 提交答案
     */
    submitAnswer(questionId, answer) {
        // TODO: 调用后端 API 提交答案
    }
}
