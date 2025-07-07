# Get List of Attribute Types

**Description**: Retrieves a list of available attribute types from MISP, with authentication headers required.

## Endpoint

- **URL:** `attributes/describeTypes`
- **Method:** `GET`
## Inputs

- **headers** (object) – Required
  - **Accept** (string) – Required
  - **Content-Type** (string) – Required
## Output

### Example

```json
[
  {
    "sane_defaults": {
      "md5": {
        "default_category": "Payload delivery",
        "to_ids": 1
      },
      "pdb": {
        "default_category": "Artifacts dropped",
        "to_ids": 0
      }
    },
    "types": [
      "md5"
    ],
    "categories": [
      "Internal reference"
    ],
    "category_type_mappings": {
      "Internal reference": [
        "text",
        "link",
        "comment",
        "other"
      ],
      "Antivirus detection": [
        "link",
        "comment",
        "text",
        "hex",
        "other"
      ]
    }
  }
]
```
### Output Parameters

- **sane_defaults** (object)
  - **md5** (object)
    - **default_category** (string)
    - **to_ids** (number)
  - **pdb** (object)
    - **default_category** (string)
    - **to_ids** (number)
- **types** (array)
- **categories** (array)
- **category_type_mappings** (object)
  - **Internal reference** (array)
  - **Antivirus detection** (array)