# Get Policy Matches

**Description**: Retrieve detailed policy violation information for a given incident ID in Symantec DLP.

## Endpoint

- **URL:** `/ProtectManager/webservices/v2/incidents/{{id}}/policymatches`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **id** (number) – Required: The incident ID.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "OK",
    "json_body": {
      "violatedRules": [
        {
          "ruleName": "symantec",
          "ruleTypeI18nKey": "KEYWORD.name",
          "matches": 3
        }
      ],
      "policyName": "symantec",
      "otherPoliciesViolated": [
        {
          "POLICYID": 28476,
          "INCIDENTID": 2147525031,
          "POLICYNAME": "BlockBATNewDLPKeywords",
          "PREVENTORPROTECTSTATUSID": 0
        },
        {
          "POLICYID": 28314,
          "INCIDENTID": 2147525029,
          "POLICYNAME": "EP-Block",
          "PREVENTORPROTECTSTATUSID": 0
        },
        {
          "POLICYID": 28355,
          "INCIDENTID": 2147525030,
          "POLICYNAME": "Qurantine-edar-policy",
          "PREVENTORPROTECTSTATUSID": 0
        },
        {
          "POLICYID": 27991,
          "INCIDENTID": 2147525032,
          "POLICYNAME": "secret policy",
          "PREVENTORPROTECTSTATUSID": 0
        }
      ],
      "matches": 3
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **violatedRules** (array)
    - **ruleName** (string)
    - **ruleTypeI18nKey** (string)
    - **matches** (number)
  - **policyName** (string)
  - **otherPoliciesViolated** (array)
    - **POLICYID** (number)
    - **INCIDENTID** (number)
    - **POLICYNAME** (string)
    - **PREVENTORPROTECTSTATUSID** (number)
  - **matches** (number)