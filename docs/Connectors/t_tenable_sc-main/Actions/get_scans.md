# Get Scans

**Description**: Gets the list of scans

## Endpoint

- **URL:** `rest/scan`
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
            "id": "2",
            "name": "test",
            "description": null,
            "uuid": "2EAED2D2-DFC7-4CFE-9C94-25CF6481C515"
          },
          {
            "id": "3",
            "name": "test2",
            "description": null,
            "uuid": "EC81E13E-B3B2-4A51-968D-E94D524B5254"
          },
          {
            "id": "4",
            "name": "POSTtest",
            "description": "This is a test for POST",
            "uuid": "2EAED2D2-DFC7-4CFE-9C94-25CF6481C515"
          }
        ],
        "manageable": [
          {
            "id": "2",
            "name": "test",
            "description": null,
            "uuid": "2EAED2D2-DFC7-4CFE-9C94-25CF6481C515"
          },
          {
            "id": "3",
            "name": "test2",
            "description": null,
            "uuid": "EC81E13E-B3B2-4A51-968D-E94D524B5254"
          },
          {
            "id": "4",
            "name": "POSTtest",
            "description": "This is a test for POST",
            "uuid": "2EAED2D2-DFC7-4CFE-9C94-25CF6481C515"
          }
        ]
      },
      "error_code": 0,
      "error_msg": "",
      "warnings": [],
      "timestamp": 1406828340
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
      - **uuid** (string)
    - **manageable** (array)
      - **id** (string)
      - **name** (string)
      - **description** (string)
      - **uuid** (string)
  - **error_code** (number)
  - **error_msg** (string)
  - **warnings** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **timestamp** (number)