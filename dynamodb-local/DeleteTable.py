import boto3
print('libraries imported')

def delete_movies_table():
    dynamodb = boto3.resource('dynamodb', 
                          region_name="us-west-2",
                          endpoint_url="http://localhost:8000",
                          aws_access_key_id="fakeMyKeyId",
                          aws_secret_access_key="fakeSecretAccessKey")
    
    table = dynamodb.Table('Movies')
    table.delete()

if __name__ == '__main__':
    delete_movies_table()
    print('Movies Table Deleted')