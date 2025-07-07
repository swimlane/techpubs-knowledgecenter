# Get Folders

**Description**: Retrieves a list of email folders from the specified 'email_address' using the Microsoft Graph API.

## Endpoint

- **URL:** `v1.0/users/{{email_address}}/mailFolders`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **email_address** (string) – Required: The account associated with the email
- **parameters** (object): Parameters
  - **include_hidden_folders** (boolean): Include hidden folders in the results
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
      "request-id": "2da48e9f-b869-4db1-8603-6d81205534f9",
      "client-request-id": "2da48e9f-b869-4db1-8603-6d81205534f9",
      "x-ms-ags-diagnostic": "{\"ServerInfo\":{\"DataCenter\":\"Brazil South\",\"Slice\":\"E\",\"Ring\":\"3\",\"ScaleUnit\":\"002\",\"RoleInstance\":\"CP1PEPF00002F10\"}}",
      "Date": "Fri, 04 Nov 2022 20:43:54 GMT"
    },
    "reason": "OK",
    "json_body": {
      "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#users('integrations%40swimlaneintegrations.onmicrosoft.com')/mailFolders",
      "value": [
        {
          "id": "AQMkADMxZmU3ZWQ4LTMzADRiLTRmN2QtYjNlMS1jNzA0MzhlYzM5ZDcALgAAAwdg-C5XAxZKsV7Iu-pcczMBAIElFP3_iINMukuDjlG8_QIAAAIBOwAAAA==",
          "displayName": "Archive",
          "parentFolderId": "AQMkADMxZmU3ZWQ4LTMzADRiLTRmN2QtYjNlMS1jNzA0MzhlYzM5ZDcALgAAAwdg-C5XAxZKsV7Iu-pcczMBAIElFP3_iINMukuDjlG8_QIAAAIBCAAAAA==",
          "childFolderCount": 0,
          "unreadItemCount": 1,
          "totalItemCount": 7,
          "sizeInBytes": 777420,
          "isHidden": false
        },
        {
          "id": "AQMkADMxZmU3ZWQ4LTMzADRiLTRmN2QtYjNlMS1jNzA0MzhlYzM5ZDcALgAAAwdg-C5XAxZKsV7Iu-pcczMBAIElFP3_iINMukuDjlG8_QIAAAIBNAAAAA==",
          "displayName": "Conversation History",
          "parentFolderId": "AQMkADMxZmU3ZWQ4LTMzADRiLTRmN2QtYjNlMS1jNzA0MzhlYzM5ZDcALgAAAwdg-C5XAxZKsV7Iu-pcczMBAIElFP3_iINMukuDjlG8_QIAAAIBCAAAAA==",
          "childFolderCount": 1,
          "unreadItemCount": 0,
          "totalItemCount": 0,
          "sizeInBytes": 0,
          "isHidden": false
        },
        {
          "id": "AQMkADMxZmU3ZWQ4LTMzADRiLTRmN2QtYjNlMS1jNzA0MzhlYzM5ZDcALgAAAwdg-C5XAxZKsV7Iu-pcczMBAIElFP3_iINMukuDjlG8_QIAAAIBCgAAAA==",
          "displayName": "Deleted Items",
          "parentFolderId": "AQMkADMxZmU3ZWQ4LTMzADRiLTRmN2QtYjNlMS1jNzA0MzhlYzM5ZDcALgAAAwdg-C5XAxZKsV7Iu-pcczMBAIElFP3_iINMukuDjlG8_QIAAAIBCAAAAA==",
          "childFolderCount": 0,
          "unreadItemCount": 0,
          "totalItemCount": 82,
          "sizeInBytes": 6203144,
          "isHidden": false
        },
        {
          "id": "AQMkADMxZmU3ZWQ4LTMzADRiLTRmN2QtYjNlMS1jNzA0MzhlYzM5ZDcALgAAAwdg-C5XAxZKsV7Iu-pcczMBAIElFP3_iINMukuDjlG8_QIAAAIBDwAAAA==",
          "displayName": "Drafts",
          "parentFolderId": "AQMkADMxZmU3ZWQ4LTMzADRiLTRmN2QtYjNlMS1jNzA0MzhlYzM5ZDcALgAAAwdg-C5XAxZKsV7Iu-pcczMBAIElFP3_iINMukuDjlG8_QIAAAIBCAAAAA==",
          "childFolderCount": 0,
          "unreadItemCount": 0,
          "totalItemCount": 0,
          "sizeInBytes": 0,
          "isHidden": false
        },
        {
          "id": "AQMkADMxZmU3ZWQ4LTMzADRiLTRmN2QtYjNlMS1jNzA0MzhlYzM5ZDcALgAAAwdg-C5XAxZKsV7Iu-pcczMBAIElFP3_iINMukuDjlG8_QIAAAIBDAAAAA==",
          "displayName": "Inbox",
          "parentFolderId": "AQMkADMxZmU3ZWQ4LTMzADRiLTRmN2QtYjNlMS1jNzA0MzhlYzM5ZDcALgAAAwdg-C5XAxZKsV7Iu-pcczMBAIElFP3_iINMukuDjlG8_QIAAAIBCAAAAA==",
          "childFolderCount": 1,
          "unreadItemCount": 1,
          "totalItemCount": 62,
          "sizeInBytes": 14221822,
          "isHidden": false
        },
        {
          "id": "AQMkADMxZmU3ZWQ4LTMzADRiLTRmN2QtYjNlMS1jNzA0MzhlYzM5ZDcALgAAAwdg-C5XAxZKsV7Iu-pcczMBAIElFP3_iINMukuDjlG8_QIAAAIBGQAAAA==",
          "displayName": "Junk Email",
          "parentFolderId": "AQMkADMxZmU3ZWQ4LTMzADRiLTRmN2QtYjNlMS1jNzA0MzhlYzM5ZDcALgAAAwdg-C5XAxZKsV7Iu-pcczMBAIElFP3_iINMukuDjlG8_QIAAAIBCAAAAA==",
          "childFolderCount": 0,
          "unreadItemCount": 1,
          "totalItemCount": 1,
          "sizeInBytes": 50975,
          "isHidden": false
        },
        {
          "id": "AQMkADMxZmU3ZWQ4LTMzADRiLTRmN2QtYjNlMS1jNzA0MzhlYzM5ZDcALgAAAwdg-C5XAxZKsV7Iu-pcczMBAIElFP3_iINMukuDjlG8_QIAAAIBCwAAAA==",
          "displayName": "Outbox",
          "parentFolderId": "AQMkADMxZmU3ZWQ4LTMzADRiLTRmN2QtYjNlMS1jNzA0MzhlYzM5ZDcALgAAAwdg-C5XAxZKsV7Iu-pcczMBAIElFP3_iINMukuDjlG8_QIAAAIBCAAAAA==",
          "childFolderCount": 0,
          "unreadItemCount": 0,
          "totalItemCount": 0,
          "sizeInBytes": 0,
          "isHidden": false
        },
        {
          "id": "AAMkADMxZmU3ZWQ4LTMzNGItNGY3ZC1iM2UxLWM3MDQzOGVjMzlkNwAuAAAAAAAHYPwuVwMWSrFeyLv6XHMzAQCBJRT9-oiDTLpLg45RvPkCAAGYcWU6AAA=",
          "displayName": "Quarantine",
          "parentFolderId": "AQMkADMxZmU3ZWQ4LTMzADRiLTRmN2QtYjNlMS1jNzA0MzhlYzM5ZDcALgAAAwdg-C5XAxZKsV7Iu-pcczMBAIElFP3_iINMukuDjlG8_QIAAAIBCAAAAA==",
          "childFolderCount": 0,
          "unreadItemCount": 0,
          "totalItemCount": 1,
          "sizeInBytes": 16890,
          "isHidden": false
        },
        {
          "id": "AQMkADMxZmU3ZWQ4LTMzADRiLTRmN2QtYjNlMS1jNzA0MzhlYzM5ZDcALgAAAwdg-C5XAxZKsV7Iu-pcczMBAIElFP3_iINMukuDjlG8_QIAAAIBCQAAAA==",
          "displayName": "Sent Items",
          "parentFolderId": "AQMkADMxZmU3ZWQ4LTMzADRiLTRmN2QtYjNlMS1jNzA0MzhlYzM5ZDcALgAAAwdg-C5XAxZKsV7Iu-pcczMBAIElFP3_iINMukuDjlG8_QIAAAIBCAAAAA==",
          "childFolderCount": 0,
          "unreadItemCount": 0,
          "totalItemCount": 1057,
          "sizeInBytes": 45926120,
          "isHidden": false
        },
        {
          "id": "AAMkADMxZmU3ZWQ4LTMzNGItNGY3ZC1iM2UxLWM3MDQzOGVjMzlkNwAuAAAAAAAHYPwuVwMWSrFeyLv6XHMzAQCBJRT9-oiDTLpLg45RvPkCAAAMXawJAAA=",
          "displayName": "TestFolder",
          "parentFolderId": "AQMkADMxZmU3ZWQ4LTMzADRiLTRmN2QtYjNlMS1jNzA0MzhlYzM5ZDcALgAAAwdg-C5XAxZKsV7Iu-pcczMBAIElFP3_iINMukuDjlG8_QIAAAIBCAAAAA==",
          "childFolderCount": 1,
          "unreadItemCount": 0,
          "totalItemCount": 11,
          "sizeInBytes": 578098,
          "isHidden": false
        }
      ],
      "@odata.nextLink": "https://graph.microsoft.com/v1.0/users/integrations@swimlaneintegrations.onmicrosoft.com/mailFolders?include_hidden_folders=True&%24skip=10"
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
    - **id** (string)
    - **displayName** (string)
    - **parentFolderId** (string)
    - **childFolderCount** (number)
    - **unreadItemCount** (number)
    - **totalItemCount** (number)
    - **sizeInBytes** (number)
    - **isHidden** (boolean)
  - **@odata.nextLink** (string)
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