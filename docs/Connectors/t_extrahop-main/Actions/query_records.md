# Query Records

**Description**: Query for records stored on a recordstore

## Endpoint

- **URL:** `/api/v1/records/search`
- **Method:** `POST`
## Inputs

- **data_body** (object) – Required
  - **context_ttl** (number)
  - **from** (string)
  - **filter** (object)
    - **field** (string)
    - **operator** (string)
    - **operand** (object)
      - **type** (string)
      - **value** (string)
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