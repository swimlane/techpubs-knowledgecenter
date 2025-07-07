# Create Security Action

**Description**: Initiates a new security action in Microsoft Graph API with details like name, reason, vendor information, and parameters.

## Endpoint

- **URL:** `/beta/security/securityActions`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required: JSON Body
  - **name** (string) – Required: Action Name
  - **actionReason** (string) – Required: Action Reason
  - **vendorInformation** (object) – Required: Vendor Information
    - **vendor** (string) – Required: Vendor
    - **provider** (string) – Required: Provider
  - **parameters** (array) – Required: Collection of parameters (key-value pairs) necessary to invoke the action, for example, URL or fileHash to block).
    - **name** (string) – Required
    - **value** (string) – Required
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