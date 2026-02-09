import boto3

class Session:
    def __init__(self, profile_name=None, aws_access_key_id=None, aws_secret_access_key=None, region_name='us-east-1'):
        self.profile_name = profile_name
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.region_name = region_name

    def create_session(self):
        if self.profile_name:
            return boto3.Session(
                profile_name=self.profile_name,
                region_name=self.region_name
            )
        elif self.aws_access_key_id:
            return boto3.Session(
                aws_access_key_id=self.aws_access_key_id,
                aws_secret_access_key=self.aws_secret_access_key,
                region_name=self.region_name
            )
        else:
            return boto3.Session(region_name=self.region_name)