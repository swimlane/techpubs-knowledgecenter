# Get Policies

**Description**: Gets the list of policies

## Endpoint

- **URL:** `rest/policy`
- **Method:** `GET`
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "OK",
    "json_body": {
      "type": "regular",
      "response": {
        "usable": [
          {
            "id": "1",
            "name": "test",
            "description": "desc",
            "status": "0",
            "uuid": "2E950182-08B6-4737-830B-4ACC8F6B92F9"
          },
          {
            "id": "2",
            "name": "test2",
            "description": "desc",
            "status": "0",
            "uuid": "929EF9DD-8A81-4864-AFD2-F87845224F6C"
          },
          {
            "id": "3",
            "name": "test3",
            "description": "desc",
            "status": "0",
            "uuid": "F4B2DE11-F6A1-4058-AFF6-F7D49C238660"
          },
          {
            "id": "4",
            "name": "test4",
            "description": "test desc",
            "status": "0",
            "uuid": "F4B2DE11-F6A1-4058-AFF6-F7D49C238660"
          },
          {
            "id": "1000001",
            "name": "nesus upload - ibm credentials",
            "description": "",
            "status": "0",
            "uuid": "BC2DC4A1-298F-4CC3-A7D4-ABED7248E406"
          },
          {
            "id": "1000002",
            "name": "nesus upload - ibm credentials - uploaded one",
            "description": "Nessus Policy exported from Tenable.sc",
            "status": "0",
            "uuid": "058E06E5-2E30-4E6C-8D27-20FBE45CED2F"
          },
          {
            "id": "1000003",
            "name": "IBM iSeries Credentials Name",
            "description": "Imported Nessus Policy",
            "status": "0",
            "uuid": "970AF7B9-1DE2-43DF-BA29-A282FACE693B"
          },
          {
            "id": "1000004",
            "name": "Nessus Upload 2",
            "description": "Imported Nessus Policy",
            "status": "0",
            "uuid": "893A5150-FB99-4405-AEA1-F88E720686C8"
          },
          {
            "id": "1000005",
            "name": "Nessus Upload 3",
            "description": "Imported Nessus Policy",
            "status": "0",
            "uuid": "308027F4-77F9-4444-A5CE-E57B3928078B"
          },
          {
            "id": "1000016",
            "name": "Tom Test",
            "description": "Imported Nessus Policy",
            "status": "0",
            "uuid": "2278CBB5-F927-4C8F-AEC1-EEF76DEB175D"
          },
          {
            "id": "1000017",
            "name": "Nessus Upload 4",
            "description": "Imported Nessus Policy",
            "status": "0",
            "uuid": "4CF267BB-0A5C-47AB-BAC3-E77E6270EBC5"
          },
          {
            "id": "1000018",
            "name": "Tom Test 2",
            "description": "Imported Nessus Policy",
            "status": "0",
            "uuid": "E8F73EF3-9D8D-4FCA-A3F4-2B4D176767B9"
          },
          {
            "id": "1000019",
            "name": "DOCtest",
            "description": "desc",
            "status": "0",
            "uuid": "178C9E5F-E768-40D4-951C-5A76E7DC6BDA"
          },
          {
            "id": "1000020",
            "name": "test5",
            "description": "test desc",
            "status": "0",
            "uuid": "A4C62370-91ED-42DA-927B-3FE248974563"
          }
        ],
        "manageable": [
          {
            "id": "1000001",
            "name": "nesus upload - ibm credentials",
            "description": "",
            "status": "0",
            "uuid": "BC2DC4A1-298F-4CC3-A7D4-ABED7248E406"
          },
          {
            "id": "1000002",
            "name": "nesus upload - ibm credentials - uploaded one",
            "description": "Nessus Policy exported from Tenable.sc",
            "status": "0",
            "uuid": "058E06E5-2E30-4E6C-8D27-20FBE45CED2F"
          },
          {
            "id": "1000003",
            "name": "IBM iSeries Credentials Name",
            "description": "Imported Nessus Policy",
            "status": "0",
            "uuid": "970AF7B9-1DE2-43DF-BA29-A282FACE693B"
          },
          {
            "id": "1000004",
            "name": "Nessus Upload 2",
            "description": "Imported Nessus Policy",
            "status": "0",
            "uuid": "893A5150-FB99-4405-AEA1-F88E720686C8"
          },
          {
            "id": "1000005",
            "name": "Nessus Upload 3",
            "description": "Imported Nessus Policy",
            "status": "0",
            "uuid": "308027F4-77F9-4444-A5CE-E57B3928078B"
          },
          {
            "id": "1000016",
            "name": "Tom Test",
            "description": "Imported Nessus Policy",
            "status": "0",
            "uuid": "2278CBB5-F927-4C8F-AEC1-EEF76DEB175D"
          },
          {
            "id": "1000017",
            "name": "Nessus Upload 4",
            "description": "Imported Nessus Policy",
            "status": "0",
            "uuid": "4CF267BB-0A5C-47AB-BAC3-E77E6270EBC5"
          },
          {
            "id": "1000018",
            "name": "Tom Test 2",
            "description": "Imported Nessus Policy",
            "status": "0",
            "uuid": "E8F73EF3-9D8D-4FCA-A3F4-2B4D176767B9"
          },
          {
            "id": "1000019",
            "name": "DOCtest",
            "description": "desc",
            "status": "0",
            "uuid": "178C9E5F-E768-40D4-951C-5A76E7DC6BDA"
          },
          {
            "id": "1000020",
            "name": "test5",
            "description": "test desc",
            "status": "0",
            "uuid": "A4C62370-91ED-42DA-927B-3FE248974563"
          }
        ]
      },
      "error_code": 0,
      "error_msg": "",
      "warnings": [],
      "timestamp": 1406233675
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **type** (string)
  - **response** (object)
    - **usable** (array)
      - **id** (string)
      - **name** (string)
      - **description** (string)
      - **status** (string)
      - **uuid** (string)
    - **manageable** (array)
      - **id** (string)
      - **name** (string)
      - **description** (string)
      - **status** (string)
      - **uuid** (string)
  - **error_code** (number)
  - **error_msg** (string)
  - **warnings** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **timestamp** (number)