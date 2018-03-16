# -*- coding: utf-8 -*-
"""Memory model module."""
from sqlalchemy import *
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, DateTime, LargeBinary, Text, String
from sqlalchemy.orm import relationship, backref
from datetime import datetime

from full_stack_app.model import DeclarativeBase, metadata, DBSession

#from full_stack_app.model.auth import user_group_table

class Memory(DeclarativeBase):
    __tablename__ = 'memorys'

    uid = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=True)
    content = Column(Text, nullable=True)
    data = Column(Unicode(255), nullable=False, default = datetime.utcnow)

    user_id = Column(Integer, ForeignKey('tg_user.user_id'), index=True)
    user = relationship('User', uselist=False,
                        backref=backref('memorys',
                                        cascade='all, delete-orphan'))


__all__ = ['Memory']
