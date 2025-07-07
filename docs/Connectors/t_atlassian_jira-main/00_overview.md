# Atlassian Jira Connector
## Overview
The Atlassian Jira connector enables interaction with Jira's issue tracking and project management capabilities directly from the Swimlane Turbine platform.

Atlassian Jira is a leading project management and issue tracking platform that enables teams to efficiently organize, track, and manage work. The Atlassian Jira connector for Swimlane Turbine allows users to seamlessly integrate Jira's capabilities into their security workflows. By leveraging this connector, teams can automate the creation, retrieval, and updating of issues, manage attachments, and enrich user data without leaving the Swimlane environment. This integration streamlines processes, enhances collaboration, and improves response times, making it an essential tool for security and project management teams.

## Prerequisites


To integrate Atlassian Jira with Swimlane Turbine, ensure you have the following prerequisites:
- HTTP Basic Authentication with the following parameters:
  * URL: The base URL of your Jira instance (e.g., https://your-domain.atlassian.net)
  * Username: Your Jira username or email address
  * API Token: A Jira API token created in your Atlassian account for authentication
- HTTP Bearer Authentication with the following parameters:
  * URL: The base URL of your Jira instance (e.g., https://your-domain.atlassian.net)
  * Access Token: A bearer token obtained through an OAuth process for secure access


## Capabilities

The Atlassian Jira connector has the following capabilities:

* Add Comment
* Create Ticket
* Get All Users Default
* Get Ticket
* Get User
* Search
* Update Ticket
* Convert RichText to ADF


## Additional Information

* In the case of using the __Create Issue__ action, please check the following urls for the  __IssueType ID__, __Project Key ID__ and other related inputs.

* [Link to sample ID for Issue Types](https://confluence.atlassian.com/jirakb/finding-the-id-for-issue-types-646186508.html)
* [Link to project ID for Issue Types](https://confluence.atlassian.com/jirakb/how-to-get-project-id-from-the-jira-user-interface-827341414.html)
