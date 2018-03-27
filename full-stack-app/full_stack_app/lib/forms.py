import tg 
from tg import request
from tg.i18n import lazy_ugettext

from tw2.forms import *
from tw2.bootstrap.forms.widgets import HorizontalForm, TextField, SubmitButton
from tw2.core import Required, Deferred

from datetime import datetime
from full_stack_app.model.memory import Memory
#from full_stack_app.model import DeclarativeBase, metadata, DBSession
#from full_stack_app.model.memory import Memory
#from full_stack_app.model.auth import User
#from tg import config
''' (
	bootstrap_css, 
	bootstrap_responsive_css, 
	Form, 
	HiddenField, 
	HorizontalForm, 
	InputField, 
	TextField, 
	PostlabeledCheckBox, 
	PasswordField, 
	SingleSelectField, 
	Spacer, 
	SubmitButton) '''

class MemoryForm(HorizontalForm):
	name = TextField(label='Memory\'s Name')
	content = TextField(label='Description')
	data = datetime.utcnow
	submit = SubmitButton(value=lazy_ugettext('Save'), css_class='btn btn-success')

class EditForm(HorizontalForm):
	uid = HiddenField()
	name = TextField(label='Memory\'s Name')
	content = TextField(label='Description')
	#data = datetime.utcnow
	submit = SubmitButton(value=lazy_ugettext('Save'), css_class='btn btn-success')