# Get Credentials

**Description**: Get the list of credentials

## Endpoint

- **URL:** `rest/credentials`
- **Method:** `GET`
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
            "id": "1000001",
            "name": "Test",
            "description": "",
            "type": "ssh",
            "uuid": "E7BC705C-9088-4F5A-81A0-A5B13F5C4331"
          },
          {
            "id": "1000002",
            "name": "test",
            "description": "",
            "type": "ssh",
            "uuid": "E58A2208-2776-4200-B6E5-A844AC26E338"
          }
        ],
        "manageable": [
          {
            "id": "1000001",
            "name": "Test",
            "description": "",
            "type": "ssh",
            "uuid": "E7BC705C-9088-4F5A-81A0-A5B13F5C4331"
          },
          {
            "id": "1000002",
            "name": "test",
            "description": "",
            "type": "ssh",
            "uuid": "E58A2208-2776-4200-B6E5-A844AC26E338"
          }
        ]
      },
      "error_code": 0,
      "error_msg": "",
      "warnings": [],
      "timestamp": 1408719365
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
      - **type** (string)
      - **uuid** (string)
    - **manageable** (array)
      - **id** (string)
      - **name** (string)
      - **description** (string)
      - **type** (string)
      - **uuid** (string)
  - **error_code** (number)
  - **error_msg** (string)
  - **warnings** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **timestamp** (number)