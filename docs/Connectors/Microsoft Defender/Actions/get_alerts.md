# Get Alerts

**Description**: Retrieve a comprehensive list of alerts from Microsoft Defender to identify potential security threats.

## Endpoint

- **URL:** `/api/alerts`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **$filter** (string)
  - **$select** (string)
  - **$orderby** (string)
  - **$top** (number)
  - **$skip** (number)
  - **$count** (boolean)
  - **$expand** (string)
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Thu, 04 May 2023 12:52:40 GMT",
      "Content-Type": "application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "Content-Encoding": "deflate",
      "Vary": "Accept-Encoding",
      "OData-Version": "4.0",
      "Strict-Transport-Security": "max-age=15724800; includeSubDomains"
    },
    "reason": "OK",
    "json_body": {
      "@odata.context": "https://api.securitycenter.microsoft.com/api/$metadata#Alerts",
      "value": [
        {
          "id": "ar638180599315648136_73827727",
          "incidentId": 400,
          "investigationId": 6,
          "assignedTo": "API Action",
          "severity": "Informational",
          "status": "Resolved",
          "classification": null,
          "determination": null,
          "investigationState": "Benign",
          "detectionSource": "AutomatedInvestigation",
          "detectorId": "5c6b7d86-c91f-4f8c-8aec-9d2086f46527",
          "category": "SuspiciousActivity",
          "threatFamilyName": null,
          "title": "Automated investigation started manually",
          "description": "SE POV User(pov@swimlaneintegrations.onmicrosoft.com) initiated an Automated investigation on se-pov-desktop.\n    The investigation automatically identifies and reviews threat artifacts for possible remediation.",
          "alertCreationTime": "2023-04-25T22:52:11.5648315Z",
          "firstEventTime": "2023-04-25T22:52:11Z",
          "lastEventTime": "2023-04-25T22:52:11Z",
          "lastUpdateTime": "2023-04-25T22:58:00.55Z",
          "resolvedTime": "2023-04-25T22:58:00.4108067Z",
          "machineId": "556b3952acb0bff29816d267822305781cc183ec",
          "computerDnsName": "se-pov-desktop",
          "rbacGroupName": null,
          "aadTenantId": "f5d73c4c-bb3d-421b-8bee-424916a4acca",
          "threatName": null,
          "mitreTechniques": [],
          "relatedUser": null,
          "loggedOnUsers": [
            {
              "accountName": "Chris Phillips",
              "domainName": "SE-POV-DESKTOP"
            }
          ],
          "comments": [],
          "evidence": [],
          "domains": []
        },
        {
          "id": "da0c7e089d-5ff6-4e04-8000-17f4e35fa783_1",
          "incidentId": 392,
          "investigationId": null,
          "assignedTo": null,
          "severity": "Informational",
          "status": "New",
          "classification": null,
          "determination": null,
          "investigationState": "UnsupportedAlertType",
          "detectionSource": "WindowsDefenderAv",
          "detectorId": "12cfe475-4973-4a03-ad53-60dca8bf9d3d",
          "category": "Malware",
          "threatFamilyName": "EICAR_Test_File",
          "title": "Malware was detected in a zip archive file",
          "description": "Malware and unwanted software are undesirable applications that perform annoying, disruptive, or harmful actions on affected devices\u200b. Some of these undesirable applications can replicate and spread from one device to another. Other devices receive commands from remote attackers and perform activities associated with cyber attacks. \n\nThis detection indicates that malware was found in an archive file.  The malware has not been launched.  If Real Time Protection is turned on and the threat is not excluded, any attempt to detonate the malware from this archive will be blocked.",
          "alertCreationTime": "2023-04-19T13:42:13.1851332Z",
          "firstEventTime": "2023-04-19T13:30:57.9123134Z",
          "lastEventTime": "2023-04-19T13:30:57.9123134Z",
          "lastUpdateTime": "2023-04-19T13:42:14.3133333Z",
          "resolvedTime": null,
          "machineId": "556b3952acb0bff29816d267822305781cc183ec",
          "computerDnsName": "se-pov-desktop",
          "rbacGroupName": null,
          "aadTenantId": "f5d73c4c-bb3d-421b-8bee-424916a4acca",
          "threatName": "Virus:DOS/EICAR_Test_File",
          "mitreTechniques": [],
          "relatedUser": null,
          "loggedOnUsers": [
            {
              "accountName": "Chris Phillips",
              "domainName": "SE-POV-DESKTOP"
            }
          ],
          "comments": [],
          "evidence": [],
          "domains": []
        },
        {
          "id": "da14ac5136-324c-4dd7-8e22-a880f7266da7_1",
          "incidentId": 392,
          "investigationId": 4,
          "assignedTo": "API Action",
          "severity": "Informational",
          "status": "Resolved",
          "classification": null,
          "determination": null,
          "investigationState": "SuccessfullyRemediated",
          "detectionSource": "WindowsDefenderAv",
          "detectorId": "d60f5b90-ecd8-4d77-8186-a801597ec762",
          "category": "Malware",
          "threatFamilyName": "EICAR_Test_File",
          "title": "'EICAR_Test_File' malware was detected",
          "description": "Malware and unwanted software are undesirable applications that perform annoying, disruptive, or harmful actions on affected machines. Some of these undesirable applications can replicate and spread from one machine to another. Others are able to receive commands from remote attackers and perform activities associated with cyber attacks.\n\nThis detection might indicate that the malware was stopped from delivering its payload. However, it is prudent to check the machine for signs of infection.",
          "alertCreationTime": "2023-04-19T13:43:49.3882906Z",
          "firstEventTime": "2023-04-19T13:30:57.913646Z",
          "lastEventTime": "2023-04-19T13:30:57.913646Z",
          "lastUpdateTime": "2023-04-19T18:28:28.84Z",
          "resolvedTime": "2023-04-19T18:28:28.5479406Z",
          "machineId": "556b3952acb0bff29816d267822305781cc183ec",
          "computerDnsName": "se-pov-desktop",
          "rbacGroupName": null,
          "aadTenantId": "f5d73c4c-bb3d-421b-8bee-424916a4acca",
          "threatName": "Virus:DOS/EICAR_Test_File",
          "mitreTechniques": [],
          "relatedUser": null,
          "loggedOnUsers": [
            {
              "accountName": "Chris Phillips",
              "domainName": "SE-POV-DESKTOP"
            }
          ],
          "comments": [],
          "evidence": [],
          "domains": []
        },
        {
          "id": "da163c9003-bc7d-4649-89e3-dfdf927da744_1",
          "incidentId": 407,
          "investigationId": null,
          "assignedTo": null,
          "severity": "Informational",
          "status": "New",
          "classification": null,
          "determination": null,
          "investigationState": "UnsupportedAlertType",
          "detectionSource": "WindowsDefenderAv",
          "detectorId": "12cfe475-4973-4a03-ad53-60dca8bf9d3d",
          "category": "Malware",
          "threatFamilyName": "EICAR_Test_File",
          "title": "Malware was detected in a zip archive file",
          "description": "Malware and unwanted software are undesirable applications that perform annoying, disruptive, or harmful actions on affected devices\u200b. Some of these undesirable applications can replicate and spread from one device to another. Other devices receive commands from remote attackers and perform activities associated with cyber attacks. \n\nThis detection indicates that malware was found in an archive file.  The malware has not been launched.  If Real Time Protection is turned on and the threat is not excluded, any attempt to detonate the malware from this archive will be blocked.",
          "alertCreationTime": "2023-04-26T15:25:00.2604342Z",
          "firstEventTime": "2023-04-26T15:05:59.1225425Z",
          "lastEventTime": "2023-04-26T15:09:18.9067858Z",
          "lastUpdateTime": "2023-04-26T15:27:59.8566667Z",
          "resolvedTime": null,
          "machineId": "556b3952acb0bff29816d267822305781cc183ec",
          "computerDnsName": "se-pov-desktop",
          "rbacGroupName": null,
          "aadTenantId": "f5d73c4c-bb3d-421b-8bee-424916a4acca",
          "threatName": "Virus:DOS/EICAR_Test_File",
          "mitreTechniques": [],
          "relatedUser": null,
          "loggedOnUsers": [],
          "comments": [],
          "evidence": [],
          "domains": []
        },
        {
          "id": "da17fbbe7a-a8fc-497d-8f87-7de15a27c2df_1",
          "incidentId": 396,
          "investigationId": 5,
          "assignedTo": "API Action",
          "severity": "Low",
          "status": "Resolved",
          "classification": null,
          "determination": null,
          "investigationState": "SuccessfullyRemediated",
          "detectionSource": "WindowsDefenderAv",
          "detectorId": "3d73c9cf-d227-4f4f-bc32-a9f0a0e842dd",
          "category": "Exploit",
          "threatFamilyName": "CVE-2015-0318",
          "title": "'CVE-2015-0318' exploit malware was detected",
          "description": "Exploits take advantage of unsecure code in operating system components and applications. Exploits allow attackers to run arbitrary code, elevate privileges, and perform other actions that increase their ability to compromise a targeted machine. Exploits are found in both commodity malware and malware used in targeted attacks.\n\nThis detection might indicate that the malware was stopped from delivering its payload. However, it is prudent to check the machine for signs of infection.",
          "alertCreationTime": "2023-04-19T22:03:07.7939898Z",
          "firstEventTime": "2023-04-19T22:01:16.2819441Z",
          "lastEventTime": "2023-04-19T22:01:16.2819441Z",
          "lastUpdateTime": "2023-04-19T22:17:02.9966667Z",
          "resolvedTime": "2023-04-19T22:17:02.7376611Z",
          "machineId": "556b3952acb0bff29816d267822305781cc183ec",
          "computerDnsName": "se-pov-desktop",
          "rbacGroupName": null,
          "aadTenantId": "f5d73c4c-bb3d-421b-8bee-424916a4acca",
          "threatName": "Exploit:SWF/CVE-2015-0318!MTB",
          "mitreTechniques": [],
          "relatedUser": null,
          "loggedOnUsers": [
            {
              "accountName": "Chris Phillips",
              "domainName": "SE-POV-DESKTOP"
            }
          ],
          "comments": [],
          "evidence": [],
          "domains": []
        },
        {
          "id": "da1c42fa48-be2d-4820-9fb0-d39bde338a59_1",
          "incidentId": 393,
          "investigationId": 4,
          "assignedTo": "API Action",
          "severity": "Informational",
          "status": "Resolved",
          "classification": null,
          "determination": null,
          "investigationState": "SuccessfullyRemediated",
          "detectionSource": "WindowsDefenderAv",
          "detectorId": "d60f5b90-ecd8-4d77-8186-a801597ec762",
          "category": "Malware",
          "threatFamilyName": "Skeeyah",
          "title": "'Skeeyah' malware was detected",
          "description": "Malware and unwanted software are undesirable applications that perform annoying, disruptive, or harmful actions on affected machines. Some of these undesirable applications can replicate and spread from one machine to another. Others are able to receive commands from remote attackers and perform activities associated with cyber attacks.\n\nThis detection might indicate that the malware was stopped from delivering its payload. However, it is prudent to check the machine for signs of infection.",
          "alertCreationTime": "2023-04-19T17:48:49.1062764Z",
          "firstEventTime": "2023-04-19T17:46:46.4770357Z",
          "lastEventTime": "2023-04-19T17:46:46.4770357Z",
          "lastUpdateTime": "2023-04-19T18:28:28.84Z",
          "resolvedTime": "2023-04-19T18:28:28.5479406Z",
          "machineId": "556b3952acb0bff29816d267822305781cc183ec",
          "computerDnsName": "se-pov-desktop",
          "rbacGroupName": null,
          "aadTenantId": "f5d73c4c-bb3d-421b-8bee-424916a4acca",
          "threatName": "Trojan:Win32/Skeeyah.A!bit",
          "mitreTechniques": [],
          "relatedUser": null,
          "loggedOnUsers": [
            {
              "accountName": "Chris Phillips",
              "domainName": "SE-POV-DESKTOP"
            }
          ],
          "comments": [],
          "evidence": [],
          "domains": []
        },
        {
          "id": "da36aabc3a-0496-4590-b652-a3b8dda1c7ef_1",
          "incidentId": 393,
          "investigationId": 4,
          "assignedTo": "API Action",
          "severity": "Low",
          "status": "Resolved",
          "classification": null,
          "determination": null,
          "investigationState": "SuccessfullyRemediated",
          "detectionSource": "WindowsDefenderAv",
          "detectorId": "3d73c9cf-d227-4f4f-bc32-a9f0a0e842dd",
          "category": "Exploit",
          "threatFamilyName": "CVE-2014-0515",
          "title": "'CVE-2014-0515' exploit malware was detected",
          "description": "Exploits take advantage of unsecure code in operating system components and applications. Exploits allow attackers to run arbitrary code, elevate privileges, and perform other actions that increase their ability to compromise a targeted machine. Exploits are found in both commodity malware and malware used in targeted attacks.\n\nThis detection might indicate that the malware was stopped from delivering its payload. However, it is prudent to check the machine for signs of infection.",
          "alertCreationTime": "2023-04-19T17:48:49.0574812Z",
          "firstEventTime": "2023-04-19T17:46:46.4770008Z",
          "lastEventTime": "2023-04-19T17:46:46.4770008Z",
          "lastUpdateTime": "2023-04-19T18:28:28.84Z",
          "resolvedTime": "2023-04-19T18:28:28.5479406Z",
          "machineId": "556b3952acb0bff29816d267822305781cc183ec",
          "computerDnsName": "se-pov-desktop",
          "rbacGroupName": null,
          "aadTenantId": "f5d73c4c-bb3d-421b-8bee-424916a4acca",
          "threatName": "Exploit:SWF/CVE-2014-0515",
          "mitreTechniques": [],
          "relatedUser": null,
          "loggedOnUsers": [
            {
              "accountName": "Chris Phillips",
              "domainName": "SE-POV-DESKTOP"
            }
          ],
          "comments": [],
          "evidence": [],
          "domains": []
        },
        {
          "id": "da3e76d950-79f2-4050-b425-82fb969bc92a_1",
          "incidentId": 407,
          "investigationId": 12,
          "assignedTo": "API Action",
          "severity": "Informational",
          "status": "Resolved",
          "classification": null,
          "determination": null,
          "investigationState": "SuccessfullyRemediated",
          "detectionSource": "WindowsDefenderAv",
          "detectorId": "d60f5b90-ecd8-4d77-8186-a801597ec762",
          "category": "Malware",
          "threatFamilyName": "EICAR_Test_File",
          "title": "'EICAR_Test_File' malware was detected",
          "description": "Malware and unwanted software are undesirable applications that perform annoying, disruptive, or harmful actions on affected machines. Some of these undesirable applications can replicate and spread from one machine to another. Others are able to receive commands from remote attackers and perform activities associated with cyber attacks.\n\nThis detection might indicate that the malware was stopped from delivering its payload. However, it is prudent to check the machine for signs of infection.",
          "alertCreationTime": "2023-04-26T15:20:10.6946Z",
          "firstEventTime": "2023-04-26T15:05:59.1225823Z",
          "lastEventTime": "2023-04-26T15:09:18.9337128Z",
          "lastUpdateTime": "2023-04-26T15:35:48.86Z",
          "resolvedTime": "2023-04-26T15:35:48.6958753Z",
          "machineId": "556b3952acb0bff29816d267822305781cc183ec",
          "computerDnsName": "se-pov-desktop",
          "rbacGroupName": null,
          "aadTenantId": "f5d73c4c-bb3d-421b-8bee-424916a4acca",
          "threatName": "Virus:DOS/EICAR_Test_File",
          "mitreTechniques": [],
          "relatedUser": null,
          "loggedOnUsers": [],
          "comments": [],
          "evidence": [],
          "domains": []
        },
        {
          "id": "da45985c2a-5b72-44af-acf2-28f061e72059_1",
          "incidentId": 393,
          "investigationId": 4,
          "assignedTo": "API Action",
          "severity": "Informational",
          "status": "Resolved",
          "classification": null,
          "determination": null,
          "investigationState": "SuccessfullyRemediated",
          "detectionSource": "WindowsDefenderAv",
          "detectorId": "d60f5b90-ecd8-4d77-8186-a801597ec762",
          "category": "Malware",
          "threatFamilyName": "Genmaldwn",
          "title": "'Genmaldwn' malware was detected",
          "description": "Malware and unwanted software are undesirable applications that perform annoying, disruptive, or harmful actions on affected machines. Some of these undesirable applications can replicate and spread from one machine to another. Others are able to receive commands from remote attackers and perform activities associated with cyber attacks.\n\nThis detection might indicate that the malware was stopped from delivering its payload. However, it is prudent to check the machine for signs of infection.",
          "alertCreationTime": "2023-04-19T17:48:49.1682795Z",
          "firstEventTime": "2023-04-19T17:46:46.4770691Z",
          "lastEventTime": "2023-04-19T17:46:46.4770691Z",
          "lastUpdateTime": "2023-04-19T18:28:28.84Z",
          "resolvedTime": "2023-04-19T18:28:28.5479406Z",
          "machineId": "556b3952acb0bff29816d267822305781cc183ec",
          "computerDnsName": "se-pov-desktop",
          "rbacGroupName": null,
          "aadTenantId": "f5d73c4c-bb3d-421b-8bee-424916a4acca",
          "threatName": "TrojanDownloader:BAT/Genmaldwn.K!bit",
          "mitreTechniques": [],
          "relatedUser": null,
          "loggedOnUsers": [
            {
              "accountName": "Chris Phillips",
              "domainName": "SE-POV-DESKTOP"
            }
          ],
          "comments": [],
          "evidence": [],
          "domains": []
        },
        {
          "id": "da59278d48-685b-44bf-912c-7040e009cd03_1",
          "incidentId": 404,
          "investigationId": 10,
          "assignedTo": "API Action",
          "severity": "Medium",
          "status": "Resolved",
          "classification": null,
          "determination": null,
          "investigationState": "Benign",
          "detectionSource": "WindowsDefenderAv",
          "detectorId": "51d03c45-b142-4de4-95df-01b0c259d8f6",
          "category": "Ransomware",
          "threatFamilyName": "CVE",
          "title": "'CVE' ransomware was detected",
          "description": "Ransomware use common methods to encrypt files using keys that are known only to attackers. As a result, victims are unable to access the contents of the encrypted files. Most ransomware display or drop a ransom note\u2014an image or an HTML file that contains information about how to obtain the attacker-supplied decryption tool for a fee.\u00a0\u00a0 \n\nTo target documents or other files that contain user data, some ransomware look for files in certain locations and files with certain extension names. It is also common for ransomware to rename encrypted files so that they all use the same extension name.\u00a0 \n\nThis detection might indicate that the malware was stopped from delivering its payload. However, it is prudent to check the machine for signs of infection.",
          "alertCreationTime": "2023-04-26T00:47:55.268943Z",
          "firstEventTime": "2023-04-26T00:44:40.7717353Z",
          "lastEventTime": "2023-04-26T00:44:40.7717353Z",
          "lastUpdateTime": "2023-04-26T01:17:24.7233333Z",
          "resolvedTime": "2023-04-26T01:17:24.3340349Z",
          "machineId": "556b3952acb0bff29816d267822305781cc183ec",
          "computerDnsName": "se-pov-desktop",
          "rbacGroupName": null,
          "aadTenantId": "f5d73c4c-bb3d-421b-8bee-424916a4acca",
          "threatName": "Ransom:Win32/CVE",
          "mitreTechniques": [],
          "relatedUser": null,
          "loggedOnUsers": [
            {
              "accountName": "Chris Phillips",
              "domainName": "SE-POV-DESKTOP"
            }
          ],
          "comments": [],
          "evidence": [],
          "domains": []
        },
        {
          "id": "da5a9d6588-c19d-4830-890b-dc56ee38c0c7_1",
          "incidentId": 409,
          "investigationId": null,
          "assignedTo": null,
          "severity": "Medium",
          "status": "New",
          "classification": null,
          "determination": null,
          "investigationState": "UnsupportedAlertType",
          "detectionSource": "WindowsDefenderAv",
          "detectorId": "f37b8bc2-cfd2-4a8e-ac62-24a7df1e698c",
          "category": "SuspiciousActivity",
          "threatFamilyName": "Meterpreter",
          "title": "Meterpreter post-exploitation tool",
          "description": "Meterpreter, a post-exploitation tool was detected on this device. Meterpreter is deployed using DLL injection. Meterpreter was used in a wide range of documented attacks, including attacks involving state-sponsored groups and groups associated with ransomware campaigns. An attacker might be attempting to establish persistence, discover and steal credentials, or install and launch a payload in the device that might lead to further system compromise. Detections of Meterpreter tools and activity should be thoroughly investigated.",
          "alertCreationTime": "2023-04-26T19:07:43.6797826Z",
          "firstEventTime": "2023-04-26T18:56:29.42738Z",
          "lastEventTime": "2023-04-26T19:01:01.5335947Z",
          "lastUpdateTime": "2023-04-26T19:09:51.96Z",
          "resolvedTime": null,
          "machineId": "556b3952acb0bff29816d267822305781cc183ec",
          "computerDnsName": "se-pov-desktop",
          "rbacGroupName": null,
          "aadTenantId": "f5d73c4c-bb3d-421b-8bee-424916a4acca",
          "threatName": "VirTool:Java/Meterpreter.A",
          "mitreTechniques": [
            "T1055.001"
          ],
          "relatedUser": null,
          "loggedOnUsers": [
            {
              "accountName": "Chris Phillips",
              "domainName": "SE-POV-DESKTOP"
            }
          ],
          "comments": [],
          "evidence": [],
          "domains": []
        },
        {
          "id": "da638181185158896141_667602127",
          "incidentId": 406,
          "investigationId": 12,
          "assignedTo": "API Action",
          "severity": "Informational",
          "status": "Resolved",
          "classification": null,
          "determination": null,
          "investigationState": "SuccessfullyRemediated",
          "detectionSource": "CustomerTI",
          "detectorId": "360fdb3b-18a9-471b-9ad0-ad80a4cbcb00",
          "category": "SuspiciousActivity",
          "threatFamilyName": null,
          "title": "test2",
          "description": "test2",
          "alertCreationTime": "2023-04-26T15:08:35.8896313Z",
          "firstEventTime": "2023-04-26T15:05:50.4145357Z",
          "lastEventTime": "2023-04-26T15:08:15.3151687Z",
          "lastUpdateTime": "2023-04-26T15:35:48.86Z",
          "resolvedTime": "2023-04-26T15:35:48.6958753Z",
          "machineId": "556b3952acb0bff29816d267822305781cc183ec",
          "computerDnsName": "se-pov-desktop",
          "rbacGroupName": null,
          "aadTenantId": "f5d73c4c-bb3d-421b-8bee-424916a4acca",
          "threatName": null,
          "mitreTechniques": [],
          "relatedUser": null,
          "loggedOnUsers": [],
          "comments": [],
          "evidence": [],
          "domains": []
        },
        {
          "id": "da638181185158896391_633475706",
          "incidentId": 406,
          "investigationId": 12,
          "assignedTo": "API Action",
          "severity": "Informational",
          "status": "Resolved",
          "classification": null,
          "determination": null,
          "investigationState": "SuccessfullyRemediated",
          "detectionSource": "CustomerTI",
          "detectorId": "360fdb3b-18a9-471b-9ad0-ad80a4cbcb00",
          "category": "SuspiciousActivity",
          "threatFamilyName": null,
          "title": "test",
          "description": "test",
          "alertCreationTime": "2023-04-26T15:08:35.8761679Z",
          "firstEventTime": "2023-04-26T15:05:47.8062393Z",
          "lastEventTime": "2023-04-26T15:09:18.9337128Z",
          "lastUpdateTime": "2023-04-26T15:35:48.4666667Z",
          "resolvedTime": "2023-04-26T15:33:39.8027026Z",
          "machineId": "556b3952acb0bff29816d267822305781cc183ec",
          "computerDnsName": "se-pov-desktop",
          "rbacGroupName": null,
          "aadTenantId": "f5d73c4c-bb3d-421b-8bee-424916a4acca",
          "threatName": null,
          "mitreTechniques": [],
          "relatedUser": null,
          "loggedOnUsers": [],
          "comments": [],
          "evidence": [],
          "domains": []
        },
        {
          "id": "da7a7c9c2f-7d77-41d9-9d39-1b63b177b9dd_1",
          "incidentId": 402,
          "investigationId": 7,
          "assignedTo": "API Action",
          "severity": "Low",
          "status": "Resolved",
          "classification": null,
          "determination": null,
          "investigationState": "Benign",
          "detectionSource": "WindowsDefenderAv",
          "detectorId": "3d73c9cf-d227-4f4f-bc32-a9f0a0e842dd",
          "category": "Exploit",
          "threatFamilyName": "Aicat",
          "title": "'Aicat' exploit malware was detected",
          "description": "Exploits take advantage of unsecure code in operating system components and applications. Exploits allow attackers to run arbitrary code, elevate privileges, and perform other actions that increase their ability to compromise a targeted machine. Exploits are found in both commodity malware and malware used in targeted attacks.\n\nThis detection might indicate that the malware was stopped from delivering its payload. However, it is prudent to check the machine for signs of infection.",
          "alertCreationTime": "2023-04-25T23:28:56.6170228Z",
          "firstEventTime": "2023-04-25T23:15:22.1010382Z",
          "lastEventTime": "2023-04-25T23:15:22.1010382Z",
          "lastUpdateTime": "2023-04-25T23:36:18.13Z",
          "resolvedTime": "2023-04-25T23:36:18.1157462Z",
          "machineId": "556b3952acb0bff29816d267822305781cc183ec",
          "computerDnsName": "se-pov-desktop",
          "rbacGroupName": null,
          "aadTenantId": "f5d73c4c-bb3d-421b-8bee-424916a4acca",
          "threatName": "Exploit:Win32/Aicat.A!ml",
          "mitreTechniques": [],
          "relatedUser": null,
          "loggedOnUsers": [
            {
              "accountName": "Chris Phillips",
              "domainName": "SE-POV-DESKTOP"
            }
          ],
          "comments": [],
          "evidence": [],
          "domains": []
        },
        {
          "id": "da86171505-000f-409f-8e29-86bbc2bf423e_1",
          "incidentId": 402,
          "investigationId": 8,
          "assignedTo": "API Action",
          "severity": "Low",
          "status": "Resolved",
          "classification": null,
          "determination": null,
          "investigationState": "SuccessfullyRemediated",
          "detectionSource": "WindowsDefenderAv",
          "detectorId": "3d73c9cf-d227-4f4f-bc32-a9f0a0e842dd",
          "category": "Exploit",
          "threatFamilyName": "CVE-2014-0515",
          "title": "'CVE-2014-0515' exploit malware was detected",
          "description": "Exploits take advantage of unsecure code in operating system components and applications. Exploits allow attackers to run arbitrary code, elevate privileges, and perform other actions that increase their ability to compromise a targeted machine. Exploits are found in both commodity malware and malware used in targeted attacks.\n\nThis detection might indicate that the malware was stopped from delivering its payload. However, it is prudent to check the machine for signs of infection.",
          "alertCreationTime": "2023-04-25T23:28:56.741128Z",
          "firstEventTime": "2023-04-25T23:15:22.1010382Z",
          "lastEventTime": "2023-04-25T23:15:22.1010382Z",
          "lastUpdateTime": "2023-04-25T23:36:08.7933333Z",
          "resolvedTime": "2023-04-25T23:36:08.6865211Z",
          "machineId": "556b3952acb0bff29816d267822305781cc183ec",
          "computerDnsName": "se-pov-desktop",
          "rbacGroupName": null,
          "aadTenantId": "f5d73c4c-bb3d-421b-8bee-424916a4acca",
          "threatName": "Exploit:SWF/CVE-2014-0515",
          "mitreTechniques": [],
          "relatedUser": null,
          "loggedOnUsers": [
            {
              "accountName": "Chris Phillips",
              "domainName": "SE-POV-DESKTOP"
            }
          ],
          "comments": [],
          "evidence": [],
          "domains": []
        },
        {
          "id": "da8b8b92a2-15ba-4e8f-aa9d-cd511e631542_1",
          "incidentId": 403,
          "investigationId": 9,
          "assignedTo": "API Action",
          "severity": "Low",
          "status": "Resolved",
          "classification": null,
          "determination": null,
          "investigationState": "Benign",
          "detectionSource": "WindowsDefenderAv",
          "detectorId": "3d73c9cf-d227-4f4f-bc32-a9f0a0e842dd",
          "category": "Exploit",
          "threatFamilyName": "CVE-2015-5122",
          "title": "'CVE-2015-5122' exploit malware was detected",
          "description": "Exploits take advantage of unsecure code in operating system components and applications. Exploits allow attackers to run arbitrary code, elevate privileges, and perform other actions that increase their ability to compromise a targeted machine. Exploits are found in both commodity malware and malware used in targeted attacks.\n\nThis detection might indicate that the malware was stopped from delivering its payload. However, it is prudent to check the machine for signs of infection.",
          "alertCreationTime": "2023-04-25T23:50:54.7027655Z",
          "firstEventTime": "2023-04-25T23:47:13.7141705Z",
          "lastEventTime": "2023-04-25T23:47:13.7141705Z",
          "lastUpdateTime": "2023-04-25T23:58:53.4233333Z",
          "resolvedTime": "2023-04-25T23:58:53.254072Z",
          "machineId": "556b3952acb0bff29816d267822305781cc183ec",
          "computerDnsName": "se-pov-desktop",
          "rbacGroupName": null,
          "aadTenantId": "f5d73c4c-bb3d-421b-8bee-424916a4acca",
          "threatName": "Exploit:SWF/CVE-2015-5122",
          "mitreTechniques": [],
          "relatedUser": null,
          "loggedOnUsers": [
            {
              "accountName": "Chris Phillips",
              "domainName": "SE-POV-DESKTOP"
            }
          ],
          "comments": [],
          "evidence": [],
          "domains": []
        },
        {
          "id": "daaee6e92d-64aa-478b-aa9b-851c8890ef01_1",
          "incidentId": 411,
          "investigationId": null,
          "assignedTo": null,
          "severity": "Informational",
          "status": "New",
          "classification": null,
          "determination": null,
          "investigationState": "UnsupportedAlertType",
          "detectionSource": "CustomerTI",
          "detectorId": "08dfd06f-d2e2-4049-899f-67b406311d84",
          "category": "CommandAndControl",
          "threatFamilyName": null,
          "title": "Connection to a custom network indicator",
          "description": "An endpoint has connected to a URL or domain in your list of custom indicators.",
          "alertCreationTime": "2023-04-28T15:26:21.1558311Z",
          "firstEventTime": "2023-04-28T15:22:12.6050889Z",
          "lastEventTime": "2023-05-01T13:17:16.729907Z",
          "lastUpdateTime": "2023-05-01T13:23:23.1066667Z",
          "resolvedTime": null,
          "machineId": "556b3952acb0bff29816d267822305781cc183ec",
          "computerDnsName": "se-pov-desktop",
          "rbacGroupName": null,
          "aadTenantId": "f5d73c4c-bb3d-421b-8bee-424916a4acca",
          "threatName": null,
          "mitreTechniques": [],
          "relatedUser": null,
          "loggedOnUsers": [
            {
              "accountName": "Chris Phillips",
              "domainName": "SE-POV-DESKTOP"
            }
          ],
          "comments": [],
          "evidence": [],
          "domains": []
        },
        {
          "id": "dac34692e9-5835-421c-8358-0393b3723ee8_1",
          "incidentId": 409,
          "investigationId": 13,
          "assignedTo": "API Action",
          "severity": "Low",
          "status": "Resolved",
          "classification": null,
          "determination": null,
          "investigationState": "Benign",
          "detectionSource": "WindowsDefenderAv",
          "detectorId": "3d73c9cf-d227-4f4f-bc32-a9f0a0e842dd",
          "category": "Exploit",
          "threatFamilyName": "Shellcode",
          "title": "'Shellcode' exploit malware was detected",
          "description": "Exploits take advantage of unsecure code in operating system components and applications. Exploits allow attackers to run arbitrary code, elevate privileges, and perform other actions that increase their ability to compromise a targeted machine. Exploits are found in both commodity malware and malware used in targeted attacks.\n\nThis detection might indicate that the malware was stopped from delivering its payload. However, it is prudent to check the machine for signs of infection.",
          "alertCreationTime": "2023-04-26T19:07:43.6314655Z",
          "firstEventTime": "2023-04-26T18:56:29.4275403Z",
          "lastEventTime": "2023-04-26T19:01:01.5342168Z",
          "lastUpdateTime": "2023-04-26T19:19:19.87Z",
          "resolvedTime": "2023-04-26T19:19:19.6865725Z",
          "machineId": "556b3952acb0bff29816d267822305781cc183ec",
          "computerDnsName": "se-pov-desktop",
          "rbacGroupName": null,
          "aadTenantId": "f5d73c4c-bb3d-421b-8bee-424916a4acca",
          "threatName": "Exploit:HTML/Shellcode.G!MSR",
          "mitreTechniques": [],
          "relatedUser": null,
          "loggedOnUsers": [
            {
              "accountName": "Chris Phillips",
              "domainName": "SE-POV-DESKTOP"
            }
          ],
          "comments": [],
          "evidence": [],
          "domains": []
        },
        {
          "id": "dae2edae68-dac2-41da-a066-46a2bfbd2187_1",
          "incidentId": 396,
          "investigationId": 5,
          "assignedTo": "API Action",
          "severity": "Low",
          "status": "Resolved",
          "classification": null,
          "determination": null,
          "investigationState": "SuccessfullyRemediated",
          "detectionSource": "WindowsDefenderAv",
          "detectorId": "3d73c9cf-d227-4f4f-bc32-a9f0a0e842dd",
          "category": "Exploit",
          "threatFamilyName": "CVE-2015-5122",
          "title": "'CVE-2015-5122' exploit malware was detected",
          "description": "Exploits take advantage of unsecure code in operating system components and applications. Exploits allow attackers to run arbitrary code, elevate privileges, and perform other actions that increase their ability to compromise a targeted machine. Exploits are found in both commodity malware and malware used in targeted attacks.\n\nThis detection might indicate that the malware was stopped from delivering its payload. However, it is prudent to check the machine for signs of infection.",
          "alertCreationTime": "2023-04-19T22:03:07.8698409Z",
          "firstEventTime": "2023-04-19T22:01:16.2819781Z",
          "lastEventTime": "2023-04-19T22:01:16.2819781Z",
          "lastUpdateTime": "2023-04-19T22:17:02.9966667Z",
          "resolvedTime": "2023-04-19T22:17:02.7376611Z",
          "machineId": "556b3952acb0bff29816d267822305781cc183ec",
          "computerDnsName": "se-pov-desktop",
          "rbacGroupName": null,
          "aadTenantId": "f5d73c4c-bb3d-421b-8bee-424916a4acca",
          "threatName": "Exploit:SWF/CVE-2015-5122",
          "mitreTechniques": [],
          "relatedUser": null,
          "loggedOnUsers": [
            {
              "accountName": "Chris Phillips",
              "domainName": "SE-POV-DESKTOP"
            }
          ],
          "comments": [],
          "evidence": [],
          "domains": []
        },
        {
          "id": "dae7ea088f-df7c-4fd3-bc22-ace8b97ca26f_1",
          "incidentId": 404,
          "investigationId": 10,
          "assignedTo": "API Action",
          "severity": "Low",
          "status": "Resolved",
          "classification": null,
          "determination": null,
          "investigationState": "Benign",
          "detectionSource": "WindowsDefenderAv",
          "detectorId": "3d73c9cf-d227-4f4f-bc32-a9f0a0e842dd",
          "category": "Exploit",
          "threatFamilyName": "Shellcode",
          "title": "'Shellcode' exploit malware was detected",
          "description": "Exploits take advantage of unsecure code in operating system components and applications. Exploits allow attackers to run arbitrary code, elevate privileges, and perform other actions that increase their ability to compromise a targeted machine. Exploits are found in both commodity malware and malware used in targeted attacks.\n\nThis detection might indicate that the malware was stopped from delivering its payload. However, it is prudent to check the machine for signs of infection.",
          "alertCreationTime": "2023-04-26T00:47:55.3387677Z",
          "firstEventTime": "2023-04-26T00:44:40.7715629Z",
          "lastEventTime": "2023-04-26T00:44:40.7717086Z",
          "lastUpdateTime": "2023-04-26T01:17:24.7233333Z",
          "resolvedTime": "2023-04-26T01:17:24.3340349Z",
          "machineId": "556b3952acb0bff29816d267822305781cc183ec",
          "computerDnsName": "se-pov-desktop",
          "rbacGroupName": null,
          "aadTenantId": "f5d73c4c-bb3d-421b-8bee-424916a4acca",
          "threatName": "Exploit:HTML/Shellcode.G!MSR",
          "mitreTechniques": [],
          "relatedUser": null,
          "loggedOnUsers": [
            {
              "accountName": "Chris Phillips",
              "domainName": "SE-POV-DESKTOP"
            }
          ],
          "comments": [],
          "evidence": [],
          "domains": []
        },
        {
          "id": "dafc3894c7-9ed6-4d21-b990-7b858617fd8a_1",
          "incidentId": 412,
          "investigationId": null,
          "assignedTo": null,
          "severity": "Informational",
          "status": "New",
          "classification": null,
          "determination": null,
          "investigationState": "UnsupportedAlertType",
          "detectionSource": "CustomerTI",
          "detectorId": "08dfd06f-d2e2-4049-899f-67b406311d84",
          "category": "CommandAndControl",
          "threatFamilyName": null,
          "title": "Connection to a custom network indicator",
          "description": "An endpoint has connected to a URL or domain in your list of custom indicators.",
          "alertCreationTime": "2023-05-01T19:18:27.6846556Z",
          "firstEventTime": "2023-05-01T19:15:14.1182628Z",
          "lastEventTime": "2023-05-01T19:15:14.1182628Z",
          "lastUpdateTime": "2023-05-01T19:18:30.2733333Z",
          "resolvedTime": null,
          "machineId": "556b3952acb0bff29816d267822305781cc183ec",
          "computerDnsName": "se-pov-desktop",
          "rbacGroupName": null,
          "aadTenantId": "f5d73c4c-bb3d-421b-8bee-424916a4acca",
          "threatName": null,
          "mitreTechniques": [],
          "relatedUser": null,
          "loggedOnUsers": [
            {
              "accountName": "Chris Phillips",
              "domainName": "SE-POV-DESKTOP"
            }
          ],
          "comments": [],
          "evidence": [],
          "domains": []
        }
      ]
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
    - **incidentId** (number)
    - **investigationId** (object)
    - **assignedTo** (object)
    - **severity** (string)
    - **status** (string)
    - **classification** (object)
    - **determination** (object)
    - **investigationState** (string)
    - **detectionSource** (string)
    - **detectorId** (string)
    - **category** (string)
    - **threatFamilyName** (object)
    - **title** (string)
    - **description** (string)
    - **alertCreationTime** (string)
    - **firstEventTime** (string)
    - **lastEventTime** (string)
    - **lastUpdateTime** (string)
    - **resolvedTime** (object)
    - **machineId** (string)
    - **computerDnsName** (string)
    - **rbacGroupName** (object)
    - **aadTenantId** (string)
    - **threatName** (object)
    - **mitreTechniques** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **relatedUser** (object)
    - **loggedOnUsers** (array)
      - **accountName** (string)
      - **domainName** (string)
    - **comments** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **evidence** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **domains** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Content-Type | string |
| Transfer-Encoding | string |
| Connection | string |
| Content-Encoding | string |
| Vary | string |
| OData-Version | string |
| Strict-Transport-Security | string |