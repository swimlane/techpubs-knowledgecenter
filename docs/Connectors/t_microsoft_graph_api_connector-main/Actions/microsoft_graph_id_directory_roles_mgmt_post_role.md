# Create Identity Directory Role Management

**Description**: Creates a new directory role in Microsoft Graph API with specified display name, status, and permissions.

## Endpoint

- **URL:** `/v1.0/roleManagement/directory/roleDefinitions`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required: JSON Body
  - **displayName** (string) – Required: The display name for the role definition
  - **isEnabled** (boolean) – Required: Flag indicating if the role is enabled for assignment. If `false`, the role is not available for assignment
  - **rolePermissions** (array) – Required: List of permissions included in the role
    - **allowedResourceActions** (array): Set of tasks that can be performed on a resource
    - **condition** (string): Optional constraints that must be met for the permission to be effective
    - **excludedResourceActions** (array): Set of tasks that may not be performed on a resource
  - **description** (string): The description for the unifiedRoleDefinition
  - **id** (string): The unique identifier for the role definition. Key, not nullable, Read-only. Inherited from entity
  - **isBuiltIn** (boolean): Flag indicating whether the role definition is part of the default set included in Azure Active Directory (Azure AD) or a custom definition
  - **resourceScopes** (array): List of the scopes or permissions the role definition applies to
  - **templateId** (string): Custom template identifier that can be set when isBuiltIn is false but is read-only when isBuiltIn is true. This identifier is typically used if one needs an identifier to be the same across different directories
  - **version** (string): Indicates version of the role definition
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
| x-ms-resource-unit | string |
| Date | string |