class restaurant(Base):

	# __tablename__ = 'reataurant'
	name = Colum(String(80), nullable = False)
	id = Colum(Integer, primary_key = True)


	# """docstring for restaurant"""
	# def __init__(self, arg):
	# 	super(restaurant, self).__init__()
	# 	self.arg = arg
	# 	