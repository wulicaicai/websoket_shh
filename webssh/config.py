import os,sys
# Redis配置
redis_options = {
    'redis_host':'127.0.0.1',
    'redis_port':6379,
    'redis_pass':'',
}

#mysql配置
mysql_options = {
    'host':"127.0.0.1",
    'user':'root',
    "passwd":"123456",
    "database":"boke",
    "charset":"utf8mb4",
    "port":3306,
    "prefix":""
}

# Tornado app配置
settings = {
    'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    # 'static_url_prefix':'static/',
    'cookie_secret':'0Q1AKOKTQHqaa+N80XhYW7KCGskOUE2snCW06UIxXgI=',
    'xsrf_cookies':False,
    'login_url':'/admin/login',
    'debug':True,
}

# 日志
log_path = os.path.join(os.path.dirname(__file__), 'logs/log')
