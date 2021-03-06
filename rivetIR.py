from py_irsend import irsend
from time import sleep
import re

def VERIZON(command):
	print("This is what was passed to irsend:" + command)

	remote = 'VERIZON_STB'

	### THIS SECTION CONTROLS POWER-------------------------------------------------------------------

	if command in ['all on','all off']:
		irsend.send_once(remote, ['TV_POWER'])
		irsend.send_once(remote, ['STB_POWER'])

	elif command.lower() in ['set top on','set top off', 'cable box on', 'cable box off']:
		irsend.send_once(remote, ['STB_POWER'])

	elif command.lower() in ['on','off']:
		irsend.send_once(remote, ['TV_POWER'])

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
						"cbs":"502",
						"nbc":"504",
						"fox":"505",
						"abc":"507",
						"tbs":"552",
						"comedy":"690",
						"discovery":"620",
						"science":"622",
						"history":"628",
						"food":"664",
						"velocity":"631",
						"cartoon":"757",
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
				
				if any(char.isdigit() for char in command):
					commandList = command.split()
					del commandList[-2::]
					newCommand = " ".join(commandList)
					print("this is returned with digits: "+newCommand)
					return cmdDict[newCommand.lower()]
				else:
					print("this is returned with no digits: "+command)
					return cmdDict[command.lower()]


			print(vzCmdCipher(command))

			### this section will run the command x number of times if provided in the voice command-------
			if any(char.isdigit() for char in command):
				#for i in range(int(command.split()[-2])):
				for i in range(int(command.split()[-2])):
					cleanedCmd = [vzCmdCipher(command)]
					irsend.send_once(remote,cleanedCmd)
					sleep(.3)
					print("sent IR")
			###---------------------------------------------------------------------------------------------
			###THIS SECTION RUNS THE COMMANDS INDIVIDUALLY--------------------------------------------------
			else:
				cleanedCmd = [vzCmdCipher(command)]
				irsend.send_once(remote,cleanedCmd)
				print("IR command sent!")

		except:
			print("Command not found!")

		


