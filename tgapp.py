from tg import expose, TGController, AppConfig
#from tg.decorators.expose import render_template
from wsgiref.simple_server import make_server
import webhelpers2
import webhelpers2.text

class RootController(TGController):
	@expose('templates/index.xhtml')
	def index(self):
		return dict(title = 'Home')

config = AppConfig(minimal = True, root_controller = RootController())
config.renderers = ['kajiki']

application = config.make_wsgi_app()

print("Serving on port 8080...")
httpd = make_server('', 8080, application)
httpd.serve_forever()