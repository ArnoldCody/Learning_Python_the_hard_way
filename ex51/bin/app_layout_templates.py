# coding:utf-8
import web
import datetime

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

# 下面代码为上传图片并保存
class Upload(object):
    def GET(self):
    	web.header("Content-Type","text/html; charset=utf-8")
        return render.upload()

    def POST(self):
        x = web.input(myfile={})
        if 'myfile' in x:
        	filepath=x.myfile.filename.replace('\\','/')#客户端为windows时注
        	filename=filepath.split('/')[-1]#获取文件名
        	ext = filename.split('.', 1)[1]#获取后缀
        	if ext == 'jpg':#判断文件后缀名
    			filedir = '/users/arnold/projects'#要上传的路径
      			now = datetime.datetime.now() #获取时间
    			t = "%d%d%d%d%d%d" %(now.year,now.month,now.day,now.hour,now.minute,now.second) #以时间作为文件名
      			filename = t+'.'+ext #文件名+后缀
       			fout = open(filedir +'/'+ filename,'w')
       			fout.write(x.myfile.file.read())
       			fout.close()
       			message = u'OK！'
       			error = False
       		else:
   	 			message = u'请上传jpg格式的文件！'
   	 			error = True
		
				
    		
if __name__ == "__main__":
	app.run()
