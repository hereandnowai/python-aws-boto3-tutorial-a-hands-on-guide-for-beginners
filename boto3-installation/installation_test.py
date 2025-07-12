#!/usr/bin/env python3
"""
This script replicates aws sts get-caller-identity output
"""

import json
import boto3


sts_client = boto3.client('sts')

response = sts_client.get_caller_identity()

user_id = response['UserId']
account = response['Account']
arn = response['Arn']

output = {
    'UserId': user_id,
    'Account': account,
    'Arn': arn
}

print(json.dumps(output, indent=4))
