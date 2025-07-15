### Step 1: Install Java (if not installed)
# DynamoDB Local runs on Java. To check if you have Java:


## java -version
# If you don’t see a version (or get an error), download Java JDK:
# https://www.oracle.com/java/technologies/javase-downloads.html
# Install it and restart VS Code.

## Step 2: Create a DynamoDB Local Project Folder
# In VS Code terminal:
# mkdir dynamodb-local
# cd dynamodb-local

## Step 3: Download DynamoDB Local
# Download from the official AWS link:
# https://s3.us-west-2.amazonaws.com/dynamodb-local/dynamodb_local_latest.zip

#Then:
# Extract the .zip file into your dynamodb-local folder.
#It will contain:
# DynamoDBLocal.jar
# DynamoDBLocal_lib/ folder

# Your folder should now look like:
# dynamodb-local/
# ├── DynamoDBLocal.jar
# └── DynamoDBLocal_lib/

## Step 4: Start the Local DynamoDB Server
# In VS Code terminal (while in the dynamodb-local folder):
# java "-Djava.library.path=./DynamoDBLocal_lib" -jar DynamoDBLocal.jar -sharedDb
# This will start DynamoDB on http://localhost:8000.

# Keep this terminal open — it runs the database server.

## Step 5:
# Download and install AWS CLI
# https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

## Step 6: Configure AWS CLI with Dummy Credentials
# Open a new terminal tab in VS Code and run:
# aws configure
# Input dummy values:
# AWS Access Key ID [None]: dummy
# AWS Secret Access Key [None]: dummy
# Default region name [None]: us-west-2
# Default output format [None]: json

## Step 7: Test by Creating a Table
# In the same terminal, run:
# aws dynamodb create-table \
#  --table-name Students \
#  --attribute-definitions AttributeName=StudentID,AttributeType=S \
#  --key-schema AttributeName=StudentID,KeyType=HASH \
#  --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
#  --endpoint-url http://localhost:8000

# You should see a JSON response confirming the table was created.

## Step 8: List Tables
#aws dynamodb list-tables --endpoint-url http://localhost:8000
# You should see:

#{
#  "TableNames": ["Students"]
#}

## Step 9: Add and Get Data
# Add (Put) an Item:
# aws dynamodb put-item \
#  --table-name Students \
#  --item '{"StudentID": {"S": "001"}, "Name": {"S": "Placidus Ali"}}' \
#  --endpoint-url http://localhost:8000

# Get an Item:
# aws dynamodb get-item \
#  --table-name Students \
#  --key '{"StudentID": {"S": "001"}}' \
#  --endpoint-url http://localhost:8000

## To list Tables
# aws dynamodb list-tables --endpoint-url http://localhost:8000 --region us-west-2
