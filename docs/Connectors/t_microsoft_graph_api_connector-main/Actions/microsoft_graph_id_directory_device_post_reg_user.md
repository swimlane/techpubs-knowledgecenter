# Add Identity Directory Device Reg User

**Description**: Registers a new user to a device in the Microsoft Graph API directory with the provided device ID and user's @odata.id.

## Endpoint

- **URL:** `/v1.0/devices/{{id}}/registeredUsers/$ref`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **id** (string) – Required: Device ID
- **json_body** (object) – Required: JSON Body
  - **@odata.id** (string) – Required: Odata ID Type User
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **error** (object)
    - **code** (string)
    - **message** (string)
    - **innerError** (object)
      - **date** (string)
      - **request-id** (string)
      - **client-request-id** (string)
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
| Date | string |