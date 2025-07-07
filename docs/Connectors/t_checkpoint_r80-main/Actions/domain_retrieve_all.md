# Domain - Get All

**Description**: Retrieves all domains from Check Point R80 using the specified JSON body input.

## Endpoint

- **URL:** `/web_api/show-dns-domains`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required: JSON Body
  - **limit** (number): The maximal number of returned results
  - **offset** (number): Number of the results to initially skip
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Fri, 30 Dec 2022 15:03:43 GMT",
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
      "objects": [
        {
          "uid": "540cbca6-4310-4d20-8b71-9dc24dc669a6",
          "name": ".269a0d7638494a48ba4f14a467532a41",
          "type": "dns-domain",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "7c7a36d8-baa5-4f43-894a-c0a15f4d9d39",
          "name": ".4b9746f8962541298a254c42a0087b51",
          "type": "dns-domain",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "36d7ea60-197b-49c0-b12f-a87b22c2b5dc",
          "name": ".a568c4777bb64746a42857d81f291e51",
          "type": "dns-domain",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "b40571f6-cb55-4575-8529-370bcefff654",
          "name": ".b97591ff0c55487586e5a9bbabeec97a",
          "type": "dns-domain",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "ca8dd987-7571-4d3e-8277-9a4e645af7fa",
          "name": ".c3bdab2c62754385aee50810613b5548",
          "type": "dns-domain",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "d412ea35-c6af-4256-9c9e-b0da4d5ab051",
          "name": ".c808845305fa4a1898a790ee79beb141",
          "type": "dns-domain",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "10c4fe17-f4ca-438d-9b99-ea6198294b96",
          "name": ".d1bcae8094014ef8bd49773a76e0ab17",
          "type": "dns-domain",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "1861ef07-2ab2-4705-a4bb-f75f31e6472e",
          "name": ".google.com",
          "type": "dns-domain",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "6e9ea079-dfe8-4579-8c50-8a8da30f25d0",
          "name": ".google.com.co",
          "type": "dns-domain",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "f25ae47c-c794-4944-a155-015027ff92ab",
          "name": ".https://icanhas.cheezburger.com/",
          "type": "dns-domain",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        }
      ],
      "from": 1,
      "to": 10,
      "total": 10
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **objects** (array)
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