# Run Hunting Query

**Description**: Execute advanced threat hunting queries through the Microsoft Graph API to identify potential threats within Microsoft 365 Defender.

## Endpoint

- **URL:** `/v1.0/security/runHuntingQuery`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required: JSON Body
  - **query** (string): The hunting query in Kusto Query Language (KQL)
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Transfer-Encoding": "chunked",
      "Content-Type": "application/json",
      "Content-Encoding": "gzip",
      "Vary": "Accept-Encoding",
      "Strict-Transport-Security": "max-age=31536000",
      "request-id": "8beed643-f868-4fd0-9e15-e0db4c50383e",
      "client-request-id": "8beed643-f868-4fd0-9e15-e0db4c50383e",
      "x-ms-ags-diagnostic": "{\"ServerInfo\":{\"DataCenter\":\"Brazil South\",\"Slice\":\"E\",\"Ring\":\"3\",\"ScaleUnit\":\"001\",\"RoleInstance\":\"CP1PEPF00003034\"}}",
      "Date": "Tue, 27 Dec 2022 21:12:51 GMT"
    },
    "reason": "OK",
    "json_body": {
      "schema": [
        {
          "Name": "Timestamp",
          "Type": "DateTime"
        },
        {
          "Name": "FileName",
          "Type": "String"
        },
        {
          "Name": "InitiatingProcessFileName",
          "Type": "String"
        }
      ],
      "results": [
        {
          "Timestamp": "2020-08-30T06:38:35.7664356Z",
          "FileName": "conhost.exe",
          "InitiatingProcessFileName": "powershell.exe"
        },
        {
          "Timestamp": "2020-08-30T06:38:30.5163363Z",
          "FileName": "conhost.exe",
          "InitiatingProcessFileName": "powershell.exe"
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
  - **schema** (array)
    - **Name** (string)
    - **Type** (string)
  - **results** (array)
    - **Timestamp** (string)
    - **FileName** (string)
    - **InitiatingProcessFileName** (string)
## Response Headers

| Header | Type |
|--------|------|
| Transfer-Encoding | string |
| Content-Type | string |
| Content-Encoding | string |
| Vary | string |
| Strict-Transport-Security | string |
| request-id | string |
| client-request-id | string |
| x-ms-ags-diagnostic | string |
| Date | string |