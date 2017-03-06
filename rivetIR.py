from py_irsend import irsend

def VERIZON(command):
	print("This is what was passed to irsend:" + command)

	remote

	if (command == 'on' | command == 'off'):
		irsend.send_once(remote, ['TV_POWER'])
		irsend.send_once(remote, ['STB_POWER'])

	else:

		def vzCipher(command):
			return {
				"test":"TV_POWER",
				"test two":"TV_POWER_OFF"
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
		


