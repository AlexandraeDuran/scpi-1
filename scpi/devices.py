from scpi.capabilities import SCPI_Source_Capability, SCPI_Measure_Capability, SCPI_Text_Capability

class SCPI_Power(SCPI_Source_Capability, SCPI_Measure_Capability, SCPI_Text_Capability):
	def __init__(self, *args, **kw):
		if len(args) == 0:
			args = ['/dev/tty.usbserial-hp-power', 9600]
		if 'timeout' not in kw:
			kw['timeout'] = 1
		super(SCPI_Power, self).__init__(*args,**kw)
