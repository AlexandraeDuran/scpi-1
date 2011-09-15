from scpi.capabilities import SCPI_Source_Capability, SCPI_Measure_Capability, SCPI_Text_Capability
from scpi.comms import SCPI_Serial

class SCPI_Power(SCPI_Source_Capability, SCPI_Measure_Capability, SCPI_Text_Capability):
	def __init__(self, *args, **kw):
		if len(args) == 0:
			args = ['/dev/tty.usbserial-hp-power', 9600]
		if 'timeout' not in kw:
			kw['timeout'] = 1
		super(SCPI_Power, self).__init__(*args,**kw)

class SCPI_Multimeter(SCPI_Measure_Capability, SCPI_Text_Capability):
	def __init__(self, *args, **kw):
		if len(args) == 0:
			args = ['/dev/tty.usbserial-hp-meter', 9600]
		if 'timeout' not in kw:
			kw['timeout'] = 1
		super(SCPI_Multimeter, self).__init__(*args,**kw)

def SCPI_Auto(port, speed=9600):
	scpi = SCPI_Serial(port, speed, timeout=2)
	idn = scpi('*IDN?')
	if idn.startswith('HEWLETT-PACKARD,34401A,'):
		return SCPI_Multimeter(port, speed)
	elif idn.startswith('HEWLETT-PACKARD,6632B,'):
		return SCPI_Power(port, speed)
