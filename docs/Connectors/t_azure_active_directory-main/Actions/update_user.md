# Update User

**Description**: Updates a user's account status in Azure Active Directory using their unique ID and the 'accountEnabled' parameter.

## Endpoint

- **URL:** `/v1.0/users/{{id}}`
- **Method:** `PATCH`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required
- **json_body** (object) – Required
  - **aboutMe** (string): A freeform text entry field for the user to describe themselves.
  - **accountEnabled** (string) – Required: true if the account is enabled; otherwise, false. This property is required when a user is created. A global administrator assigned the Directory.AccessAsUser.All delegated permission can update the accountEnabled status of all administrators in the tenant.
  - **ageGroup** (string): Sets the age group of the user. Allowed values:null, Minor, NotAdult and Adult. Refer to the legal age group property definitions for further information.
  - **birthday** (string): The birthday of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
  - **businessPhones** (string): The telephone numbers for the user. NOTE:Although this is a string collection, only one number can be set for this property.
  - **city** (string): The city in which the user is located.
  - **companyName** (string): The company name which the user is associated. This property can be useful for describing the company that an external user comes from. The maximum length is 64 characters.
  - **consentProvidedForMinor** (string): Sets whether consent has been obtained for minors. Allowed values:null, Granted, Denied and NotRequired. Refer to the legal age group property definitions for further information.
  - **country** (string): The country/region in which the user is located; for example, US or UK.
  - **department** (string): The name for the department in which the user works.
  - **displayName** (string): The name displayed in the address book for the user. This is usually the combination of the user's first name, middle initial and last name. This property is required when a user is created and it cannot be cleared during updates.
  - **employeeId** (string): The employee identifier assigned to the user by the organization. The maximum length is 16 characters.
  - **employeeType** (string): Captures enterprise worker type. For example, Employee, Contractor, Consultant, or Vendor. Returned only on $select.
  - **givenName** (string): The given name (first name) of the user.
  - **employeeHireDate** (string): The hire date of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
  - **employeeLeaveDateTime** (string): The date and time when the user left or will leave the organization. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
  - **employeeOrgData** (string): Represents organization data (e.g. division and costCenter) associated with a user.
  - **interests** (string): A list for the user to describe their interests.
  - **jobTitle** (string): The user's job title.
  - **mail** (string): The SMTP address for the user, for example, jeff@contoso.onmicrosoft.com. Changes to this property will also update the user's proxyAddresses collection to include the value as a SMTP address. For Azure AD B2C accounts, this property can be updated up to only ten times with unique SMTP addresses. Cannot be updated to null.
  - **mailNickname** (string): The mail alias for the user. This property must be specified when a user is created.
  - **mobilePhone** (string): The primary cellular telephone number for the user.
  - **mySite** (string): The URL for the user's personal site.
  - **officeLocation** (string): The office location in the user's place of business.
  - **onPremisesExtensionAttributes** (string): Contains extensionAttributes 1-15 for the user. Note that the individual extension attributes are neither selectable nor filterable. For an onPremisesSyncEnabled user, the source of authority for this set of properties is the on-premises and is read-only and is read-only. These extension attributes are also known as Exchange custom attributes 1-15.
  - **onPremisesImmutableId** (string): This property is used to associate an on-premises Active Directory user account to their Azure AD user object. This property must be specified when creating a new user account in the Graph if you are using a federated domain for the user's userPrincipalName (UPN) property. Important:The $ and _ characters cannot be used when specifying this property.
  - **otherMails** (string): A list of additional email addresses for the user; for example:["bob@contoso.com", "Robert@fabrikam.com"].
  - **passwordPolicies** (string): Specifies password policies for the user. This value is an enumeration with one possible value being DisableStrongPassword, which allows weaker passwords than the default policy to be specified. DisablePasswordExpiration can also be specified. The two may be specified together; for example:DisablePasswordExpiration, DisableStrongPassword.
  - **passwordProfile** (object): Specifies the password profile for the user. The profile contains the user's password. The password in the profile must satisfy minimum requirements as specified by the passwordPolicies property. By default, a strong password is required. As a best practice, always set the forceChangePasswordNextSignIn to true. This cannot be used for federated users.
  - **pastProjects** (string): A list for the user to enumerate their past projects.
  - **postalCode** (string): The postal code for the user's postal address. The postal code is specific to the user's country/region. In the United States of America, this attribute contains the ZIP code.
  - **preferredLanguage** (string): The preferred language for the user. Should follow ISO 639-1 Code; for example en-US.
  - **responsibilities** (string): A list for the user to enumerate their responsibilities.
  - **schools** (string): A list for the user to enumerate the schools they have attended.
  - **skills** (string): A list for the user to enumerate their skills.
  - **state** (string): The state or province in the user's address.
  - **streetAddress** (string): The street address of the user's place of business.
  - **surname** (string): The user's surname (family name or last name).
  - **usageLocation** (string): A two letter country code (ISO standard 3166). Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. Examples include:US, JP, and GB. Not nullable.
  - **userPrincipalName** (string): The user principal name (UPN) of the user. The UPN is an Internet-style login name for the user based on the Internet standard RFC 822. By convention, this should map to the user's email name. The general format is alias@domain, where domain must be present in the tenant's collection of verified domains. The verified domains for the tenant can be accessed from the verifiedDomains property of organization.
  - **userType** (string): A string value that can be used to classify user types in your directory, such as Member and Guest.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Fri, 18 Aug 2023 11:47:19 GMT",
      "Content-Type": "text/html; charset=UTF-8",
      "Content-Length": "1000",
      "Connection": "keep-alive",
      "Cache-Control": "private",
      "Content-Encoding": "gzip",
      "Vary": "Accept-Encoding",
      "x-content-type-options": "nosniff",
      "X-XSS-Protection": "1; mode=block",
      "x-ms-version": "12.43.2.1 (v12.42.0.1#6c4023fb99.230803-0127) Signed",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "X-UA-Compatible": "IE=edge",
      "X-Frame-Options": "SAMEORIGIN",
      "x-azure-ref": "20230818T114719Z-v7556zx97h4335ppu1mubfv65s000000021g00000000yd3z",
      "X-Cache": "CONFIG_NOCACHE",
      "Accept-Ranges": "bytes"
    },
    "reason": "OK",
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
| Date | string |
| Content-Type | string |
| Content-Length | string |
| Connection | string |
| Cache-Control | string |
| Content-Encoding | string |
| Vary | string |
| x-content-type-options | string |
| X-XSS-Protection | string |
| x-ms-version | string |
| Strict-Transport-Security | string |
| X-UA-Compatible | string |
| X-Frame-Options | string |
| x-azure-ref | string |
| X-Cache | string |
| Accept-Ranges | string |