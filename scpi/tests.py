def test():
	#power = serial.Serial('/dev/tty.usbserial-0000101D', 9600, timeout=1)
	power = SCPI_Serial('/dev/tty.usbserial-0000101D', 9600, timeout=1)

	power.write('*RST\n')
	#power.write('*IDN?\n') # 'HEWLETT-PACKARD,6632B,0,A.00.07\r\n'
	#print "%r" % power.readline()
	print power.cmdres('*IDN?')

	power.write('SYST:REM\n')
	power.write('VOLT 0\n')
	power.write('OUTPUT ON\n')

	starttime = time.time()
	for i in range(0,100):
		power.write('VOLT %.03f\n' % (i/10.0))
		power.cmdres('SYST:ERROR?')
		print power.volt
	#	print time.time()-starttime, i/100.0
	#	time.sleep(0.01)

	power.write('OUTPUT OFF\n')
	power.write('*RST\n')
