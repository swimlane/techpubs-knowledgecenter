# Update Security Event Status

**Description**: Updates the status of a specified security event in CyberArk to open or closed, using the provided securityEventId.

## Endpoint

- **URL:** `/PasswordVault/API/pta/API/Events/{{securityEventId}}`
- **Method:** `PATCH`
## Inputs

- **path_parameters** (object) – Required
  - **securityEventId** (string) – Required: Security event id.
- **json_body** (object)
  - **mStatus** (string): The new status of the event.
  - **closeReason** (string): The close reason for the security event after you have investigated and handled the event successfully or determined to close it for other reasons.
  - **reasonText** (string): Free text for the user to elaborate on the close reason. Limited to 100 characters.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "Success",
    "json_body": {
      "id": "444445e56bbb0b0a063f4444",
      "type": "PSMSuspiciousActivity",
      "score": 70,
      "createTime": 1586134861000,
      "lastUpdateTime": 1586134861000,
      "audits": [
        {
          "id": "5e3045e56bbb0b0a063fbbbb",
          "type": "PSM_SSH_COMMAND",
          "sensorType": "VAULT",
          "action": "PSM Command",
          "psmCommand": "bla",
          "createTime": 1586134861000,
          "vaultUser": "vuser",
          "account": {
            "accountAsStr": "hi2@example.cyber-ark.co.il",
            "type": "LOCAL_UNIX",
            "account": {
              "mTarget": {
                "mOriginalAddress": "10.1.8.182",
                "mResolvedAddress": {
                  "mOriginalAddress": "10.1.8.182",
                  "mAddress": "10.1.8.182",
                  "mHostName": "cyber",
                  "mFqdn": "example.cyber-ark.co.il"
                }
              },
              "mUser": "hi2"
            }
          },
          "source": {
            "mOriginalAddress": "1.1.1.1"
          },
          "target": {
            "mOriginalAddress": "10.1.8.182",
            "mResolvedAddress": {
              "mOriginalAddress": "10.1.8.182",
              "mAddress": "10.1.8.182",
              "mHostName": "cyber",
              "mFqdn": "example.cyber-ark.co.il"
            }
          },
          "cloudData": {}
        }
      ],
      "additionalData": {
        "matchPatterns": "kill(.*)"
      },
      "mStatus": "CLOSED",
      "closeReason": "HANDLED",
      "reasonText": "Handled by SOC team"
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **id** (string)
  - **type** (string)
  - **score** (number)
  - **createTime** (number)
  - **lastUpdateTime** (number)
  - **audits** (array)
    - **id** (string)
    - **type** (string)
    - **sensorType** (string)
    - **action** (string)
    - **psmCommand** (string)
    - **createTime** (number)
    - **vaultUser** (string)
    - **account** (object)
      - **accountAsStr** (string)
      - **type** (string)
      - **account** (object)
        - **mTarget** (object)
          - **mOriginalAddress** (string)
          - **mResolvedAddress** (object)
            - **mOriginalAddress** (string)
            - **mAddress** (string)
            - **mHostName** (string)
            - **mFqdn** (string)
        - **mUser** (string)
    - **source** (object)
      - **mOriginalAddress** (string)
    - **target** (object)
      - **mOriginalAddress** (string)
      - **mResolvedAddress** (object)
        - **mOriginalAddress** (string)
        - **mAddress** (string)
        - **mHostName** (string)
        - **mFqdn** (string)
    - **cloudData** (object)
  - **additionalData** (object)
    - **matchPatterns** (string)
  - **mStatus** (string)
  - **closeReason** (string)
  - **reasonText** (string)