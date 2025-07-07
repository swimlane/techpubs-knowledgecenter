# Get Security Events

**Description**: Retrieve all Privileged Threat Analytics (PTA) security events from CyberArk to monitor and analyze threats.

## Endpoint

- **URL:** `/PasswordVault/API/pta/API/Events/`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **fromUpdateDate** (number): The starting date to get the security events from (calculated by the number of seconds since 1970)
  - **status** (string): The status of the security event (open or closed).
  - **accountID** (string): The unique account identifier of the account that is referred to in the Security Event.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "Success",
    "json_body": [
      {
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
        "mStatus": "OPEN"
      },
      {
        "id": "555545e56aaa0b0a063ff555",
        "type": "PSMSuspiciousActivity",
        "score": 70,
        "createTime": 1586134862000,
        "lastUpdateTime": 1586134862000,
        "audits": [
          {
            "id": "5e3045e56bbb0b0a063faaaa",
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
            "cloudData": {},
            "accountId": "id_1"
          }
        ],
        "additionalData": {
          "matchPatterns": "kill(.*)"
        },
        "mStatus": "CLOSED",
        "closeReason": "HANDLED",
        "reasonText": "Handled by SOC team"
      }
    ]
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (array)
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
    - **accountId** (string)
  - **additionalData** (object)
    - **matchPatterns** (string)
  - **mStatus** (string)
  - **closeReason** (string)
  - **reasonText** (string)