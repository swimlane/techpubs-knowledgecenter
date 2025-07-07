# Run Scan

**Description**: Launches the scan associated with the ID or UUID

## Endpoint

- **URL:** `rest/scan/{{id}}/launch`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required
- **parameters** (object)
  - **diagnosticTarget** (string)
  - **diagnosticPassword** (string)
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
        "scanID": "2",
        "scanResult": {
          "initiatorID": "1",
          "ownerID": "1",
          "scanID": "2",
          "resultsSyncID": -1,
          "jobID": "143301",
          "repositoryID": "1",
          "name": "test",
          "description": "",
          "details": "Plugin #",
          "status": "Queued",
          "downloadFormat": "v2",
          "dataFormat": "IPv4",
          "resultType": "active",
          "id": "3"
        }
      },
      "error_code": 0,
      "error_msg": "",
      "warnings": [],
      "timestamp": 1407510276
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
    - **scanID** (string)
    - **scanResult** (object)
      - **initiatorID** (string)
      - **ownerID** (string)
      - **scanID** (string)
      - **resultsSyncID** (number)
      - **jobID** (string)
      - **repositoryID** (string)
      - **name** (string)
      - **description** (string)
      - **details** (string)
      - **status** (string)
      - **downloadFormat** (string)
      - **dataFormat** (string)
      - **resultType** (string)
      - **id** (string)
  - **error_code** (number)
  - **error_msg** (string)
  - **warnings** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **timestamp** (number)