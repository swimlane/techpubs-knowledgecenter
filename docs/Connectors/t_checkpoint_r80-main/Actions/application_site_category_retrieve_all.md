# Application Site Category - Get all

**Description**: Retrieves all application site categories from Check Point R80, with a requirement for a JSON body input.

## Endpoint

- **URL:** `/web_api/show-application-site-categories`
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
      "Date": "Thu, 29 Dec 2022 20:54:57 GMT",
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
          "uid": "6a6536de-422b-40aa-8c52-d10cea3614c2",
          "name": "022b2205d1554d6e9d5b65afd48be623",
          "type": "application-site-category",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "3d1bb760-f161-4adc-b3f1-8511fc23c314",
          "name": "255be4485c2540459fc60d92e26dfba0",
          "type": "application-site-category",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "5fff11f2-43be-44ef-89ac-ca2f8c6c18be",
          "name": "5580bfaf58a04f78bff2b9137ea10715",
          "type": "application-site-category",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "49b81f91-8a54-4d4c-b24a-e7c129cc6d43",
          "name": "6ec278abefe24aa4bbf022c817154547",
          "type": "application-site-category",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "00fa9e44-40c9-0f65-e053-08241dc22da2",
          "name": "Adds other software",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-409e-0f65-e053-08241dc22da2",
          "name": "Alcohol",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-40c3-0f65-e053-08241dc22da2",
          "name": "Allows remote connect",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-40ca-0f65-e053-08241dc22da2",
          "name": "Allows remote control",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-415a-0f65-e053-08241dc22da2",
          "name": "Anonymizer",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-409f-0f65-e053-08241dc22da2",
          "name": "Art / Culture",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-4107-0f65-e053-08241dc22da2",
          "name": "BitTorrent protocol",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-40a1-0f65-e053-08241dc22da2",
          "name": "Blogs / Personal Pages",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-40b0-0f65-e053-08241dc22da2",
          "name": "Botnets",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-4156-0f65-e053-08241dc22da2",
          "name": "Browser Plugin",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-41ae-0f65-e053-08241dc22da2",
          "name": "Browser Toolbar",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-40a3-0f65-e053-08241dc22da2",
          "name": "Business / Economy",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-4173-0f65-e053-08241dc22da2",
          "name": "Business Applications",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "84937779-09b9-4c08-81a4-8751731f6b4f",
          "name": "c24a6583da2a4f7784f7e0ed9ce084ab",
          "type": "application-site-category",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "36daf673-4e36-45bb-a243-04dc33b08092",
          "name": "c517ddddd8d74a5b94929c71f14d0cfa",
          "type": "application-site-category",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "45c0f443-16d0-4fcd-8a7b-f781ecc4c6b2",
          "name": "cbf9bd2e73114b1cb00a51b23f04aba5",
          "type": "application-site-category",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "00fa9e44-40b8-0f65-e053-08241dc22da2",
          "name": "Child Abuse",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-41b2-0f65-e053-08241dc22da2",
          "name": "Cloud Services",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-41b0-0f65-e053-08241dc22da2",
          "name": "Communication Standard",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-407b-0f65-e053-08241dc22da2",
          "name": "Computers / Internet",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-418c-0f65-e053-08241dc22da2",
          "name": "Content Provider and Sharing",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-4154-0f65-e053-08241dc22da2",
          "name": "Critical Risk",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-41b1-0f65-e053-08241dc22da2",
          "name": "Cryptocurrency",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "c2fdfa26-2fbc-456d-87f0-b92874485943",
          "name": "Custom_Application_Site",
          "type": "application-site-category",
          "domain": {
            "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
            "name": "Check Point Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "6aaf723f-d412-4020-9a36-ceb7231d0f53",
          "name": "d3296854ce854eb7a763a4002e5e427b",
          "type": "application-site-category",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "00fa9e44-4179-0f65-e053-08241dc22da2",
          "name": "Download Manager",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-407d-0f65-e053-08241dc22da2",
          "name": "Education",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-416f-0f65-e053-08241dc22da2",
          "name": "Email",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-40f2-0f65-e053-08241dc22da2",
          "name": "Encrypts communications",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-407e-0f65-e053-08241dc22da2",
          "name": "Entertainment",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "033eb0a3-e9df-42b7-873a-ce341ae66654",
          "name": "f883a9f22ac2451bb644b6b45c72b853",
          "type": "application-site-category",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "00fa9e44-4191-0f65-e053-08241dc22da2",
          "name": "Facebook Business",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-4192-0f65-e053-08241dc22da2",
          "name": "Facebook Education",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-4193-0f65-e053-08241dc22da2",
          "name": "Facebook Entertainment",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-4199-0f65-e053-08241dc22da2",
          "name": "Facebook File Sharing",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-4194-0f65-e053-08241dc22da2",
          "name": "Facebook Friends & Family",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-4195-0f65-e053-08241dc22da2",
          "name": "Facebook Games",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-4196-0f65-e053-08241dc22da2",
          "name": "Facebook Lifestyle",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-419a-0f65-e053-08241dc22da2",
          "name": "Facebook Popular",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-4197-0f65-e053-08241dc22da2",
          "name": "Facebook Sports",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-4198-0f65-e053-08241dc22da2",
          "name": "Facebook Utilities",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-4166-0f65-e053-08241dc22da2",
          "name": "Facebook Widgets",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-40b3-0f65-e053-08241dc22da2",
          "name": "Fashion",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-4175-0f65-e053-08241dc22da2",
          "name": "File Storage and Sharing",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-4080-0f65-e053-08241dc22da2",
          "name": "Financial Services",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-4167-0f65-e053-08241dc22da2",
          "name": "Friendster Widgets",
          "type": "application-site-category",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        }
      ],
      "from": 1,
      "to": 50,
      "total": 172
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