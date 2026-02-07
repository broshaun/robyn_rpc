## Python 虚拟master环境搭建
- python3.10 -m venv .master
- source .master/bin/activate

## Python 虚拟slave环境搭建
- python3.10 -m venv .slave
- source .slave/bin/activate



# 
## 安装包
- pip install --upgrade pip
- pip install -r ./.pip/requirements.txt

## 执行代码
- cd src
- python3 main.py