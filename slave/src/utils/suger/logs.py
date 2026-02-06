import traceback
from datetime import datetime
from pathlib import Path
import config

def error(e: Exception, wrapped: str = ""):
    """
    统一异常日志处理函数 - 纯日志写入，无返回值
    :param e: 捕获到的异常对象 (必填)
    :param wrapped: 异常发生的位置/函数名 (可选，精准定位异常用)
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    today = datetime.now().strftime("%Y_%m_%d")

    file_name = f"logs_{today}.txt"
    log_file_path = Path(config.F.LOGS, file_name).resolve()
    log_file_path.parent.mkdir(parents=True, exist_ok=True)

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
    

    if config.DEBUG:
        print(log_message)
    else:
        with open(log_file_path, "a", encoding="utf-8") as log_file:
            log_file.write(log_message)