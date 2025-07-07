# Post Threat Assessment URL

**Description**: Initiates a security threat assessment on a specified URL via Microsoft Graph API to identify potential risks. Requires a 'url' in the JSON body.

## Endpoint

- **URL:** `/v1.0/informationProtection/threatAssessmentRequests`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required: JSON Body
  - **url** (string) – Required: The URL string
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