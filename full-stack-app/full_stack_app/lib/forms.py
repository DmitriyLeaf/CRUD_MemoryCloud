#import tw2.core
#import tw2.forms
#from tw2.forms import *
#from tw2.bootstrap.forms.widgets import HorizontalForm
#import tw2.bootstrap.forms.widgets as twb

#import tw2.bootstrap.forms.widgets as twb

from tw2.core import Required, Deferred
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
	name = TextField(label='name')
	data = TextField(label='data')
	content = TextField(label='content')
	submit = SubmitButton(value=l_('Save'), css_class='btn btn-defaulf')