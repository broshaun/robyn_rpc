
# docker镜像
- docker build -t rpc:slave .

### 正式环境部署镜像
- docker-compose up

### 正式环境停止镜像
- docker-compose down




# 开发环境

## Python 虚拟slave环境搭建
- python3.10 -m venv .slave
- source .slave/bin/activate

## 安装包
- pip install --upgrade pip
- pip install -r ./.pip/requirements.txt

## 执行代码
- cd src
- python3 main.py