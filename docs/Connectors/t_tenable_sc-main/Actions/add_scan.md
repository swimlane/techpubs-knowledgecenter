# Add Scan

**Description**: Adds a Scan, depending on access and permissions

## Endpoint

- **URL:** `rest/scan`
- **Method:** `POST`
## Inputs

- **json_body** (object)
  - **name** (string)
  - **type** (string)
  - **description** (string)
  - **repository** (object)
    - **id** (number)
  - **zone** (object)
    - **id** (number)
  - **dhcpTracking** (string)
  - **classifyMitigatedAge** (number)
  - **schedule** (object)
    - **type** (string)
  - **reports** (array)
    - **id** (number)
    - **reportSource** (string)
  - **assets** (array)
    - **id** (number)
  - **credentials** (array)
    - **id** (number)
  - **emailOnLaunch** (string)
  - **emailOnFinish** (string)
  - **timeoutAction** (string)
  - **scanningVirtualHosts** (string)
  - **rolloverType** (string)
  - **ipList** (string)
  - **maxScanTime** (number)
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
        "id": "4",
        "name": "POSTtest",
        "description": "This is a test for POST",
        "ipList": "",
        "type": "policy",
        "policyID": "1000002",
        "pluginID": "-1",
        "zoneID": "-1",
        "dhcpTracking": "false",
        "classifyMitigatedAge": "0",
        "emailOnLaunch": "false",
        "emailOnFinish": "false",
        "timeoutAction": "import",
        "scanningVirtualHosts": "false",
        "rolloverType": "template",
        "status": "0",
        "createdTime": "1406815242",
        "modifiedTime": "1406815242",
        "maxScanTime": "3600",
        "ownerGID": "0",
        "reports": [],
        "assets": [],
        "credentials": [],
        "numDependents": "0",
        "schedule": {
          "id": "17",
          "dependentID": "14",
          "objectType": "scan",
          "type": "dependent",
          "start": "",
          "repeatRule": "",
          "enabled": "true",
          "nextRun": 0,
          "dependent": {
            "id": "14",
            "name": "Daily IP Scan",
            "description": "",
            "status": "1024"
          }
        },
        "policy": {
          "id": "1000002",
          "name": "POST TEST",
          "description": "Test of post for use with scan post test",
          "uuid": "29F2B9E1-ADE9-4550-B63C-CEA1423E52FC"
        },
        "pluginPrefs": [],
        "creator": {
          "id": "1",
          "username": "head3",
          "firstname": "",
          "lastname": "",
          "uuid": "96F2AD1B-1B83-462E-908A-84E6054F6B64"
        },
        "owner": {
          "id": "1",
          "username": "head3",
          "firstname": "",
          "lastname": "",
          "uuid": "96F2AD1B-1B83-462E-908A-84E6054F6B64"
        },
        "repository": {
          "id": "2",
          "name": "test",
          "description": "test",
          "type": "Local",
          "dataFormat": "IPv4",
          "uuid": "A2FF7E13-2C0E-470E-A3C9-E077FE065A54"
        },
        "ownerGroup": {
          "id": "0",
          "name": "Full Access",
          "description": "Full Access group"
        },
        "uuid": "29F2B9E1-ADE9-4550-B63C-CEA1423E52FC"
      },
      "error_code": 0,
      "error_msg": "",
      "warnings": [],
      "timestamp": 1406815242
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
    - **id** (string)
    - **name** (string)
    - **description** (string)
    - **ipList** (string)
    - **type** (string)
    - **policyID** (string)
    - **pluginID** (string)
    - **zoneID** (string)
    - **dhcpTracking** (string)
    - **classifyMitigatedAge** (string)
    - **emailOnLaunch** (string)
    - **emailOnFinish** (string)
    - **timeoutAction** (string)
    - **scanningVirtualHosts** (string)
    - **rolloverType** (string)
    - **status** (string)
    - **createdTime** (string)
    - **modifiedTime** (string)
    - **maxScanTime** (string)
    - **ownerGID** (string)
    - **reports** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **assets** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **credentials** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **numDependents** (string)
    - **schedule** (object)
      - **id** (string)
      - **dependentID** (string)
      - **objectType** (string)
      - **type** (string)
      - **start** (string)
      - **repeatRule** (string)
      - **enabled** (string)
      - **nextRun** (number)
      - **dependent** (object)
        - **id** (string)
        - **name** (string)
        - **description** (string)
        - **status** (string)
    - **policy** (object)
      - **id** (string)
      - **name** (string)
      - **description** (string)
      - **uuid** (string)
    - **pluginPrefs** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **creator** (object)
      - **id** (string)
      - **username** (string)
      - **firstname** (string)
      - **lastname** (string)
      - **uuid** (string)
    - **owner** (object)
      - **id** (string)
      - **username** (string)
      - **firstname** (string)
      - **lastname** (string)
      - **uuid** (string)
    - **repository** (object)
      - **id** (string)
      - **name** (string)
      - **description** (string)
      - **type** (string)
      - **dataFormat** (string)
      - **uuid** (string)
    - **ownerGroup** (object)
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