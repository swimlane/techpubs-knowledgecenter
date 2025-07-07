# Get Component Data

**Description**: Retrieves incident component data from Symantec DLP using a specific component ID provided in the path parameters.

## Endpoint

- **URL:** `/ProtectManager/webservices/v2/incidents/{{id}}/components/{{componentId}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **id** (number) – Required: The incident ID.
  - **componentId** (number) – Required: The message component ID.
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **file** (object)
  - **file** (string)
  - **file_name** (string)