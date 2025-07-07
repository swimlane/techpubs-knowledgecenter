# Cancel Security Action

**Description**: Cancels an ongoing security action in Microsoft Graph API using the specified action_id.

## Endpoint

- **URL:** `/beta/security/securityActions/{{action_id}}/cancelSecurityAction`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **action_id** (string) – Required: Action ID
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **response_text** (string)
## Response Headers

| Header | Type |
|--------|------|
| Cache-Control | string |
| Strict-Transport-Security | string |
| request-id | string |
| client-request-id | string |
| x-ms-ags-diagnostic | string |
| Date | string |