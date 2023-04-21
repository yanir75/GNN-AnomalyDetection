import json
with open('flaws_cloudtrail00.json', 'r') as f:
    data = json.loads(f.read())
di = {
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDA3HQLQ32SRYK4AY6UJ",
        "arn": "arn:aws:iam::811596193553:user/cloud_user",
        "accountId": "811596193553",
        "accessKeyId": "ASIA3HQLQ32SX4QDO45J",
        "userName": "cloud_user",
        "sessionContext": {
            "sessionIssuer": {},
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-03-14T08:29:50Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2023-03-14T11:23:25Z",
    "eventSource": "ec2.amazonaws.com",
    "eventName": "StartInstances",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "2.46.70.163",
    "userAgent": "AWS Internal",
    "requestParameters": {
        "instancesSet": {
            "items": [
                {
                    "instanceId": "i-0ac2c5d2f9147291a"
                }
            ]
        }
    },
    "responseElements": {
        "requestId": "e39d268b-dc9c-42a5-9ef5-5abdfe8a5ae5",
        "instancesSet": {
            "items": [
                {
                    "instanceId": "i-0ac2c5d2f9147291a",
                    "currentState": {
                        "code": 0,
                        "name": "pending"
                    },
                    "previousState": {
                        "code": 80,
                        "name": "stopped"
                    }
                }
            ]
        }
    },
    "requestID": "e39d268b-dc9c-42a5-9ef5-5abdfe8a5ae5",
    "eventID": "c6c4f90f-330e-4164-84f8-cd397e7be91d",
    "readOnly": False,
    "eventType": "AwsApiCall",
    "managementEvent": True,
    "recipientAccountId": "811596193553",
    "eventCategory": "Management",
    "sessionCredentialFromConsole": "true"
}

di1 = {
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDA3HQLQ32SY2BOR5WIG",
        "arn": "arn:aws:iam::811596193553:user/cloud_user",
        "accountId": "811596193553",
        "accessKeyId": "AKIA3HQLQ32SSBRTNM2E",
        "userName": "cloud_user"
    },
    "eventTime": "2023-03-21T09:34:55Z",
    "eventSource": "ec2.amazonaws.com",
    "eventName": "TerminateInstances",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "54.90.42.239",
    "userAgent": "APN/1.0 HashiCorp/1.0 Terraform/1.4.2 (+https://www.terraform.io) terraform-provider-aws/4.59.0 (+https://registry.terraform.io/providers/hashicorp/aws) aws-sdk-go/1.44.221 (go1.19.6; linux; amd64)",
    "requestParameters": {
        "instancesSet": {
            "items": [
                {
                    "instanceId": "i-0102a8fbd94d1925f"
                }
            ]
        }
    },
    "responseElements": {
        "requestId": "1eb78b80-18c5-4b78-b608-909c7dbd62ae",
        "instancesSet": {
            "items": [
                {
                    "instanceId": "i-0102a8fbd94d1925f",
                    "currentState": {
                        "code": 32,
                        "name": "shutting-down"
                    },
                    "previousState": {
                        "code": 16,
                        "name": "running"
                    }
                }
            ]
        }
    },
    "requestID": "1eb78b80-18c5-4b78-b608-909c7dbd62ae",
    "eventID": "ea46b9b3-3657-4ed4-ac3b-aba1321aed9b",
    "readOnly": False,
    "eventType": "AwsApiCall",
    "managementEvent": True,
    "recipientAccountId": "811596193553",
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "TLSv1.2",
        "cipherSuite": "ECDHE-RSA-AES128-GCM-SHA256",
        "clientProvidedHostHeader": "ec2.us-east-1.amazonaws.com"
    }
}
for i in range(1000):
    data['Records'].append(di)

for i in range(1000):
    data['Records'].append(di1)
with open('attack.json', 'w') as fp:
    json.dump(data, fp)