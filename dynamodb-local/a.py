import boto3

dynamodb = boto3.client(
    'dynamodb',
    region_name="us-west-2",
    endpoint_url="http://localhost:8000",
    aws_access_key_id="fakeMyKeyId",
    aws_secret_access_key="fakeSecretAccessKey"
)

response = dynamodb.list_tables()
print("Tables:", response["TableNames"])

# After loading data
table = dynamodb.Table('Students')
response = table.scan()
print("Loaded rows:", len(response.get('Items', [])))
