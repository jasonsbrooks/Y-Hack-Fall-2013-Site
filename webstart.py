"""
URL routing & initialization for webapp
"""

from os.path import join
from main import app
from flask import send_from_directory, Blueprint, send_file


print "Starting webapp!"
# splash
from splash.views import splash
app.register_blueprint(splash)

if __name__ == '__main__':
    app.run()
