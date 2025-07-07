# Get Incident Components

**Description**: Retrieves all components of a Symantec DLP incident, such as ID, name, and MIME-type, using the given incident ID.

## Endpoint

- **URL:** `/ProtectManager/webservices/v2/incidents/{{id}}/components`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **id** (number) – Required: The incident ID.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "OK",
    "json_body": [
      {
        "messageComponentId": 42,
        "messageComponentName": "Body",
        "mimeType": "text/plain",
        "originalSize": 200,
        "messageComponentTypeName": "Body",
        "isComponentAvailable": false
      },
      {
        "messageComponentId": 43,
        "messageComponentName": "SecretFile.doc",
        "mimeType": "application/msword",
        "originalSize": 134753,
        "messageComponentTypeName": "Attachment",
        "isComponentAvailable": true
      }
    ]
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (array)
  - **messageComponentId** (number)
  - **messageComponentName** (string)
  - **mimeType** (string)
  - **originalSize** (number)
  - **messageComponentTypeName** (string)
  - **isComponentAvailable** (boolean)