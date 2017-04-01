from py_irsend import irsend

def VERIZON(command):
	print("This is what was passed to irsend:" + command)

	remote = 'VERIZON_STB'

	if command in ['on','off']:
		irsend.send_once(remote, ['TV_POWER'])
		irsend.send_once(remote, ['STB_POWER'])

	elif command.lower().find('channel') !=-1:
		print(command + 'testing for debug...')

	else:
		try:
			def vzCmdCipher(command):
				cmdDict = {
					"menu":"MENU",
					"guide":"GUIDE",
					"info":"INFO",
					"up arrow":"CIRCLE_UP",
					"right arrow":"CIRCLE_RIGHT",
					"down arrow":"CIRCLE_DOWN",
					"left arrow":"CIRCLE_LEFT",
					"ok button":"OK_BTN",
					"exit":"EXIT",
					"widgets":"WIDGETS",
					"on demand":"ON_DEMAND",
					"options":"OPTIONS",
					"mute":"MUTE",
					"last":"LAST",
					"volume up":"VOLUME_UP",
					"volume down":"VOLUME_DOWN",
					"fios button":"FIOS_TV_BTN",
					"channel up":"CHANNEL_UP",
					"channel down":"CHANNEL_DOWN",
					"previous":"PREVIOUS",
					"dvr":"DVR_BTN",
					"next":"NEXT",
					"rewind":"REWIND",
					"play":"PLAY_BTN",
					"pause":"PAUSE_BTN",
					"fast forward":"FFWD",
					"stop":"STOP",
					"record":"REC"
				}

				return cmdDict[command.lower()] #this approach makes sure all commands are lower case!


			print(vzCmdCipher(command))

			#IRSEND the command!
			cleanedCmd = [vzCmdCipher(command)]
			irsend.send_once(remote,cleanedCmd)

		except:
			print("Command not found!")

		


