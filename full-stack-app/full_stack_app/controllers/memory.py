# -*- coding: utf-8 -*-
"""Memory controller module"""

from tg import expose, redirect, validate, flash, url, require, request
# from tg.i18n import ugettext as _
from tg import predicates

from full_stack_app.lib.base import BaseController
from full_stack_app.model import DBSession
from full_stack_app.model.memory import Memory
from full_stack_app.lib.forms import MemoryForm

__all__ = ['MemoryController']

class MemoryController(BaseController):
    allow_only = predicates.not_anonymous()

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
    def new(self, name, content):
        user = request.identity['user']
        DBSession.add(Memory(name=name, content=content, user=user))
        redirect('/memory')

    @expose('json')
    def post_delete(self, uid):
    	memory = DBSession.query(Memory).get(uid)
    	DBSession.delete(memory)
    	redirect('/memory')
    	#return dict(page='index')
    	

    '''@expose('full_stack_app.templates.edit')
    def edit(self, uid, submit):
    	memory = DBSession.query(Memory).filter_by(uid=uid).one()
    	return dict(page='edit',
    		memory=memory)

    @expose()
    def delete(self, uid):
    	delete = DBSession.delete(Memory).filter_by(uid=uid).one()
    	return redirect("index")'''