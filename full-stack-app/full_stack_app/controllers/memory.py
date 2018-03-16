# -*- coding: utf-8 -*-
"""Memory controller module"""

from tg import expose, redirect, validate, flash, url
# from tg.i18n import ugettext as _
# from tg import predicates

from full_stack_app.lib.base import BaseController
from full_stack_app.model import DBSession
from full_stack_app import model


class MemoryController(BaseController):
    # Uncomment this line if your controller requires an authenticated user
    # allow_only = predicates.not_anonymous()
    
    @expose('full_stack_app.templates.memory')
    def memory(self):
    	m_name = [memorys.name for memorys in DBSession.query(Memory).order_by(Memory.name)]
        m_content = [memorys.content for memorys in DBSession.query(Memory).order_by(Memory.content)]
        m_data = [memorys.data for memorys in DBSession.query(Memory).order_by(Memory.data)]
        m_user = [memorys.user for memorys in DBSession.query(Memory).order_by(Memory.user)]
        return dict(page='memory',
        	m_name=m_name,
        	m_content=m_content,
        	m_data=m_data,
        	m_user=m_user)
