# Add User

**Description**: Adds a new user to the CyberArk Vault with the provided username via a JSON body input.

## Endpoint

- **URL:** `/PasswordVault/API/Users/`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required
  - **username** (string) – Required: The name of the user.
  - **userType** (string): The user type that was returned according to the license.
  - **unauthorizedInterfaces** (array): The user type that was returned according to the license.
  - **location** (string): The location in the Vault where the user will be created.
  - **expiryDate** (number): The date when the user expires.
  - **userActivityLogRetentionDays** (number): The number of days that a user's account activity records are stored before they are deleted.
  - **loginFromHour** (number): The starting time of the timeframe in which a user can log in to an account.
  - **loginToHour** (number): The ending time of the timeframe in which a user can log in to an account.
  - **enableUser** (boolean): Whether the user will be enabled upon creation.
  - **authenticationMethod** (array): The authentication method that the user will use to log on.
  - **initialPassword** (string): The password that the user will use to log on for the first time.
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
    "status_code": 201,
    "response_headers": {},
    "reason": "Created",
    "json_body": {
      "enableUser": true,
      "changePassOnNextLogon": true,
      "expiryDate": 1577836800,
      "suspended": false,
      "lastSuccessfulLoginDate": 1561282853,
      "unAuthorizedInterfaces": [
        "PSMP",
        "PSM"
      ],
      "authenticationMethod": [
        "AuthTypePass"
      ],
      "passwordNeverExpires": true,
      "distinguishedName": "newUser@cyberark",
      "description": "This user is privileged",
      "businessAddress": {
        "workStreet": "9999999",
        "workCity": "White Mountain",
        "workState": "10 First Street",
        "workZip": "123456",
        "workCountry": "Canada"
      },
      "internet": {
        "homePage": "Cyberark.com",
        "homeEmail": "user@gmail.com",
        "businessEmail": "user@cyberark.com",
        "otherEmail": "user2@gmail.com"
      },
      "phones": {
        "homeNumber": "555123456",
        "businessNumber": "555456789",
        "cellularNumber": "555789789",
        "faxNumber": "999999",
        "pagerNumber": "111111"
      },
      "personalDetails": {
        "street": "3 Second Street",
        "city": "Tel Aviv",
        "state": "Israel",
        "zip": "123456",
        "country": "Israel",
        "title": "Manager",
        "organization": "CyberArk",
        "department": "R&D",
        "profession": "software development",
        "firstName": "John",
        "middleName": "David",
        "lastName": "Smith"
      },
      "id": 350,
      "username": "newUser",
      "source": "CyberArk",
      "userType": "EPVUser",
      "componentUser": false,
      "vaultAuthorization": [
        "AddSafes",
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
  - **id** (number)
  - **username** (string)
  - **source** (string)
  - **userType** (string)
  - **componentUser** (boolean)
  - **vaultAuthorization** (array)
  - **location** (string)