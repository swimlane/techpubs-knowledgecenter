# Get Process from Endpoint

**Description**: Get Process from an Endpoint

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
          "processes": {
            "all": [
              {
                "pid": 2092,
                "ppid": 496,
                "name": "TaniumReceiver.exe",
                "commandLine": "\"C:\\Program Files\\Tanium\\TaniumServer\\TaniumReceiver.exe\" --service",
                "userName": "admin",
                "groupName": "test-group",
                "memoryResidentBytes": 59842560
              },
              {
                "pid": 5760,
                "ppid": 1112,
                "name": "TaniumClient.exe",
                "commandLine": "\"C:\\Program Files (x86)\\Tanium\\TaniumClient\\TaniumClient.exe\" -c",
                "userName": "SYSTEM",
                "groupName": "NT AUTHORITY",
                "memoryResidentBytes": 17965056
              },
              {
                "pid": 1036,
                "ppid": 496,
                "name": "TaniumBlobService.exe",
                "commandLine": "\"C:\\Program Files\\Tanium\\Tanium ModuleServer\\services\\blob-service\\TaniumBlobService.exe\"",
                "userName": "SYSTEM",
                "groupName": "NT AUTHORITY",
                "memoryResidentBytes": 7426048
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
      - **processes** (object)
        - **all** (array)
          - **pid** (number)
          - **ppid** (number)
          - **name** (string)
          - **commandLine** (string)
          - **userName** (string)
          - **groupName** (string)
          - **memoryResidentBytes** (number)