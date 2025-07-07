# Set Email Read Status

**Description**: Marks an email as read in Microsoft Graph API using the specified email address and ID. Requires 'isRead' parameter.

## Endpoint

- **URL:** `/v1.0/users/{{email_address}}/messages/{{email_id}}`
- **Method:** `PATCH`
## Inputs

- **path_parameters** (object) – Required
  - **email_address** (string) – Required
  - **email_id** (string) – Required
- **json_body** (object) – Required
  - **isRead** (string) – Required
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **@odata.etag** (string)
  - **id** (string)
  - **createdDateTime** (string)
  - **lastModifiedDateTime** (string)
  - **changeKey** (string)
  - **categories** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **receivedDateTime** (string)
  - **sentDateTime** (string)
  - **hasAttachments** (boolean)
  - **internetMessageId** (string)
  - **subject** (string)
  - **bodyPreview** (string)
  - **importance** (string)
  - **parentFolderId** (string)
  - **conversationId** (string)
  - **conversationIndex** (string)
  - **isDeliveryReceiptRequested** (object)
  - **isReadReceiptRequested** (boolean)
  - **isRead** (boolean)
  - **isDraft** (boolean)
  - **webLink** (string)
  - **inferenceClassification** (string)
  - **body** (object)
    - **contentType** (string)
    - **content** (string)
  - **sender** (object)
    - **emailAddress** (object)
      - **name** (string)
      - **address** (string)
  - **from** (object)
    - **emailAddress** (object)
      - **name** (string)
      - **address** (string)
  - **toRecipients** (array)
    - **emailAddress** (object)
      - **name** (string)
      - **address** (string)
  - **ccRecipients** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **bccRecipients** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **replyTo** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **flag** (object)
    - **flagStatus** (string)
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