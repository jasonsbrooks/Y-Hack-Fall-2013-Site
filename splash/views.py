from flask import (Flask, render_template, Response, request, 
    Blueprint, redirect, send_from_directory, send_file, jsonify, g)
import time, os, json, base64, hmac, sha, urllib


splash = Blueprint('splash', __name__, template_folder="")

@splash.route('/')
def home():
    return render_template('templates/home.html')

@splash.route('/sign_s3/')
def sign_s3():
    AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    S3_BUCKET = os.environ.get('S3_BUCKET')

    object_name = request.args.get('s3_object_name')
    mime_type = request.args.get('s3_object_type')

    expires = int(time.time()+10)
    amz_headers = "x-amz-acl:public-read"

    put_request = "PUT\n\n%s\n%d\n%s\n/%s/%s" % (mime_type, expires, amz_headers, S3_BUCKET, object_name)

    signature = base64.encodestring(hmac.new(AWS_SECRET_KEY,put_request, sha).digest())
    signature = urllib.quote_plus(signature.strip())

    url = 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET, object_name)

    return json.dumps({
        'signed_request': '%s?AWSAccessKeyId=%s&Expires=%d&Signature=%s' % (url, AWS_ACCESS_KEY, expires, signature),
         'url': url
      })

@splash.route('/send_url/', methods=["POST"])
def receive_url():
	url = request.form["red_url"]