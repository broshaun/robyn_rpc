import os
import config


class PDFsS():
    def check_existing_file(self, candidate_names):
        """检查文件是否已存在"""
        if not os.path.exists(config.PDF):
            os.makedirs(config.PDF, exist_ok=True)
            return None
            
        for name in candidate_names:
            file_path = os.path.join(config.PDF, name)
            if os.path.isfile(file_path):
                return name
        return None
    
