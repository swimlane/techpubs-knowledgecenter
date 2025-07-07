# Search for Device

**Description**: You can search through all discovered devices on your sensor or console by specifying your criteria

## Endpoint

- **URL:** `/api/v1/devices/search`
- **Method:** `POST`
## Inputs

- **data_body** (object) – Required
  - **filter** (object)
    - **field** (string)
    - **operand** (string)
    - **operator** (string)
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