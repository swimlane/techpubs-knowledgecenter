# Revoke Signin Sessions

**Description**: Invalidates all refresh tokens and browser session cookies for a user to ensure secure sign-out via Microsoft Graph API.

## Endpoint

- **URL:** `v1.0/users/{{id}}/revokeSignInSessions`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **id** (string) – Required: User ID
## Output

### Example

```json
[
  {
    "status_code": 200,
    "reason": "OK",
    "response_headers": {},
    "json_body": {
      "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#Edm.Boolean",
      "value": true
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **value** (boolean)
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
| Date | string |