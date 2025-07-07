# Get User Details

**Description**: Retrieve detailed information for a specified user in CyberArk Vault by providing the UserID.

## Endpoint

- **URL:** `/PasswordVault/API/Users/{{UserID}}/`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **UserID** (string) – Required: The ID of the user for which information is returned.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "Success",
    "json_body": {
      "enableUser": true,
      "changePassOnNextLogon": false,
      "expiryDate": 1577836800,
      "suspended": false,
      "lastSuccessfulLoginDate": 1561282853,
      "unAuthorizedInterfaces": [
        "GUI"
      ],
      "authenticationMethod": [
        "AuthTypePass"
      ],
      "passwordNeverExpires": true,
      "distinguishedName": "JohnDoeRoe",
      "description": "John Doe Roe",
      "businessAddress": {
        "workStreet": "Kuritania street",
        "workCity": "Curitania",
        "workState": "Suritania",
        "workZip": "90211",
        "workCountry": "Ruritania"
      },
      "internet": {
        "homePage": "example.com",
        "homeEmail": "John@example.net",
        "businessEmail": "John@example.com",
        "otherEmail": "John@example.org"
      },
      "phones": {
        "homeNumber": "555-0100",
        "businessNumber": "555-0101",
        "cellularNumber": "0491 570 156",
        "faxNumber": "555-0102",
        "pagerNumber": "555-0103"
      },
      "personalDetails": {
        "street": "Main street",
        "city": "Curitania",
        "state": "Suritania",
        "zip": "90210",
        "country": "Ruritania",
        "title": "Mr. John",
        "organization": "Acme",
        "department": "newco",
        "profession": "Doing Job",
        "firstName": "John",
        "middleName": "Doe",
        "lastName": "Roe"
      },
      "groupsMembership": [
        {
          "groupID": 16,
          "groupName": "PVWAMonitor",
          "groupType": "Vault"
        },
        {
          "groupID": 17,
          "groupName": "PVWAUsers",
          "groupType": "Vault"
        },
        {
          "groupID": 11,
          "groupName": "Vault Admins",
          "groupType": "Vault"
        }
      ],
      "id": 24,
      "username": "JohnDR",
      "source": "CyberArk",
      "userType": "EPVUser",
      "componentUser": false,
      "vaultAuthorization": [
        "AuditUsers"
      ],
      "location": "\\"
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **enableUser** (boolean)
  - **changePassOnNextLogon** (boolean)
  - **expiryDate** (number)
  - **suspended** (boolean)
  - **lastSuccessfulLoginDate** (number)
  - **unAuthorizedInterfaces** (array)
  - **authenticationMethod** (array)
  - **passwordNeverExpires** (boolean)
  - **distinguishedName** (string)
  - **description** (string)
  - **businessAddress** (object)
    - **workStreet** (string)
    - **workCity** (string)
    - **workState** (string)
    - **workZip** (string)
    - **workCountry** (string)
  - **internet** (object)
    - **homePage** (string)
    - **homeEmail** (string)
    - **businessEmail** (string)
    - **otherEmail** (string)
  - **phones** (object)
    - **homeNumber** (string)
    - **businessNumber** (string)
    - **cellularNumber** (string)
    - **faxNumber** (string)
    - **pagerNumber** (string)
  - **personalDetails** (object)
    - **street** (string)
    - **city** (string)
    - **state** (string)
    - **zip** (string)
    - **country** (string)
    - **title** (string)
    - **organization** (string)
    - **department** (string)
    - **profession** (string)
    - **firstName** (string)
    - **middleName** (string)
    - **lastName** (string)
  - **groupsMembership** (array)
    - **groupID** (number)
    - **groupName** (string)
    - **groupType** (string)
  - **id** (number)
  - **username** (string)
  - **source** (string)
  - **userType** (string)
  - **componentUser** (boolean)
  - **vaultAuthorization** (array)
  - **location** (string)