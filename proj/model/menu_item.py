class menu_item(Base):
	# __tablename__ = 'menu_item'

	name = Colum(String(80), nullable = False)
	id = Colum(Integer, primary_key = True)
	restaurant_id = Colum(Integer, ForeignKey('restaurant.id'))
	restaurant = relationship()

	# """docstring for menu_item"""
	# def __init__(self, arg):
	# 	super(menu_item, self).__init__()
	# 	self.arg = arg
		