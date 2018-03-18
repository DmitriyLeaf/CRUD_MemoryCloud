import tg
from tg.i18n import lazy_ugettext

from tw2.forms import *
from tw2.bootstrap.forms.widgets import HorizontalForm, TextField, SubmitButton

from datetime import datetime
from full_stack_app.model import DeclarativeBase, metadata, DBSession
from full_stack_app.model.memory import Memory
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
	name = TextField(label='Name')
	data = TextField(label='Data', default = datetime.utcnow)
	content = TextField(label='content')
	submit = SubmitButton(value=lazy_ugettext('Save'), css_class='btn btn-defaulf')

def save(self):
	new_memory = Memory(name, content, data)
	session.add(new_memory)
	return 