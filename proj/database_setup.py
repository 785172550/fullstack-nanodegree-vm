# coding: UTF-8
import sys
from sqlalchemy import Column, String, ForeignKey, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# create the sqlalchemy base object
Base = declarative_base()

class Restaurant(Base):
	__tablename__ = 'restaurant'

	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)

class MenuItem(Base):
	__tablename__ = 'menu_item'

	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
	restaurant = relationship(Restaurant)


engine = create_engine('sqlite:///restaurant_menu.db')
Base.metadata.create_all(engine)