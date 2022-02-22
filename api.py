
from flask import Flask,jsonify,request
api=Flask(__name__)

tasks=[
    {
        "id":1,
        "title":"Walking",
        "description":"Walk outside for 5 minutes",
        "done":True
    }
]
@api.route("/")
def hi():
    return "hello"

@api.route("/getdata")
def bye():
    return jsonify({
        "data":tasks
    })
@api.route("/adddata",methods=["POST"])
def add():
    task={
      "id":tasks[-1]["id"]+1,
        "title":request.json["title"],
        "description":request.json["description"],
        "done":True  
    }
    tasks.append(task)
    return jsonify({
       "message":"Task added" 
    })

api.run()