# Create Identity Directory Domain

**Description**: Adds a new domain to the Microsoft Graph API tenant using the specified 'id' provided in the JSON body input.

## Endpoint

- **URL:** `v1.0/domains`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required
  - **authenticationType** (string)
  - **availabilityStatus** (string)
  - **id** (string) – Required
  - **isAdminManaged** (boolean)
  - **isDefault** (boolean)
  - **isInitial** (boolean)
  - **isRoot** (boolean)
  - **isVerified** (boolean)
  - **passwordNotificationWindowInDays** (number)
  - **passwordValidityPeriodInDays** (number)
  - **state** (object)
    - **@odata.type** (string)
  - **supportedServices** (array)
## Output

### Example

```json
[
  {
    "status_code": 201,
    "response_headers": {
      "Cache-Control": "no-cache",
      "Transfer-Encoding": "chunked",
      "Content-Type": "application/json;odata.metadata=minimal;odata.streaming=true;IEEE754Compatible=false;charset=utf-8",
      "Content-Encoding": "gzip",
      "Location": "https://graph.microsoft.com/v2/f5d73c4c-bb3d-421b-8bee-424916a4acca/domains/myradom.test.directory",
      "Vary": "Accept-Encoding",
      "Strict-Transport-Security": "max-age=31536000",
      "request-id": "73f2f6f6-c705-452a-8d93-b5645597115e",
      "client-request-id": "73f2f6f6-c705-452a-8d93-b5645597115e",
      "x-ms-ags-diagnostic": "{\"ServerInfo\":{\"DataCenter\":\"South Central US\",\"Slice\":\"E\",\"Ring\":\"5\",\"ScaleUnit\":\"005\",\"RoleInstance\":\"SN4PEPF0000000A\"}}",
      "x-ms-resource-unit": "1",
      "OData-Version": "4.0",
      "Date": "Tue, 20 Dec 2022 19:08:29 GMT"
    },
    "reason": "Created",
    "json_body": {
      "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#domains/$entity",
      "authenticationType": "Managed",
      "availabilityStatus": null,
      "id": "myradom.test.directory",
      "isAdminManaged": true,
      "isDefault": false,
      "isInitial": false,
      "isRoot": false,
      "isVerified": false,
      "supportedServices": [],
      "passwordValidityPeriodInDays": null,
      "passwordNotificationWindowInDays": null,
      "state": null
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **authenticationType** (string)
  - **availabilityStatus** (object)
  - **id** (string)
  - **isAdminManaged** (boolean)
  - **isDefault** (boolean)
  - **isInitial** (boolean)
  - **isRoot** (boolean)
  - **isVerified** (boolean)
  - **supportedServices** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **passwordValidityPeriodInDays** (object)
  - **passwordNotificationWindowInDays** (object)
  - **state** (object)
## Response Headers

| Header | Type |
|--------|------|
| Cache-Control | string |
| Transfer-Encoding | string |
| Content-Type | string |
| Content-Encoding | string |
| Location | string |
| Vary | string |
| Strict-Transport-Security | string |
| request-id | string |
| client-request-id | string |
| x-ms-ags-diagnostic | string |
| x-ms-resource-unit | string |
| OData-Version | string |
| Date | string |