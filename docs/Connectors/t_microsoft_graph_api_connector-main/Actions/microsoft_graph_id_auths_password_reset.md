# Reset Password

**Description**: Initiate a password reset for a specified user by providing their ID and methodId via the Microsoft Graph API.

## Endpoint

- **URL:** `/v1.0/users/{{id}}/authentication/methods/{{methodId}}/resetPassword`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **id** (string) – Required: User ID
  - **methodId** (string) – Required: Password Method ID
- **json_body** (object)
  - **newPassword** (string): The new password. Required for tenants with hybrid password scenarios. If omitted for a cloud-only password, the system returns a system-generated password.
  - **include_uppercase** (boolean): Include Atleast One Uppercase Letter.
  - **include_lowercase** (boolean): Include Atleast One Lowercase Letter.
  - **include_digit** (boolean): Include Atleast One One Digit.
  - **include_special** (boolean): Include Atleast One Special Character.
  - **length** (number): Password length with minimum 20.
  - **auto_generate** (boolean): Auto Generate Random password.
## Output

### Example

```json
[
  {
    "status_code": 204,
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
      "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#microsoft.graph.passwordResetResponse",
      "newPassword": "Cuyo5459"
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **newPassword** (string)
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