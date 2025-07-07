# Scan Retest

**Description**: Launches a retest scan based on the provided base scan identifier.

## Endpoint

- **URL:** `/api/1.0/scans/retest`
- **Method:** `post`
## Inputs

- **json_body** (object) – Required
  - **AgentName** (string)
  - **BaseScanId** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 201,
    "response_headers": {
      "Date": "Thu, 28 Mar 2024 09:53:50 GMT",
      "Content-Type": "application/json; charset=utf-8",
      "Content-Length": "3369",
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
    "reason": "Created",
    "json_body": {
      "AdditionalWebsites": null,
      "AgentId": null,
      "AgentName": null,
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
      "InitiatedTime": "28/03/2024 03:53 AM",
      "InitiatedDate": "28/03/2024",
      "InitiatedAt": "2024-03-28T09:53:50.5351532+00:00",
      "MaxDynamicSignatures": 60,
      "MaxScanDuration": 48,
      "Duration": "00:00:00",
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
      "TotalVulnerabilityCount": 0,
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
      "IsWebsiteLatestCompletedFullScanTask": false,
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
      "CompletedSteps": 0,
      "EstimatedLaunchTime": null,
      "EstimatedSteps": 0,
      "FailureReason": null,
      "FailureReasonDescription": null,
      "FailureReasonString": null,
      "GlobalThreatLevel": "Unknown",
      "GlobalVulnerabilityCriticalCount": 0,
      "GlobalVulnerabilityHighCount": 0,
      "GlobalVulnerabilityInfoCount": 0,
      "GlobalVulnerabilityBestPracticeCount": 0,
      "GlobalVulnerabilityLowCount": 0,
      "GlobalVulnerabilityMediumCount": 0,
      "Id": "af6d0ffd-529e-4056-b39f-b141021fae74",
      "IsCompleted": false,
      "Percentage": 0,
      "Phase": "Pending",
      "ScanTaskGroupId": "9725ef27-50d8-4f96-e85f-b13b04474c98",
      "ScanType": "Retest",
      "ScheduledScanId": null,
      "State": "Queued",
      "StateChanged": null,
      "ThreatLevel": "Unknown",
      "VulnerabilityCriticalCount": 0,
      "VulnerabilityHighCount": 0,
      "VulnerabilityInfoCount": 0,
      "VulnerabilityBestPracticeCount": 0,
      "VulnerabilityLowCount": 0,
      "VulnerabilityMediumCount": 0,
      "WebsiteId": "f3a1c84e-bf9f-452d-1525-b11d048449cf",
      "Initiated": "2024-03-28T09:53:50.5351532+00:00",
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
  - **AgentId** (object)
  - **AgentName** (object)
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
  - **StateChanged** (object)
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