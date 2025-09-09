# Get User Related Machines

**Description**: Retrieve a list of machines associated with a specific user in Microsoft Defender using the user's unique identifier.

## Endpoint

- **URL:** `/api/users/{{id}}/machines`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required: The ID is not the full UPN, but only the user name. (for example, to retrieve machines for user1@contoso.com use /api/users/user1/machines).
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Mon, 26 May 2025 09:21:18 GMT",
      "Content-Type": "application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "Content-Encoding": "deflate",
      "Vary": "Accept-Encoding",
      "mise-correlation-id": "c6ccd948-929b-4073-be4d-df4328ff6798",
      "OData-Version": "4.0",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains"
    },
    "reason": "OK",
    "json_body": {
      "@odata.context": "https://api.securitycenter.microsoft.com/api/$metadata#Machines",
      "value": [
        {
          "id": "machine-1",
          "computerDnsName": "device1.corp.example.com",
          "firstSeen": "2024-01-01T00:00:00Z",
          "lastSeen": "2024-01-02T00:00:00Z",
          "osPlatform": "Windows10",
          "onboardingStatus": "onboarded",
          "osProcessor": "x64",
          "version": "10.0.19045",
          "osBuild": 19045,
          "lastIpAddress": "10.0.0.5",
          "lastExternalIpAddress": "203.0.113.1",
          "healthStatus": "Active",
          "rbacGroupName": "Finance",
          "rbacGroupId": "group-fin-001",
          "riskScore": "Low",
          "aadDeviceId": "d9f1373e-1733-437e-8f4c-3f77f60d3c92",
          "machineTags": [
            "laptop",
            "finance"
          ],
          "exposureLevel": "Medium",
          "deviceValue": "High",
          "ipAddresses": [
            {
              "ipAddress": "10.0.0.5",
              "type": "IPv4"
            },
            {
              "ipAddress": "fe80::abcd",
              "type": "IPv6"
            }
          ],
          "osArchitecture": "64-bit"
        },
        {
          "id": "machine-2",
          "computerDnsName": "device2.corp.example.com",
          "firstSeen": "2024-03-10T08:15:00Z",
          "lastSeen": "2024-03-11T08:15:00Z",
          "osPlatform": "Windows11",
          "onboardingStatus": "onboarded",
          "osProcessor": "x64",
          "version": "10.0.22000",
          "osBuild": 22000,
          "lastIpAddress": "10.0.0.10",
          "lastExternalIpAddress": "203.0.113.2",
          "healthStatus": "Inactive",
          "rbacGroupName": "HR",
          "rbacGroupId": "group-hr-001",
          "riskScore": "Medium",
          "aadDeviceId": null,
          "machineTags": [
            "desktop",
            "hr"
          ],
          "exposureLevel": "Low",
          "deviceValue": "Normal",
          "ipAddresses": [
            {
              "ipAddress": "10.0.0.10",
              "type": "IPv4"
            }
          ],
          "osArchitecture": "64-bit"
        }
      ]
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **value** (array)
    - **id** (string)
    - **computerDnsName** (string)
    - **firstSeen** (string)
    - **lastSeen** (string)
    - **osPlatform** (string)
    - **onboardingStatus** (string)
    - **osProcessor** (string)
    - **version** (string)
    - **osBuild** (number)
    - **lastIpAddress** (string)
    - **lastExternalIpAddress** (string)
    - **healthStatus** (string)
    - **rbacGroupName** (string)
    - **rbacGroupId** (string)
    - **riskScore** (string)
    - **aadDeviceId** (object)
    - **machineTags** (array)
    - **exposureLevel** (string)
    - **deviceValue** (string)
    - **ipAddresses** (array)
      - **ipAddress** (string)
      - **type** (string)
    - **osArchitecture** (string)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Content-Type | string |
| Transfer-Encoding | string |
| Connection | string |
| Content-Encoding | string |
| Vary | string |
| mise-correlation-id | string |
| OData-Version | string |
| Strict-Transport-Security | string |