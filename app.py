from random import choice
from flask import Flask, jsonify, render_template, url_for, request
from flask_cors import CORS
from werkzeug import exceptions

app = Flask(__name__) # Boilerplate
CORS(app)
# app.use("/", controller)
# If you go to "/", you get an index. This is a route.

@app.route("/") 
def index():
    return render_template("index.html", app_name="Trina and Jianli's Princess API")

@app.route("/hive")
def hive(): #dictionary
    return jsonify({ 
        "number_of_bees": 300,
        "queen": True
    })

@app.route("/bee/new", methods=["POST"])
def create_bee():
    data = request.json
    print(data)
    return {
        "success": True,
        "message": "We definitely really created your bee."
    }, 201

@app.route("/princesses/all", methods=["GET"])
def all_bees():
    if request.method == "GET":
        return jsonify([{
            "name": "Beep Beep",
            "age": 20
        }, 
        {
            "name": "Killer Bee",
            "age": 70
        }])

@app.route("/princesses/<int:id>", methods=["GET", "DELETE"]) #Flask lets us do type requirements
def interact_with_bee(id):
    chosen_name = choice(["Beetholomew", "Beeatrice", "Beenedict", "Beeyonce", "Beenard", "Beelinda", "Beenjamin"])
     
    if request.method == "GET":
        return jsonify({
        "id": id,
        "name": chosen_name,
        "age": "never ask a lady's age"
        }), 200

    elif request.method == "DELETE":
        return jsonify({
            "success": True,
            "message": f"{chosen_name} she lost her royalty."
        }), 201

@app.errorhandler(exceptions.NotFound)
def page_not_found(err):
    return render_template("404.html", data={
        "error": err,
        "message": "No, Shrek did not kidnap them, you are just terrible at finding people, or websites"
    })

if __name__ == "__main__":
    app.run(debug=True)
