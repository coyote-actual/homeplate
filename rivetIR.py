from py_irsend import irsend

def VERIZON(command):
	print("This is what was passed to irsend:" + command)
	if command == 'on':
		irsend.send_once('VERIZON_STB', ['TV_POWER'])
		irsend.send_once('VERIZON_STB', ['STB_POWER'])


	elif command == 'off':
		irsend.send_once('VERIZON_STB', ['TV_POWER'])
		irsend.send_once('VERIZON_STB', ['STB_POWER'])
		


