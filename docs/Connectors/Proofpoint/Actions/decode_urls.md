# Decode Urls

**Description**: Reverts ProofPoint TAP-rewritten URLs back to their original form, requiring a list of URLs in the JSON body.

## Endpoint

- **URL:** `/v2/url/decode`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required: Auto-generated description for `json_body`. Please update manually if needed.
  - **urls** (array) – Required: Auto-generated description for `urls`. Please update manually if needed.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Fri, 13 Oct 2023 09:06:25 GMT",
      "Content-Type": "application/json",
      "Content-Length": "853",
      "Connection": "keep-alive",
      "Vary": "Accept-Encoding",
      "X-Content-Type-Options": "nosniff",
      "Strict-Transport-Security": "max-age=15724800; includeSubDomains"
    },
    "reason": "OK",
    "json_body": {
      "urls": [
        {
          "encodedUrl": "https://urldefense.proofpoint.com/v2/url u=http-3A__links.mkt3337.com_ctt-3Fkn-3D3-26ms-3DMzQ3OTg3MDQS1-26r-3DMzkxNzk3NDkwMDA0S0-26b-3D0-26j-3DMTMwMjA1ODYzNQS2-26mt-3D1-26rt-3D0&d=DwMFaQ&c=Vxt5e0Osvvt2gflwSlsJ5DmPGcPvTRKLJyp031rXjhg&r=MujLDFBJstxoxZI_GKbsW7wxGM7nnIK__qZvVy6j9Wc&m=QJGhloAyfD0UZ6n8r6y9dF-khNKqvRAIWDRU_K65xPI&s=ew-rOtBFjiX1Hgv71XQJ5BEgl9TPaoWRm_Xp9Nuo8bk&e=",
          "success": false
        },
        {
          "encodedUrl": "https://urldefense.proofpoint.com/v1/url?u=http://www.bouncycastle.org/&amp;k=oIvRg1%2BdGAgOoM1BIlLLqw%3D%3D%0A&amp;r=IKM5u8%2B%2F%2Fi8EBhWOS%2BqGbTqCC%2BrMqWI%2FVfEAEsQO%2F0Y%3D%0A&amp;m=Ww6iaHO73mDQpPQwOwfLfN8WMapqHyvtu8jM8SjqmVQ%3D%0A&amp;s=d3583cfa53dade97025bc6274c6c8951dc29fe0f38830cf8e5a447723b9f1c9a",
          "decodedUrl": "http://www.bouncycastle.org/",
          "success": true
        }
      ]
    }
  }
]
```
### Output Parameters

- **status_code** (number): Auto-generated description for `status_code`. Please update manually if needed.
- **reason** (string): Auto-generated description for `reason`. Please update manually if needed.
- **json_body** (object): Auto-generated description for `json_body`. Please update manually if needed.
  - **urls** (array): Auto-generated description for `urls`. Please update manually if needed.
    - **encodedUrl** (string): Auto-generated description for `encodedUrl`. Please update manually if needed.
    - **success** (boolean): Auto-generated description for `success`. Please update manually if needed.
    - **decodedUrl** (string): Auto-generated description for `decodedUrl`. Please update manually if needed.
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Date | string | Auto-generated description for `Date`. Please update manually if needed. |
| Content-Type | string | Auto-generated description for `Content-Type`. Please update manually if needed. |
| Content-Length | string | Auto-generated description for `Content-Length`. Please update manually if needed. |
| Connection | string | Auto-generated description for `Connection`. Please update manually if needed. |
| Vary | string | Auto-generated description for `Vary`. Please update manually if needed. |
| X-Content-Type-Options | string | Auto-generated description for `X-Content-Type-Options`. Please update manually if needed. |
| Strict-Transport-Security | string | Auto-generated description for `Strict-Transport-Security`. Please update manually if needed. |