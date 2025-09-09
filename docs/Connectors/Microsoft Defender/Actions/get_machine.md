# Get Machine

**Description**: Retrieves details for a specified machine from Microsoft Defender using the provided machine ID.

## Endpoint

- **URL:** `/api/machines/{{id}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Thu, 04 May 2023 17:56:56 GMT",
      "Content-Type": "application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "Content-Encoding": "deflate",
      "Vary": "Accept-Encoding",
      "OData-Version": "4.0",
      "Strict-Transport-Security": "max-age=15724800; includeSubDomains"
    },
    "reason": "OK",
    "json_body": {
      "@odata.context": "https://api.securitycenter.microsoft.com/api/$metadata#Machines/$entity",
      "id": "556b3952acb0bff29816d267822305781cc183ec",
      "mergedIntoMachineId": null,
      "isPotentialDuplication": false,
      "isExcluded": false,
      "exclusionReason": null,
      "computerDnsName": "se-pov-desktop",
      "firstSeen": "2023-04-19T13:27:53.1618923Z",
      "lastSeen": "2023-05-04T17:40:05.684607Z",
      "osPlatform": "Windows10",
      "osVersion": null,
      "osProcessor": "x64",
      "version": "21H2",
      "lastIpAddress": "172.20.10.4",
      "lastExternalIpAddress": "174.209.205.235",
      "agentVersion": "10.8470.19041.2788",
      "osBuild": 19044,
      "healthStatus": "Active",
      "deviceValue": "Normal",
      "rbacGroupId": 0,
      "rbacGroupName": null,
      "riskScore": "Medium",
      "exposureLevel": "High",
      "isAadJoined": true,
      "aadDeviceId": null,
      "machineTags": [],
      "defenderAvStatus": "Updated",
      "onboardingStatus": "Onboarded",
      "osArchitecture": "64-bit",
      "managedBy": "Intune",
      "managedByStatus": "Unknown",
      "ipAddresses": [
        {
          "ipAddress": "172.20.10.5",
          "macAddress": "000C2992A643",
          "type": "Ethernet",
          "operationalStatus": "Up"
        },
        {
          "ipAddress": "172.20.10.4",
          "macAddress": "000C2992A64D",
          "type": "Ethernet",
          "operationalStatus": "Up"
        },
        {
          "ipAddress": "2600:1005:b06a:4c66:f78f:83dc:7271:383e",
          "macAddress": "000C2992A64D",
          "type": "Ethernet",
          "operationalStatus": "Up"
        },
        {
          "ipAddress": "2600:1005:b06a:4c66:103a:4e1b:bd95:793e",
          "macAddress": "000C2992A64D",
          "type": "Ethernet",
          "operationalStatus": "Up"
        },
        {
          "ipAddress": "fe80::359c:fd3a:8880:ddb6",
          "macAddress": "000C2992A64D",
          "type": "Ethernet",
          "operationalStatus": "Up"
        },
        {
          "ipAddress": "169.254.5.16",
          "macAddress": "147DDAA128C4",
          "type": "Ethernet",
          "operationalStatus": "Down"
        },
        {
          "ipAddress": "fe80::f1fc:1543:f2f4:228d",
          "macAddress": "147DDAA128C4",
          "type": "Ethernet",
          "operationalStatus": "Down"
        },
        {
          "ipAddress": "127.0.0.1",
          "macAddress": null,
          "type": "SoftwareLoopback",
          "operationalStatus": "Up"
        },
        {
          "ipAddress": "::1",
          "macAddress": null,
          "type": "SoftwareLoopback",
          "operationalStatus": "Up"
        }
      ],
      "vmMetadata": null
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **id** (string)
  - **mergedIntoMachineId** (object)
  - **isPotentialDuplication** (boolean)
  - **isExcluded** (boolean)
  - **exclusionReason** (object)
  - **computerDnsName** (string)
  - **firstSeen** (string)
  - **lastSeen** (string)
  - **osPlatform** (string)
  - **osVersion** (object)
  - **osProcessor** (string)
  - **version** (string)
  - **lastIpAddress** (string)
  - **lastExternalIpAddress** (string)
  - **agentVersion** (string)
  - **osBuild** (number)
  - **healthStatus** (string)
  - **deviceValue** (string)
  - **rbacGroupId** (number)
  - **rbacGroupName** (object)
  - **riskScore** (string)
  - **exposureLevel** (string)
  - **isAadJoined** (boolean)
  - **aadDeviceId** (object)
  - **machineTags** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **defenderAvStatus** (string)
  - **onboardingStatus** (string)
  - **osArchitecture** (string)
  - **managedBy** (string)
  - **managedByStatus** (string)
  - **ipAddresses** (array)
    - **ipAddress** (string)
    - **macAddress** (object)
    - **type** (string)
    - **operationalStatus** (string)
  - **vmMetadata** (object)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Content-Type | string |
| Transfer-Encoding | string |
| Connection | string |
| Content-Encoding | string |
| Vary | string |
| OData-Version | string |
| Strict-Transport-Security | string |