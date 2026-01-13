from flask import Flask
app = Flask(__name__)
@app.route('/.well-known/pki-validation/E78E4C2873904DC5CD480619D64BA7DF.txt')
def pki_validation():
	# Your logic here
	return '5FB6AD0ED84488914C299E36B43DD3D0445F6BE6C5065203AB58B1E1D181ABA9 comodoca.com 657dd2fd7a947'
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)

# https://www.ssls.com/