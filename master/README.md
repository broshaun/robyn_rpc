# 微服务主服务
## 使用robyn作为master服务访问rpc服务
```当前服务用于转发至其它服务的服务```


### docker镜像编译
- docker build -t rpc:master .

### 正式环境部署镜像
- docker-compose up

### 正式环境停止镜像
- docker-compose down

### 配置
#### app/config 配置项目设定
- DEBUG=True 为开发环境
- EBUG=False 为生产环境



# 开发环境
## Python 虚拟master环境搭建
- python3.10 -m venv .master
- source .master/bin/activate
## 安装包
- pip install --upgrade pip
- pip install -r ./.pip/requirements.txt

## 执行代码
- cd src
- python3 main.py