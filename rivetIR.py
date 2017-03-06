from py_irsend import irsend

def VERIZON(command):
	print("This is what was passed to irsend:" + command)

	remote = 'VERIZON_STB'

	if command in ['on','off']:
		irsend.send_once(remote, ['TV_POWER'])
		irsend.send_once(remote, ['STB_POWER'])

	else:

		def vzCipher(command):
			return {
				"menu":"MENU",
				"guide":"GUIDE",
				"info":"INFO",
				"up arrow":"CIRCLE_UP",
				"right arrow":"CIRCLE_RIGHT",
				"down arrow":"CIRCLE_DOWN",
				"left arrow":"CIRCLE_LEFT",
				"ok button":"OK_BTN"
			}[command]

		print(vzCipher(command))




	'''
	if command == 'on':
		irsend.send_once('VERIZON_STB', ['TV_POWER'])
		irsend.send_once('VERIZON_STB', ['STB_POWER'])


	elif command == 'off':
		irsend.send_once('VERIZON_STB', ['TV_POWER'])
		irsend.send_once('VERIZON_STB', ['STB_POWER'])
	'''
		


