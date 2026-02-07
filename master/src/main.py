from robyn import Robyn
import config
from utils.middle import BlueRouter
from app.rpclient import RPCView
from app.files import ImgesV


app = Robyn(__file__)

app.serve_directory(
    route="/html",
    directory_path= config.HTML,
    index_file="index.html",
)
app.serve_directory(
    route="/dist",
    directory_path= config.DIST,
    index_file="index.html",
)

app.serve_directory(
    route="/logs",
    directory_path=config.LOGS,
    show_files_listing=True
)

app.serve_directory(
    route="/imgs",
    directory_path=config.IMGS,
    show_files_listing=True
)

BlueRouter(app,'/files').include_views({
    '/img':ImgesV,
})


BlueRouter(app,'/api').include_views({
    '/:rpc_server/*sub_path':RPCView, 
})


if __name__ == "__main__":
    app.start(host=config.WebIP.HOST,port=config.WebIP.PORT)

