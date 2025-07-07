# Get Hosts

**Description**: Gets the list of Hosts identified from all scan results that are on Tenable.sc

## Endpoint

- **URL:** `/rest/hosts`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **limit** (number): The limit parameter should be an integer greater than 0
  - **startOffset** (number): The startOffset parameter should an integer greater than 0
  - **endOffset** (number): The endOffset parameter should an integer greater than 0
  - **pagination** (boolean): The pagination parameter should a boolean
  - **fields** (string): Specify the fields want to include in the response
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "ok",
    "json_body": {
      "type": "regular",
      "response": [
        {
          "id": "154",
          "uuid": "68262460-941b-4762-906e-47298f79911e",
          "tenableUUID": "58bd0909-f66d-4248-8c20-2501b208bb65",
          "name": "Aerified",
          "ipAddress": "201.22.196.102",
          "os": "Linux",
          "firstSeen": "1770798",
          "lastSeen": "1685038"
        },
        {
          "id": "47",
          "uuid": "e9344880-c32f-458c-b78e-211ce81d10cb",
          "tenableUUID": "dce3a590-70f0-4530-9843-5d3c83666f75",
          "name": "Windows 10",
          "ipAddress": "90.248.112.168",
          "os": "Windows 10",
          "firstSeen": "1755893",
          "lastSeen": "1221376"
        }
      ],
      "error_code": 0,
      "error_msg": "",
      "warnings": [],
      "timestamp": 1626889388
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **type** (string)
  - **response** (array)
    - **id** (string)
    - **uuid** (string)
    - **tenableUUID** (string)
    - **name** (string)
    - **ipAddress** (string)
    - **os** (string)
    - **firstSeen** (string)
    - **lastSeen** (string)
  - **error_code** (number)
  - **error_msg** (string)
  - **warnings** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **timestamp** (number)