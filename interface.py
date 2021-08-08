from flask import Flask,jsonify
from function import addition
app=Flask(__name__)

@app.route('/')
def welcome():
    print("we are learning flask")
    return 'welcome arati chya gavat'


@app.route('/addition')
def name():
    a = 100
    b = 30
    result =addition(a,b)
    return({"message":f"addition is: {result}"})


@app.route('/name')
def jso():
    return jsonify({"message":"hxhj"})



if __name__ == "__main__":
        app.run()