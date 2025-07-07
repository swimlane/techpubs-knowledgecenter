# Get Identity Directory Domain List

**Description**: Retrieve domain objects for identity management via Microsoft Graph API, providing an overview of configured domains.

## Endpoint

- **URL:** `v1.0/domains`
- **Method:** `GET`
## Inputs

- **parameters** (object): URL Query Parameters
  - **count** (string): Include a count of the total number of items in a collection alongside the page of data values returned from Microsoft Graph
  - **filter** (string): Use the $filter query parameter to retrieve just a subset of a collection. For guidance on using $filter, see https://learn.microsoft.com/en-us/graph/filter-query-parameter
  - **orderby** (string): To sort the results in ascending or descending order, append either asc or desc to the field name, separated by a space.
  - **top** (number): Sets the page size of results
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
      "request-id": "b5a524cf-a136-43aa-ba1e-2cd046055f52",
      "client-request-id": "b5a524cf-a136-43aa-ba1e-2cd046055f52",
      "x-ms-ags-diagnostic": "{\"ServerInfo\":{\"DataCenter\":\"South Central US\",\"Slice\":\"E\",\"Ring\":\"5\",\"ScaleUnit\":\"003\",\"RoleInstance\":\"SN4PEPF000004FC\"}}",
      "x-ms-resource-unit": "1",
      "OData-Version": "4.0",
      "Date": "Tue, 20 Dec 2022 18:47:40 GMT"
    },
    "reason": "OK",
    "json_body": {
      "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#domains",
      "value": [
        {
          "authenticationType": "Managed",
          "availabilityStatus": null,
          "id": "bestcompanyever.com",
          "isAdminManaged": true,
          "isDefault": false,
          "isInitial": false,
          "isRoot": false,
          "isVerified": false,
          "supportedServices": [],
          "passwordValidityPeriodInDays": null,
          "passwordNotificationWindowInDays": null,
          "state": null
        },
        {
          "authenticationType": "Managed",
          "availabilityStatus": null,
          "id": "swimlaneintegrations.onmicrosoft.com",
          "isAdminManaged": true,
          "isDefault": true,
          "isInitial": true,
          "isRoot": true,
          "isVerified": true,
          "supportedServices": [
            "Email",
            "OfficeCommunicationsOnline"
          ],
          "passwordValidityPeriodInDays": 2147483647,
          "passwordNotificationWindowInDays": 14,
          "state": null
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
    - **authenticationType** (string)
    - **availabilityStatus** (object)
    - **id** (string)
    - **isAdminManaged** (boolean)
    - **isDefault** (boolean)
    - **isInitial** (boolean)
    - **isRoot** (boolean)
    - **isVerified** (boolean)
    - **supportedServices** (array)
    - **passwordValidityPeriodInDays** (number)
    - **passwordNotificationWindowInDays** (number)
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