from decimal import Decimal
from scpi.comms import SCPI_Serial
from scpi.properties import SCPI_Property_Decimal, SCPI_Property_Boolean, SCPI_Property_Text_and_Mode

class SCPI_Basic(SCPI_Serial):
	def reset(self):
		return self('*RST')

class SCPI_Measure_Capability(SCPI_Serial):
	def meas_voltage(self):
		return Decimal(self('MEAS:VOLT:DC?'))
	mU = property(meas_voltage)

	def meas_current(self):
		return Decimal(self('MEAS:CURR?'))
	mI = property(meas_current)	

class SCPI_Source_Capability(SCPI_Serial):
	oU = SCPI_Property_Decimal('SOURCE:VOLT')
	oI = SCPI_Property_Decimal('SOURCE:CURR')
	oO = SCPI_Property_Boolean('OUTP')
	
	def output_protection_clear(self):
		return self('OUTP:PROT:CLE')

class SCPI_Text_Capability(SCPI_Serial):
	text = SCPI_Property_Text_and_Mode('DISP:WIND:TEXT','DISP:WIND:MODE')
	
