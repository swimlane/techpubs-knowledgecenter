# Get Scan Details

**Description**: Gets the detail of a scan.

## Endpoint

- **URL:** `/api/1.0/scans/detail/{{id}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Thu, 28 Mar 2024 06:35:55 GMT",
      "Content-Type": "application/json; charset=utf-8",
      "Content-Length": "3475",
      "Connection": "keep-alive",
      "Cache-Control": "no-cache",
      "Pragma": "no-cache",
      "Expires": "-1",
      "X-Content-Type-Options": "nosniff",
      "X-Frame-Options": "DENY",
      "Referrer-Policy": "no-referrer",
      "X-XSS-Protection": "1; mode=block",
      "Origin-Trial": "Au1hLO38HdoU0c5ahko3BUGr8p9Kt881bvrcCP4vESne1HV+B1XX/MZhfZNP/TWW4+BPBlKO9h3fokvWCxZdsQAAAABieyJvcmlnaW4iOiJodHRwczovL3d3dy5uZXRzcGFya2VyY2xvdWQuY29tOjQ0MyIsImZlYXR1cmUiOiJVMkZTZWN1cml0eUtleUFQSSIsImV4cGlyeSI6MTY1ODg3OTk5OX0=",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains; preload",
      "Expect-CT": "max-age=30,report-uri=\"https://www.netsparkercloud.com/report-ct/\""
    },
    "reason": "OK",
    "json_body": {
      "AdditionalWebsites": null,
      "AgentId": "13dfd27f-2d54-4db9-d2ff-b13901187ca9",
      "AgentName": "i-0492384b150671939",
      "Cookies": null,
      "CrawlAndAttack": true,
      "DeletedOn": null,
      "EnableHeuristicChecksInCustomUrlRewrite": true,
      "ExcludedLinks": "[\"gtm\\\\.js\",\"WebResource\\\\.axd\",\"ScriptResource\\\\.axd\"]",
      "ExcludeLinks": true,
      "DisallowedHttpMethods": "[]",
      "FindAndFollowNewLinks": true,
      "ImportedLinks": null,
      "AllImportedLinks": "",
      "DesktopScanId": null,
      "InitiatedTime": "22/03/2024 01:56 PM",
      "InitiatedDate": "22/03/2024",
      "InitiatedAt": "2024-03-22T19:56:21.4427686+00:00",
      "MaxDynamicSignatures": 60,
      "MaxScanDuration": 48,
      "Duration": "00:23:46.6821882",
      "PolicyDescription": "Performs recommended security checks",
      "PolicyId": "b2018666-2a01-e411-976c-0a45dbb897e8",
      "PolicyUserId": "3f2e0a60-a5ec-e311-80bc-000c29e428b5",
      "PolicyIsDefault": true,
      "PolicyIsShared": true,
      "PolicyName": "Default Security Checks",
      "AuthenticationProfileId": null,
      "AuthenticationProfileOption": "DontUse",
      "ReportPolicyDescription": "Default report policy.",
      "ReportPolicyId": "013660af-56b7-4176-85be-cf2b84966816",
      "ReportPolicyUserId": "3f2e0a60-a5ec-e311-80bc-000c29e428b5",
      "ReportPolicyIsDefault": true,
      "ReportPolicyIsShared": true,
      "ReportPolicyName": "Default Report Policy",
      "Scope": "EnteredPathAndBelow",
      "SubPathMaxDynamicSignatures": 30,
      "TargetPath": "/",
      "TargetUrl": "http://php.testinvicti.com/",
      "TargetUrlRoot": "http://php.testinvicti.com/",
      "TimeWindow": null,
      "TotalVulnerabilityCount": 44,
      "UrlRewriteAnalyzableExtensions": "htm,html",
      "UrlRewriteBlockSeparators": "/$.,;|:",
      "UrlRewriteMode": "Heuristic",
      "UrlRewriteRules": null,
      "UrlRewriteExcludedLinks": null,
      "UserId": "7d85ab71-641d-4fed-096f-b11404a17c3d",
      "VcsCommitInfo": {
        "CiBuildConfigurationName": null,
        "CiBuildHasChange": null,
        "CiBuildId": null,
        "CiBuildServerName": "",
        "CiBuildServerVersion": null,
        "CiBuildUrl": null,
        "CiNcPluginVersion": null,
        "CiTimestamp": null,
        "ComitterId": null,
        "Committer": null,
        "CommitterName": null,
        "CommitterOverride": null,
        "IntegrationSystem": null,
        "IsCommiterExistAndAuthorizedInNc": null,
        "VcsName": null,
        "VcsVersion": null
      },
      "WebsiteName": "Sample",
      "WebsiteUrl": "http://php.testinvicti.com/",
      "WebsiteDescription": null,
      "WebsiteProtocol": "Http",
      "WebsiteIsDeleted": false,
      "IsWebsiteLatestCompletedFullScanTask": true,
      "EnablePciScanTask": false,
      "PciScanTask": null,
      "UserName": "Greg Sherman",
      "QueuedScanTaskExist": false,
      "ScanTaskProfileId": null,
      "ScanTaskProfile": null,
      "WebsiteGroupIds": [
        "dafa9879-4ce8-4e74-0973-b11404a17c78"
      ],
      "Comments": null,
      "BusinessLogicRecorderSetting": null,
      "ScanProfileChanged": false,
      "CompletedSteps": 21310,
      "EstimatedLaunchTime": null,
      "EstimatedSteps": 21310,
      "FailureReason": null,
      "FailureReasonDescription": null,
      "FailureReasonString": null,
      "GlobalThreatLevel": "Critical",
      "GlobalVulnerabilityCriticalCount": 6,
      "GlobalVulnerabilityHighCount": 11,
      "GlobalVulnerabilityInfoCount": 0,
      "GlobalVulnerabilityBestPracticeCount": 0,
      "GlobalVulnerabilityLowCount": 18,
      "GlobalVulnerabilityMediumCount": 9,
      "Id": "87be9df1-9f81-46e9-e860-b13b04474ccc",
      "IsCompleted": true,
      "Percentage": 100,
      "Phase": "Complete",
      "ScanTaskGroupId": "9725ef27-50d8-4f96-e85f-b13b04474c98",
      "ScanType": "Full",
      "ScheduledScanId": null,
      "State": "Complete",
      "StateChanged": "2024-03-22T20:21:53.9273209+00:00",
      "ThreatLevel": "Critical",
      "VulnerabilityCriticalCount": 6,
      "VulnerabilityHighCount": 11,
      "VulnerabilityInfoCount": 0,
      "VulnerabilityBestPracticeCount": 0,
      "VulnerabilityLowCount": 18,
      "VulnerabilityMediumCount": 9,
      "WebsiteId": "f3a1c84e-bf9f-452d-1525-b11d048449cf",
      "Initiated": "2024-03-22T19:56:21.4427686+00:00",
      "Tags": []
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **AdditionalWebsites** (object)
  - **AgentId** (string)
  - **AgentName** (string)
  - **Cookies** (object)
  - **CrawlAndAttack** (boolean)
  - **DeletedOn** (object)
  - **EnableHeuristicChecksInCustomUrlRewrite** (boolean)
  - **ExcludedLinks** (string)
  - **ExcludeLinks** (boolean)
  - **DisallowedHttpMethods** (string)
  - **FindAndFollowNewLinks** (boolean)
  - **ImportedLinks** (object)
  - **AllImportedLinks** (string)
  - **DesktopScanId** (object)
  - **InitiatedTime** (string)
  - **InitiatedDate** (string)
  - **InitiatedAt** (string)
  - **MaxDynamicSignatures** (number)
  - **MaxScanDuration** (number)
  - **Duration** (string)
  - **PolicyDescription** (string)
  - **PolicyId** (string)
  - **PolicyUserId** (string)
  - **PolicyIsDefault** (boolean)
  - **PolicyIsShared** (boolean)
  - **PolicyName** (string)
  - **AuthenticationProfileId** (object)
  - **AuthenticationProfileOption** (string)
  - **ReportPolicyDescription** (string)
  - **ReportPolicyId** (string)
  - **ReportPolicyUserId** (string)
  - **ReportPolicyIsDefault** (boolean)
  - **ReportPolicyIsShared** (boolean)
  - **ReportPolicyName** (string)
  - **Scope** (string)
  - **SubPathMaxDynamicSignatures** (number)
  - **TargetPath** (string)
  - **TargetUrl** (string)
  - **TargetUrlRoot** (string)
  - **TimeWindow** (object)
  - **TotalVulnerabilityCount** (number)
  - **UrlRewriteAnalyzableExtensions** (string)
  - **UrlRewriteBlockSeparators** (string)
  - **UrlRewriteMode** (string)
  - **UrlRewriteRules** (object)
  - **UrlRewriteExcludedLinks** (object)
  - **UserId** (string)
  - **VcsCommitInfo** (object)
    - **CiBuildConfigurationName** (object)
    - **CiBuildHasChange** (object)
    - **CiBuildId** (object)
    - **CiBuildServerName** (string)
    - **CiBuildServerVersion** (object)
    - **CiBuildUrl** (object)
    - **CiNcPluginVersion** (object)
    - **CiTimestamp** (object)
    - **ComitterId** (object)
    - **Committer** (object)
    - **CommitterName** (object)
    - **CommitterOverride** (object)
    - **IntegrationSystem** (object)
    - **IsCommiterExistAndAuthorizedInNc** (object)
    - **VcsName** (object)
    - **VcsVersion** (object)
  - **WebsiteName** (string)
  - **WebsiteUrl** (string)
  - **WebsiteDescription** (object)
  - **WebsiteProtocol** (string)
  - **WebsiteIsDeleted** (boolean)
  - **IsWebsiteLatestCompletedFullScanTask** (boolean)
  - **EnablePciScanTask** (boolean)
  - **PciScanTask** (object)
  - **UserName** (string)
  - **QueuedScanTaskExist** (boolean)
  - **ScanTaskProfileId** (object)
  - **ScanTaskProfile** (object)
  - **WebsiteGroupIds** (array)
  - **Comments** (object)
  - **BusinessLogicRecorderSetting** (object)
  - **ScanProfileChanged** (boolean)
  - **CompletedSteps** (number)
  - **EstimatedLaunchTime** (object)
  - **EstimatedSteps** (number)
  - **FailureReason** (object)
  - **FailureReasonDescription** (object)
  - **FailureReasonString** (object)
  - **GlobalThreatLevel** (string)
  - **GlobalVulnerabilityCriticalCount** (number)
  - **GlobalVulnerabilityHighCount** (number)
  - **GlobalVulnerabilityInfoCount** (number)
  - **GlobalVulnerabilityBestPracticeCount** (number)
  - **GlobalVulnerabilityLowCount** (number)
  - **GlobalVulnerabilityMediumCount** (number)
  - **Id** (string)
  - **IsCompleted** (boolean)
  - **Percentage** (number)
  - **Phase** (string)
  - **ScanTaskGroupId** (string)
  - **ScanType** (string)
  - **ScheduledScanId** (object)
  - **State** (string)
  - **StateChanged** (string)
  - **ThreatLevel** (string)
  - **VulnerabilityCriticalCount** (number)
  - **VulnerabilityHighCount** (number)
  - **VulnerabilityInfoCount** (number)
  - **VulnerabilityBestPracticeCount** (number)
  - **VulnerabilityLowCount** (number)
  - **VulnerabilityMediumCount** (number)
  - **WebsiteId** (string)
  - **Initiated** (string)
  - **Tags** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Content-Type | string |
| Content-Length | string |
| Connection | string |
| Cache-Control | string |
| Pragma | string |
| Expires | string |
| X-Content-Type-Options | string |
| X-Frame-Options | string |
| Referrer-Policy | string |
| X-XSS-Protection | string |
| Origin-Trial | string |
| Strict-Transport-Security | string |
| Expect-CT | string |