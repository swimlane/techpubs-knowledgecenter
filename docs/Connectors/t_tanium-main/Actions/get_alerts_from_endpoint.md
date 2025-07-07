# Get Alerts from Endpoint

**Description**: Get Alerts from an Endpoint

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
        "directConnectEndpoint": {
          "alerts": {
            "all": [
              {
                "schema": 1,
                "key": "available-mem{heuristic=\"available-mem\"}",
                "type": "available-mem",
                "ref": null,
                "topProcessesExpr": null,
                "labels": {
                  "heuristic": "available-mem"
                },
                "pendingAt": "2022-03-15T15:54:38.574990164Z",
                "start": "2022-03-15T15:54:38.574990164Z",
                "resolvedAt": null,
                "leadup": 300000000000,
                "value": 168.48828125
              }
            ]
          }
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
    - **directConnectEndpoint** (object)
      - **alerts** (object)
        - **all** (array)
          - **schema** (number)
          - **key** (string)
          - **type** (string)
          - **ref** (object)
          - **topProcessesExpr** (object)
          - **labels** (object)
            - **heuristic** (string)
          - **pendingAt** (string)
          - **start** (string)
          - **resolvedAt** (object)
          - **leadup** (number)
          - **value** (number)