# Retrieve Authentication Methods

**Description**: Retrieve a user's authentication methods in Microsoft Graph API using their mail ID.

## Endpoint

- **URL:** `/v1.0/users/{{mailid}}/authentication/methods`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **mailid** (string) – Required: The account associated with the email.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "client-request-id": "30bcb75d-a62f-85ad-90e1-d7d1978e9ca3",
      "content-type": "application/json;odata.metadata=minimal;odata.streaming=true;IEEE754Compatible=false;charset=utf-8",
      "request-id": "2a6161df-44ca-494f-935d-20e3534d3745"
    },
    "reason": "OK",
    "json_body": {
      "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#users('integrations%40swimlaneintegrations.onmicrosoft.com')/authentication/methods",
      "@microsoft.graph.tips": "Use $select to choose only the properties your app needs, as this can lead to performance improvements. For example: GET users('<key>')/authentication/methods?$select=id",
      "value": [
        {
          "@odata.type": "#microsoft.graph.passwordAuthenticationMethod",
          "id": "28c10230-6103-485e-b985-444c60001490",
          "password": null,
          "createdDateTime": "2021-12-15T01:31:09Z"
        },
        {
          "@odata.type": "#microsoft.graph.softwareOathAuthenticationMethod",
          "id": "c03db085-34e7-47bc-b7d6-b54069b6042f",
          "secretKey": null
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
  - **@microsoft.graph.tips** (string)
  - **value** (array)
    - **@odata.type** (string)
    - **id** (string)
    - **password** (object)
    - **createdDateTime** (string)
    - **secretKey** (object)
## Response Headers

| Header | Type |
|--------|------|
| client-request-id | string |
| content-type | string |
| request-id | string |