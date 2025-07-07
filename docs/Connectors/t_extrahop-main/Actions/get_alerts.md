# Get Alerts

**Description**: Retrieve all alerts.

## Endpoint

- **URL:** `/api/v1/alerts`
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
      "apply_all": true,
      "author": "string",
      "categories": [
        "string"
      ],
      "cc": [],
      "description": "string",
      "disabled": true,
      "field_name": "string",
      "field_name2": "string",
      "field_op": "string",
      "id": 0,
      "interval_length": 0,
      "mod_time": 0,
      "name": "string",
      "notify_snmp": true,
      "object_type": "string",
      "operand": "string",
      "operator": "string",
      "param": {},
      "param2": {},
      "protocols": [
        "string"
      ],
      "refire_interval": 0,
      "severity": 0,
      "stat_name": "string",
      "type": "string",
      "units": "string"
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **apply_all** (boolean)
  - **author** (string)
  - **categories** (array)
  - **cc** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **description** (string)
  - **disabled** (boolean)
  - **field_name** (string)
  - **field_name2** (string)
  - **field_op** (string)
  - **id** (number)
  - **interval_length** (number)
  - **mod_time** (number)
  - **name** (string)
  - **notify_snmp** (boolean)
  - **object_type** (string)
  - **operand** (string)
  - **operator** (string)
  - **param** (object)
  - **param2** (object)
  - **protocols** (array)
  - **refire_interval** (number)
  - **severity** (number)
  - **stat_name** (string)
  - **type** (string)
  - **units** (string)