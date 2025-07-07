# Add Tag to Attribute

**Description**: Associates a specified tag with an attribute in MISP, requiring the attribute's ID, tag's ID, and locality.

## Endpoint

- **URL:** `attributes/addTag/{{attributeId}}/{{tagId}}/local:{{local}}`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required
  - **attributeId** (string) – Required
  - **tagId** (string) – Required
  - **local** (number) – Required
- **headers** (object) – Required
  - **Accept** (string) – Required
  - **Content-Type** (string) – Required
## Output

### Example

```json
[
  {
    "saved": true,
    "success": "Tag added.",
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