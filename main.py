from escpos import *


import printer

from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def helloIndex():
	Epson = Usb(0x04b8,0x0202)	
	# Print text
	Epson.text("Hello World\n")	
	# Print image
	Epson.image("logo.gif")	
	# exit()
	# Print QR Code
	Epson.qr("You can readme from your smartphone")
	# Print barcode
	Epson.barcode('1324354657687','EAN13',64,2,'','')
	# Cut paper
	Epson.cut()
	return 'Hello World from Python Flask!'

app.run(host='0.0.0.0', port= 81)


""" Seiko Epson Corp. Receipt Printer M129 Definitions (EPSON TM-T88IV) """
