# Create Contact

**Description**: Adds a new contact to a specified folder in Microsoft Graph API using the provided 'id'.

## Endpoint

- **URL:** `/v1.0/users/{{id}}/contacts`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required
- **json_body** (object) – Required
  - **givenName** (string): The contact's given name.
  - **surname** (string): The contact's surname.
  - **emailAddresses** (array): The contact's email addresses.
    - **address** (string): The email address of the contact.
    - **name** (string): The display name of the contact.
  - **businessPhones** (array): The contact's business phone numbers.
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
      "request-id": "f2584bdf-0295-424e-bdb1-2df08413c0c3",
      "client-request-id": "f2584bdf-0295-424e-bdb1-2df08413c0c3",
      "x-ms-ags-diagnostic": "{\"ServerInfo\":{\"DataCenter\":\"Central India\",\"Slice\":\"E\",\"Ring\":\"3\",\"ScaleUnit\":\"002\",\"RoleInstance\":\"PN2PEPF00000273\"}}",
      "x-ms-resource-unit": "2",
      "OData-Version": "4.0",
      "Date": "Wed, 06 Nov 2024 15:54:59 GMT"
    },
    "reason": "OK",
    "json_body": {
      "id": "id-value",
      "createdDateTime": "2015-11-09T02:14:32Z",
      "lastModifiedDateTime": "2015-11-09T02:14:32Z",
      "displayName": "Pavel Bansky"
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **id** (string)
  - **createdDateTime** (string)
  - **lastModifiedDateTime** (string)
  - **displayName** (string)
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