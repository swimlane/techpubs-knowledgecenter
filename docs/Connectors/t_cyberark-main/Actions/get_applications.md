# Get Applications

**Description**: Obtain a complete list of applications stored in the CyberArk Vault, ensuring secure access to application credentials.

## Endpoint

- **URL:** `/PasswordVault/WebServices/PIMServices.svc/Applications/`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **AppID** (string): The application name.
  - **Location** (string): The location of the application in the Vault hierarchy.
  - **IncludeSublocations** (boolean): Whether or not the search will be performed in sublocations of the specified location.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "Success",
    "json_body": {
      "application": [
        {
          "AccessPermittedFrom": "string",
          "AccessPermittedTo": "string",
          "AllowExtendedAuthenticationRestrictions": false,
          "AppID": "string",
          "BusinessOwnerEmail": "string",
          "BusinessOwnerFName": "string",
          "BusinessOwnerLName": "string",
          "BusinessOwnerPhone": "string",
          "Description": "string",
          "Disabled": false,
          "ExpirationDate": "string",
          "Location": "string"
        }
      ]
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **application** (array)
    - **AccessPermittedFrom** (string)
    - **AccessPermittedTo** (string)
    - **AllowExtendedAuthenticationRestrictions** (boolean)
    - **AppID** (string)
    - **BusinessOwnerEmail** (string)
    - **BusinessOwnerFName** (string)
    - **BusinessOwnerLName** (string)
    - **BusinessOwnerPhone** (string)
    - **Description** (string)
    - **Disabled** (boolean)
    - **ExpirationDate** (string)
    - **Location** (string)