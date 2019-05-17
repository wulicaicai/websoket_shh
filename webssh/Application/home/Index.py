from .Base import *
class Index(Base):
    def get(self):
        self.render('index.html')

    def post(self):
        """保存用户提交的代码"""
        code = self.request.body_arguments.get('code')[0].decode()
        with open(self.settings['ROOT_PATH']+'/static/test.py','w',encoding="UTF8") as f:
            f.write(code)
        self.write({"code":0,"msg":"保存成功"})
