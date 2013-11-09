from flask import (Flask, render_template, Response, request, 
    Blueprint, redirect, send_from_directory, send_file, jsonify, g)
import time, os, json, base64, hmac, sha, urllib
from splash import urlNewSoloCup
import boto
from boto.s3.key import Key
import random, string
from werkzeug.utils import secure_filename

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
bucket_name = AWS_ACCESS_KEY_ID.lower() + '-solocups'

splash = Blueprint('splash', __name__, template_folder="")

def id_generator(size=15, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

@splash.route('/')
def home():
    return render_template('templates/home.html')

@splash.route('/photo_upload/', methods=["POST"])
def photo_upload():
    file = request.files['Photo']
    filename = secure_filename(file.filename)
    conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    bucket = conn.get_bucket(bucket_name)
    k = Key(bucket)
    k.key = id_generator() + "-" + filename
    k.set_contents_from_string(file.read())
    k.make_public()
    url = k.generate_url(expires_in=0, query_auth=False)
    return url

@splash.route('/process_photo/', methods=["GET"])
def process_photo():
    createdURL = request.args.get('newLink')
    # print createdURL
    # return createdURL
    url = urlNewSoloCup(createdURL)
    return url