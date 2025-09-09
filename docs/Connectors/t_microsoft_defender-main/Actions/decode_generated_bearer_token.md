# Decode Generated Bearer Token

**Description**: Decodes a JWT token to expose the contents of Microsoft Defender bearer tokens, aiding in integration tasks.

## Endpoint

- **Method:** `GET`
## Output

### Example

```json
[
  {
    "data": {
      "aud": "00000002-0000-0000-c000-000000000000",
      "iss": "https://sts.windows.net/f5d73c4c-bb3d-421b-8bee-424916a4acca/",
      "iat": 1711522981,
      "nbf": 1711522981,
      "exp": 1711526881,
      "aio": "E2NgYNBqzq9y5r7iP+fO4k0fVva1AQA=",
      "appid": "c806de2d-6f0a-4fcf-91b9-fc285ee6da31",
      "appidacr": "1",
      "idp": "https://sts.windows.net/f5d73c4c-bb3d-421b-8bee-424916a4acca/",
      "oid": "84e31d9d-b042-4ced-8437-7c17db9ee8b4",
      "rh": "0.AS0ATDzX9T27G0KL7kJJFqSsygIAAAAAAAAAwAAAAAAAAAAtAAA.",
      "sub": "84e31d9d-b042-4ced-8437-7c17db9ee8b4",
      "tenant_region_scope": "NA",
      "tid": "f5d73c4c-bb3d-421b-8bee-424916a4acca",
      "uti": "HbP57Z85NEa5E8fETawZAA",
      "ver": "1.0"
    }
  }
]
```
### Output Parameters

- **data** (object)
  - **aud** (string)
  - **iss** (string)
  - **iat** (number)
  - **nbf** (number)
  - **exp** (number)
  - **aio** (string)
  - **appid** (string)
  - **appidacr** (string)
  - **idp** (string)
  - **oid** (string)
  - **rh** (string)
  - **sub** (string)
  - **tenant_region_scope** (string)
  - **tid** (string)
  - **uti** (string)
  - **ver** (string)