# Extract Device List

**Description**: Extract the list of devices discovered by the sensor or console

## Endpoint

- **URL:** `/api/v1/devices`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **limit** (number)
  - **offset** (number)
  - **search_type** (string)
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "OK",
    "json_body": {}
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)