from py_irsend import irsend
from time import sleep

def VERIZON(command):
	print("This is what was passed to irsend:" + command)

	remote = 'VERIZON_STB'

	if command in ['on','off']:
		irsend.send_once(remote, ['TV_POWER'])
		irsend.send_once(remote, ['STB_POWER'])

	### THIS SECTION IS FOR CHANNEL CONTROL-----------------------------------------------------------

	elif command.find('channel') !=-1:
		channelSplit = command.split()

			### change channel based on channel number in this section
		if channelSplit[1].isdigit():
			for chan in channelSplit[1]:
				irsend.send_once(remote, ['BTN_'+chan])
				sleep(.05)
			irsend.send_once(remote, ['ENTER_BTN'])

		else:
			### change channels based on channel names in this section
			try:
				def chanCipher(command):
					chanDict = {
						"comedy":"690",
						"hgtv":"665",
					}

					chanNameSplit = command.split()
					chanName = chanNameSplit[1]

					return chanDict[chanName.lower()]

				for chan in chanCipher(command):
					irsend.send_once(remote, ['BTN_'+chan])
					sleep(.05)
				irsend.send_once(remote, ['ENTER_BTN'])
			except:
				print("Channel not found!")

	###-----------------------------------------------------------------------------------------------
	### THIS SECTION IS FOR INDIVIDUAL REMOTE COMMAND BUTTONS-----------------------------------------
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
					"record":"REC",
					''' ### these buttons probably are not needed
					"1 button":"BTN_1",
					"2 button":"BTN_2",
					"3 button":"BTN_3",
					"4 button":"BTN_4",
					"5 button":"BTN_5",
					"6 button":"BTN_6",
					"7 button":"BTN_7",
					"8 button":"BTN_8",
					"9 button":"BTN_9",
					"0 button":"BTN_0",
					'''
					"asteric":"ASTERIC_BTN",
					"hash":"HASH_BTN",
					"a button":"A_BTN",
					"b button":"B_BTN",
					"c button":"C_BTN",
					"d button":"D_BTN",
					"input":"AV_INPUT",
					"pip":"PIP_BTN",
					"enter button":"ENTER_BTN",
				}
				print("this is command: "+command)
				if any(char.isdigit() for char in command):
					shaveDigit = command.split().remove(command.split()[-1])
					print("shaveDigit: "+shaveDigit)
					return cmdDict[shaveDigit.lower()]
				else:
					return cmdDict[command.lower()]


			print(vzCmdCipher(command))

			### this section will run the command x number of times if provided in the voice command
			print("made it here0")
			if any(char.isdigit() for char in command):
				commandSplit = command.split()
				print("made it here")
				for cmd in range(commandSplit[-1]):
					print("made it here2")
					cleanedCmd = [vzCmdCipher(command)]
					irsend.send_once(remote,cleanedCmd)
					sleep(.05)

			else:
				cleanedCmd = [vzCmdCipher(command)]
				irsend.send_once(remote,cleanedCmd)

		except:
			print("Command not found!")

		


