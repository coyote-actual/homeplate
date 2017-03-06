from py_irsend import irsend

def VERIZON(command):
	print("This is what was passed to irsend:" + command)

	def cipher(command):
		return {
			"on":"TV_POWER",
			"off":"TV_POWER_OFF"
		}[command]

	print(cipher(command))




	'''
	if command == 'on':
		irsend.send_once('VERIZON_STB', ['TV_POWER'])
		irsend.send_once('VERIZON_STB', ['STB_POWER'])


	elif command == 'off':
		irsend.send_once('VERIZON_STB', ['TV_POWER'])
		irsend.send_once('VERIZON_STB', ['STB_POWER'])
	'''
		


