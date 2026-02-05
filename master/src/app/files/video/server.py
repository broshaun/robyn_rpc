import os
import config

class VideosS():
    # 支持的输入视频格式
    SUPPORTED_INPUT_FORMATS = [
        'mp4', 'avi', 'mov', 'wmv', 'flv', 
        'mkv', 'webm', 'mpeg', 'mpg', '3gp'
    ]
    
    def check_existing_file(self, candidate_names):
        """检查文件是否已存在"""
        if not os.path.exists(config.VIDEO):
            os.makedirs(config.VIDEO, exist_ok=True)
            return None
            
        for name in candidate_names:
            file_path = os.path.join(config.VIDEO, name)
            if os.path.isfile(file_path):
                return name
        return None
    

    def is_valid_mp4_header(self, file_content):
        """
        验证文件头是否符合MP4特征
        MP4文件通常以ftyp（文件类型）框开头，包含特定的品牌标识
        """
        # MP4文件至少需要12字节（ftyp框的最小长度）
        if len(file_content) < 12:
            return False
            
        # MP4文件的ftyp框标识（前4字节为长度，接下来4字节为'ftyp'）
        # 检查第4-8字节是否为'ftyp'
        if len(file_content) >= 8 and file_content[4:8] == b'ftyp':
            return True
            
        # 常见的MP4品牌标识（在ftyp框之后）
        mp4_brands = [
            b'isom',  # 通用MP4标识
            b'iso2',  # ISO基础媒体文件格式
            b'avc1',  # 包含H.264视频
            b'mp41',  # MP4版本1
            b'mp42',  # MP4版本2
            b'3gp5',  # 3GPP版本5
            b'3gp6'   # 3GPP版本6
        ]
        
        # 检查是否包含已知的MP4品牌标识（从第8字节开始）
        for brand in mp4_brands:
            if len(file_content) >= 8 + len(brand) and file_content[8:8+len(brand)] == brand:
                return True
                

    