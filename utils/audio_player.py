"""
音频播放辅助模块。

提供答题反馈音效和背景音频的播放功能，使用系统默认音频播放器。
"""

import os
import platform
from typing import Optional


class AudioPlayer:
    """音频播放辅助类。"""

    def __init__(self, audio_dir: str = "assets/audio"):
        """
        初始化音频播放器。

        Args:
            audio_dir: 音频文件目录路径
        """
        self._audio_dir = audio_dir
        self._system = platform.system()

    def play_feedback(self, is_correct: bool):
        """
        播放答题反馈音效。

        Args:
            is_correct: 是否回答正确
        """
        filename = "correct.mp3" if is_correct else "wrong.mp3"
        filepath = os.path.join(self._audio_dir, filename)
        self._play_file(filepath)

    def play_background(self, loop: bool = True):
        """
        播放背景音乐。

        Args:
            loop: 是否循环播放
        """
        filepath = os.path.join(self._audio_dir, "background.mp3")
        self._play_file(filepath)

    def stop(self):
        """停止音频播放。"""
        # TODO: 根据不同系统实现音频停止
        pass

    def _play_file(self, filepath: str):
        """
        使用系统默认播放器播放音频文件。

        Args:
            filepath: 音频文件绝对路径
        """
        if not os.path.exists(filepath):
            return

        if self._system == "Windows":
            import winsound
            # TODO: 使用 winsound 或 Windows Media Player
            pass
        elif self._system == "Darwin":
            os.system(f"afplay '{filepath}' &")
        else:
            os.system(f"mpg123 '{filepath}' &")
