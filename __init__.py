from flask import Flask, request
from connectdb import connection
from findword import fword
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
	if 'long' in request.args and 'lat' in request.args and 'radius' in request.args and 'ids' in request.args:
		longitude = float(request.args["long"])
		latitude = float(request.args["lat"])
                radius = float(request.args["radius"])
                ids = request.args.getlist("ids")
                try:
                    j = fword(longitude,latitude,radius,ids)
                    return j
                except Exception as e:
                    return str(e)
	else:
		return "bad request"

def nearest(longitude,latitude):
	min = 99999999
	minPos = -1
	for i in xrange(len(stuff)):
		if min > ((stuff[i][0]-longitude)**2 + (stuff[i][1]-latitude)**2):
			min = ((stuff[i][0]-longitude)**2 + (stuff[i][1]-latitude)**2)
			minPos=i
	return stuff[minPos]

