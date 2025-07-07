# List Incidents

**Description**: Retrieve all incidents from Microsoft Azure Sentinel using specified subscription ID, resource group, and workspace name.

## Endpoint

- **URL:** `/subscriptions/{{subscriptionId}}/resourceGroups/{{resourceGroupName}}/providers/Microsoft.OperationalInsights/workspaces/{{workspaceName}}/providers/Microsoft.SecurityInsights/incidents`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **subscriptionId** (string) – Required: The ID of the target subscription.
  - **resourceGroupName** (string) – Required: The name of the resource group. The name is case insensitive.
  - **workspaceName** (string) – Required: The name of the workspace. Regex pattern - ^[A-Za-z0-9][A-Za-z0-9-]+[A-Za-z0-9]$
- **parameters** (object) – Required: URL Query Parameters
  - **api-version** (string) – Required: The API version to use for this action.
  - **$filter** (string): Filter the results, based on a Boolean condition.
  - **$orderby** (string): Sort the results.
  - **$skipToken** (string): Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
  - **$top** (number): Return only the first n results.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Cache-Control": "no-cache",
      "Pragma": "no-cache",
      "Transfer-Encoding": "chunked",
      "Content-Type": "application/json; charset=utf-8",
      "Content-Encoding": "gzip",
      "Expires": "-1",
      "Vary": "Accept-Encoding",
      "Server": "Kestrel",
      "x-ms-ratelimit-remaining-subscription-reads": "11999",
      "x-ms-request-id": "b0182057-82a0-4253-aa3c-5be0c8ab9809",
      "x-ms-correlation-request-id": "b0182057-82a0-4253-aa3c-5be0c8ab9809",
      "x-ms-routing-request-id": "SOUTHINDIA:20230729T110918Z:b0182057-82a0-4253-aa3c-5be0c8ab9809",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "X-Content-Type-Options": "nosniff",
      "Date": "Sat, 29 Jul 2023 11:09:17 GMT"
    },
    "reason": "OK",
    "json_body": {
      "value": [
        {
          "id": "/subscriptions/38d4cde9-8ef2-4c61-bc61-7fa8658ab74b/resourceGroups/test/providers/Microsoft.OperationalInsights/workspaces/swimlaneazuresentinel/providers/Microsoft.SecurityInsights/Incidents/99353b3a-794c-4d8a-ac01-df3f109900ed",
          "name": "99353b3a-794c-4d8a-ac01-df3f109900ed",
          "etag": "\"09001676-0000-1100-0000-64c45d7e0000\"",
          "type": "Microsoft.SecurityInsights/Incidents",
          "properties": {
            "title": "Azure Sentinel update alert",
            "description": "update alert",
            "severity": "Medium",
            "status": "New",
            "owner": {
              "objectId": null,
              "email": null,
              "assignedTo": null,
              "userPrincipalName": null
            },
            "labels": [],
            "firstActivityTimeUtc": "2023-07-28T19:45:39.4493887Z",
            "lastActivityTimeUtc": "2023-07-28T19:50:00.684261Z",
            "lastModifiedTimeUtc": "2023-07-29T00:29:50.7425845Z",
            "createdTimeUtc": "2023-07-29T00:29:50.7425845Z",
            "incidentNumber": 17081,
            "additionalData": {
              "alertsCount": 1,
              "bookmarksCount": 0,
              "commentsCount": 0,
              "alertProductNames": [
                "Azure Sentinel"
              ],
              "tactics": []
            },
            "relatedAnalyticRuleIds": [
              "/subscriptions/38d4cde9-8ef2-4c61-bc61-7fa8658ab74b/resourceGroups/test/providers/Microsoft.OperationalInsights/workspaces/swimlaneazuresentinel/providers/Microsoft.SecurityInsights/alertRules/6134bf18-8d6a-46ff-a3f1-cdd43cafbf57"
            ],
            "incidentUrl": "https://portal.azure.com/#asset/Microsoft_Azure_Security_Insights/Incident/subscriptions/38d4cde9-8ef2-4c61-bc61-7fa8658ab74b/resourceGroups/test/providers/Microsoft.OperationalInsights/workspaces/swimlaneazuresentinel/providers/Microsoft.SecurityInsights/Incidents/99353b3a-794c-4d8a-ac01-df3f109900ed",
            "providerName": "Azure Sentinel",
            "providerIncidentId": "17081"
          }
        },
        {
          "id": "/subscriptions/38d4cde9-8ef2-4c61-bc61-7fa8658ab74b/resourceGroups/test/providers/Microsoft.OperationalInsights/workspaces/swimlaneazuresentinel/providers/Microsoft.SecurityInsights/Incidents/49b0b22c-9ba2-40e5-888f-e230f1624d75",
          "name": "49b0b22c-9ba2-40e5-888f-e230f1624d75",
          "etag": "\"09007d75-0000-1100-0000-64c45d4e0000\"",
          "type": "Microsoft.SecurityInsights/Incidents",
          "properties": {
            "title": "Sentinel Test alert",
            "description": "test alert",
            "severity": "Medium",
            "status": "New",
            "owner": {
              "objectId": null,
              "email": null,
              "assignedTo": null,
              "userPrincipalName": null
            },
            "labels": [],
            "firstActivityTimeUtc": "2023-07-28T19:45:39.4493887Z",
            "lastActivityTimeUtc": "2023-07-28T19:50:00.684261Z",
            "lastModifiedTimeUtc": "2023-07-29T00:29:02.0205176Z",
            "createdTimeUtc": "2023-07-29T00:29:02.0205176Z",
            "incidentNumber": 17080,
            "additionalData": {
              "alertsCount": 1,
              "bookmarksCount": 0,
              "commentsCount": 0,
              "alertProductNames": [
                "Azure Sentinel"
              ],
              "tactics": []
            },
            "relatedAnalyticRuleIds": [
              "/subscriptions/38d4cde9-8ef2-4c61-bc61-7fa8658ab74b/resourceGroups/test/providers/Microsoft.OperationalInsights/workspaces/swimlaneazuresentinel/providers/Microsoft.SecurityInsights/alertRules/8a0d8e78-58a9-4d66-af3a-b054778b4aa2"
            ],
            "incidentUrl": "https://portal.azure.com/#asset/Microsoft_Azure_Security_Insights/Incident/subscriptions/38d4cde9-8ef2-4c61-bc61-7fa8658ab74b/resourceGroups/test/providers/Microsoft.OperationalInsights/workspaces/swimlaneazuresentinel/providers/Microsoft.SecurityInsights/Incidents/49b0b22c-9ba2-40e5-888f-e230f1624d75",
            "providerName": "Azure Sentinel",
            "providerIncidentId": "17080"
          }
        }
      ],
      "nextLink": "https://management.azure.com/subscriptions/38d4cde9-8ef2-4c61-bc61-7fa8658ab74b/resourceGroups/test/providers/Microsoft.OperationalInsights/workspaces/swimlaneazuresentinel/providers/Microsoft.SecurityInsights/incidents?api-version=2023-02-01&$top=2&$skipToken=H4sIAAAAAAAACj1WXVMiSRD8L_rIRaAsrq4R95D9MUMDgzQ4uBMX94CeFog6rq42snH32y-rdZ0IhZ7urs7KzKrmr197P9vN9cPe6V5nFtzpf5dm8YLquZzb9eRgFQA4IP755_7s_PRw_3xmT3v86k7Hb7cnw90i2V3_YVLKC5ZLZ86rbbWLL9W5vFS7x0V17o-rXXtcnVev_NtObkN_cviM_TBfMEzwZ6dfj46ODvejLU5P9ovp9BQiPFKfK8A_528mfbwCBhwFTPz1jRgptgW6vepacIybV3HNpPvl5kvqpkHnucunN-124budm-63bve12719W2B64vTrTYfzr9shpp3LL93tBLjuDvnqOdSuO0j-81wLrMqIK4lAg-rzvYFdDaSGkU9cSwSfUDkDJLRc7yzj9Owb5wSlNfpRR4ZxGv-S6xz6kfRWOm6uhKed6L7CGwez1ZebyEVTz63uVef7uv99fKPjK51Xrj5wXUhhFGYbeZhh3KR4Ggz6gEy8Q4kVD9Q4FcYaBzzHCHEl4gdxTkXTma1eBPMcOo1pA8Ntmk_pSAmzxPu-fP7EM6z5KdEiURc930dfYcT1TjcmTPV8zdPZW-4vEUghxxXsTOMxT5ReeZjMFJTyl7if5-h8SjrmORUc47WoODY_dP0ZcVTgfEN8pIDzjO01HvPjVMbJeAkDz0U8l7bK-qgOBI4ZIUfOaX6V4kmqE1PWeMQfSXnfQ5w35N1Az4q-Ub4i_FrnucdykMjfG2PymRJng0bj3HpOKI6EsfJwpnlpHkTHc8tph0vz2On6KudB_cm9kv3uL1ej0Pyp3zljRL4iHzTWTElS_CX5pLmUr4b6win_eKP-3PyhE7Wlb0rq8_uczG8VuN-86vpd5pN6ECzHZsV8jTB-A-8Nt3ZV52f1j_qlwspKIv_EVnrTUnDy4Kh_g6H6wua81Nel4X6u_-BP-Tacz_iflBeOBfQv87uKrCWeR1EN7olK50dZf80nxUiSHzSe3aryNv7myf6gr7QGDRZ8ozjONI7LOgf1EcdJcRFHFUPGVea4Dq-q8zDzb955rdAMOpaemnHB6KENhjhdRNkVSt5GX5InXXsjQv_HgmbSvHOe5RXjV8Fb-t6QfHfz4SM6ZqWLDrROB29wAay7KbubJhLDsA8vdoRpi-_6afvYiNazkSdxF8Z-9h23yR_YOeKmaDbrk_1KHIJR9l3mq_la0mc_VmNvafs5ewOWycyy_9OFtfABkXxyQ936mbDVmt_9qjEduc71ssh9ocEB5t5KsEG467jFQNgnmlvmylZ424dN5JX7-xLoWlkPIV59R7zBRH-Xj4OlAq_cF9YbDAN8XdZmoTob9rtxrkFMX-y6Jc6RIvONIackdAdWntzx7dk1cGK9pQvopzm8Gm0hsnnBIihYojX-QhZLo3VfagP46Jc7GY9ldAFRvDD1MBmWXINvND3YmylCc5lx26tJ7XEYVwVBy0C0pNUy_3C9Wbt5sWbX0_AzemUTxcY1nU9uTCL1vm_-0b66lhXvA-uGqHIdq9ydVU_7s02-vXuMA8f9cbbiRThe5zot7RlciyG11LpYYNBRX7hkZTN0nrwGs2OgYNlyycyAlxXnbSrqGfVk_u7JCy6IRuDdmDXzxnrh_RCxpIz8Ims_3FKWiyAG36QWrpefRYP7vqeOfKJd0wMH9PTX7NPcjzE5oOFITyqIUNhrWLWoTS2kz2JiliayjorhY4_dI2mFM3ltGw-tuZY4Vn6iPPRASXxDpKM--y2dGHi5xXvvN627Jc0H6xn1sAHB-RGKiFjUyrvcCeiTS8gqcPxeFZNYMygwRGuelAf6ykbLarZSRF_AVJgQp_jHmY8068zjflXzd8R3sqE9nZtHLG5e_OWIdzmOWJLUtTwpygZlOmOB8bmrg6FAC_UtT45630Z7MEdoaHdD3LwSrPqBuAe-xvCNfqIX0ob3Ane4HusOmJtwBynoBlsZzXygpm0ppMfjIvYwivTcjg2NTAzZKeaM59sRyh5u6OxkWxepGzasK0LWZoJQiZofnsSMSmNDkflibfTE0G8UQbTi-_q7YoxL4iqpH6F-F85d4PkuL883kEiZ3Jr8T3P_tgeDhrjDnCaIlr6kta7gq_UP1ZFfBZMWvOeNPLLaS5otFa36Wnvbm956UQrWwxjryIuA9xLDaV18ZTweOJvzHyV8yT8H6yL4of62meqhdk4y6AV7ge8d7P2x97R8kOu9019792v9GXtwZA-9Oy7y4zl_v9x-vn5_y9f__vv3_yuvC8b7CgAA"
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **value** (array)
    - **id** (string)
    - **name** (string)
    - **etag** (string)
    - **type** (string)
    - **properties** (object)
      - **title** (string)
      - **description** (string)
      - **severity** (string)
      - **status** (string)
      - **owner** (object)
        - **objectId** (object)
        - **email** (object)
        - **assignedTo** (object)
        - **userPrincipalName** (object)
      - **labels** (array)
        - **file_name** (string) – Required
        - **file** (string) – Required
      - **firstActivityTimeUtc** (string)
      - **lastActivityTimeUtc** (string)
      - **lastModifiedTimeUtc** (string)
      - **createdTimeUtc** (string)
      - **incidentNumber** (number)
      - **additionalData** (object)
        - **alertsCount** (number)
        - **bookmarksCount** (number)
        - **commentsCount** (number)
        - **alertProductNames** (array)
        - **tactics** (array)
          - **file_name** (string) – Required
          - **file** (string) – Required
      - **relatedAnalyticRuleIds** (array)
      - **incidentUrl** (string)
      - **providerName** (string)
      - **providerIncidentId** (string)
  - **nextLink** (string)
## Response Headers

| Header | Type |
|--------|------|
| Cache-Control | string |
| Pragma | string |
| Transfer-Encoding | string |
| Content-Type | string |
| Content-Encoding | string |
| Expires | string |
| Vary | string |
| Server | string |
| x-ms-ratelimit-remaining-subscription-reads | string |
| x-ms-request-id | string |
| x-ms-correlation-request-id | string |
| x-ms-routing-request-id | string |
| Strict-Transport-Security | string |
| X-Content-Type-Options | string |
| Date | string |