# Get Static Incident Details

**Description**: Retrieve static attributes for a specified incident in Symantec DLP, ensuring compliance with user permissions.

## Endpoint

- **URL:** `/ProtectManager/webservices/v2/incidents/{{id}}/staticAttributes`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **id** (number) – Required: The incident ID.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "OK",
    "json_body": {
      "incidentId": 1,
      "infoMap": {
        "attachmentInfo": [
          {
            "messageComponentName": "ftpMe.txt",
            "messageComponentId": 2,
            "wasCracked": true,
            "documentFormat": "ascii",
            "messageComponentType": 3,
            "originalSize": "640 Bytes",
            "attachmentSize": "640 Bytes"
          }
        ],
        "messageOriginatorID": 1,
        "fileCreateDate": "2019-06-26T17:33:06.71",
        "uniqueMessageId": "F1472CC7-CF59-405C-9F12-CE428B112978",
        "fileAccessDate": "2019-06-26T00:00:00",
        "messageType": "ENDPOINTUSB",
        "endpointFilePath": "E:\\ftpMe.txt",
        "endpointApplicationPath": "\\Device\\HarddiskVolume1\\WINDOWS\\explorer.exe",
        "senderIPAddress": "10.66.221.73",
        "endpointVolumeName": "\\Device\\Harddisk1\\DP(1)0-0+3",
        "fileCreatedBy": "LEVY-XP-1\\dirk",
        "domainUserName": "LEVY-XP-1\\dirk",
        "policyId": 1,
        "policyName": "v9 - Hello World Silent",
        "policyVersion": 3,
        "policyGroupName": "V9 Automation Policies",
        "policyGroupId": 2,
        "fileModifiedBy": "LEVY-XP-1\\dirk",
        "messageId": 1,
        "messageSource": "ENDPOINT",
        "matchCount": 7,
        "creationDate": "2019-06-26T17:29:50.937",
        "isBlockedStatusSuperseded": false,
        "detectionServerName": "v15 - Monitor (Discover, Endpoint)",
        "endpointConnectionStatus": "CONNECTED",
        "endpointFileName": "ftpMe.txt",
        "networkSenderPort": 0,
        "detectionDate": "2019-06-26T17:29:50.937",
        "messageTypeId": 13,
        "detectionServerId": 1,
        "endpointMachineIpAddress": "10.66.221.73",
        "messageDate": "2019-06-26T17:33:07.796",
        "fileOwner": "LEVY-XP-1\\dirk",
        "endpointMachineName": "LEVY-XP-1",
        "endpointApplicationName": "explorer.exe"
      }
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **incidentId** (number)
  - **infoMap** (object)
    - **attachmentInfo** (array)
      - **messageComponentName** (string)
      - **messageComponentId** (number)
      - **wasCracked** (boolean)
      - **documentFormat** (string)
      - **messageComponentType** (number)
      - **originalSize** (string)
      - **attachmentSize** (string)
    - **messageOriginatorID** (number)
    - **fileCreateDate** (string)
    - **uniqueMessageId** (string)
    - **fileAccessDate** (string)
    - **messageType** (string)
    - **endpointFilePath** (string)
    - **endpointApplicationPath** (string)
    - **senderIPAddress** (string)
    - **endpointVolumeName** (string)
    - **fileCreatedBy** (string)
    - **domainUserName** (string)
    - **policyId** (number)
    - **policyName** (string)
    - **policyVersion** (number)
    - **policyGroupName** (string)
    - **policyGroupId** (number)
    - **fileModifiedBy** (string)
    - **messageId** (number)
    - **messageSource** (string)
    - **matchCount** (number)
    - **creationDate** (string)
    - **isBlockedStatusSuperseded** (boolean)
    - **detectionServerName** (string)
    - **endpointConnectionStatus** (string)
    - **endpointFileName** (string)
    - **networkSenderPort** (number)
    - **detectionDate** (string)
    - **messageTypeId** (number)
    - **detectionServerId** (number)
    - **endpointMachineIpAddress** (string)
    - **messageDate** (string)
    - **fileOwner** (string)
    - **endpointMachineName** (string)
    - **endpointApplicationName** (string)