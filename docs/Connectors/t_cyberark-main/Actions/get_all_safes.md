# Get All Safes

**Description**: Retrieve all accessible Safes within the CyberArk Vault based on user permissions.

## Endpoint

- **URL:** `/PasswordVault/API/Safes/`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **search** (string): Searches according to the Safe name. Search is performed according to the REST standard (search="search word").
  - **offset** (number): Offset of the first Safe that is returned in the collection of results
  - **limit** (number): The maximum number of Safes that are returned.
  - **sort** (string): Sorts according to the safeName property in ascending order (default) or descending order to control the sort direction.
  - **includeAccounts** (boolean): Whether or not to return accounts for each Safe as part of the response.
  - **extendedDetails** (boolean): Whether or not to return all Safe details or only safeName as part of the response.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "Success",
    "json_body": {
      "value": [
        {
          "safeUrlId": "VaultInternal",
          "safeName": "VaultInternal",
          "safeNumber": 2,
          "description": "",
          "location": "\\",
          "creator": {
            "id": "2",
            "name": "Administrator"
          },
          "olacEnabled": false,
          "managingCPM": "",
          "numberOfVersionsRetention": null,
          "numberOfDaysRetention": 30,
          "autoPurgeEnabled": false,
          "creationTime": 1608827926,
          "lastModificationTime": 1610319618268452,
          "isExpiredMember": false
        }
      ],
      "count": 1769,
      "nextLink": "api/safes?offset=25&limit=25&useCache=False"
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **value** (array)
    - **safeUrlId** (string)
    - **safeName** (string)
    - **safeNumber** (number)
    - **description** (string)
    - **location** (string)
    - **creator** (object)
      - **id** (string)
      - **name** (string)
    - **olacEnabled** (boolean)
    - **managingCPM** (string)
    - **numberOfVersionsRetention** (object)
    - **numberOfDaysRetention** (number)
    - **autoPurgeEnabled** (boolean)
    - **creationTime** (number)
    - **lastModificationTime** (number)
    - **isExpiredMember** (boolean)
  - **count** (number)
  - **nextLink** (string)