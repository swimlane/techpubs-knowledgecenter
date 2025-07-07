# Post Threat Assessment File

**Description**: Submit a file for security threat assessment to Microsoft Graph API, ensuring the necessary attachment is included in the JSON body.

## Endpoint

- **URL:** `/v1.0/informationProtection/threatAssessmentRequests`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required: JSON Body
  - **attachments** (array) – Required
    - **contentData** (string)
    - **fileName** (string)
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