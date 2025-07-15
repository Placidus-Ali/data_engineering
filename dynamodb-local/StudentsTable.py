import boto3

def create_students_table(table_name):
    dynamodb = boto3.client(
        "dynamodb",
        region_name="us-west-2",
        endpoint_url="http://localhost:8000",
        aws_access_key_id="fakeMyKeyId",
        aws_secret_access_key="fakeSecretAccessKey"
    )

    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'StudentID',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'StudentID',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    return table

# Create the table
table_name = 'Students'
table = create_students_table(table_name)

# Wait until it's active
dynamodb = boto3.resource(
    'dynamodb',
    region_name='us-west-2',
    endpoint_url='http://localhost:8000',
    aws_access_key_id='fakeMyKeyId',
    aws_secret_access_key='fakeSecretAccessKey'
)
table = dynamodb.Table(table_name)

table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
print("Table Status:", table.table_status)


