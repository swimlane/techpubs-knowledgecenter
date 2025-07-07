# Get Group Members

**Description**: Retrieve a list of members from a specified group within the Fortinet Fortigate system.

## Endpoint

- **URL:** `/api/v2/cmdb/firewall/addrgrp/`
- **Method:** `GET`
## Inputs

- **parameters** (object): Object contains filter property which takes values of format <attributeName><operator><attributeValue>.
  - **filter** (string): Query string to filter the results. Format is <attributeName><operator><attributeValue>. Example values are name==test, name!=test etc. For operator values pls refer https://fndn.fortinet.net/index.php?/fortiapi/1-fortios/94/ 
## Output

### Example

```json
[
  {
    "status_code": 429,
    "response_headers": {
      "date": "Mon, 08 May 2023 21:41:54 GMT",
      "x-frame-options": "SAMEORIGIN",
      "content-security-policy": "frame-ancestors 'self'",
      "x-xss-protection": "1; mode=block",
      "content-length": "354",
      "content-type": "text/html; charset=iso-8859-1",
      "Connection": "keep-alive"
    },
    "reason": "Too Many Requests",
    "json_body": {
      "name": "ExampleAddressGroup",
      "type": "default",
      "category": "default",
      "uuid": "123e4567-e89b-12d3-a456-426655440000",
      "member": [
        {
          "name": "ExampleAddress1"
        },
        {
          "name": "ExampleAddress2"
        }
      ],
      "comment": "Example comment",
      "exclude": "enable",
      "exclude-member": [
        {
          "name": "ExcludedAddress1"
        },
        {
          "name": "ExcludedAddress2"
        }
      ],
      "color": 15,
      "tagging": [
        {
          "name": "TagName",
          "category": "TagCategory",
          "tags": [
            "Tag1",
            "Tag2"
          ]
        }
      ],
      "allow-routing": "enable",
      "fabric-object": "enable"
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **name** (string)
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