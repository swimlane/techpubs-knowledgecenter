# Update Address Group

**Description**: Updates an existing Network Address Group in Fortinet Fortigate using the specified group name provided in path parameters.

## Endpoint

- **URL:** `/api/v2/cmdb/firewall/addrgrp/{{name}}`
- **Method:** `PUT`
## Inputs

- **path_parameters** (object) – Required
  - **name** (string) – Required
- **json_body** (object) – Required
  - **name** (string): To update the name, provide `new_name` here.
  - **type** (string)
  - **category** (string)
  - **uuid** (string)
  - **member** (array)
    - **name** (string)
  - **comment** (string)
  - **exclude** (string)
  - **exclude-member** (array)
    - **name** (string)
  - **color** (number)
  - **tagging** (array)
    - **name** (string)
    - **category** (string)
    - **tags** (array)
  - **allow-routing** (string)
  - **fabric-object** (string)
- **parameters** (object)
  - **vdom** (string): Specify the Virtual Domain(s) from which results are returned or changes are applied to. If this parameter is not provided, the management VDOM will be used. If the admin does not have access to the VDOM, a permission error will be returned.
  - **action** (string): If supported, an action can be specified. "clone" - Clone this specific resource. When action=clone is set, the extra parameters Nkey must be provided.
  - **nkey** (string): If action=clone, use Nkey to specify the ID for the new resource to be created.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Mon, 16 Oct 2023 17:08:40 GMT",
      "content-length": "354",
      "content-type": "text/html; charset=iso-8859-1",
      "Content-Type": "text/xml;charset=UTF-8",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "x-frame-options": "SAMEORIGIN",
      "x-xss-protection": "1; mode=block",
      "strict-transport-security": "max-age=63072000; includeSubDomains;"
    },
    "reason": "",
    "json_body": {}
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| content-length | string |
| content-type | string |
| Content-Type | string |
| Transfer-Encoding | string |
| Connection | string |
| x-frame-options | string |
| x-xss-protection | string |
| strict-transport-security | string |