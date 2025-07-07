# Host - Get All

**Description**: Retrieves a comprehensive list of all hosts from Check Point R80, requiring a JSON body with query details.

## Endpoint

- **URL:** `/web_api/show-hosts`
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
      "Date": "Fri, 30 Dec 2022 17:59:00 GMT",
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
          "uid": "5ccebaae-2138-41ff-bddf-442ce62f2442",
          "name": "1.1.1.1",
          "type": "host",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "ipv4-address": "1.1.1.1"
        },
        {
          "uid": "c9869133-4ff0-4fe4-a072-bcec7162073d",
          "name": "1.2.3.4",
          "type": "host",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "ipv4-address": "1.2.3.4"
        },
        {
          "uid": "5c933edc-22b2-4e01-bfcc-b9811841ef8a",
          "name": "152.32.139.164",
          "type": "host",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "ipv4-address": "152.32.139.164"
        },
        {
          "uid": "6d60eeec-234f-4ec6-b164-0893dcaeb3bd",
          "name": "157.52.193.73",
          "type": "host",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "ipv4-address": "157.52.193.73"
        },
        {
          "uid": "de03d634-6a64-4c37-80bd-8fe26b83a87b",
          "name": "157.52.193.85",
          "type": "host",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "ipv4-address": "157.52.193.85"
        },
        {
          "uid": "2ca0f9ac-0c05-4416-ae88-c523a493737b",
          "name": "176.31.182.86",
          "type": "host",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "ipv4-address": "176.31.182.86"
        },
        {
          "uid": "f67de17e-4244-4b1e-9051-e901150f9724",
          "name": "192.162.240.162",
          "type": "host",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "ipv4-address": "192.162.240.162"
        },
        {
          "uid": "cca3bff6-56e1-4481-b73e-611523ba63b1",
          "name": "1bbf4b9330c04b7e92f937b952990a82",
          "type": "host",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "ipv4-address": "192.168.0.6"
        },
        {
          "uid": "b387b0cb-fec5-4d97-a963-f7ea3f979d21",
          "name": "22.22.22.22",
          "type": "host",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "ipv4-address": "22.22.22.22"
        },
        {
          "uid": "252c01e4-66a5-4218-9d0e-3cde58f4305c",
          "name": "3e3b3617b58a4cd5af8139bbfd280bf4",
          "type": "host",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "ipv4-address": "192.168.0.98"
        },
        {
          "uid": "d786df41-83a2-4de4-95be-dbec83a7a38a",
          "name": "71c0bae48e884367951607d6c267c931",
          "type": "host",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "ipv4-address": "192.168.0.7"
        },
        {
          "uid": "ebf39b82-34cc-4af1-9515-2013a1ccbe55",
          "name": "7a1efd06d8b24f37b5a1d7b0ecda8581",
          "type": "host",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "ipv4-address": "192.168.0.5"
        },
        {
          "uid": "cb77539a-a5b6-402a-90ad-1f09370cfb4d",
          "name": "8.8.8.8",
          "type": "host",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "ipv4-address": "8.8.8.8"
        },
        {
          "uid": "3ad67056-09df-4d59-aef0-b27d3b499fad",
          "name": "8508bde15f9b48108619e94ebf56c36e",
          "type": "host",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "ipv4-address": "192.168.0.10"
        },
        {
          "uid": "86f4a65f-dc44-412c-b770-0ac221717588",
          "name": "906fcbf16cb54f08907334a37f61899b",
          "type": "host",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "ipv4-address": "170.0.0.4"
        },
        {
          "uid": "5e2cfa85-d905-434c-b9b1-569fd8dba9b1",
          "name": "9652e911ed4140bd884553258a448303",
          "type": "host",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "ipv4-address": "170.0.0.0"
        },
        {
          "uid": "e5965e15-502c-4a93-94b1-df6bd672c553",
          "name": "973e2548acd84bf78a227b18c271bbe6",
          "type": "host",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "ipv4-address": "192.168.0.100"
        },
        {
          "uid": "5ade906a-a2b4-4f94-9d18-e5f8fd5819c0",
          "name": "aaff3a2c3b3a46d2a0fbee0d188767b7",
          "type": "host",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "ipv4-address": "192.168.0.9"
        },
        {
          "uid": "445b9332-5444-4d95-bdce-713de7d7f52c",
          "name": "c388f07101fc4a3390143e5d4e975514",
          "type": "host",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "ipv4-address": "192.168.0.4"
        },
        {
          "uid": "8ddb761a-fa3a-4da2-a494-fdfef2c1f16c",
          "name": "d07dc6d13a3446b3ac01d65ca8c567c6",
          "type": "host",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "ipv4-address": "192.168.0.99"
        },
        {
          "uid": "c9b4f197-1242-4bed-bc55-2e2dfe8bd621",
          "name": "d5e40a765a844f25a3d68712224d2fba",
          "type": "host",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "ipv4-address": "192.168.0.3"
        },
        {
          "uid": "a3c6d70b-a3e0-49e6-a7e6-8e6d20a81f10",
          "name": "e0fdba1660bb4febb5e3f2d4d23c4d4c",
          "type": "host",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "ipv4-address": "170.0.0.3"
        },
        {
          "uid": "3715973a-2048-446f-82d0-f74b81532e56",
          "name": "e50e60f28a2e49a192b79f61fb9ca557",
          "type": "host",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "ipv4-address": "192.168.0.8"
        },
        {
          "uid": "d8885063-5897-4f21-b9cd-f33a34ffa851",
          "name": "f43a0cfca2534ed0bf16207dc9acce49",
          "type": "host",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "ipv4-address": "170.0.0.2"
        },
        {
          "uid": "7615680c-3c6b-425a-83d2-49a507d60150",
          "name": "fa04e70f406b4317a96ecf4e82e50ae3",
          "type": "host",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "ipv4-address": "170.0.0.1"
        },
        {
          "uid": "507d2dae-cbb8-49dc-8497-282b8180012d",
          "name": "TayTest",
          "type": "host",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "ipv4-address": "192.168.0.20"
        },
        {
          "uid": "e9ce7076-da09-4ef9-95f3-374fb88503dd",
          "name": "TayTest84q90y8wqh228",
          "type": "host",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "ipv4-address": "192.168.0.21"
        }
      ],
      "from": 1,
      "to": 27,
      "total": 27
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
    - **ipv4-address** (string)
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