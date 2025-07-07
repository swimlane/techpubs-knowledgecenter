# Get Emails

**Description**: Retrieves a list of emails for a given 'email_address' using the Microsoft Graph API, ensuring targeted account access.

## Endpoint

- **URL:** `/v1.0/users/{{email_address}}/messages`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **email_address** (string) – Required: The account associated with the email
- **parameters** (object): URL Query Parameters
  - **count** (string): Include a count of the total number of items in a collection alongside the page of data values returned from Microsoft Graph
  - **filter** (string): Use the $filter query parameter to retrieve just a subset of a collection. For guidance on using $filter, see https://learn.microsoft.com/en-us/graph/filter-query-parameter
  - **orderby** (string): To sort the results in ascending or descending order, append either asc or desc to the field name, separated by a space.
  - **top** (number): Sets the page size of results
- **headers** (object)
  - **Prefer** (string): The format of the body and uniqueBody properties to be returned in. Values can be "text" or "html". A Preference-Applied header is returned as confirmation if this Prefer header is specified. If the header is not specified, the body and uniqueBody properties are returned in HTML format.
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
    - **@odata.type** (string)
    - **meetingMessageType** (string)
    - **type** (string)
    - **isOutOfDate** (boolean)
    - **isAllDay** (boolean)
    - **isDelegated** (boolean)
    - **responseRequested** (boolean)
    - **allowNewTimeProposals** (object)
    - **meetingRequestType** (string)
    - **startDateTime** (object)
      - **dateTime** (string)
      - **timeZone** (string)
    - **endDateTime** (object)
      - **dateTime** (string)
      - **timeZone** (string)
    - **recurrence** (object)
    - **previousLocation** (object)
    - **previousStartDateTime** (object)
    - **previousEndDateTime** (object)
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