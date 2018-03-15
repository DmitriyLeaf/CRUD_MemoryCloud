from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import relation, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from zope.sqlalchemy import ZopeTransactionExtension
from datetime import datetime
from webob import UTC

#from memory.model import DeclarativeBase

maker = sessionmaker(autoflush = True, autocommit = False, extension = ZopeTransactionExtension())
DBSession = scoped_session(maker)
DeclarativeBase = declarative_base()
metadata = DeclarativeBase.metadata

MODIFICATION_DATE = datetime(2018, , , , , tzinfo = UTC)

class Memory(DeclarativeBase):
	__tablename__ = "memories"

	id = Column(Integer, primary_key = True)
	name = Column(String(100))
	description = Column(Text, nullable = True)
	timestamp = Column(Date, nullable = True, default = datetime.utcnow)

	@property 
	def updated_at(self):
		return MODIFICATION_DATE

class FakeModel(object):
	__file__ = 'model.py'

	memory = Memory
	DBSession = DBSession

	def init_model(self, engine):
		if metadata.bind is None:
			DBSession.configure(bind = engine)
			metadata.bind = engine

class FakePackage(object):
	__file__ = 'package.py'
	__name__ = 'tests'

	model = FakeModel()

class CrudTest(object):
	def setUp(self):
        self.root_controller = self.controller_factory()
        conf = AppConfig(minimal = True, root_controller = self.root_controller)
        conf.package = FakePackage()
        conf.model = conf.package.model
        conf.use_dotted_templatenames = True
        conf.renderers = ['json', 'jinja', 'mako']
        conf.default_renderer = 'jinja'
        conf.use_sqlalchemy = True
        conf.paths = {'controllers':'tests',
                      'templates':['tests']}
        conf.disable_request_extensions = False
        conf.prefer_toscawidgets2 = True
        conf.use_transaction_manager = True
        conf['sqlalchemy.url'] = 'sqlite:///:memory:'

        self.app = TestApp(conf.make_wsgi_app())

        metadata.create_all()

    def tearDown(self):
        metadata.drop_all()
