# Get Incident Message Body

**Description**: Retrieves the message body of a specified incident from Symantec DLP, requiring an 'id' path parameter for access.

## Endpoint

- **URL:** `/ProtectManager/webservices/v2/incidents/{{id}}/messageBody`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **id** (number) – Required: The incident ID.
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **file** (object)
  - **file** (string)
  - **file_name** (string)