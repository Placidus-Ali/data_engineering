from decimal import Decimal
import json
import boto3
print('Import Successfully')

def load_data(data):
    dynamodb = boto3.resource('dynamodb', 
                          region_name="us-west-2",
                          endpoint_url="http://localhost:8000",
                          aws_access_key_id="fakeMyKeyId",
                          aws_secret_access_key="fakeSecretAccessKey")
    
    table = dynamodb.Table('Students')

    for record in data:
        item = record['PutRequest']['Item']
        
        # Write item using unpacked types
        table.put_item(Item={
            'StudentID': item['StudentID']['S'],
            'Name': item['Name']['S'],
            'Age': int(item['Age']['N']),
            'Department': item['Department']['S']
        })
# Start Here
if __name__ == '__main__':
    with open('Student.json') as json_file:
        student_data = json.load(json_file, parse_float=Decimal)
        load_data(student_data)
print('Loaded successfully')