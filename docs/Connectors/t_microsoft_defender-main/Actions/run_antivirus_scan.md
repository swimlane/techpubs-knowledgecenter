# Run Antivirus Scan

**Description**: Initiates a Microsoft Defender antivirus scan on an entity using machine ID with options to customize the comment and scan type.

## Endpoint

- **URL:** `/api/machines/{{id}}/runAntiVirusScan`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required
- **json_body** (object) – Required
  - **Comment** (string) – Required: Comment to associate with the action.
  - **ScanType** (string) – Required: Defines the type of the Scan. Possible values are Quick or Full. Quick- Perform quick scan on the device. Full- Perform full scan on the device.
## Output

### Example

```json
[
  {
    "status_code": 201,
    "response_headers": {
      "Date": "Fri, 13 Dec 2024 07:45:13 GMT",
      "Content-Type": "application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "Content-Encoding": "deflate",
      "Vary": "Accept-Encoding",
      "OData-Version": "4.0",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains"
    },
    "reason": "OK",
    "json_body": {
      "id": "5382f7ea-7557-4ab7-9782-d50480024a4e",
      "type": "Isolate",
      "scope": "Selective",
      "requestor": "Analyst@TestPrd.onmicrosoft.com",
      "requestorComment": "test for docs",
      "status": "Succeeded",
      "machineId": "7b1f4967d9728e5aa3c06a9e617a22a4a5a17378",
      "computerDnsName": "desktop-test",
      "creationDateTimeUtc": "2019-01-02T14:39:38.2262283Z",
      "lastUpdateDateTimeUtc": "2019-01-02T14:40:44.6596267Z",
      "relatedFileInfo": null
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
  - **requestorComment** (string)
  - **status** (string)
  - **machineId** (string)
  - **computerDnsName** (string)
  - **creationDateTimeUtc** (string)
  - **lastUpdateDateTimeUtc** (string)
  - **relatedFileInfo** (object)
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