# Import Indicators

**Description**: Submits or updates a batch of indicators to Microsoft Defender using the specified JSON body format.

## Endpoint

- **URL:** `api/indicators/import`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required
  - **Indicators** (array)
    - **indicatorValue** (string): The Value of the Indicator entity.
    - **indicatorType** (string): The Type of the Indicator entity.
    - **action** (string): The action that is taken if the indicator is discovered in the organization.
    - **application** (string): The application associated with the indicator.
    - **source** (string): The source of the indicator.
    - **expirationTime** (string): The expiration time of the indicator.
    - **sourceType** (string): User in case the Indicator created by a user (for example, from the portal), AadApp in case it submitted using automated application via the API.
    - **severity** (string): The severity of the indicator. The severity of the indicator. Possible values are - Informational, Low, Medium, and High.
    - **title** (string): The title of the indicator.
    - **description** (string): The description of the indicator.
    - **recommendedActions** (string): The recommended actions for the indicator.
    - **rbacGroupNames** (array): RBAC device group names where the indicator is exposed and active. Empty list in case it exposed to all devices.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "OK",
    "json_body": {
      "value": [
        {
          "id": "2841",
          "indicator": "220e7d15b011d7fac48f2bd61114db1022197f7f",
          "isFailed": false,
          "failureReason": null
        },
        {
          "id": "2842",
          "indicator": "2233223322332233223322332233223322332233223322332233223322332222",
          "isFailed": false,
          "failureReason": null
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
  - **value** (array)
    - **id** (string)
    - **indicator** (string)
    - **isFailed** (boolean)
    - **failureReason** (object)