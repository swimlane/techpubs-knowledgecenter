# Get Identity Directory Role Management List

**Description**: Retrieve a list of directory roles for identity and access management from Microsoft Graph API.

## Endpoint

- **URL:** `/v1.0/roleManagement/directory/roleDefinitions`
- **Method:** `GET`
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **value** (array)
    - **id** (string)
    - **description** (string)
    - **displayName** (string)
    - **isBuiltIn** (boolean)
    - **isEnabled** (boolean)
    - **resourceScopes** (array)
    - **templateId** (string)
    - **version** (string)
    - **rolePermissions** (array)
      - **allowedResourceActions** (array)
      - **condition** (object)
    - **inheritsPermissionsFrom@odata.context** (string)
    - **inheritsPermissionsFrom** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
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
| x-ms-resource-unit | string |
| OData-Version | string |
| Date | string |