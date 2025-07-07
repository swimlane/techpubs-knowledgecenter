# Move Email

**Description**: Relocate an email to a different folder in the user's mailbox using the specified email address, email ID, and destination ID.

## Endpoint

- **URL:** `/v1.0/users/{{email_address}}/messages/{{email_id}}/move`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **email_address** (string) – Required: The account associated with the email
  - **email_id** (string) – Required: The ID of the email
- **json_body** (object) – Required: JSON Body
  - **destinationId** (string) – Required: The destination folder ID, or a well-known folder name
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
| Location | string |
| Vary | string |
| Strict-Transport-Security | string |
| request-id | string |
| client-request-id | string |
| x-ms-ags-diagnostic | string |
| Date | string |