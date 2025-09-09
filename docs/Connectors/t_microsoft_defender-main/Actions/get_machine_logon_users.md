# Get Machine Logon Users

**Description**: Retrieve a list of users who have logged onto a specific machine by using the machine ID in Microsoft Defender.

## Endpoint

- **URL:** `/api/machines/{{id}}/logonusers`
- **Method:** `get`
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
      "Date": "Thu, 04 May 2023 17:56:11 GMT",
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
      "@odata.context": "https://api.securitycenter.microsoft.com/api/$metadata#Users",
      "value": [
        {
          "id": "se-pov-desktop\\chris phillips",
          "accountName": "chris phillips",
          "accountDomain": "se-pov-desktop",
          "accountSid": null,
          "firstSeen": "2023-04-26T15:03:14Z",
          "lastSeen": "2023-04-26T15:03:14Z",
          "mostPrevalentMachineId": null,
          "leastPrevalentMachineId": null,
          "logonTypes": "Interactive",
          "logOnMachinesCount": null,
          "isDomainAdmin": true,
          "isOnlyNetworkUser": null
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
    - **accountName** (string)
    - **accountDomain** (string)
    - **accountSid** (object)
    - **firstSeen** (string)
    - **lastSeen** (string)
    - **mostPrevalentMachineId** (object)
    - **leastPrevalentMachineId** (object)
    - **logonTypes** (string)
    - **logOnMachinesCount** (object)
    - **isDomainAdmin** (boolean)
    - **isOnlyNetworkUser** (object)
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