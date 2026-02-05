import os
import logging
from datetime import datetime, timedelta
from logging.handlers import TimedRotatingFileHandler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor



# 日志文件夹配置
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)  # 确保日志文件夹存在


# --------------------------
# 1. 日志配置（每天生成一个日志文件）
# --------------------------
def get_logger():
    """获取按天分割的日志处理器"""
    logger = logging.getLogger("daily_task")
    logger.setLevel(logging.INFO)

    # 按天轮转日志，保留30天
    log_handler = TimedRotatingFileHandler(
        filename=os.path.join(LOG_DIR, "task.log"),  # 基础文件名
        when="midnight",  # 每天午夜轮转
        interval=1,       # 间隔1天
        backupCount=30,   # 保留30天日志
        encoding="utf-8"
    )
    # 日志文件名格式：task.log.2023-10-01（轮转后自动添加日期）
    log_handler.suffix = "%Y-%m-%d"

    # 日志格式：时间 + 级别 + 消息
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    log_handler.setFormatter(formatter)

    logger.addHandler(log_handler)
    return logger

logger = get_logger()




from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta




scheduler = BackgroundScheduler()
scheduler.start()  # 启动调度器


# --------------------------
# 1. 定义示例任务
# --------------------------
def task1():
    """示例任务1：每30秒执行一次"""
    print(f"任务1执行：{datetime.now()}")

def task2():
    """示例任务2：每天12点执行"""
    print(f"任务2执行：{datetime.now()}")

def task3():
    """示例任务3：每周一9点执行"""
    print(f"任务3执行：{datetime.now()}")


# --------------------------
# 2. 向调度器添加任务
# --------------------------
# 任务1：每30秒执行
scheduler.add_job(
    task1,
    trigger="interval",
    seconds=30,
    id="task_1",
    name="每30秒执行的任务"
)

# 任务2：每天12点执行
scheduler.add_job(
    task2,
    trigger="cron",
    hour=12,
    minute=0,
    id="task_2",
    name="每天12点执行的任务"
)

# 任务3：每周一9点执行
scheduler.add_job(
    task3,
    trigger="cron",
    day_of_week=0,  # 0=周一（周一到周日：0-6）
    hour=9,
    minute=0,
    id="task_3",
    name="每周一9点执行的任务"
)


def show_jobs():
    # 获取所有调度任务
    jobs = scheduler.get_jobs()
    
    # 格式化任务信息（提取需要展示的字段）
    job_list = []
    for job in jobs:
        # 处理下次执行时间（转为字符串，无则显示“无”）
        next_run = job.next_run_time.strftime("%Y-%m-%d %H:%M:%S") if job.next_run_time else "无"
        
        job_info = {
            "id": job.id,
            "name": job.name,
            "trigger": str(job.trigger),  # 触发方式（如interval/cron）
            "next_run": next_run,
            "func": job.func.__name__  # 任务函数名
        }
        job_list.append(job_info)

    return job_list





# --------------------------
# 2. 定义定时任务（每天0点执行，失败重试3次）
# --------------------------
def daily_task():
    """每天0点执行的任务（模拟可能失败的场景）"""
    task_date = datetime.now().strftime("%Y-%m-%d")
    logger.info(f"[{task_date}] 任务开始执行")

    try:
        # 模拟任务逻辑（50%概率失败，测试重试）
        import random
        if random.random() < 0.5:
            raise Exception("任务执行失败（模拟错误）")
        
        logger.info(f"[{task_date}] 任务执行成功")
        return True

    except Exception as e:
        logger.error(f"[{task_date}] 任务执行失败：{str(e)}")
        raise  # 抛出异常触发重试



def init_scheduler():
    # 配置执行器（线程池）
    executors = {
        'default': ThreadPoolExecutor(5)
    }

    # 初始化后台调度器（不阻塞Flask运行）
    scheduler = BackgroundScheduler(executors=executors)

    # 添加任务：每天0点执行，失败重试3次，间隔10分钟
    scheduler.add_job(
        daily_task,
        trigger="cron",
        hour=0,
        minute=0,
        second=0,
        max_instances=1,
        retry=True,
        retry_count=3,
        retry_delay=600  # 10分钟=600秒
    )

    scheduler.start()
    logger.info("调度器启动成功，每天0点执行任务")



def query_logs(date_str):
    '日志查询功能'

    logs = []
    error_msg = ""

    if date_str:
        # 校验日期格式（YYYY-MM-DD）
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            log_file = os.path.join(LOG_DIR, f"task.log.{date_str}")
            
            if os.path.exists(log_file):
                with open(log_file, "r", encoding="utf-8") as f:
                    logs = f.readlines()  # 读取当天所有日志
            else:
                error_msg = f"未找到 {date_str} 的日志文件"
        except ValueError:
            error_msg = "日期格式错误，请使用 YYYY-MM-DD"

    # 渲染网页（简单HTML表单）
    return logs