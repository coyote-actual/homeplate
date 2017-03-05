### This is the main homeplate app that will control many functions of my personal home automation system ###
###              For use with Flask and Python          Joseph Pistono - 2017 - Black Fleet Inc.		  ###


from flask import Flask, request, jsonify
import rivetIR


app = Flask(__name__)
tokenKey = 'BLK862702'


@app.route('/post', methods = ['POST'])
def post():
    # Get the parsed contents of the form data
    json = request.json
'''
    if json['token'] == tokenKey:

    	if json['device'] == 'VERIZON':
    		rivetIR.VERIZON(json['command'])

    else:
    	print('Invalid Token')
'''
    return jsonify(json)