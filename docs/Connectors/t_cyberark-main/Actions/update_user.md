# Update User

**Description**: Modifies a CyberArk Vault user's details by utilizing their userID and new username. Requires both userID and username.

## Endpoint

- **URL:** `/PasswordVault/API/Users/{{userID}}/`
- **Method:** `PUT`
## Inputs

- **path_parameters** (object) – Required
  - **userID** (string) – Required
- **json_body** (object) – Required
  - **username** (string) – Required: The name of the user.
  - **userType** (string): The user type that was returned according to the license.
  - **unauthorizedInterfaces** (array): The user type that was returned according to the license.
  - **location** (string): The location in the Vault where the user will be created.
  - **expiryDate** (number): The date when the user expires.
  - **userActivityLogRetentionDays** (number): The number of days that a user's account activity records are stored before they are deleted.
  - **loginFromHour** (number): The starting time of the timeframe in which a user can log in to an account.
  - **loginToHour** (number): The ending time of the timeframe in which a user can log in to an account.
  - **enableUser** (boolean): Whether the user is enabled.
  - **authenticationMethod** (array): The authentication method that the user uses to log on.
  - **password** (string): The password that the user will use to log on for the first time.
  - **changePassOnNextLogon** (boolean): Whether or not the user must change their password from the second log on onward.
  - **passwordNeverExpires** (boolean): Whether the user's password will not expire unless they decide to change it.
  - **distinguishedName** (string): The user's distinguished name.
  - **vaultAuthorization** (array): The user permissions.
  - **businessAddress** (object): The user's postal address, including city, state, zip, country and street.
    - **workStreet** (string)
    - **workCity** (string)
    - **workState** (string)
    - **workZip** (string)
    - **workCountry** (string)
  - **internet** (object): The user's email addresses, including Home page, Home email, Business email and Other email.
    - **homePage** (string)
    - **homeEmail** (string)
    - **businessEmail** (string)
    - **otherEmail** (string)
  - **phones** (object): The user's phone numbers, including Home, Business, Cellular, Fax and Pager.
    - **homeNumber** (string)
    - **businessNumber** (string)
    - **cellularNumber** (string)
    - **faxNumber** (string)
    - **pagerNumber** (string)
  - **description** (string): Notes and comments.
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
  - **id** (number)
  - **username** (string)
  - **source** (string)
  - **userType** (string)
  - **componentUser** (boolean)
  - **vaultAuthorization** (array)
  - **location** (string)