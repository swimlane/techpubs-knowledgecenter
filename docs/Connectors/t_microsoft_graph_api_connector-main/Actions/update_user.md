# Update User

**Description**: Updates a user's properties in Microsoft Graph API using the specified 'user_id' and provided JSON body data.

## Endpoint

- **URL:** `/v1.0/users/{{user_id}}`
- **Method:** `PATCH`
## Inputs

- **path_parameters** (object) – Required
  - **user_id** (string) – Required
- **json_body** (object) – Required
  - **aboutMe** (string): A freeform text entry field for the user to describe themselves.
  - **accountEnabled** (boolean): True if the account is enabled; otherwise, false.
  - **ageGroup** (string): Sets the age group of the user.
  - **birthday** (string): The birthday of the user.
  - **businessPhones** (array): The telephone numbers for the user.
  - **city** (string): The city in which the user is located.
  - **companyName** (string): The name of the company that the user is associated.
  - **consentProvidedForMinor** (string): Sets whether consent has been obtained for minors.
  - **country** (string): The country/region in which the user is located.
  - **customSecurityAttributes** (object): An open complex type that holds the value of a custom security attribute that is assigned to a directory object.
    - **@odata.type** (string)
  - **department** (string): The name for the department in which the user works.
  - **displayName** (string): The name displayed in the address book for the user.
  - **employeeId** (string): The employee identifier assigned to the user by the organization.
  - **employeeType** (string): Captures enterprise worker type.
  - **givenName** (string): The given name (first name) of the user.
  - **employeeHireDate** (string): The hire date of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time.
  - **employeeLeaveDateTime** (string): The date and time when the user left or will leave the organization. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time.
  - **employeeOrgData** (object): Represents organization data (for example, division and costCenter) associated with a user.
    - **costCenter** (string): The cost center associated with the user.
    - **division** (string): The name of the division in which the user works.
  - **interests** (array): A list for the user to describe their interests.
  - **jobTitle** (string): The user's job title.
  - **mail** (string): The SMTP address for the user,
  - **mailNickname** (string): The mail alias for the user.
  - **mobilePhone** (string): The primary cellular telephone number for the user.
  - **mySite** (string): The URL for the user's personal site.
  - **officeLocation** (string): The office location in the user's place of business.
  - **onPremisesExtensionAttributes** (object)
    - **extensionAttribute1** (string): First customizable extension attribute.
    - **extensionAttribute2** (string): Second customizable extension attribute.
    - **extensionAttribute3** (string): Third customizable extension attribute.
    - **extensionAttribute4** (string): Fourth customizable extension attribute.
    - **extensionAttribute5** (string): Fifth customizable extension attribute.
    - **extensionAttribute6** (string): Sixth customizable extension attribute.
    - **extensionAttribute7** (string): Seventh customizable extension attribute.
    - **extensionAttribute8** (string): Eighth customizable extension attribute.
    - **extensionAttribute9** (string): Ninth customizable extension attribute.
    - **extensionAttribute10** (string): Tenth customizable extension attribute.
    - **extensionAttribute11** (string): Eleventh customizable extension attribute.
    - **extensionAttribute12** (string): Twelfth customizable extension attribute.
    - **extensionAttribute13** (string): Thirteenth customizable extension attribute.
    - **extensionAttribute14** (string): Fourteenth customizable extension attribute.
    - **extensionAttribute15** (string): Fifteenth customizable extension attribute.
  - **onPremisesImmutableId** (string): This property is used to associate an on-premises Active Directory user account to their Microsoft Entra user object.
  - **otherMails** (array): A list of additional email addresses for the user.
  - **passwordPolicies** (string): Specifies password policies for the user.
  - **passwordProfile** (object): Specifies the password profile for the user. The profile contains the user's password.
    - **forceChangePasswordNextSignIn** (boolean): true if the user must change their password on the next sign-in; otherwise false.
    - **forceChangePasswordNextSignInWithMfa** (boolean): If true, at next sign-in, the user must perform a multifactor authentication (MFA) before being forced to change their password.
    - **password** (string): The password for the user.
  - **pastProjects** (array): A list for the user to enumerate their past projects.
  - **postalCode** (string): The postal code for the user's postal address.
  - **preferredLanguage** (string): The preferred language for the user. Should follow ISO 639-1 Code.
  - **responsibilities** (array): A list for the user to enumerate their responsibilities.
  - **schools** (array): A list for the user to enumerate the schools they attended.
  - **skills** (array): A list for the user to enumerate their skills.
  - **state** (string): The state or province in the user's address.
  - **streetAddress** (string): The street address of the user's place of business.
  - **surname** (string): The user's surname (family name or last name).
  - **usageLocation** (string): A two letter country code (ISO standard 3166).
  - **userPrincipalName** (string): The user principal name (UPN) of the user. The UPN is an Internet-style sign-in name for the user based on the Internet standard RFC 822.
  - **userType** (string): A string value that can be used to classify user types in your directory.
## Output

### Example

```json
[
  {
    "status_code": 204,
    "response_headers": {
      "Cache-Control": "no-cache",
      "Strict-Transport-Security": "max-age=31536000",
      "request-id": "38dd3b1c-ff86-4da9-9647-bdcde1a611c8",
      "client-request-id": "38dd3b1c-ff86-4da9-9647-bdcde1a611c8",
      "x-ms-ags-diagnostic": "{\"ServerInfo\":{\"DataCenter\":\"Central India\",\"Slice\":\"E\",\"Ring\":\"3\",\"ScaleUnit\":\"000\",\"RoleInstance\":\"PN1PEPF00007040\"}}",
      "x-ms-resource-unit": "1",
      "Date": "Tue, 28 May 2024 10:09:05 GMT"
    },
    "reason": "No Content",
    "response_text": ""
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **response_text** (string)
## Response Headers

| Header | Type |
|--------|------|
| Cache-Control | string |
| Strict-Transport-Security | string |
| request-id | string |
| client-request-id | string |
| x-ms-ags-diagnostic | string |
| x-ms-resource-unit | string |
| Date | string |