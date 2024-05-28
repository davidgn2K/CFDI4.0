from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", name="NOMBRE", age=21)

@views.route("/profile")
def profile():
    ##args = request.args
    ##name = args.get('name')
    return render_template("profile.html")

@views.route("/json")
def get_json():
    return jsonify({'name': 'tim' 'manly', 'coolness':10},{'name':'jessi'})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))

@views.route("/facturacion")
def facturacion():
    return render_template("datos.html")