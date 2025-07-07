# Get Addresses

**Description**: Fetches a list of configured addresses from Fortinet Fortigate to enhance security automation playbooks.

## Endpoint

- **URL:** `/api/v2/cmdb/firewall/address/`
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
      "http_method": "GET",
      "revision": "124.0.206.9538334086041268915.1559577065",
      "results": [
        {
          "q_origin_key": "AD-Server",
          "name": "AD-Server",
          "uuid": "********-****-****-****-************",
          "subnet": "10.100.77.240 255.255.255.255",
          "type": "ipmask",
          "start-mac": "00:00:00:00:00:00",
          "end-mac": "00:00:00:00:00:00",
          "start-ip": "10.100.77.240",
          "end-ip": "255.255.255.255",
          "fqdn": "",
          "country": "",
          "wildcard-fqdn": "",
          "cache-ttl": 0,
          "wildcard": "10.100.99.240 255.255.255.255",
          "sdn": "",
          "interface": "",
          "tenant": "",
          "organization": "",
          "epg-name": "",
          "subnet-name": "",
          "sdn-tag": "",
          "policy-group": "",
          "comment": "",
          "visibility": "enable",
          "associated-interface": "",
          "color": 0,
          "filter": "",
          "sdn-addr-type": "private",
          "obj-id": "",
          "list": [],
          "tagging": [],
          "allow-routing": "disable"
        }
      ]
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **http_method** (string)
  - **revision** (string)
  - **results** (array)
    - **q_origin_key** (string)
    - **name** (string)
    - **uuid** (string)
    - **subnet** (string)
    - **type** (string)
    - **start-mac** (string)
    - **end-mac** (string)
    - **start-ip** (string)
    - **end-ip** (string)
    - **fqdn** (string)
    - **country** (string)
    - **wildcard-fqdn** (string)
    - **cache-ttl** (number)
    - **wildcard** (string)
    - **sdn** (string)
    - **interface** (string)
    - **tenant** (string)
    - **organization** (string)
    - **epg-name** (string)
    - **subnet-name** (string)
    - **sdn-tag** (string)
    - **policy-group** (string)
    - **comment** (string)
    - **visibility** (string)
    - **associated-interface** (string)
    - **color** (number)
    - **filter** (string)
    - **sdn-addr-type** (string)
    - **obj-id** (string)
    - **list** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **tagging** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **allow-routing** (string)
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