# Get Scan Results

**Description**: Gets the list of scan results

## Endpoint

- **URL:** `rest/scanResult`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **startTime** (number)
  - **endTime** (number)
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "OK",
    "json_body": {
      "type": "regular",
      "response": {
        "usable": [
          {
            "id": "1",
            "name": "Test Scan",
            "description": "",
            "status": "Completed"
          }
        ],
        "manageable": [
          {
            "id": "1",
            "name": "Test Scan",
            "description": "",
            "status": "Completed"
          }
        ]
      },
      "error_code": 0,
      "error_msg": "",
      "warnings": [],
      "timestamp": 1407249641
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **type** (string)
  - **response** (object)
    - **usable** (array)
      - **id** (string)
      - **name** (string)
      - **description** (string)
      - **status** (string)
    - **manageable** (array)
      - **id** (string)
      - **name** (string)
      - **description** (string)
      - **status** (string)
  - **error_code** (number)
  - **error_msg** (string)
  - **warnings** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **timestamp** (number)