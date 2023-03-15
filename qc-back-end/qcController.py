from flask import Flask
import qcClientsModel

app = Flask(__name__)

@app.route("/")
def connectionStatus():
    return "Backend running properly"

@app.route("/getNextClient",methods = ['POST', 'GET'])
def getNextClient():
    print("Send the next graphs to the FE")
    return qcClientsModel.generateGraphs()

if __name__ == '__main__':
   app.run(debug = True)