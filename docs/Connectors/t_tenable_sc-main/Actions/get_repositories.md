# Get Repositories

**Description**: Get the list of repositories

## Endpoint

- **URL:** `rest/repository`
- **Method:** `GET`
## Inputs

- **parameters** (object) – Required
  - **type** (string) – Required
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
      "response": [
        {
          "id": "37",
          "name": "ag repo1",
          "description": "Copied from QA",
          "dataFormat": "agent",
          "uuid": "A2FF7E13-2C0E-470E-A3C9-E077FE065A54"
        },
        {
          "id": "38",
          "name": "jm ipv4",
          "description": "copied from QA",
          "dataFormat": "IPv4",
          "uuid": "2E950182-08B6-4737-830B-4ACC8F6B92F9"
        },
        {
          "id": "39",
          "name": "ipv6 rep",
          "description": "Copied from QA (name changed)",
          "dataFormat": "IPv6",
          "uuid": "FF00F4D0-5B9F-4A26-998C-19430295284A"
        },
        {
          "id": "40",
          "name": "universal rep",
          "description": "first universal",
          "dataFormat": "universal",
          "uuid": "61606F1A-72CF-4A6D-A2B8-74787C6A8BEF"
        },
        {
          "id": "43",
          "name": "Test Local mobile Repository",
          "description": "DevForm test of mobile repository post",
          "dataFormat": "mobile",
          "uuid": "8DFA4F06-646A-4A63-A56D-08CCC9098682"
        },
        {
          "id": "44",
          "name": "Test w/pluginPrefs",
          "description": "",
          "dataFormat": "IPv4",
          "uuid": "E33F8169-7C8B-4D1E-B69F-4C50B6347088"
        }
      ],
      "error_code": 0,
      "error_msg": "",
      "warnings": [],
      "timestamp": 1423767348
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
    - **name** (string)
    - **description** (string)
    - **dataFormat** (string)
    - **uuid** (string)
  - **error_code** (number)
  - **error_msg** (string)
  - **warnings** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **timestamp** (number)