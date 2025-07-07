# Group - Get All

**Description**: Retrieves a comprehensive list of all configured groups within Check Point R80, requiring a JSON body input.

## Endpoint

- **URL:** `/web_api/show-groups`
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
      "Date": "Fri, 30 Dec 2022 16:25:10 GMT",
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
          "uid": "b92f7002-60dc-49bf-9b96-3e3367068687",
          "name": "01138b85ae344cd5b6a07c82971bd7e6",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "dfa5bce4-3ef9-4b07-b67e-e722d14c2b7c",
          "name": "0a3d08b37b78440eb084d6563114dde6",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "953f821a-0c4d-4814-a467-ce526ecf8414",
          "name": "0c006d9fef314b96a7d488a5c29c4720",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "618d7dc4-1640-49ea-ae8c-61e6dc32a47c",
          "name": "0d55eebb433c460aadcb15d23418666c",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "90d0997c-30a2-4ab3-b4f3-549da3c9ae39",
          "name": "10a4b9b7aaae469783c0b4c78b637dbc",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "9570eb14-cedb-4548-8013-44826d12ac9c",
          "name": "14f3101faf574cce8b70299b86edf3a6",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "d6d67969-2fb6-40d8-939e-f4a0ff51eb01",
          "name": "15b04022c146456c9fc15d5c0a019838",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "48d4570c-b986-4512-b9a0-b49c6ae18338",
          "name": "1700bb1853784840ae4617618f1154a3",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "659d836d-01dc-4a08-b474-d4b2a8bddce7",
          "name": "176d404bb30243e8b3658ceb6f324b28",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "55128216-06b3-4757-8380-fa93dea06831",
          "name": "1dc127ea6453423983a7c93c81c27e2b",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "64f3d5db-b68b-47f1-bab0-1d84652ee0cc",
          "name": "1e42458c82534f52b08bae242e0b1a09",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "96b2b0b6-fd44-4f97-bf73-015ba95bdb92",
          "name": "1fd4cde8e81647c4aa5d9cd09c9e77c8",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "b3eaedaa-1508-4b16-878f-5aec0e2d202e",
          "name": "20fc68604253457080197c5393c08b67",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "8792689c-f075-4e61-8c40-8e58788872c3",
          "name": "2284bc27029b431b81d8eb93c11c1979",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "ef6eb9c6-556e-4851-8234-c5d7478c3d22",
          "name": "22b30301f38845eebe31457ef5182fbb",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "85652d94-5440-4bf5-aca6-70f7f30a4851",
          "name": "257dd2bce0694778a34b9bfae0c1ffdc",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "e8470d84-361a-4d65-90a4-8b72c22fde53",
          "name": "26312c4ab25e40168873a5cb9e6467c0",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "df4c3386-1e5b-48ba-96b4-f7c3aa5c08ba",
          "name": "2dd4a2e231914815a7623d8fd3b633a6",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "ff55ea67-0036-4701-8e13-25e8c92d1829",
          "name": "304cb379a78c425b8a11ea1cd8927a24",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "7c8d2f1a-860d-47fd-a80a-758189d22094",
          "name": "31da84c6f37042a181b8091d4574ab30",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "efbd8b21-0523-4c42-9b3b-6a04b44ab367",
          "name": "330c5bc6fa96485999dceeeb9b65e0c4",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "b154ee2e-7646-4b59-9c47-c5ad20b0259b",
          "name": "339f3a246328430eae7d172ae5d3dbcc",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "c1af28a6-38eb-4b5c-9e54-9fb408b552c7",
          "name": "38be7cc707d545869bc4241631c66011",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "2d5d7b6a-cf08-45e2-9449-16194f9c51f9",
          "name": "3904ea88eeef43b69d37002cf4971091",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "4c112ae1-18e4-4753-86bd-f81b6cbf2087",
          "name": "3a84dd5de9f642bda23705e7640ffebf",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "baeb28c4-2133-4102-92c5-dcb80ef1c052",
          "name": "4027d2f1620242ecbc8d9294ee001772",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "3ab71c91-cdd7-4426-baec-674c1b0b00e0",
          "name": "411c2e8776e845de8e24555d76d5b920",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "f660256c-cf35-42af-86fe-69beffcf61a6",
          "name": "490a88d0fa264296b9df63eefe2a875f",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "20a3d74c-0a2e-4d6c-9d5d-d0f7c4628a49",
          "name": "494bee1e0ea3468ea820c2e3ae13d5f1",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "1d3cef79-39fa-4963-8f53-087aad42d2ac",
          "name": "58be9a40c36446999b65a8496ba309f5",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "f77d26fa-2304-4bbf-bcd8-097c5e699f11",
          "name": "5f3ec42a0d55405b8c042e7978deaded",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "a95cfe1d-1dbb-4be0-9b7b-d6325d19f688",
          "name": "69c8bb0bf3ec4141917ec0a6a54cce07",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "e8fecd9c-43d4-410d-a4fa-3f1165ad0ade",
          "name": "69f7135cbdd94d139719765c0e6faa9a",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "42ddcb38-c02d-4fb8-9969-20023ce1e029",
          "name": "6e509951c3d24139a0304f73aa782aec",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "2d2a30f0-40c0-4c3b-bca9-5400e7f03918",
          "name": "724978f9c13b429085d5c1a6401f8720",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "3c22fb06-2862-4cd1-bb0e-b7f2c2d98ebc",
          "name": "783487fb4f994b11b12bfd8dd2e92d15",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "d312cdee-9f4e-4eeb-971c-58ec06bfcbeb",
          "name": "7e11893bef4943eabd418bb1bd16c086",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "f79fde18-0950-4a7e-8e55-4962ae7698f5",
          "name": "7f54edf5a65b4aabb1879a6f4ceebe58",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "2a36205e-6d3c-4f47-be49-d11bb623ac86",
          "name": "7fb38652a6e44c0aa9ba14633ce7abcf",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "65f63997-c89f-435b-9b75-06a51ad86bb9",
          "name": "7ffe795368a346bf917d24e7b2ce86a1",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "a9199148-994a-4949-ba8c-bc680636e7fb",
          "name": "8411143b87934642a1d43c48b566f257",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "bb9eb593-69a4-4955-aa0f-b90bda459b8d",
          "name": "86f2ad71e0d145a38dc3508b3a6c0089",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "2748fa63-ac32-4b7b-b494-b6161af1b11c",
          "name": "870d6d2d44de4c38a87fce12e481c12e",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "7fab09c5-6247-4a11-85aa-dfdb8c90b5d8",
          "name": "88856c30e67e45d7ae0c2746d9e47069",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "0cc0f84a-3a85-4483-8fdb-45f86781aa0e",
          "name": "8a55e2f8b2c1448795d87fffc4c833fd",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "0b7172f1-9c18-479a-a7ae-8966e101afd6",
          "name": "91b93d395f284e978f95a8821129603e",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "b67fa3e0-27fb-4bc5-91e2-8bf1b7fb1d97",
          "name": "96e63a62cce4413a86aa94b37417f8fc",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "961d7918-2b33-4001-99b7-ebe3e7393339",
          "name": "9a1e448182f540399a59b6d58304cd5d",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "a529382a-7e29-4725-8fbd-761aa3ff6797",
          "name": "9b881f2a5b394195ad915cb63a53fd2d",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "2905c4fd-0501-4c37-ae33-4ef7b05039a6",
          "name": "9cd1b0e496074684b7f01ad3cbed9a81",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        }
      ],
      "from": 1,
      "to": 50,
      "total": 75
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