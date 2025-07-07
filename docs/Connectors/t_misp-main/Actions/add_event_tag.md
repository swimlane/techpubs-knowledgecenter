# Add Event Tag

**Description**: Associates a tag with an event in MISP using the event ID, tag ID, and locality parameter.

## Endpoint

- **URL:** `events/addTag/{{eventId}}/{{tagId}}/local:{{local}}`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required
  - **eventId** (string) – Required
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