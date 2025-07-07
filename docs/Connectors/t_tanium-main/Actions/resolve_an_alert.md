# resolve an alert

**Description**: Assign Resolved Status to Alert

## Endpoint

- **URL:** `/plugin/products/gateway/graphql`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required
  - **variables** (object) – Required
    - **guid** (string) – Required
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
        "threatResponseAlertResolve": {
          "resolved": true,
          "guid": "12345678-90ab-cdef-1234-567890abcdef",
          "error": null
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
    - **threatResponseAlertResolve** (object)
      - **resolved** (boolean)
      - **guid** (string)
      - **error** (object)