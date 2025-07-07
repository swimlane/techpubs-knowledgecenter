# Application Site - Get All

**Description**: Retrieves all application sites from Check Point R80, configured via a specified JSON body input.

## Endpoint

- **URL:** `/web_api/show-application-sites`
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
      "Date": "Thu, 29 Dec 2022 23:06:36 GMT",
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
          "uid": "00fa9e3c-36ef-0f65-e053-08241dc22da2",
          "name": "#hashtags",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-4035-0f65-e053-08241dc22da2",
          "name": "050 Plus",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e3d-a077-0f65-e053-08241dc22da2",
          "name": "1000keyboards",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e43-56d7-0f65-e053-08241dc22da2",
          "name": "1000memories",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e3d-1ab6-0f65-e053-08241dc22da2",
          "name": "1001",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e3d-a055-0f65-e053-08241dc22da2",
          "name": "100bao",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-3b53-0f65-e053-08241dc22da2",
          "name": "115",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-3b8d-0f65-e053-08241dc22da2",
          "name": "115-audio",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-3b54-0f65-e053-08241dc22da2",
          "name": "115-download",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-3b55-0f65-e053-08241dc22da2",
          "name": "115-upload",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-3b8c-0f65-e053-08241dc22da2",
          "name": "115-video",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "3f209d1e-5357-1973-e053-08241dc21a6d",
          "name": "121 Video Calling",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e3c-d47d-0f65-e053-08241dc22da2",
          "name": "123 Flash Chat",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e3c-ac90-0f65-e053-08241dc22da2",
          "name": "123 Web Messenger",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e3d-1f73-0f65-e053-08241dc22da2",
          "name": "123spider-Bot",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e3d-a078-0f65-e053-08241dc22da2",
          "name": "12seconds",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e3d-2a47-0f65-e053-08241dc22da2",
          "name": "1337x.org",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e3c-6992-0f65-e053-08241dc22da2",
          "name": "160by2",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "03056251-cadc-4398-e053-08241dc2ce72",
          "name": "1and1",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e3c-4a17-0f65-e053-08241dc22da2",
          "name": "1ClickWebSlideShow",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e3d-e3d4-0f65-e053-08241dc22da2",
          "name": "1filesharing.com",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "02c97c6c-b916-1a09-e053-08241dc2659f",
          "name": "1kxun",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "1946e844-c221-5859-e053-08241dc2a3fc",
          "name": "1Password",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e3c-49ba-0f65-e053-08241dc22da2",
          "name": "21tweets",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e3d-a07a-0f65-e053-08241dc22da2",
          "name": "22books",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e3d-a090-0f65-e053-08241dc22da2",
          "name": "24sevenoffice",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "9339c2f3-fc98-496b-adb5-ad3e0626d7ae",
          "name": "26091d25fc614d00b03c58793b3cbb62",
          "type": "application-site",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "00fa9e3d-a091-0f65-e053-08241dc22da2",
          "name": "280slides",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e3d-4965-0f65-e053-08241dc22da2",
          "name": "2Big2Send",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e3c-38d7-0f65-e053-08241dc22da2",
          "name": "2ch",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e41-f98b-0f65-e053-08241dc22da2",
          "name": "2ch-posting",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e41-f65e-0f65-e053-08241dc22da2",
          "name": "2ndrive",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e3d-e453-0f65-e053-08241dc22da2",
          "name": "2shared",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e3d-1aaa-0f65-e053-08241dc22da2",
          "name": "2udoku",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e3d-a092-0f65-e053-08241dc22da2",
          "name": "30boxes",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e3d-e27a-0f65-e053-08241dc22da2",
          "name": "33 Live",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-0abe-0f65-e053-08241dc22da2",
          "name": "360 Mobile Manager",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-0a9a-0f65-e053-08241dc22da2",
          "name": "360 Safeguard",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-0a9f-0f65-e053-08241dc22da2",
          "name": "360 Services",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-0ac1-0f65-e053-08241dc22da2",
          "name": "360 Software Manager",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e3d-e408-0f65-e053-08241dc22da2",
          "name": "360desktop",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e3c-ace5-0f65-e053-08241dc22da2",
          "name": "360share Pro",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-3b59-0f65-e053-08241dc22da2",
          "name": "360Yunpan",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-3b5b-0f65-e053-08241dc22da2",
          "name": "360Yunpan-download",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e44-3b5a-0f65-e053-08241dc22da2",
          "name": "360Yunpan-upload",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "9252681d-915b-45d3-9a47-e2cd8f4e5abc",
          "name": "361c26ec85ad4cecb631d10dec685023",
          "type": "application-site",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "00fa9e3c-4a30-0f65-e053-08241dc22da2",
          "name": "3B",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e3d-a093-0f65-e053-08241dc22da2",
          "name": "3d-pack",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e3c-acaf-0f65-e053-08241dc22da2",
          "name": "3DEE",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        },
        {
          "uid": "00fa9e3c-b03a-0f65-e053-08241dc22da2",
          "name": "3LUXE",
          "type": "application-site",
          "domain": {
            "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
            "name": "APPI Data",
            "domain-type": "data domain"
          }
        }
      ],
      "from": 1,
      "to": 50,
      "total": 7351
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