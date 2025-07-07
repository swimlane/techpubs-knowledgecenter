# Get Emails From Folder

**Description**: Retrieve emails from a specified folder within a user's Microsoft Graph API account by using the email address and folder ID.

## Endpoint

- **URL:** `/v1.0/users/{{email_address}}/mailFolders/{{folder_id}}/messages`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **email_address** (string) – Required: The account associated with the email
  - **folder_id** (string) – Required: The folder ID, or a well-known folder name. For a list of supported well-known folder names, see https://learn.microsoft.com/en-us/graph/api/resources/mailfolder?view=graph-rest-1.0
- **parameters** (object): URL Query Parameters
  - **count** (string): Include a count of the total number of items in a collection alongside the page of data values returned from Microsoft Graph
  - **filter** (string): Use the $filter query parameter to retrieve just a subset of a collection. For guidance on using $filter, see https://learn.microsoft.com/en-us/graph/filter-query-parameter
  - **orderby** (string): To sort the results in ascending or descending order, append either asc or desc to the field name, separated by a space.
  - **top** (number): Sets the page size of results
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **@odata.count** (number)
  - **value** (array)
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
    - **isDeliveryReceiptRequested** (boolean)
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
  - **@odata.nextLink** (string)
## Response Headers

| Header | Type |
|--------|------|
| Cache-Control | string |
| Transfer-Encoding | string |
| Content-Type | string |
| Content-Encoding | string |
| Strict-Transport-Security | string |
| request-id | string |
| client-request-id | string |
| x-ms-ags-diagnostic | string |
| Date | string |