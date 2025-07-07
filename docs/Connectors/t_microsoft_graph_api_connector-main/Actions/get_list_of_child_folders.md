# Get List of Child Folders

**Description**: Retrieve a list of child folders from a specified folder in Microsoft Graph API using the provided email address and folder ID.

## Endpoint

- **URL:** `/v1.0/users/{{email_address}}/mailFolders/{{folder_id}}/childFolders`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **email_address** (string) – Required: The account associated with the email.
  - **folder_id** (string) – Required: The mailFolder's unique identifier.
- **parameters** (object)
  - **includeHiddenFolders** (boolean): To include hidden child folders in the response.
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **value** (array)
    - **id** (string)
    - **displayName** (string)
    - **parentFolderId** (string)
    - **childFolderCount** (number)
    - **unreadItemCount** (number)
    - **totalItemCount** (number)
    - **sizeInBytes** (number)
    - **isHidden** (boolean)
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