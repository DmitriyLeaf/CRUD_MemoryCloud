# -*- coding: utf-8 -*-
"""Memory controller module"""

from tg import expose, redirect, validate, flash, url
# from tg.i18n import ugettext as _
# from tg import predicates

from full_stack_app.lib.base import BaseController
from full_stack_app.model import DBSession
from full_stack_app.model.memory import Memory
from full_stack_app.lib.forms import MemoryForm

__all__ = ['MemoryController']


class MemoryController(BaseController):
    # Uncomment this line if your controller requires an authenticated user
    # allow_only = predicates.not_anonymous()
    
    @expose('full_stack_app.templates.memory')
    def index(self):
    	memories = DBSession.query(Memory).all()
    	memory_form = MemoryForm()
        return dict(page='memory',
        	memories=memories,
        	memory_form=memory_form)
