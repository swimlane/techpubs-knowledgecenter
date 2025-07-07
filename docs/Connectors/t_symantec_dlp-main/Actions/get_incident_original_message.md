# Get Incident Original Message

**Description**: Retrieves the original message of a specified incident in Symantec DLP using the incident ID.

## Endpoint

- **URL:** `/ProtectManager/webservices/v2/incidents/{{id}}/originalMessage`
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