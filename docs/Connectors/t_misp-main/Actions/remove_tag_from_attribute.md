# Remove Tag from Attribute

**Description**: Removes a specified tag from an attribute in MISP by utilizing the provided attributeId and tagId.

## Endpoint

- **URL:** `attributes/removeTag/{{attributeId}}/{{tagId}}`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required
  - **attributeId** (string) – Required
  - **tagId** (string) – Required
- **headers** (object) – Required
  - **Accept** (string) – Required
  - **Content-Type** (string) – Required
## Output

### Example

```json
[
  {
    "saved": true,
    "success": "Tag removed.",
    "check_publish": true,
    "errors": "Tag could not be added."
  }
]
```
### Output Parameters

- **saved** (boolean)
- **success** (string)
- **check_publish** (boolean)
- **errors** (string)