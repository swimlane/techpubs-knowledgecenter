# Send Email

**Description**: Send a custom email to a specified address using Microsoft Graph API, with required recipient's email and message content.

## Endpoint

- **URL:** `/v1.0/users/{{email_address}}/sendMail`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **email_address** (string) – Required: The account associated with the email
- **json_body** (object) – Required: JSON Body
  - **saveToSentItems** (boolean): Indicates whether to save the message in Sent Items. Specify it only if the parameter is false; default is true. Optional.
  - **message** (object) – Required: The message to send
    - **subject** (string): The subject of the email
    - **body** (object): The body of the message. It can be in HTML or text format.
      - **content** (string): The content of the item
      - **contentType** (string): The type of the content. Possible values are text and html.
    - **replyTo** (array): The email addresses to use when replying.
      - **emailAddress** (object) – Required
        - **address** (string) – Required
        - **name** (string)
    - **toRecipients** (array) – Required: The list of direct recipient objects.
      - **emailAddress** (object) – Required
        - **address** (string) – Required
        - **name** (string)
    - **ccRecipients** (array): The list of CC recipient objects.
      - **emailAddress** (object) – Required
        - **address** (string) – Required
        - **name** (string)
    - **bccRecipients** (array): The list of BCC recipient objects.
      - **emailAddress** (object) – Required
        - **address** (string) – Required
        - **name** (string)
    - **attachments** (array): Items attached to this email
      - **contentBytes** (string)
      - **name** (string)
      - **@odata.type** (string)
      - **contentType** (string)
## Output

### Example

```json
[
  {
    "status_code": 202,
    "response_headers": {
      "Cache-Control": "private",
      "Strict-Transport-Security": "max-age=31536000",
      "request-id": "0be49b36-fbe5-428f-a8aa-33b238f4525c",
      "client-request-id": "0be49b36-fbe5-428f-a8aa-33b238f4525c",
      "x-ms-ags-diagnostic": "{\"ServerInfo\":{\"DataCenter\":\"Brazil South\",\"Slice\":\"E\",\"Ring\":\"3\",\"ScaleUnit\":\"000\",\"RoleInstance\":\"CP1PEPF00002F05\"}}",
      "Date": "Sat, 05 Nov 2022 13:08:01 GMT",
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