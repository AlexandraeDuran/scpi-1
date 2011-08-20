from decimal import Decimal
from scpi.types import SCPI_Decimal

class SCPI_Property(object):
	def __init__(self, verb):
		self.verb = verb
		
	def __get__(self, obj, objtype=None):
		result = obj.cmd('%s?' % self.verb)
		return result
	
	def __set__(self, obj, val):
		obj.cmd('%s %s' % (self.verb, val))

class SCPI_Property_Decimal(SCPI_Property):
	def __init__(self,*args,**kw):
		super(SCPI_Property_Decimal, self).__init__(*args,**kw)
		self._min = None
		self._max = None

	def init_minmax(self,obj):
		if self._min == None or self._max == None:
			self._min = Decimal( obj.cmd('%s? MIN' % self.verb) )
			self._max = Decimal( obj.cmd('%s? MAX' % self.verb) )

	def __get__(self, obj, objtype=None):
		self.init_minmax(obj)
		result = super(SCPI_Property_Decimal, self).__get__(obj, objtype)
		return SCPI_Decimal(result, property=self)

	def __set__(self, obj, val):
		self.init_minmax(obj)
		val = Decimal("%.15g" % val)
		if self._min > val or val > self._max:
			 raise SCPI_Out_Of_Range_Exception('%s=%s outside of range %s - %s' % (self._name, val, self._min, self._max))
		val = str(val)
		super(SCPI_Property_Decimal, self).__set__(obj, val)

class SCPI_Property_Boolean(SCPI_Property):
	def __get__(self, obj, objtype=None):
		result = super(SCPI_Property_Boolean, self).__get__(obj, objtype)
		return result == '1'

	def __set__(self, obj, val):
		if val not in [True, False]:
			 raise SCPI_Out_Of_Range_Exception('%s is not a boolean' % val)
		if val:
			val = '1'
		else:
			val = '0'
		super(SCPI_Property_Boolean, self).__set__(obj, val)

class SCPI_Property_Text_and_Mode(object):
	def __init__(self, text_verb, mode_verb):
		self.text_verb = text_verb
		self.mode_verb = mode_verb

	def __get__(self, obj, objtype=None):
		if obj.cmd('%s?' % self.mode_verb) == 'NORM':
			return
		
		result = obj.cmd('%s?' % self.text_verb)
		if result.startswith('"') and result.endswith('"'):
			return result[1:-1]
		else:
			return # Umm, raise exception, protocol error or something..

	def __set__(self, obj, val):
		if val:
			obj.cmd('%s "%s"' % (self.text_verb, val))
			obj.cmd('%s TEXT' % (self.mode_verb,))
		else:
			obj.cmd('%s ""' % (self.text_verb,))
			obj.cmd('%s NORM' % (self.mode_verb,))			
