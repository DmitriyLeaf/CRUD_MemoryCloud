from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import relation

from memory.model import DeclarativeBase

class Genre(DeclarativeBase):
	__tablename__ = "memories"
	def __init__(self, arg):
		super(Genre, self).__init__()
		self.arg = arg
