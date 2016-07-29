# coding:utf-8
import web

urls = (
	'/hello', 'Index',
	'/upload', 'Upload'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout") #渲染 templates 下的 layout.html

class Index(object):
	def GET(self):
		return render.hello_form_layout_template()
		
	def POST(self):
		form = web.input(name="Nobody", greet="Hello")
		greeting = "%s, %s" % (form.greet, form.name)
		return render.index_layout_template(greeting = greeting)

class Upload(object):
    def GET(self):
        return render.upload()

    def POST(self):
        x = web.input(myfile={})
        web.debug(x['myfile'].filename) # 这里是文件名
        web.debug(x['myfile'].value) # 这里是文件内容
        web.debug(x['myfile'].file.read()) # 或者使用一个文件对象
        raise web.seeother('/upload')


				
    		
if __name__ == "__main__":
	app.run()
