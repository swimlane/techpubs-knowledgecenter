# Get Groups

**Description**: Retrieves a list of groups from Okta Identity Management without requiring additional parameters.

## Endpoint

- **URL:** `/api/v1/groups`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **q** (string): Finds a group that matches the name property. Paging and searching are currently mutually exclusive.  You can't page a query.  The default limit for a query is 300 results. Query is intended for an auto-complete picker use case where users refine their search string to constrain the results.
  - **filter** (string): All filters must be URL encoded. For example, filter=lastUpdated gt "2013-06-01T00:00:00.000Z" is encoded as filter=lastUpdated%20gt%20%222013-06-01T00:00:00.000Z%22. Examples: Filter group with a specific ID:
  filter=id eq "00g1emaKYZTWRYYRRTSK"
Filter groups that are of the type `OKTA_GROUP`:
  filter=type eq "OKTA_GROUP"
Filter groups that are of the type `OKTA_GROUP` with profile updated after 11/11/2015:
  filter=type eq "OKTA_GROUP" and lastUpdated gt "2016-11-11T00:00:00.000Z"
Filter groups that are of the type `OKTA_GROUP` with profile or memberships updated before 11/11/2015:
  filter=type eq "OKTA_GROUP" and (lastUpdated lt "2015-11-11T00:00:00.000Z" or lastMembershipUpdated lt "2015-11-11T00:00:00.000Z")
  - **after** (string): Specifies the pagination cursor for the next page of groups. The after cursor should be treated as an opaque value and obtained through the next link relation.
  - **limit** (number): Specifies the number of group results in a page. Don't write code that depends on the default or maximum value, as it might change. If you receive an HTTP 500 status code, you likely exceeded the request timeout. Retry your request with a smaller limit and page the results. The Okta default Everyone group isn't returned for users with a group Admin role. Note: We strongly encourage using a limit that's less than or equal to 200. Any number greater than 200 affects performance and accuracy.
  - **expand** (string): If specified, additional metadata is included in the response. Possible values are stats and app. This additional metadata is listed in the _embedded key of the response. Note: You can use the stats value to return the number of users within a group.  This is listed as the _embedded.stats.usersCount value in the response.
  - **search** (string): Searches for groups with a supported filtering expression for all attributes except for _embedded, _links, and objectClass. Search currently performs a startsWith match but it should be considered an implementation detail and might change without notice in the future. This operation supports pagination. Using search requires URL encoding, for example, search=type eq "OKTA_GROUP" is encoded as search=type+eq+%22OKTA_GROUP%22. This operation searches many properties:
  Any group profile property, including imported app group profile properties.
  The top-level properties id, created, lastMembershipUpdated, lastUpdated, and type.
  The source of groups with type of APP_GROUP, accessed as source.id.
  You can also use sortBy and sortOrder parameters.
  - **sortBy** (string): Specifies field to sort by (for search queries only). sortBy can be any single property, for example sortBy=profile.name.
  - **sortOrder** (string): Specifies sort order: asc or desc (for search queries only). This parameter is ignored if if sortBy is not present. Groups with the same value for the sortBy property will be ordered by id.
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
      "id": "00g1emaKYZTWRYYRRTSK",
      "created": "2015-02-06T10:11:28.000Z",
      "lastUpdated": "2015-10-05T19:16:43.000Z",
      "lastMembershipUpdated": "2015-11-28T19:15:32.000Z",
      "objectClass": [
        "okta:user_group"
      ],
      "type": "OKTA_GROUP",
      "profile": {
        "name": "West Coast users",
        "description": "All users West of The Rockies"
      },
      "_links": {
        "logo": [
          {
            "name": "medium",
            "href": "https://{yourOktaDomain}/img/logos/groups/okta-medium.png",
            "type": "image/png"
          },
          {
            "name": "large",
            "href": "https://{yourOktaDomain}/img/logos/groups/okta-large.png",
            "type": "image/png"
          }
        ],
        "users": {
          "href": "https://{yourOktaDomain}/api/v1/groups/00g1emaKYZTWRYYRRTSK/users"
        },
        "apps": {
          "href": "https://{yourOktaDomain}/api/v1/groups/00g1emaKYZTWRYYRRTSK/apps"
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
  - **created** (string)
  - **lastUpdated** (string)
  - **lastMembershipUpdated** (string)
  - **objectClass** (array)
  - **type** (string)
  - **profile** (object)
    - **name** (string)
    - **description** (string)
  - **_links** (object)
    - **logo** (array)
      - **name** (string)
      - **href** (string)
      - **type** (string)
    - **users** (object)
      - **href** (string)
    - **apps** (object)
      - **href** (string)
## Response Headers

| Header | Type |
|--------|------|
| content-length | string |
| content-type | string |
| Date | string |