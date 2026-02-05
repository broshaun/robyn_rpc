import os
import config


class AudiosS():

    def check_existing_file(self, candidate_names):
        """检查文件是否已存在"""
        if not os.path.exists(config.AUDIO):
            os.makedirs(config.AUDIO, exist_ok=True)
            return None
            
        for name in candidate_names:
            file_path = os.path.join(config.AUDIO, name)
            if os.path.isfile(file_path):
                return name
        return None


    def is_valid_mp3_header(self, file_content):
        """验证文件头是否符合MP3特征"""
        # MP3文件典型的文件头特征
        mp3_signatures = [
            b'ID3',          # ID3v2标签
            b'\xFF\xFB',     # MP3帧头
            b'\xFF\xF3',     # MP3帧头
            b'\xFF\xF2',     # MP3帧头
            b'\xFF\xFA'      # MP3帧头
        ]
        # 文件内容过短，不可能是MP3
        if len(file_content) < 3:
            return False
        # 检查是否匹配任何已知的MP3文件头
        for signature in mp3_signatures:
            if file_content.startswith(signature):
                return True
        return False
