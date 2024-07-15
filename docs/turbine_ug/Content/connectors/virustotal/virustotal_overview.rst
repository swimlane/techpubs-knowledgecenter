.. _virustotal_connector:

VirusTotal Connector
====================

Overview
--------

The VirusTotal Analysis connector enables automated interactions with VirusTotal's APIs, facilitating the submission and retrieval of security analyses and threat intelligence.

VirusTotal is a premier service for analyzing and identifying potential threats across files, URLs, domains, and IP addresses. The VirusTotal Analysis Connector for Swimlane Turbine enables users to automate the submission and retrieval of analysis results, manage private file reports, and conduct comprehensive searches within the VirusTotal database. By integrating with VirusTotal, security teams can enhance their threat detection and response capabilities, leveraging detailed intelligence to make informed decisions and streamline their security workflows within the Swimlane Turbine platform.

Prerequisites
-------------

To effectively utilize the VirusTotal Analysis connector within the Swimlane platform, ensure you have the following prerequisites:

- **API Key Authentication**:
  - **URL**: The base endpoint for VirusTotal API services.
  - **API Key**: Your personal key provided by VirusTotal to access their API.

Public Key
----------

1. In order to get the API key, you must first register with the VirusTotal Community by going `here <https://www.virustotal.com/gui/sign-in>`_. Then click **New? Join the community**.
2. Provide a name, email, username, and password. Once complete, click **Join us**. An activation link will be sent to the email you provided.
3. Click on the activation link to activate your VirusTotal Community membership.
4. Return to the VirusTotal homepage and click the blue message icon on the lower right-hand corner of the homepage. This will bring up the VirusTotal Bot window. Click the option, **I have a feed of new files that I can upload, I want free API quota to do so**.
5. A window opens where you can create a message to VirusTotal. Complete the **Subject** and **Email** fields and then include a simple message stating why you need a free API Key.
6. Once VirusTotal reviews your message, you can sign into your account and find your public API in the corresponding menu item, API key, under your username.

Premium Key
-----------

1. Login to your account. Click your username and then click **API key**.
2. Click **Request premium API key**.
3. Fill out the request prompt on this page. Required fields include "Company size", "Company country", and "Already paying customer?".
4. VirusTotal will respond to your request.

Capabilities
------------

This connector has the capability to get different kinds of reports including domain, file hash, IP, and URL reports. VirusTotal is also able to scan either a file or a URL.

- Analyse a URL
- Analyse File
- Analyses Get
- Delete a Private File Report
- Get a Private File Report
- Get a URL for Uploading Large Files
- Get a Widget Rendering URL
- Get List of Private Files
- Get Object Descriptors Related to a File
- Get Objects Related to a Private File
- Reanalyse File
- Reanalyse URL
- Rescan a Private File
- Retrieve the Widgets HTML Content
- Search
- Submit Private URL Submission
- Upload a Private File

Asset Setup
-----------

The asset requires an API key to use. If your organization requires the use of a proxy, then that proxy can be used during the asset setup.

The Public API:

- is limited to 500 requests per day and a rate of 4 requests per minute
- must not be used in commercial products or services
- must not be used in business workflows that do not contribute new files

Notes
-----

For more information on VirusTotal:
- `VirusTotal Documentation <https://developers.virustotal.com/v3.0/>`_
- `Public API vs. Premium API <https://developers.virustotal.com/v3.0/reference#public-vs-premium-api>`_
- `Obtaining Public API Key <https://support.virustotal.com/hc/en-us/articles/115002088769-Please-give-me-an-API-key>`_

.. toctree::
   :titlesonly:

   /Content/connectors/virustotal/virustotal_actions
   /Content/connectors/virustotal/virustotal_assets