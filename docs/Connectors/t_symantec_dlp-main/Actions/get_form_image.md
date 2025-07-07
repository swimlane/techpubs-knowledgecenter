# Get Form Image

**Description**: Retrieves the form image for a given message and violation ID from Symantec DLP, requiring path parameters: id, messageId, and violationId.

## Endpoint

- **URL:** `/ProtectManager/webservices/v2/incidents/{{id}}/message/{{messageId}}/violation/{{violationId}}/image`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **id** (number) – Required: The incident ID.
  - **messageId** (number) – Required: The message ID.
  - **violationId** (number) – Required: The violation condition ID.
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **file** (object)
  - **file** (string)
  - **file_name** (string)