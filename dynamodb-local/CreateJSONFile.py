import boto3
print('boto3 imported')

[
  {
    "PutRequest": {
      "Item": {
        "StudentID": { "S": "001" },
        "Name": { "S": "Placidus Ali" },
        "Age": { "N": "24" },
        "Department": { "S": "Computer Science" }
      }
    }
  },
  {
    "PutRequest": {
      "Item": {
        "StudentID": { "S": "002" },
        "Name": { "S": "Mary John" },
        "Age": { "N": "22" },
        "Department": { "S": "Engineering" }
      }
    }
  }
]
