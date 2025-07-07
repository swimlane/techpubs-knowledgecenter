# Access Layer - Get All

**Description**: Retrieve a comprehensive list of all access control boundaries defined in Check Point R80.

## Endpoint

- **URL:** `/web_api/show-access-layers`
- **Method:** `POST`
## Inputs

- **json_body** (object): JSON Body
  - **limit** (number): The maximal number of returned results
  - **offset** (number): Number of the results to initially skip
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Tue, 27 Dec 2022 13:01:23 GMT",
      "Server": "CPWS",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "X-Frame-Options": "SAMEORIGIN",
      "Content-Type": "application/json",
      "X-UA-Compatible": "IE=EmulateIE8",
      "X-Forwarded-Host-Port": "443",
      "Keep-Alive": "timeout=15, max=99",
      "Connection": "Keep-Alive",
      "Transfer-Encoding": "chunked"
    },
    "reason": "OK",
    "json_body": {
      "access-layers": [
        {
          "uid": "1063010e-4878-48d2-ae1e-f2cf056e142c",
          "name": "6c1aa2ecb1424ec19e42f0a9cef6fead",
          "type": "access-layer",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "51cd7670-764a-4f62-923f-0dd206486c1b",
          "name": "8d349f194a434548b445ff6abbcff524",
          "type": "access-layer",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "b6f0fb96-941d-44dc-a7ed-fc52d567b5d4",
          "name": "bcb2daba476a4225a3d60d928a0e4803",
          "type": "access-layer",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "723a569f-9a66-4289-bc06-3945609e3183",
          "name": "ced6c207ff854eb8bed7efd424ef5b0b",
          "type": "access-layer",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "ad28d864-3189-4d33-bce1-e33b571d9f9d",
          "name": "cfa5387ccbeb4adcbeb18887b1531d9e",
          "type": "access-layer",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        }
      ],
      "from": 3,
      "to": 7,
      "total": 15
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **access-layers** (array)
    - **uid** (string)
    - **name** (string)
    - **type** (string)
    - **domain** (object)
      - **uid** (string)
      - **name** (string)
      - **domain-type** (string)
  - **from** (number)
  - **to** (number)
  - **total** (number)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Server | string |
| Strict-Transport-Security | string |
| X-Frame-Options | string |
| Content-Type | string |
| X-UA-Compatible | string |
| X-Forwarded-Host-Port | string |
| Keep-Alive | string |
| Connection | string |
| Transfer-Encoding | string |