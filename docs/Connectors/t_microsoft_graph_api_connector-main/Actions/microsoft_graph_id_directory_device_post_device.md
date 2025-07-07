# Create Identity Directory Device

**Description**: Registers a new device in the Microsoft Graph API directory, specifying account status, display name, OS, and version.

## Endpoint

- **URL:** `/v1.0/devices`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required: JSON Body
  - **accountEnabled** (boolean) – Required: true if the account is enabled; otherwise, false. Required. Default is true
  - **alternativeSecurityIds** (array): Alternative Security IDs
    - **type** (number)
    - **identityProvider** (string)
    - **key** (string)
  - **displayName** (string) – Required: The display name for the device
  - **operatingSystem** (string) – Required: The type of operating system on the device
  - **operatingSystemVersion** (string) – Required: The version of the operating system on the device
  - **approximateLastSignInDateTime** (string): The timestamp type represents date and time information using ISO 8601 format and is always in UTC time
  - **complianceExpirationDateTime** (string): The timestamp type represents date and time information using ISO 8601 format and is always in UTC time
  - **deviceId** (string) – Required
  - **extensionAttributes** (object): Contains extension attributes 1-15 for the device. The individual extension attributes are not selectable. These properties are mastered in cloud and can be set during creation or update of a device object in Azure AD
    - **extensionAttribute1** (string)
    - **extensionAttribute2** (string)
    - **extensionAttribute3** (string)
    - **extensionAttribute4** (string)
    - **extensionAttribute5** (string)
    - **extensionAttribute6** (string)
    - **extensionAttribute7** (string)
    - **extensionAttribute8** (string)
    - **extensionAttribute9** (string)
    - **extensionAttribute10** (string)
    - **extensionAttribute11** (string)
    - **extensionAttribute12** (string)
    - **extensionAttribute13** (string)
    - **extensionAttribute14** (string)
    - **extensionAttribute15** (string)
  - **isCompliant** (boolean)
  - **isManaged** (boolean)
  - **onPremisesLastSyncDateTime** (string): The last time at which the object was synced with the on-premises directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time
  - **onPremisesSyncEnabled** (boolean): true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced
  - **profileType** (string): The profile type of the device. Possible values are `RegisteredDevice` (default), `SecureVM`, `Printer`, `Shared`, `IoT`
  - **systemLabels** (array): List of labels applied to the device by the system
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