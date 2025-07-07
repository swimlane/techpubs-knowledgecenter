# Create Address

**Description**: Creates a new address object within Fortinet Fortigate for security policies and configurations, requiring a JSON body input.

## Endpoint

- **URL:** `/api/v2/cmdb/firewall/address`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required
  - **name** (string)
  - **uuid** (string)
  - **subnet** (string)
  - **type** (string)
  - **sub-type** (string)
  - **clearpass-spt** (string)
  - **macaddr** (array)
    - **macaddr** (string)
  - **start-ip** (string)
  - **end-ip** (string)
  - **fqdn** (string)
  - **country** (string)
  - **wildcard-fqdn** (string)
  - **cache-ttl** (number)
  - **wildcard** (string)
  - **sdn** (string)
  - **fsso-group** (array)
    - **name** (string)
  - **interface** (string)
  - **tenant** (string)
  - **organization** (string)
  - **epg-name** (string)
  - **subnet-name** (string)
  - **sdn-tag** (string)
  - **policy-group** (string)
  - **obj-tag** (string)
  - **obj-type** (string)
  - **tag-detection-level** (string)
  - **tag-type** (string)
  - **comment** (string)
  - **associated-interface** (string)
  - **color** (number)
  - **filter** (string)
  - **sdn-addr-type** (string)
  - **node-ip-only** (string)
  - **obj-id** (string)
  - **list** (array)
    - **ip** (string)
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
      "date": "Mon, 08 May 2023 21:41:54 GMT",
      "x-frame-options": "SAMEORIGIN",
      "content-security-policy": "frame-ancestors 'self'",
      "x-xss-protection": "1; mode=block",
      "content-length": "354",
      "content-type": "text/html; charset=iso-8859-1",
      "Connection": "keep-alive"
    },
    "reason": "OK",
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
| date | string |
| x-frame-options | string |
| content-security-policy | string |
| x-xss-protection | string |
| content-length | string |
| content-type | string |
| Connection | string |