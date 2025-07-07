# Export Email as EML

**Description**: Exports an email as an EML file using a specified ID and email address through the Microsoft Graph API.

## Endpoint

- **URL:** `/v1.0/users/{{email_address}}/messages/{{id}}/$value`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **email_address** (string) – Required
  - **id** (string) – Required
- **filename** (string): Filename for the generated eml file. Default - {First_20_Characters_Of_Message_ID}.eml
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "OK",
    "file": {}
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **file** (object): Attachments
  - **file** (string)
  - **file_name** (string)