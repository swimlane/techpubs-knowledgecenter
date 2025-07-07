# Delete Identity Directory Device Registered User

**Description**: Remove a registered user from a device in the Microsoft Graph API directory by specifying 'id' and 'userId'.

## Endpoint

- **URL:** `/v1.0/devices/{{id}}/registeredUsers/{{userId}}/$ref`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **id** (string) – Required: Device ID
  - **userId** (string) – Required: User ID
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