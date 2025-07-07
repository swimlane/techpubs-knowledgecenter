# Publish Event

**Description**: Publishes a specified event in MISP using the provided eventId, requiring headers and path parameters.

## Endpoint

- **URL:** `events/publish/{{eventId}}`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required
  - **eventId** (string) – Required
- **headers** (object) – Required
  - **Accept** (string) – Required
  - **Content-Type** (string) – Required
## Output

### Example

```json
[
  {
    "name": "Publish",
    "message": "Job queued",
    "url": "https://misp.local/events/alert/1",
    "id": "string"
  }
]
```
### Output Parameters

- **name** (string)
- **message** (string)
- **url** (string)
- **id** (string)