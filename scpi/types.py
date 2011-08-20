from decimal import Decimal

class SCPI_Decimal(Decimal):
	def __new__(obj_type,*args,**kw):
		kw_property = kw.get('property',None)
		del(kw['property'])
		obj = super(SCPI_Decimal,obj_type).__new__(obj_type, *args, **kw)
		obj.property = kw_property
		return obj

	@property
	def max(self):
		return self.property._max

	@property
	def min(self):
		return self.property._min
