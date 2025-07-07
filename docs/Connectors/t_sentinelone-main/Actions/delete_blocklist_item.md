# Delete Blocklist Item

**Description**: Removes a specified item from the SentinelOne blocklist, allowing agents to access the previously blocked file.

## Endpoint

- **URL:** `/web/api/v2.1/restrictions`
- **Method:** `DELETE`
## Inputs

- **json_body** (object) – Required
  - **data** (object) – Required
    - **ids** (array)
    - **type** (string): Type.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "OK",
    "json_body": {
      "data": {
        "affected": 1
      },
      "errors": [
        {}
      ]
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **data** (object)
    - **affected** (number)
  - **errors** (array)