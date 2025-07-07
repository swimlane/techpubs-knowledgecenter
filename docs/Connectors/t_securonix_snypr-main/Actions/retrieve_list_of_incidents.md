# Retrieve List of Incidents

**Description**: Retrieve List of Incidents.

## Endpoint

- **URL:** `Snypr/ws/incident/get`
- **Method:** `GET`
## Inputs

- **parameters** (object) – Required
  - **type** (string) – Required: Enter the type as list.
  - **from** (string) – Required: Enter the start time (EPOCH) in ms.
  - **to** (string) – Required: Enter the end time in ms.
  - **offset** (number): This parameter is optional and used for pagination.
  - **status** (string): Enter the status of the incident. This parameter is optional.
  - **rangeType** (string) – Required
  - **allowChildCases** (boolean): Enter true to receive the list of child cases associated with a parent case in the response. Otherwise, enter false. This parameter is optional.
  - **max** (number): Enter the maximum number of records the API will display. This is a numeral value and it is optional.
  - **sort** (string)
  - **order** (string)
  - **tenantname** (string): The name of the tenant from where the incidents will be retrieved.
- **headers** (object) – Required
  - **Accept** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "content-length": "140",
      "content-type": "application/json",
      "Date": "Mon, 19 Feb 2023 20:37:23 GMT"
    },
    "reason": "OK",
    "json_body": {
      "status": "OK",
      "result": {
        "data": {
          "totalIncidents": 3,
          "incidentItems": [
            {
              "violatorText": "Test3 AutoCase1",
              "lastUpdateDate": 1683709649498,
              "violatorId": "7",
              "incidentType": "HighRiskUsers",
              "incidentId": "21",
              "incidentStatus": "CLAIMED",
              "riskscore": 0,
              "assignedUser": "Admin Admin",
              "priority": "Medium",
              "reason": [
                "Number Of Threat: 3",
                "Threat Model: TM1",
                {
                  "Policies": [
                    "pol1_aa",
                    "pol1_rta",
                    "pol1_rga"
                  ]
                }
              ],
              "violatorSubText": "TestAutoCase3",
              "entity": "Users",
              "workflowName": "SOCTeamReview",
              "url": "https://10.150.31.110:8443/Snypr/configurableDashboards/view?&type=incident&id=21",
              "isWhitelisted": false,
              "watchlisted": false,
              "tenantInfo": {
                "tenantid": 1,
                "tenantname": "Securonix",
                "tenantshortcode": "SE"
              },
              "statusCompleted": false,
              "sandBoxPolicy": false,
              "parentCaseId": "",
              "casecreatetime": 1683700081678,
              "bulkactionallowed": true,
              "type": "HighRiskUsers",
              "solrquery": "index = violation and ((@policyname = \"pol1_aa\" and @accountname=\"TESTAUTOCASE3\") or (@policyname = \"pol1_rga\" and @accountname=\"TESTAUTOCASE3\") or (@policyname = \"pol1_rta\" and @accountname=\"TESTAUTOCASE3\")) and @tenantname=\"Securonix\" and datetime between \"11/28/2022 21:37:52\" \"12/28/2022 21:37:53\"",
              "policystarttime": 1669693072000,
              "policyendtime": 1672285073000
            }
          ]
        }
      }
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **status** (string)
  - **result** (object)
    - **data** (object)
      - **totalIncidents** (number)
      - **incidentItems** (array)
        - **violatorText** (string)
        - **lastUpdateDate** (number)
        - **violatorId** (string)
        - **incidentType** (string)
        - **incidentId** (string)
        - **incidentStatus** (string)
        - **riskscore** (number)
        - **assignedUser** (string)
        - **priority** (string)
        - **reason** (array)
        - **violatorSubText** (string)
        - **entity** (string)
        - **workflowName** (string)
        - **url** (string)
        - **isWhitelisted** (boolean)
        - **watchlisted** (boolean)
        - **tenantInfo** (object)
          - **tenantid** (number)
          - **tenantname** (string)
          - **tenantshortcode** (string)
        - **statusCompleted** (boolean)
        - **sandBoxPolicy** (boolean)
        - **parentCaseId** (string)
        - **casecreatetime** (number)
        - **bulkactionallowed** (boolean)
        - **type** (string)
        - **solrquery** (string)
        - **policystarttime** (number)
        - **policyendtime** (number)
## Response Headers

| Header | Type |
|--------|------|
| content-length | string |
| content-type | string |
| Date | string |