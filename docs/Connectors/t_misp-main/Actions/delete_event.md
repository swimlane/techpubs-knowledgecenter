# Delete Event

**Description**: Removes a specified event from MISP using the event ID provided in path parameters, with necessary headers.

## Endpoint

- **URL:** `events/delete/{{eventId}}`
- **Method:** `DELETE`
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
    "saved": true,
    "success": true,
    "name": "Event deleted.",
    "message": "Could not delete Event",
    "url": "/events/delete/1",
    "errors": "Event was not deleted."
  }
]
```
### Output Parameters

- **saved** (boolean)
- **success** (boolean)
- **name** (string)
- **message** (string)
- **url** (string)
- **errors** (string)