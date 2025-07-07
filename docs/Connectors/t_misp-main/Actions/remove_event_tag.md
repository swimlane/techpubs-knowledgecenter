# Remove Event Tag

**Description**: Removes a specified tag from an event in MISP using the provided event and tag IDs, requiring headers and path parameters.

## Endpoint

- **URL:** `events/removeTag/{{eventId}}/{{tagId}}`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required
  - **eventId** (string) – Required
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