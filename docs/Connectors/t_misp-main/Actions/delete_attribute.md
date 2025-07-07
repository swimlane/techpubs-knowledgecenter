# Delete Attribute

**Description**: Removes a specified attribute from MISP using the provided attribute ID, requiring path parameters and headers.

## Endpoint

- **URL:** `attributes/delete/{{attributeId}}`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required
  - **attributeId** (string) – Required
- **headers** (object) – Required
  - **Accept** (string) – Required
  - **Content-Type** (string) – Required
## Output

### Example

```json
[
  {
    "message": "Attribute deleted."
  }
]
```
### Output Parameters

- **message** (string)