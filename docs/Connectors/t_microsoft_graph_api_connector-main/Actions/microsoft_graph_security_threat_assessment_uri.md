# Post Threat Assessment URI

**Description**: Submits a URI for threat assessment to Microsoft Graph API, requiring 'messageUri' and 'recipientEmail' in the request.

## Endpoint

- **URL:** `/v1.0/informationProtection/threatAssessmentRequests`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required: JSON Body
  - **messageUri** (string) – Required: The resource URI of the mail message for assessment
  - **recipientEmail** (string) – Required: The mail recipient whose policies are used to assess the mail
  - **expectedAssessment** (string): The expected assessment from the ubmitter. Possible values are `block`, `unblock`
  - **category** (string): The threat category. Possible values are `spam`, `phishing`, `malware`
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **error** (object)
    - **code** (string)
    - **message** (string)
    - **innerError** (object)
      - **date** (string)
      - **request-id** (string)
      - **client-request-id** (string)
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
| Date | string |