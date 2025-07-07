# Forward Email

**Description**: Forwards an email from a specified address to designated recipients with an optional comment using Microsoft Graph API.

## Endpoint

- **URL:** `/v1.0/users/{{email_address}}/messages/{{email_id}}/forward`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **email_address** (string) – Required: The account associated with the email
  - **email_id** (string) – Required: The ID of the email
- **json_body** (object) – Required: JSON Body
  - **comment** (string) – Required: A comment to include. Can be an empty string.
  - **toRecipients** (array) – Required: The list of direct recipient objects.
    - **emailAddress** (object) – Required
      - **address** (string) – Required
      - **name** (string)
## Output

### Example

```json
[
  {
    "status_code": 202,
    "response_headers": {
      "Cache-Control": "private",
      "Strict-Transport-Security": "max-age=31536000",
      "request-id": "3378699e-5ce6-48bf-a2bf-df77a101ca85",
      "client-request-id": "3378699e-5ce6-48bf-a2bf-df77a101ca85",
      "x-ms-ags-diagnostic": "{\"ServerInfo\":{\"DataCenter\":\"Brazil South\",\"Slice\":\"E\",\"Ring\":\"3\",\"ScaleUnit\":\"002\",\"RoleInstance\":\"CP1PEPF00002F15\"}}",
      "Date": "Fri, 04 Nov 2022 23:07:11 GMT",
      "Content-Length": "0"
    },
    "reason": "Accepted",
    "response_text": ""
  }
]
```
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
| Content-Length | string |