# Get Email Attachments

**Description**: Retrieve all attachments from a specified email in Microsoft Graph API using the provided email address and email ID.

## Endpoint

- **URL:** `/v1.0/users/{{email_address}}/messages/{{email_id}}/attachments`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **email_address** (string) – Required: The account associated with the email
  - **email_id** (string) – Required: The ID of the email to retrieve attachments from
- **parameters** (object)
  - **$expand** (string): To get the properties of an item attachment (contact, event, or message).
- **remove_content_bytes** (boolean): The account associated with the email
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Cache-Control": "private",
      "Transfer-Encoding": "chunked",
      "Content-Type": "application/json; odata.metadata=minimal; odata.streaming=true; IEEE754Compatible=false; charset=utf-8",
      "Content-Encoding": "gzip",
      "Vary": "Accept-Encoding",
      "Strict-Transport-Security": "max-age=31536000",
      "request-id": "d11c96e4-5b4d-4a7f-92ce-8d9cf5684d80",
      "client-request-id": "d11c96e4-5b4d-4a7f-92ce-8d9cf5684d80",
      "x-ms-ags-diagnostic": "{\"ServerInfo\":{\"DataCenter\":\"Central US\",\"Slice\":\"E\",\"Ring\":\"2\",\"ScaleUnit\":\"001\",\"RoleInstance\":\"DS2PEPF00001339\"}}",
      "Date": "Tue, 08 Nov 2022 01:06:18 GMT"
    },
    "reason": "OK",
    "json_body": {
      "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#users('integrations%40swimlaneintegrations.onmicrosoft.com')/messages('AAMkADMxZmU3ZWQ4LTMzNGItNGY3ZC1iM2UxLWM3MDQzOGVjMzlkNwBGAAAAAAAHYPwuVwMWSrFeyLv6XHMzBwCBJRT9-oiDTLpLg45RvPkCAAAAAAEJAACBJRT9-oiDTLpLg45RvPkCAAEzLdDCAAA%3D')/attachments",
      "value": [
        {
          "@odata.type": "#microsoft.graph.fileAttachment",
          "@odata.mediaContentType": "image/png",
          "id": "AAMkADMxZmU3ZWQ4LTMzNGItNGY3ZC1iM2UxLWM3MDQzOGVjMzlkNwBGAAAAAAAHYPwuVwMWSrFeyLv6XHMzBwCBJRT9-oiDTLpLg45RvPkCAAAAAAEJAACBJRT9-oiDTLpLg45RvPkCAAEzLdDCAAABEgAQAH0jgrUmhqdEq-kVrgjt3SU=",
          "lastModifiedDateTime": "2022-05-11T04:55:25Z",
          "name": "test_file.png",
          "contentType": "image/png",
          "size": 1569,
          "isInline": false,
          "contentId": null,
          "contentLocation": null
        }
      ]
    },
    "attachments": [
      [
        {
          "file_name": "test_file.png",
          "file": "d9196813-5631-4bbd-a1e3-6bf30cb1cd0b"
        }
      ]
    ]
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
    - **@odata.mediaContentType** (string)
    - **id** (string)
    - **lastModifiedDateTime** (string)
    - **name** (string)
    - **contentType** (string)
    - **size** (number)
    - **isInline** (boolean)
    - **contentId** (object)
    - **contentLocation** (object)
- **attachments** (array)
  - **0** (object)
    - **file_name** (string)
    - **file** (string)
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