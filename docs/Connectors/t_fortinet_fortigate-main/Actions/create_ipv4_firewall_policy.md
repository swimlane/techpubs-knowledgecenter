# Create IPV4 Firewall Policy

**Description**: Establishes a new IPv4 firewall policy in Fortinet Fortigate to manage network traffic.

## Endpoint

- **URL:** `/api/v2/cmdb/firewall/policy`
- **Method:** `POST`
## Inputs

- **json_body** (object)
  - **policyid** (number)
  - **status** (string)
  - **name** (string)
  - **uuid** (string)
  - **srcintf** (array)
    - **name** (string)
  - **dstintf** (array)
    - **name** (string)
  - **action** (string)
  - **nat64** (string)
  - **nat46** (string)
  - **ztna-status** (string)
  - **ztna-device-ownership** (string)
  - **srcaddr** (array)
    - **name** (string)
  - **dstaddr** (array)
    - **name** (string)
  - **srcaddr6** (array)
    - **name** (string)
  - **dstaddr6** (array)
    - **name** (string)
  - **ztna-ems-tag** (array)
    - **name** (string)
  - **ztna-tags-match-logic** (string)
  - **ztna-geo-tag** (array)
    - **name** (string)
  - **internet-service** (string)
  - **internet-service-name** (array)
    - **name** (string)
  - **internet-service-group** (array)
    - **name** (string)
  - **internet-service-custom** (array)
    - **name** (string)
  - **network-service-dynamic** (array)
    - **name** (string)
  - **internet-service-custom-group** (array)
    - **name** (string)
  - **internet-service-src** (string)
  - **internet-service-src-name** (array)
    - **name** (string)
  - **internet-service-src-group** (array)
    - **name** (string)
  - **internet-service-src-custom** (array)
    - **name** (string)
  - **network-service-src-dynamic** (array)
    - **name** (string)
  - **internet-service-src-custom-group** (array)
    - **name** (string)
  - **reputation-minimum** (number)
  - **reputation-direction** (string)
  - **src-vendor-mac** (array)
    - **id** (number)
  - **internet-service6** (string)
  - **internet-service6-name** (array)
    - **name** (string)
  - **internet-service6-group** (array)
    - **name** (string)
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