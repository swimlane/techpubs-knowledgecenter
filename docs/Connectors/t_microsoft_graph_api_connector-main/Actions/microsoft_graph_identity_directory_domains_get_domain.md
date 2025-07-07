# Get Identity Directory Domain

**Description**: Retrieve details for a specific domain in Microsoft Graph API using the provided domain ID.

## Endpoint

- **URL:** `v1.0/domains/{{id}}`
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
      "Cache-Control": "no-cache",
      "Transfer-Encoding": "chunked",
      "Content-Type": "application/json;odata.metadata=minimal;odata.streaming=true;IEEE754Compatible=false;charset=utf-8",
      "Content-Encoding": "gzip",
      "Vary": "Accept-Encoding",
      "Strict-Transport-Security": "max-age=31536000",
      "request-id": "c09cf6ea-706b-4950-a1f9-30941a7317f9",
      "client-request-id": "c09cf6ea-706b-4950-a1f9-30941a7317f9",
      "x-ms-ags-diagnostic": "{\"ServerInfo\":{\"DataCenter\":\"South Central US\",\"Slice\":\"E\",\"Ring\":\"5\",\"ScaleUnit\":\"001\",\"RoleInstance\":\"SA2PEPF00000851\"}}",
      "x-ms-resource-unit": "1",
      "OData-Version": "4.0",
      "Date": "Tue, 20 Dec 2022 19:24:30 GMT"
    },
    "reason": "OK",
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
| Vary | string |
| Strict-Transport-Security | string |
| request-id | string |
| client-request-id | string |
| x-ms-ags-diagnostic | string |
| x-ms-resource-unit | string |
| OData-Version | string |
| Date | string |