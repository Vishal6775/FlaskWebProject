import boto3
import sagemaker

class CreateS3Bucket:
    def  __init__(self):
        self.client = boto3.client('s3')
        
    def create_bucket(self):
        response = self.client.create_bucket(
                        Bucket='training-testing-data-bucket',
                        CreateBucketConfiguration=
                        {
                            'LocationConstraint': 'us-west-2',
                        },
                    )
        return response
