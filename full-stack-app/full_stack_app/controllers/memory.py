# -*- coding: utf-8 -*-
"""Memory controller module"""

from tg import expose, redirect, validate, flash, url, require, request
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
        return dict(page='memory',
        	memories=memories)

    @expose('full_stack_app.templates.adding')
    def adding(self):
        memory_form = MemoryForm()
        return dict(page='adding',
        	memory_form=memory_form)

    @expose()
    def new():
		m = model.Memory()
        m.name = self.name
        m.content = self.content
        model.DBSession.add(m)
        model.DBSession.flush()
        transaction.commit()
		redirect('/')

    '''@expose('full_stack_app.templates.edit')
    def edit(self, uid, submit):
    	memory = DBSession.query(Memory).filter_by(uid=uid).one()
    	return dict(page='edit',
    		memory=memory)

    @expose()
    def delete(self, uid):
    	delete = DBSession.delete(Memory).filter_by(uid=uid).one()
    	return redirect("index")'''