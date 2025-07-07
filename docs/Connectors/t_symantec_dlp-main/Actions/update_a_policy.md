# Update a Policy

**Description**: Enable or disable a specific Symantec DLP policy by using the provided policy ID. Required inputs include 'policyId' and 'enable'.

## Endpoint

- **URL:** `/ProtectManager/webservices/v2/policy/{{policyId}}`
- **Method:** `PUT`
## Inputs

- **path_parameters** (object) – Required
  - **policyId** (number) – Required: The Policy ID.
- **json_body** (object) – Required
  - **enable** (boolean) – Required: Set true when you want to activate the policy, set false when you want to deactivate the policy.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "OK",
    "json_body": "Policy is updated successfully."
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (string)