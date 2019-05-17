import os,sys
from tornado import web,ioloop,httpserver
from tornado.web import StaticFileHandler
from tornado import options
from urls import urls
import config
import platform
debug = config.settings.get('debug')
#设置环境变量
path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(path)
sys.path.insert(0,path)
options.define("port", default=5000, type=int, help="run server on the given port.") # 定义服务器监听端口选项
if __name__  == '__main__':
    app = web.Application(
        urls,
        **config.settings,
        log_path = config.log_path,
        ROOT_PATH = path
    )
    http_server = httpserver.HTTPServer(app)
    if not debug:
        http_server.bind(options.options.port)
        http_server.start(0)
    else:
        app.listen(options.options.port)
    ioloop.IOLoop.current().start()
    # nohup python3 -u /www/wwwroot/boke/server.py > /www/wwwroot/boke/server.log 2>&1 &
