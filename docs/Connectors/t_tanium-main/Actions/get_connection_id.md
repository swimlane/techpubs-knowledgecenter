# Get Connection ID

**Description**: Get Connection ID

## Endpoint

- **URL:** `/plugin/products/gateway/graphql`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required
  - **variables** (object) – Required
    - **id** (string) – Required
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
        "openDirectConnection": {
          "connectionID": "86d9a9ac-0229-481b-9d88-5f1bcb1b177b"
        }
      }
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **data** (object)
    - **openDirectConnection** (object)
      - **connectionID** (string)