# Delete Directory Administrative Unit Member

**Description**: Removes a member from a specified Directory Administrative Unit in Microsoft Graph API using 'id' and 'memberId'.

## Endpoint

- **URL:** `/v1.0/directory/administrativeUnits/{{id}}/members/{{memberId}}/$ref`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **id** (string) – Required: Unit ID
  - **memberId** (string) – Required: Member ID
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **response_text** (string)
## Response Headers

| Header | Type |
|--------|------|
| Cache-Control | string |
| Strict-Transport-Security | string |
| request-id | string |
| client-request-id | string |
| x-ms-ags-diagnostic | string |
| x-ms-resource-unit | string |
| Date | string |