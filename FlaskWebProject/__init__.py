"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import FlaskWebProject.views
from FlaskWebProject.services.AWSCreateS3Bucket import *

s3 = CreateS3Bucket()
#response = s3.create_bucket()
#print(response)