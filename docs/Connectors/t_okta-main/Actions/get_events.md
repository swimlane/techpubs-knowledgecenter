# Get Events

**Description**: Retrieves a list of all System Log events from Okta Identity Management for monitoring or analysis.

## Endpoint

- **URL:** `/api/v1/logs`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **since** (string): Filters the lower time bound of the log events published property for bounded queries or persistence time for polling queries.
  - **until** (string): Filters the upper time bound of the log events published property for bounded queries or persistence time for polling queries.
  - **after** (string): Retrieves the next page of results. Okta returns a link in the HTTP Header (rel=next) that includes the after query parameter.
  - **filter** (string): Filter expression that filters the results. All operators except [ ] are supported.
  - **q** (string): Filters log events results by one or more case insensitive keywords. URL encoded string. Max length is 40 characters per keyword, with a maximum of 10 keyword filters per query (before encoding.
  - **limit** (number): Sets the number of results that are returned in the response. Integer between 0 and 1000.
  - **sortOrder** (string): The order of the returned events that are sorted by the published property.
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
      "actor": {
        "id": "00uttidj01jqL21aM1d6",
        "type": "User",
        "alternateId": "john.doe@example.com",
        "displayName": "John Doe",
        "detailEntry": null
      },
      "client": {
        "userAgent": {
          "rawUserAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
          "os": "Mac OS X",
          "browser": "CHROME"
        },
        "zone": null,
        "device": "Computer",
        "id": null,
        "ipAddress": "10.0.0.1",
        "geographicalContext": {
          "city": "New York",
          "state": "New York",
          "country": "United States",
          "postalCode": 10013,
          "geolocation": {
            "lat": 40.3157,
            "lon": -74.01
          }
        }
      },
      "device": {
        "id": "guofdhyjex1feOgbN1d9",
        "name": "Mac15,6",
        "os_platform": "OSX",
        "os_version": "14.6.0",
        "managed": false,
        "registered": true,
        "device_integrator": null,
        "disk_encryption_type": "ALL_INTERNAL_VOLUMES",
        "screen_lock_type": "BIOMETRIC",
        "jailbreak": null,
        "secure_hardware_present": true
      },
      "authenticationContext": {
        "authenticationProvider": null,
        "credentialProvider": null,
        "credentialType": null,
        "issuer": null,
        "interface": null,
        "authenticationStep": 0,
        "rootSessionId": "idxBager62CSveUkTxvgRtonA",
        "externalSessionId": "idxBager62CSveUkTxvgRtonA"
      },
      "displayMessage": "User login to Okta",
      "eventType": "user.session.start",
      "outcome": {
        "result": "SUCCESS",
        "reason": null
      },
      "published": "2024-08-13T15:58:20.353Z",
      "securityContext": {
        "asNumber": 394089,
        "asOrg": "ASN 0000",
        "isp": "google",
        "domain": null,
        "isProxy": false
      },
      "severity": "INFO",
      "debugContext": {
        "debugData": {
          "requestId": "ab609228fe84ce59cdcbfa690bcce016",
          "requestUri": "/idp/idx/authenticators/poll",
          "url": "/idp/idx/authenticators/poll"
        }
      },
      "legacyEventType": "core.user_auth.login_success",
      "transaction": {
        "type": "WEB",
        "id": "ab609228fe84ce59cdcbfa690bgce016",
        "detail": null
      },
      "uuid": "dc9fd3c0-598c-11ef-8478-2b7584bf8d5a",
      "version": 0,
      "request": {
        "ipChain": [
          {
            "ip": "10.0.0.1",
            "geographicalContext": {
              "city": "New York",
              "state": "New York",
              "country": "United States",
              "postalCode": 10013,
              "geolocation": {
                "lat": 40.3157,
                "lon": -74.01
              }
            },
            "version": "V4",
            "source": null
          }
        ]
      },
      "target": [
        {
          "id": "pfdfdhyjf0HMbkP2e1d7",
          "type": "AuthenticatorEnrollment",
          "alternateId": "unknown",
          "displayName": "Okta Verify",
          "detailEntry": null
        },
        {
          "id": "0oatxlef9sQvvqInq5d6",
          "type": "AppInstance",
          "alternateId": "Okta Admin Console",
          "displayName": "Okta Admin Console",
          "detailEntry": null
        }
      ]
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json** (object)
  - **actor** (object)
    - **id** (string)
    - **type** (string)
    - **alternateId** (string)
    - **displayName** (string)
    - **detailEntry** (object)
  - **client** (object)
    - **userAgent** (object)
      - **rawUserAgent** (string)
      - **os** (string)
      - **browser** (string)
    - **zone** (object)
    - **device** (string)
    - **id** (object)
    - **ipAddress** (string)
    - **geographicalContext** (object)
      - **city** (string)
      - **state** (string)
      - **country** (string)
      - **postalCode** (number)
      - **geolocation** (object)
        - **lat** (number)
        - **lon** (number)
  - **device** (object)
    - **id** (string)
    - **name** (string)
    - **os_platform** (string)
    - **os_version** (string)
    - **managed** (boolean)
    - **registered** (boolean)
    - **device_integrator** (object)
    - **disk_encryption_type** (string)
    - **screen_lock_type** (string)
    - **jailbreak** (object)
    - **secure_hardware_present** (boolean)
  - **authenticationContext** (object)
    - **authenticationProvider** (object)
    - **credentialProvider** (object)
    - **credentialType** (object)
    - **issuer** (object)
    - **interface** (object)
    - **authenticationStep** (number)
    - **rootSessionId** (string)
    - **externalSessionId** (string)
  - **displayMessage** (string)
  - **eventType** (string)
  - **outcome** (object)
    - **result** (string)
    - **reason** (object)
  - **published** (string)
  - **securityContext** (object)
    - **asNumber** (number)
    - **asOrg** (string)
    - **isp** (string)
    - **domain** (object)
    - **isProxy** (boolean)
  - **severity** (string)
  - **debugContext** (object)
    - **debugData** (object)
      - **requestId** (string)
      - **requestUri** (string)
      - **url** (string)
  - **legacyEventType** (string)
  - **transaction** (object)
    - **type** (string)
    - **id** (string)
    - **detail** (object)
  - **uuid** (string)
  - **version** (number)
  - **request** (object)
    - **ipChain** (array)
      - **ip** (string)
      - **geographicalContext** (object)
        - **city** (string)
        - **state** (string)
        - **country** (string)
        - **postalCode** (number)
        - **geolocation** (object)
          - **lat** (number)
          - **lon** (number)
      - **version** (string)
      - **source** (object)
  - **target** (array)
    - **id** (string)
    - **type** (string)
    - **alternateId** (string)
    - **displayName** (string)
    - **detailEntry** (object)
## Response Headers

| Header | Type |
|--------|------|
| content-length | string |
| content-type | string |
| Date | string |