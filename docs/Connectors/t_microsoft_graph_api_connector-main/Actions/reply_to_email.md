# Reply to Email

**Description**: Send a custom reply to an email by specifying the recipient's address and email ID using Microsoft Graph API.

## Endpoint

- **URL:** `/v1.0/users/{{email_address}}/messages/{{email_id}}/reply`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **email_address** (string) – Required: The account associated with the email
  - **email_id** (string) – Required: The ID of the email
- **json_body** (object) – Required: JSON Body
  - **comment** (string): A comment to include. Can be an empty string.
  - **saveToSentItems** (boolean): Indicates whether to save the message in Sent Items. Specify it only if the parameter is false; default is true. Optional.
  - **message** (object): The message to send
    - **subject** (string): The subject of the email
    - **body** (object): The body of the message. It can be in HTML or text format.
      - **content** (string): The content of the item
      - **contentType** (string): The type of the content. Possible values are text and html.
    - **sender** (object): The account that is actually used to generate the message. In most cases, this value is the same as the from property
      - **address** (string) – Required
      - **name** (string)
    - **replyTo** (array): The email addresses to use when replying.
      - **emailAddress** (object) – Required
        - **address** (string) – Required
        - **name** (string)
    - **toRecipients** (array): The list of direct recipient objects.
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
      "request-id": "ff02930a-6227-4d5f-ab7f-2be87c82657f",
      "client-request-id": "ff02930a-6227-4d5f-ab7f-2be87c82657f",
      "x-ms-ags-diagnostic": "{\"ServerInfo\":{\"DataCenter\":\"Brazil South\",\"Slice\":\"E\",\"Ring\":\"3\",\"ScaleUnit\":\"001\",\"RoleInstance\":\"CP1PEPF0000307A\"}}",
      "Date": "Sat, 05 Nov 2022 13:41:17 GMT",
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