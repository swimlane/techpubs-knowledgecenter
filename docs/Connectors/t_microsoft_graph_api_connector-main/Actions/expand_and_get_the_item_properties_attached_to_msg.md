# Expand and Get Item Properties Attached to Message

**Description**: Retrieves properties of an email attachment in Microsoft Graph API using the provided email address, email ID, and attachment ID.

## Endpoint

- **URL:** `/v1.0/users/{{email_address}}/messages/{{email_id}}/attachments/{{attachment_id}}/`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **email_address** (string) – Required: The account associated with the email.
  - **email_id** (string) – Required: The ID of the email to retrieve attachments from.
  - **attachment_id** (string) – Required: Attachment ID.
- **remove_content_bytes** (boolean): Remove Content Bytes from the response.
- **parameters** (object)
  - **$expand** (string): To get the properties of an item attachment (contact, event, or message).
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **@odata.type** (string)
  - **id** (string)
  - **lastModifiedDateTime** (string)
  - **name** (string)
  - **contentType** (object)
  - **size** (number)
  - **isInline** (boolean)
  - **item@odata.associationLink** (string)
  - **item@odata.navigationLink** (string)
  - **item** (object)
    - **@odata.type** (string)
    - **id** (string)
    - **createdDateTime** (string)
    - **lastModifiedDateTime** (string)
    - **receivedDateTime** (string)
    - **sentDateTime** (string)
    - **hasAttachments** (boolean)
    - **internetMessageId** (string)
    - **subject** (string)
    - **bodyPreview** (string)
    - **importance** (string)
    - **conversationId** (string)
    - **conversationIndex** (string)
    - **isDeliveryReceiptRequested** (boolean)
    - **isReadReceiptRequested** (boolean)
    - **isRead** (boolean)
    - **isDraft** (boolean)
    - **webLink** (string)
    - **internetMessageHeaders** (array)
      - **name** (string)
      - **value** (string)
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
    - **flag** (object)
      - **flagStatus** (string)
    - **attachments** (array)
      - **@odata.type** (string)
      - **@odata.mediaContentType** (string)
      - **id** (string)
      - **lastModifiedDateTime** (string)
      - **name** (string)
      - **contentType** (string)
      - **size** (number)
      - **isInline** (boolean)
      - **contentId** (object)
      - **contentLocation** (object)
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