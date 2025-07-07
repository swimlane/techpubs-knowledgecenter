# Get Endpoints

**Description**: The following query retrieves known endpoints from Tanium.

## Endpoint

- **URL:** `/plugin/products/gateway/graphql`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required
  - **variables** (object) – Required
    - **count** (number)
    - **time** (number)
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "X-Frame-Options": "SAMEORIGIN",
      "X-Content-Type-Options": "nosniff",
      "X-XSS-Protection": "1",
      "Referrer-Policy": "no-referrer",
      "Server": "restify",
      "x-request-id": "31dd35f5-42a5-4d04-845a-6a3ea7c4304f",
      "tanium-gateway-version": "1.9.72.0000",
      "Content-Encoding": "gzip",
      "cache-control": "no-store",
      "Pragma": "no-cache",
      "Expires": "0",
      "content-type": "application/json; charset=utf-8",
      "Date": "Thu, 16 Nov 2023 16:02:59 GMT",
      "Transfer-Encoding": "chunked"
    },
    "reason": "OK",
    "json_body": {
      "data": {
        "endpoints": {
          "edges": [
            {
              "node": {
                "computerID": "2682372884",
                "name": "wintantest",
                "serialNumber": "VMware-42 10 1f f4 04 1b c4 48-8c 77 eb 57 6c 88 69 17",
                "ipAddress": "10.32.28.55"
              }
            }
          ]
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
    - **endpoints** (object)
      - **edges** (array)
        - **node** (object)
          - **computerID** (string)
          - **name** (string)
          - **serialNumber** (string)
          - **ipAddress** (string)
## Response Headers

| Header | Type |
|--------|------|
| X-Frame-Options | string |
| X-Content-Type-Options | string |
| X-XSS-Protection | string |
| Referrer-Policy | string |
| Server | string |
| x-request-id | string |
| tanium-gateway-version | string |
| Content-Encoding | string |
| cache-control | string |
| Pragma | string |
| Expires | string |
| content-type | string |
| Date | string |
| Transfer-Encoding | string |