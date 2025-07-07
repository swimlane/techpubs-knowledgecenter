# Get Users

**Description**: Retrieves a list of users from Okta Identity Management, providing an overview of user accounts.

## Endpoint

- **URL:** `/api/v1/users`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **q** (string): Finds users who match the specified query. This doesn't support pagination. This might not deliver optimal performance for large orgs, and is deprecated for such use cases.  To ensure optimal performance, use a search parameter instead. Use the q parameter for a simple lookup of users by name, for example when creating a people picker. The value of q is matched against firstName, lastName, or email. This performs a startsWith match, but this is an implementation detail and can change without notice. You don't need to specify firstName, lastName, or email.
  - **filter** (string): Filters users with a supported expression for a subset of properties. This requires URL encoding. For example, filter=lastUpdated gt "2013-06-01T00:00:00.000Z" is encoded as filter=lastUpdated%20gt%20%222013-06-01T00:00:00.000Z%22. Filtering is case-sensitive for attribute names and query values, while attribute operators are case-insensitive. Filtering supports the following limited number of properties: status, lastUpdated, id, profile.login, profile.email, profile.firstName, and profile.lastName. Additionally, filtering supports only the equal eq operator from the standard Okta API filtering semantics, except in the case of the lastUpdated property. This property can also use the inequality operators (gt, ge, lt, and le). For logical operators, only the logical operators and and or are supported. The not operator isn't supported. See Filtering and Operators. for more information.
  - **after** (string): Specifies the pagination cursor for the next page of groups. The after cursor should be treated as an opaque value and obtained through the next link relation.
  - **limit** (number): Specifies the number of results returned. Defaults to 10 if q is provided.
  - **expand** (string): An optional parameter to include metadata in the `_embedded` attribute. Valid value: `classification`.
  - **search** (string): Searches for users with a supported filtering expression for most properties. Okta recommends using this parameter for search for best performance. This operation supports pagination. Use an ID lookup for records that you update to ensure your results contain the latest data. Property names in the search parameter are case sensitive, whereas operators (eq, sw, and so on) and string values are case insensitive. Unlike with user logins, diacritical marks are significant in search string values: a search for isaac.brock finds Isaac.Brock, but doesn't find a property whose value is isáàc.bröck. This operation requires URL encoding.  For example, search=profile.department eq "Engineering" is encoded as search=profile.department%20eq%20%22Engineering%22.
  - **sortBy** (string): Specifies field to sort by (for search queries only). This can be any single property, for example sortBy=profile.lastName. Users with the same value for the sortBy property will be ordered by id.
  - **sortOrder** (string): Specifies sort order asc or desc (for search queries only). Sorting is done in ASCII sort order (that is, by ASCII character value), but isn't case sensitive. sortOrder is ignored if sortBy is not present.
- **headers** (object)
  - **Content-Type** (string): Specifies the media type of the resource. Optional okta-response value can be included for performance optimization. Complex DelAuth configurations may degrade performance when fetching specific parts of the response, and passing this parameter can omit these parts, bypassing the bottleneck. Enum values for okta-response:
  omitCredentials: Omits the credentials subobject from the response.
  omitCredentialsLinks: Omits the following HAL links from the response: Change Password, Change Recovery Question, Forgot Password, Reset Password, Reset Factors, Unlock.
  omitTransitioningToStatus: Omits the transitioningToStatus field from the response.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "content-length": "140",
      "content-type": "application/json",
      "Date": "Wed, 8 Jan 2025 20:37:23 GMT"
    },
    "reason": "OK",
    "json": {
      "id": "00u118oQYT4TBGuay0g4",
      "status": "ACTIVE",
      "created": "2022-04-04T15:56:05.000Z",
      "activated": null,
      "statusChanged": null,
      "lastLogin": "2022-05-04T19:50:52.000Z",
      "lastUpdated": "2022-05-05T18:15:44.000Z",
      "passwordChanged": "2022-04-04T16:00:22.000Z",
      "type": {
        "id": "oty1162QAr8hJjTaq0g4"
      },
      "profile": {
        "firstName": "Alice",
        "lastName": "Smith",
        "mobilePhone": null,
        "secondEmail": null,
        "login": "alice.smith@example.com",
        "email": "alice.smith@example.com"
      },
      "realmId": "guo1afiNtSnZYILxO0g4",
      "credentials": {
        "password": {},
        "provider": {
          "type": "OKTA",
          "name": "OKTA"
        }
      },
      "_links": {
        "self": {
          "href": "http://your-subdomain.okta.com/api/v1/users/00u118oQYT4TBGuay0g4"
        }
      }
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json** (object)
  - **id** (string)
  - **status** (string)
  - **created** (string)
  - **activated** (object)
  - **statusChanged** (object)
  - **lastLogin** (string)
  - **lastUpdated** (string)
  - **passwordChanged** (string)
  - **type** (object)
    - **id** (string)
  - **profile** (object)
    - **firstName** (string)
    - **lastName** (string)
    - **mobilePhone** (object)
    - **secondEmail** (object)
    - **login** (string)
    - **email** (string)
  - **realmId** (string)
  - **credentials** (object)
    - **password** (object)
    - **provider** (object)
      - **type** (string)
      - **name** (string)
  - **_links** (object)
    - **self** (object)
      - **href** (string)
## Response Headers

| Header | Type |
|--------|------|
| content-length | string |
| content-type | string |
| Date | string |