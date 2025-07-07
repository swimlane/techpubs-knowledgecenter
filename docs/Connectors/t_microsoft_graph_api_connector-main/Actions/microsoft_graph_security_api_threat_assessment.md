# Get Threat Assessment

**Description**: Retrieve detailed insights on a specific threat by supplying an 'id' to the Microsoft Graph Security API.

## Endpoint

- **URL:** `/v1.0/informationProtection/threatAssessmentRequests/{{id}}?$expand=results`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **id** (string) – Required: Assessment ID
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **@odata.type** (string)
  - **id** (string)
  - **createdDateTime** (string)
  - **contentType** (string)
  - **expectedAssessment** (string)
  - **category** (string)
  - **status** (string)
  - **requestSource** (string)
  - **recipientEmail** (string)
  - **destinationRoutingReason** (string)
  - **contentData** (string)
  - **createdBy** (object)
    - **user** (object)
      - **id** (string)
      - **displayName** (string)
  - **results@odata.context** (string)
  - **results** (array)
    - **id** (string)
    - **createdDateTime** (string)
    - **resultType** (string)
    - **message** (string)
## Response Headers

| Header | Type |
|--------|------|
| Cache-Control | string |
| Transfer-Encoding | string |
| Content-Type | string |
| Content-Encoding | string |
| Vary | string |
| Strict-Transport-Security | string |
| request-id | string |
| client-request-id | string |
| x-ms-ags-diagnostic | string |
| OData-Version | string |
| Date | string |