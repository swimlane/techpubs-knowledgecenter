# Get Investigation

**Description**: Retrieves a specific Microsoft Defender investigation using the provided ID, applicable to both investigation and alert IDs.

## Endpoint

- **URL:** `/api/investigations/{{id}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required: The Investigation ID.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Fri, 07 Feb 2025 06:30:27 GMT",
      "Content-Type": "application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "Content-Encoding": "deflate",
      "Vary": "Accept-Encoding",
      "mise-correlation-id": "08ce5338-e4be-4eab-a417-d0a5cf40bfac",
      "OData-Version": "4.0",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains"
    },
    "reason": "OK",
    "json_body": {
      "id": "63004",
      "startTime": "2020-01-06T13:05:15Z",
      "endTime": "2020-01-06T13:05:15Z",
      "state": "Running",
      "cancelledBy": "",
      "statusDetails": "",
      "machineId": "e828a0624ed33f919db541065190d2f75e50a071",
      "computerDnsName": "desktop-test123",
      "triggeringAlertId": "da637139127150012465_1011995739"
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **id** (string)
  - **startTime** (string)
  - **endTime** (string)
  - **state** (string)
  - **cancelledBy** (string)
  - **statusDetails** (string)
  - **machineId** (string)
  - **computerDnsName** (string)
  - **triggeringAlertId** (string)
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