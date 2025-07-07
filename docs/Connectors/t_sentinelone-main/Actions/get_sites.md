# Get Sites

**Description**: Retrieves a list of SentinelOne sites matching filter criteria to manage and organize network topology.

## Endpoint

- **URL:** `/web/api/v2.1/sites`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **accountId** (string): Account ID
  - **accountIds** (array): List of Account IDs to filter by.
  - **accountName__contain** (array): Free-text filter by account name (supports multiple values).
  - **activeLicenses** (number): Active licenses.
  - **adminOnly** (boolean): Show sites the user has Admin privileges to.
  - **availableMoveSites** (boolean): Only return sites the user can move agents through.
  - **countOnly** (boolean): If true, only total number of items will be returned, without any of the actual objects.
  - **createdAt** (string): Timestamp of site creation.
  - **cursor** (string): Cursor position returned by the last request. Use to iterate over more than 1000 items.
  - **description** (string): The description for the Site.
  - **description__contains** (array): Free-text filter by site description (supports multiple values).
  - **expiration** (string): Expiration.
  - **externalId** (string): Id in a CRM external system.
  - **features** (array): If sent return only sites that support this features.
  - **healthStatus** (boolean): Health status.
  - **isDefault** (boolean): Is default.
  - **limit** (number): Limit number of returned items (1-1000)
  - **module** (string): Module.
  - **name** (string): Name.
  - **name__contains** (array): Free-text filter by site name (supports multiple values).
  - **query** (string): Full text search for fields - name, account_name, description. (Note - on single-account consoles account name will not be matched).
  - **registrationToken** (string): Registration token.
  - **siteIds** (array): List of Site IDs to filter by.
  - **siteType** (string): Site type.
  - **skip** (number): Skip first number of items (0-1000). To iterate over more than 1000 items, use "cursor".
  - **skipCount** (boolean): If true, total number of items will not be calculated, which speeds up execution time.
  - **sku** (string): Sku.
  - **sortBy** (string): The column to sort the results by.
  - **sortOrder** (string): Sort direction.
  - **state** (string): Site state.
  - **states** (array): List of states to filter
  - **totalLicenses** (number): Total licenses.
  - **updatedAt** (string): Timestamp of last update.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Server": "nginx",
      "Date": "Mon, 28 Aug 2023 10:07:53 GMT",
      "Content-Type": "application/json",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "X-RQID": "fb4ea2f2-3f64-4aa0-817d-7f77429fd646",
      "Access-Control-Allow-Origin": "https://usea1-identity.sentinelone.net",
      "Access-Control-Allow-Credentials": "true",
      "Vary": "Origin",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "X-Frame-Options": "SAMEORIGIN",
      "X-Content-Type-Options": "nosniff",
      "Content-Security-Policy": "default-src 'self' ; connect-src 'self' *.sentinelone.net cdn.pendo.io app.pendo.io *.pendo.io data.pendo.io *.scalyr.com *.storage.googleapis.com sentry.io *.sentry.io *.google-analytics.com *.gstatic.com unpkg.com cdn.auth0.com wss://*.sentinelone.net https://www.googletagmanager.com https://cdnjs.cloudflare.com data: ; script-src 'self' 'unsafe-inline' 'unsafe-eval' cdn.pendo.io app.pendo.io pendo-io-static.storage.googleapis.com cdn.pendo.io *.storage.googleapis.com data.pendo.io https://www.google-analytics.com https://www.googletagmanager.com https://unpkg.com https://cdnjs.cloudflare.com ; img-src 'self' data: https://www.google-analytics.com cdn.pendo.io app.pendo.io *.sentinelone.com *.storage.googleapis.com data.pendo.io ; style-src 'self' 'unsafe-inline' app.pendo.io cdn.pendo.io *.storage.googleapis.com https://cdnjs.cloudflare.com ; font-src 'self' data: https://cdn.auth0.com ; frame-src 'self' blob: https://receptive.io https://*.pendo.io https://pendo-io-extensions.storage.googleapis.com/ https://*.youtube.com ; frame-ancestors 'self' app.pendo.io ; object-src 'none'",
      "Cache-Control": "no-store",
      "Pragma": "no-cache",
      "Expires": "-1",
      "Content-Encoding": "gzip"
    },
    "reason": "OK",
    "json_body": {
      "data": {
        "allSites": {
          "activeLicenses": 764,
          "totalLicenses": 40
        },
        "sites": [
          {
            "accountId": "1286405255240245908",
            "accountName": "swimlane",
            "activeLicenses": 2,
            "createdAt": "2021-11-10T21:37:36.553082Z",
            "creator": "Sandeep Minhas",
            "creatorId": "1170348439571106212",
            "description": null,
            "expiration": null,
            "externalId": "33c29bd6-a9ff-3881-ad02-b80a19baa4ec",
            "healthStatus": true,
            "id": "1286405255257023125",
            "isDefault": true,
            "licenses": {
              "bundles": [
                {
                  "displayName": "Core",
                  "majorVersion": 1,
                  "minorVersion": 4,
                  "name": "core",
                  "surfaces": [
                    {
                      "count": 25,
                      "name": "Total Agents"
                    }
                  ],
                  "totalSurfaces": 25
                }
              ],
              "modules": [
                {
                  "displayName": "Ranger",
                  "majorVersion": 1,
                  "name": "ranger"
                }
              ],
              "settings": [
                {
                  "displayName": "365 Days",
                  "groupName": "malicious_data_retention",
                  "setting": "365 Days",
                  "settingGroup": "malicious_data_retention",
                  "settingGroupDisplayName": "Malicious Data Retention"
                },
                {
                  "displayName": "Available",
                  "groupName": "marketplace_access_status",
                  "setting": "Available",
                  "settingGroup": "marketplace_access_status",
                  "settingGroupDisplayName": "Marketplace Access"
                },
                {
                  "displayName": "Account",
                  "groupName": "account_level_ranger",
                  "setting": "Account",
                  "settingGroup": "account_level_ranger",
                  "settingGroupDisplayName": "Ranger Consolidation Level"
                }
              ]
            },
            "name": "Default site",
            "registrationToken": "eyJ1cmwiOiAiaHR0cHM6Ly91c2VhMS1wYXJ0bmVycy5zZW50aW5lbG9uZS5uZXQiLCAic2l0ZV9rZXkiOiAiYWI0ZWUwNGM3ZDY2ZWRlZCJ9",
            "siteType": "Paid",
            "sku": "Core",
            "state": "active",
            "suite": "Core",
            "totalLicenses": 25,
            "unlimitedExpiration": true,
            "unlimitedLicenses": false,
            "updatedAt": "2023-08-27T08:04:39.306240Z"
          },
          {
            "accountId": "1286405255240245908",
            "accountName": "swimlane",
            "activeLicenses": 0,
            "createdAt": "2023-08-24T21:24:49.803179Z",
            "creator": "Travis Riley",
            "creatorId": "1286405906565325677",
            "description": "Content Team test site",
            "expiration": null,
            "externalId": null,
            "healthStatus": true,
            "id": "1758952600032266153",
            "isDefault": false,
            "licenses": {
              "bundles": [
                {
                  "displayName": "Complete",
                  "majorVersion": 1,
                  "minorVersion": 7,
                  "name": "complete",
                  "surfaces": [
                    {
                      "count": 10,
                      "name": "Total Agents"
                    }
                  ],
                  "totalSurfaces": 10
                }
              ],
              "modules": [
                {
                  "displayName": "Remote Script Orchestration",
                  "majorVersion": 1,
                  "name": "rso"
                },
                {
                  "displayName": "STAR",
                  "majorVersion": 1,
                  "name": "star"
                }
              ],
              "settings": [
                {
                  "displayName": "Enabled",
                  "groupName": "remote_shell_availability",
                  "setting": "Enabled",
                  "settingGroup": "remote_shell_availability",
                  "settingGroupDisplayName": "Remote Shell"
                },
                {
                  "displayName": "365 Days",
                  "groupName": "malicious_data_retention",
                  "setting": "365 Days",
                  "settingGroup": "malicious_data_retention",
                  "settingGroupDisplayName": "Malicious Data Retention"
                },
                {
                  "displayName": "Available",
                  "groupName": "marketplace_access_status",
                  "setting": "Available",
                  "settingGroup": "marketplace_access_status",
                  "settingGroupDisplayName": "Marketplace Access"
                },
                {
                  "displayName": "14 Days",
                  "groupName": "dv_retention",
                  "setting": "14 Days",
                  "settingGroup": "dv_retention",
                  "settingGroupDisplayName": "Deep Visibility Data Retention"
                }
              ]
            },
            "name": "content-test-site",
            "registrationToken": "eyJ1cmwiOiAiaHR0cHM6Ly91c2VhMS1wYXJ0bmVycy5zZW50aW5lbG9uZS5uZXQiLCAic2l0ZV9rZXkiOiAiNzZmNmIwMjhlZGYwNTkyMiJ9",
            "siteType": "Trial",
            "sku": "Complete",
            "state": "active",
            "suite": "Complete",
            "totalLicenses": 10,
            "unlimitedExpiration": true,
            "unlimitedLicenses": false,
            "updatedAt": "2023-08-27T08:04:39.306240Z"
          },
          {
            "accountId": "1286405255240245908",
            "accountName": "swimlane",
            "activeLicenses": 0,
            "createdAt": "2023-08-24T21:26:37.249272Z",
            "creator": "Travis Riley",
            "creatorId": "1286405906565325677",
            "description": null,
            "expiration": null,
            "externalId": null,
            "healthStatus": true,
            "id": "1758953501354646085",
            "isDefault": false,
            "licenses": {
              "bundles": [
                {
                  "displayName": "Core",
                  "majorVersion": 1,
                  "minorVersion": 4,
                  "name": "core",
                  "surfaces": [
                    {
                      "count": 5,
                      "name": "Total Agents"
                    }
                  ],
                  "totalSurfaces": 5
                }
              ],
              "modules": [],
              "settings": [
                {
                  "displayName": "365 Days",
                  "groupName": "malicious_data_retention",
                  "setting": "365 Days",
                  "settingGroup": "malicious_data_retention",
                  "settingGroupDisplayName": "Malicious Data Retention"
                },
                {
                  "displayName": "Available",
                  "groupName": "marketplace_access_status",
                  "setting": "Available",
                  "settingGroup": "marketplace_access_status",
                  "settingGroupDisplayName": "Marketplace Access"
                }
              ]
            },
            "name": "content-second-site",
            "registrationToken": "eyJ1cmwiOiAiaHR0cHM6Ly91c2VhMS1wYXJ0bmVycy5zZW50aW5lbG9uZS5uZXQiLCAic2l0ZV9rZXkiOiAiZGJjZjE2ZDdkNDkwMTA1ZCJ9",
            "siteType": "Trial",
            "sku": "Core",
            "state": "active",
            "suite": "Core",
            "totalLicenses": 5,
            "unlimitedExpiration": true,
            "unlimitedLicenses": false,
            "updatedAt": "2023-08-27T08:04:39.306240Z"
          }
        ]
      },
      "pagination": {
        "nextCursor": null,
        "totalItems": 3
      }
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **data** (object)
    - **allSites** (object)
      - **activeLicenses** (number)
      - **totalLicenses** (number)
    - **sites** (array)
      - **accountId** (string)
      - **accountName** (string)
      - **activeLicenses** (number)
      - **createdAt** (string)
      - **creator** (string)
      - **creatorId** (string)
      - **description** (object)
      - **expiration** (object)
      - **externalId** (object)
      - **healthStatus** (boolean)
      - **id** (string)
      - **isDefault** (boolean)
      - **licenses** (object)
        - **bundles** (array)
          - **displayName** (string)
          - **majorVersion** (number)
          - **minorVersion** (number)
          - **name** (string)
          - **surfaces** (array)
            - **count** (number)
            - **name** (string)
          - **totalSurfaces** (number)
        - **modules** (array)
          - **file_name** (string) – Required
          - **file** (string) – Required
        - **settings** (array)
          - **displayName** (string)
          - **groupName** (string)
          - **setting** (string)
          - **settingGroup** (string)
          - **settingGroupDisplayName** (string)
      - **name** (string)
      - **registrationToken** (string)
      - **siteType** (string)
      - **sku** (string)
      - **state** (string)
      - **suite** (string)
      - **totalLicenses** (number)
      - **unlimitedExpiration** (boolean)
      - **unlimitedLicenses** (boolean)
      - **updatedAt** (string)
  - **pagination** (object)
    - **nextCursor** (object)
    - **totalItems** (number)
## Response Headers

| Header | Type |
|--------|------|
| Server | string |
| Date | string |
| Content-Type | string |
| Transfer-Encoding | string |
| Connection | string |
| X-RQID | string |
| Access-Control-Allow-Origin | string |
| Access-Control-Allow-Credentials | string |
| Vary | string |
| Strict-Transport-Security | string |
| X-Frame-Options | string |
| X-Content-Type-Options | string |
| Content-Security-Policy | string |
| Cache-Control | string |
| Pragma | string |
| Expires | string |
| Content-Encoding | string |