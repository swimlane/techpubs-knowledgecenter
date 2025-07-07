# Network - Get all

**Description**: Retrieves all network objects within the Check Point R80 environment, utilizing a JSON body input for specifications.

## Endpoint

- **URL:** `/web_api/show-networks`
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
      "Date": "Fri, 30 Dec 2022 19:12:55 GMT",
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
          "uid": "4f078348-5f64-45a2-b501-944b78511eba",
          "name": "22def595c2a64f8f976461beff69da69",
          "type": "network",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "subnet4": "192.168.1.0",
          "mask-length4": 24,
          "subnet-mask": "255.255.255.0"
        },
        {
          "uid": "6dc91c6f-aba8-4125-b8eb-7cc881687712",
          "name": "4afb132b3bc343c888c639231b55b8e3",
          "type": "network",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "subnet4": "192.168.0.0",
          "mask-length4": 24,
          "subnet-mask": "255.255.255.0"
        },
        {
          "uid": "3961bf82-4919-4325-8827-17e143dfab5b",
          "name": "4c060194807f4b32a8386a8f247714d8",
          "type": "network",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "subnet4": "192.170.1.0",
          "mask-length4": 24,
          "subnet-mask": "255.255.255.0"
        },
        {
          "uid": "1cc919e4-9ae5-4b82-9397-3c122ecae9b8",
          "name": "6e354d445e4b41ff936f92f223e3b4f2",
          "type": "network",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "subnet4": "192.160.1.0",
          "mask-length4": 24,
          "subnet-mask": "255.255.255.0"
        },
        {
          "uid": "4c82e477-ea87-4bb8-8180-d5345522a57a",
          "name": "CP_default_Office_Mode_addresses_pool",
          "type": "network",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "subnet4": "172.16.10.0",
          "mask-length4": 24,
          "subnet-mask": "255.255.255.0"
        },
        {
          "uid": "9e6b89ff-7923-4b79-887d-a5b1f34e3237",
          "name": "d82a1c82a6b7491caf3591a0c4f0cdda",
          "type": "network",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "subnet4": "192.160.0.0",
          "mask-length4": 24,
          "subnet-mask": "255.255.255.0"
        },
        {
          "uid": "caee1116-8087-4310-9208-b422d3628a7e",
          "name": "IPv6_Link_Local_Hosts",
          "type": "network",
          "domain": {
            "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
            "name": "Check Point Data",
            "domain-type": "data domain"
          },
          "subnet6": "fe80::",
          "mask-length6": 64
        }
      ],
      "from": 1,
      "to": 7,
      "total": 7
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
    - **subnet4** (string)
    - **mask-length4** (number)
    - **subnet-mask** (string)
    - **subnet6** (string)
    - **mask-length6** (number)
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