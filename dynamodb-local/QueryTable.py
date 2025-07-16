import boto3
from boto3.dynamodb.conditions import key
print('libraries imported')

def query_students(Department):
    dynamodb = boto3.resource('dynamodb', 
                          region_name="us-west-2",
                          endpoint_url="http://localhost:8000",
                          aws_access_key_id="fakeMyKeyId",
                          aws_secret_access_key="fakeSecretAccessKey")
    
    table = dynamodb.Table('Students')
    response = table.query(
        KeyConditionExpression = key('Department').eq(Department)
    )
    return response['Items']

if __name__ == '__main__':
    query_data = 'Department'
    print(f' Students Department {query_data}')
    Student = query_students(query_data)
    for i in Student:
        print(Student['Department'], ":", Student['Name'])

print('Query successful')
