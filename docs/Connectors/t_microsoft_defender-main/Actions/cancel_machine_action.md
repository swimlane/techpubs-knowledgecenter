# Cancel Machine Action

**Description**: Cancels a pending machine action in Microsoft Defender using the specified 'machineactionid'.

## Endpoint

- **URL:** `/api/machineactions/{{machineactionid}}/cancel`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required
  - **machineactionid** (string) – Required: The machine action ID.
- **json_body** (object) – Required
  - **Comment** (string): Comment to associate with the cancellation action.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Fri, 07 Feb 2025 10:57:23 GMT",
      "Content-Type": "application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "Content-Encoding": "deflate",
      "Vary": "Accept-Encoding",
      "mise-correlation-id": "8d39c870-35e0-4d26-aa40-b15aa1b5c79a",
      "OData-Version": "4.0",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains"
    },
    "reason": "OK",
    "json_body": {
      "id": "5382f7ea-7557-4ab7-9782-d50480024a4e",
      "type": "CollectInvestigationPackage",
      "scope": "Selective",
      "requestor": "Analyst@TestPrd.onmicrosoft.com",
      "externalID": "",
      "requestSource": "",
      "commands": [
        "PutFile"
      ],
      "cancellationRequestor": "",
      "requestorComment": "test for docs",
      "cancellationComment": "",
      "status": "Succeeded",
      "machineId": "7b1f4967d9728e5aa3c06a9e617a22a4a5a17378",
      "computerDnsName": "desktop-test",
      "cancellationDateTimeUtc": "2019-01-02T14:39:38.2262283Z",
      "creationDateTimeUtc": "2019-01-02T14:39:38.2262283Z",
      "lastUpdateDateTimeUtc": "2019-01-02T14:40:44.6596267Z",
      "title": "",
      "relatedFileInfo": ""
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **id** (string)
  - **type** (string)
  - **scope** (string)
  - **requestor** (string)
  - **externalID** (string)
  - **requestSource** (string)
  - **commands** (array)
  - **cancellationRequestor** (string)
  - **requestorComment** (string)
  - **cancellationComment** (string)
  - **status** (string)
  - **machineId** (string)
  - **computerDnsName** (string)
  - **cancellationDateTimeUtc** (string)
  - **creationDateTimeUtc** (string)
  - **lastUpdateDateTimeUtc** (string)
  - **title** (string)
  - **relatedFileInfo** (string)
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