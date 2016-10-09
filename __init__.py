from flask import Flask, request
from connectdb import connection

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)
@app.route("/")
def hello():
	try:
		c,conn = connection()
		return "okay"
	except Exception as e:
		return (str(e))
	return "this bad boy is working!"
@app.route("/getWord", methods=['GET'])
def getWord():
	if 'long' in request.args and 'lat' in request.args:
		longitude = float(request.args["long"])
		latitude = float(request.args["lat"])
		return str(nearest(longitude, latitude))
	else:
		return "bad request"
stuff = []
stuff.append([0.0,0.0])
stuff.append([13.0,13.0])

def nearest(longitude,latitude):
	min = 99999999
	minPos = -1
	for i in xrange(len(stuff)):
		if min > ((stuff[i][0]-longitude)**2 + (stuff[i][1]-latitude)**2):
			min = ((stuff[i][0]-longitude)**2 + (stuff[i][1]-latitude)**2)
			minPos=i
	return stuff[minPos]

