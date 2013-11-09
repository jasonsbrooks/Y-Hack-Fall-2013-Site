from flask import (Flask, render_template, Response, request, 
    Blueprint, redirect, send_from_directory, send_file, jsonify, g)



splash = Blueprint('splash', __name__, template_folder="")

@splash.route('/')
def home():
    return render_template('templates/home.html')