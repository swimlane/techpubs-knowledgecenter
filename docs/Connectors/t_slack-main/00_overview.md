# Slack Connector

## Overview

The Slack connector allows seamless integration of Swimlane Turbine with Slack's communication platform, enabling automated interactions and workflows within Slack channels and conversations.

Slack is a powerful communication platform that allows teams to collaborate effectively in real-time. The Slack Turbine Connector enables users to automate a variety of Slack interactions, such as sending messages, managing channels, and retrieving user information. By integrating with Swimlane Turbine, security teams can streamline incident response communications, coordinate actions across channels, and enhance situational awareness without leaving the security automation workflow.

## Prerequisites


To effectively utilize the Slack connector with Swimlane Turbine, ensure you have the following prerequisites:
- API Key Authentication:
  * URL: The base URL for Slack API requests.
  * API Key: Your unique Slack API token for authentication.
- HTTP Bearer Authentication:
  * URL: The base URL for Slack API requests.
  * Token: A bearer token such as a JWT for secure access.


## Capabilities

The Slack Connector has the following capabilities:

* Create, archive, and retrieve history of conversations
* Get Message Permalink
* Invite and remove users from a conversation
* Retrieve current users in a conversation
* Send broadcast messages
* Lookup by Email

## Asset Setup

The asset for this connector requires the following inputs:

*  API Token - Bot or User Token

To set up a Slack Bot OAUTH API with the appropriate permissions follow these steps:

### Create a Slack App:

* Go to the Slack API website: https://api.slack.com/.
* Click on "Your Apps" in the top-right corner and then click on "Create New App."
* Provide a name for your app and select the Slack workspace where you want to install the app. 
* Once the app is created, you'll be redirected to the app's settings page.

### Configure your Slack App:

* From the app's settings page, navigate to "OAuth & Permissions".
* Under the "Scopes" section for "Bot Token Scopes", add the necessary scopes for the API calls:
* chat:write: This scope allows your app to send messages to channels and conversations. 
* channels:history: This scope grants access to conversation history in public channels. 
* channels:join: This scope allows your app to invite users to public channels. 
* channels:manage: This scope grants the ability to manage public channels, including archiving, inviting, and kicking users. 
* channels:read: This scope provides access to channel and conversation information. 
* chat:write.customize: This scope allows your app to customize messages with blocks and attachments. 
* groups:write: This scope allows your app to create new channels 
* groups:history: This scope grants access to conversation history in private channels. 
* groups:read: This scope provides access to private channel information. 
* im:history: This scope grants access to conversation history in direct messages. 
* mpim:history: This scope allows your app to view messages and other content in group direct messages that your Slack app has been added to.
* im:read: This scope provides access to direct message channel information. 
* users:read: This scope allows your app to retrieve user information. 
* users:read.email: This scope provides access to user email addresses. 
* im:write: This scope allows your app to start direct messages with people.
* mpim:write: This scope allows your app to start group direct messages with people.
* channels:write.invites: This scope allows your app to invite members to public channels.
* groups:write.invites: This scope allows your app to invite members to private channels.
* mpim:write.invites: This scope allows your app to invite members to group direct messages.
* mpim:read: Provides access to basic information about group direct messages that your Slack app has been added to.
* Save the changes.

### Install the app to your workspace:

* In the app's settings page, go to "OAuth & Permissions".
* Scroll down to the "OAuth Tokens for Your Workspace" section and click on the "Install App to Workspace" button. 
* Authorize the app to access your Slack workspace by following the prompts.

### Obtain your access tokens:

* After installing the app, you'll be provided with access tokens such as "Bot User OAuth Access Token".

## Notes

* [Slack API Documentation or Methods Link](https://api.slack.com/methods)

See the following topics for more about User and Bot OAuth Tokens:
* [Token Types](https://api.slack.com/authentication/token-types) 
* [Scopes](https://api.slack.com/scopes)
* [Web API](https://api.slack.com/web)

This connector was last tested against product version: 4.12.0

## Additional Notes

* For __LookUp by Email__ action, please set the __scope__ parameter to __users:read.email__ .
