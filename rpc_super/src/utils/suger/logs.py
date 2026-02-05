import traceback
from datetime import datetime
from pathlib import Path
import config  # 你的项目配置文件

def error(e: Exception, wrapped: str = ""):
    """
    统一异常日志处理函数 - 纯日志写入，无返回值
    :param e: 捕获到的异常对象 (必填)
    :param wrapped: 异常发生的位置/函数名 (可选，精准定位异常用)
    """
    # 时间格式化 与原代码一致
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    today = datetime.now().strftime("%Y_%m_%d")
    
    # 日志文件路径 + 自动创建日志目录（解决目录不存在报错问题，原代码无此逻辑）
    file_name = f"logs_{today}.txt"
    log_file_path = Path(config.F.LOGS, file_name).resolve()
    log_file_path.parent.mkdir(parents=True, exist_ok=True)

    # 异常堆栈+日志内容，完全复用你原有的格式、分隔符、内容排版
    stack_trace = traceback.format_exc()
    log_message = (
        f"{'-'*100}\n"
        f"[{timestamp}] 异常发生:\n"
        f"异常位置: {wrapped}\n"
        f"异常类型: {type(e).__name__}\n"
        f"异常详情: {str(e)}\n"
        f"堆栈跟踪:\n{stack_trace}\n"
        f"{'-'*100}\n"
    )
    
    # 调试模式打印控制台，生产模式写入日志文件
    if config.DEBUG:
        print(log_message)
    else:
        with open(log_file_path, "a", encoding="utf-8") as log_file:
            log_file.write(log_message)