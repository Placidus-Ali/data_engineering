import boto3

def create_movie_table(table_name):
    
    dynamodb = boto3.client("dynamodb", 
                            region_name="us-west-2",
                            endpoint_url="http://localhost:8000",
                            aws_access_key_id="fakeMyKeyId",
                            aws_secret_access_key="fakeSecretAccessKey") # specify because I am using Dynamodb local
   
    table = dynamodb.create_table(
        
        TableName = table_name,
        KeySchema = [
            {
                'AttributeName': 'year',
                'KeyType': 'HASH' #Partition Key
            },
            {
                'AttributeName': 'title',
                'KeyType': 'RANGE' # Sort Key
            }
        ],
        AttributeDefinitions = [
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput= {
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }

    )
    return table

# Create Table
table_name = 'Movies'
create_movie_table(table_name=table_name)

# Check status
dynamodb = boto3.resource('dynamodb', 
                          region_name="us-west-2",
                          endpoint_url="http://localhost:8000",
                          aws_access_key_id="fakeMyKeyId",
                          aws_secret_access_key="fakeSecretAccessKey")

table = dynamodb.Table(table_name)

print('Table Status:', table.table_status)
