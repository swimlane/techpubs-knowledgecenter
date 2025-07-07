# List a Users Direct Membership

**Description**: Retrieve a user's direct group memberships, directory roles, and administrative units in Microsoft Graph API using their email address.

## Endpoint

- **URL:** `/v1.0/users/{{email_address}}/memberOf`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **email_address** (string) – Required: The account associated with the email.
- **parameters** (object)
  - **$filter** (string): Filters results (rows).
  - **$count** (string): Include count of items.
  - **$search** (string): Search items by search phrases.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Cache-Control": "no-cache",
      "Transfer-Encoding": "chunked",
      "Content-Type": "application/json;odata.metadata=minimal;odata.streaming=true;IEEE754Compatible=false;charset=utf-8",
      "Content-Encoding": "gzip",
      "Vary": "Accept-Encoding",
      "Strict-Transport-Security": "max-age=31536000",
      "request-id": "fffdaaac-17ba-4eb6-8fac-779da55a44b3",
      "client-request-id": "fffdaaac-17ba-4eb6-8fac-779da55a44b3",
      "x-ms-ags-diagnostic": "{\"ServerInfo\":{\"DataCenter\":\"Central India\",\"Slice\":\"E\",\"Ring\":\"3\",\"ScaleUnit\":\"000\",\"RoleInstance\":\"PN1PEPF00007039\"}}",
      "x-ms-resource-unit": "2",
      "OData-Version": "4.0",
      "Date": "Thu, 16 Jan 2025 06:48:40 GMT"
    },
    "reason": "OK",
    "json_body": {
      "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#directoryObjects",
      "value": [
        {
          "@odata.type": "#microsoft.graph.directoryRole",
          "id": "4c04548e-9bc4-45fb-8738-168610ddbe0c",
          "deletedDateTime": null,
          "description": "Can manage all aspects of Azure AD and Microsoft services that use Azure AD identities.",
          "displayName": "Global Administrator",
          "roleTemplateId": "62e90394-69f5-4237-9190-012177145e10"
        },
        {
          "@odata.type": "#microsoft.graph.directoryRole",
          "id": "417c2fd9-6d31-4d37-927f-a6e54d37a4a4",
          "deletedDateTime": null,
          "description": "Can perform common billing related tasks like updating payment information.",
          "displayName": "Billing Administrator",
          "roleTemplateId": "b0f54661-2d74-4c50-afa3-1ec803f12efe"
        },
        {
          "@odata.type": "#microsoft.graph.administrativeUnit",
          "id": "244f1027-d748-411c-8813-da2e987c5226",
          "deletedDateTime": null,
          "displayName": "Integration Testing second unit",
          "description": null,
          "isMemberManagementRestricted": false,
          "membershipRule": null,
          "membershipType": null,
          "membershipRuleProcessingState": null,
          "visibility": null
        },
        {
          "@odata.type": "#microsoft.graph.directoryRole",
          "id": "80f18745-7890-4f24-9637-f227e5148d6d",
          "deletedDateTime": null,
          "description": "Can manage all aspects of users and groups, including resetting passwords for limited admins.",
          "displayName": "User Administrator",
          "roleTemplateId": "fe930be7-5e62-47db-91af-98c3a49a38b1"
        },
        {
          "@odata.type": "#microsoft.graph.directoryRole",
          "id": "b8d0b017-384c-40cb-b37b-99ee5d3f8a8f",
          "deletedDateTime": null,
          "description": "Can manage all aspects of the Exchange product.",
          "displayName": "Exchange Administrator",
          "roleTemplateId": "29232cdf-9323-42fd-ade2-1d097af3e4de"
        }
      ]
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **value** (array)
    - **@odata.type** (string)
    - **id** (string)
    - **deletedDateTime** (object)
    - **description** (string)
    - **displayName** (string)
    - **roleTemplateId** (string)
    - **isMemberManagementRestricted** (boolean)
    - **membershipRule** (object)
    - **membershipType** (object)
    - **membershipRuleProcessingState** (object)
    - **visibility** (object)
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