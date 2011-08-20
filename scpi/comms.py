import serial as pyserial

class SCPI_Serial(object):
	def __init__(self, *args, **kw):
		super(SCPI_Serial, self).__init__()
		self.serial = pyserial.Serial(*args, **kw)

#	def _write(self, *args, **kw):
#		return self.serial.write(*args, **kw)

#	def _readline(self):
#		return self.serial.readline()

	def __call__(self, cmd, no_errors=False):
		"""Send command and wait for result"""
		if not no_errors:
			self.clr_errors()

		cmd_split = cmd.split(' ',1)
		verb = cmd_split[0]
		verb_question = verb.endswith('?')
		self.serial.write('%s\n' % (cmd,))
#		print "cmd: %s, verb: %s, all: %s, q: %s" % (cmd, verb, cmd_split, verb_question)
		if verb_question:
			res = self.serial.readline().rstrip()
		else:
			res = None

		if no_errors:
			return res

		error = self.error()
		if error != '+0,"No error"' or (verb_question and res == ''):
			raise SCPI_Exception( error )
		return res

	cmdres = __call__
	cmd = __call__
	
	def error(self):
		return self('SYST:ERR?', no_errors=True)
	
	def clr_errors(self):
		error = self.error()
		while error != '+0,"No error"' and error != '':
			error = self.error()			
