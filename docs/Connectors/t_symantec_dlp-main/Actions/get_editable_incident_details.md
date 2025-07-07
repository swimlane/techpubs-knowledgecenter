# Get Editable Incident Details

**Description**: Retrieve editable attributes of a specified incident in Symantec DLP, including user permissions verification.

## Endpoint

- **URL:** `/ProtectManager/webservices/v2/incidents/{{id}}/history`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **id** (number) – Required: The incident ID.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "OK",
    "json_body": {
      "incidentId": 1,
      "infoMap": {
        "preventOrProtectStatusId": 0,
        "incidentStatusName": "incident.status.New",
        "isHidingNotAllowed": false,
        "severityId": 1,
        "incidentStatusId": 1,
        "isHidden": false
      },
      "customAttributeGroups": [
        {
          "name": "custom_attribute_group.default",
          "customAttributes": [
            {
              "name": "custom-attr-1",
              "index": 1,
              "displayOrder": 1,
              "email": false
            },
            {
              "name": "custom-attr-4",
              "index": 3,
              "displayOrder": 2,
              "email": false
            },
            {
              "name": "Manager",
              "index": 2,
              "displayOrder": 3,
              "email": false
            }
          ],
          "nameInternationalized": true
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
  - **incidentId** (number)
  - **infoMap** (object)
    - **preventOrProtectStatusId** (number)
    - **incidentStatusName** (string)
    - **isHidingNotAllowed** (boolean)
    - **severityId** (number)
    - **incidentStatusId** (number)
    - **isHidden** (boolean)
  - **customAttributeGroups** (array)
    - **name** (string)
    - **customAttributes** (array)
      - **name** (string)
      - **index** (number)
      - **displayOrder** (number)
      - **email** (boolean)
    - **nameInternationalized** (boolean)