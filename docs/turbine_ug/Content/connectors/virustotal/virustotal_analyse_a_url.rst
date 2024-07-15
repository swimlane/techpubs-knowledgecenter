.. _analyse_a_url:

Analyse a URL
=============

Submits a URL to Virustotal for comprehensive security analysis and returns the results. Requires a data body input.

Inputs
------

.. list-table:: 
   :header-rows: 1

   * - Name
     - Type
     - Description
     - Required
   * - data_body
     - object
     - Data Body
     - Yes

.. list-table:: 
   :header-rows: 1

   * - Name
     - Type
     - Description
     - Examples
     - Required
   * - url
     - string
     - URL to analyse
     - `https://swimlane.com`
     - Yes

Output
------

.. list-table:: 
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - status_code
     - number
     - Status Code
   * - response_headers
     - object
     - Response Headers
   * - reason
     - string
     - Reason
   * - json_body
     - object
     - JSON Body

.. list-table:: 
   :header-rows: 1

   * - Name
     - Type
     - Description
     - Examples
   * - status_code
     - number
     - Status Code
     - 200
   * - response_headers
     - object
     - Response Headers
     - Content-Type: application/json\n Vary: Accept-Encoding\n Content-Encoding: gzip\n X-Cloud-Trace-Context: bae3ee6e9bb6214c9bd1fe4cd0dab04a;o=1\n Date: Wed, 06 Mar 2024 15:19:50 GMT\n Server: Google Frontend\n Cache-Control: private\n Transfer-Encoding: chunked
   * - reason
     - string
     - Reason
     - OK
   * - json_body
     - object
     - JSON Body
     - data:\n type: analysis\n id: u-dd014af5ed6b38d9130e3f466f850e46d21b951199d53a18ef29ee9341614eaf-1709738102\n links:\n self: https://www.virustotal.com/api/v3/analyses/u-dd014af5ed6b38d9130e3f466f850e46d21b951199d53a18ef29ee9341614eaf-1709738102

Response Headers
----------------

.. list-table:: 
   :header-rows: 1

   * - Name
     - Type
     - Examples
   * - Content-Type
     - string
     - application/json
   * - Vary
     - string
     - Accept-Encoding
   * - Content-Encoding
     - string
     - gzip
   * - X-Cloud-Trace-Context
     - string
     - bae3ee6e9bb6214c9bd1fe4cd0dab04a;o=1
   * - Date
     - string
     - Wed, 06 Mar 2024 15:19:50 GMT
   * - Server
     - string
     - Google Frontend
   * - Cache-Control
     - string
     - private
   * - Transfer-Encoding
     - string
     - chunked

JSON Body
---------

.. list-table:: 
   :header-rows: 1

   * - Name
     - Type
     - Examples
   * - data
     - object
     - type: analysis\n id: u-dd014af5ed6b38d9130e3f466f850e46d21b951199d53a18ef29ee9341614eaf-1709738102\n links:\n self: https://www.virustotal.com/api/v3/analyses/u-dd014af5ed6b38d9130e3f466f850e46d21b951199d53a18ef29ee9341614eaf-1709738102

Data Properties
---------------

.. list-table:: 
   :header-rows: 1

   * - Name
     - Type
     - Examples
   * - type
     - string
     - analysis
   * - id
     - string
     - u-dd014af5ed6b38d9130e3f466f850e46d21b951199d53a18ef29ee9341614eaf-1709738102
   * - links
     - object
     - self: https://www.virustotal.com/api/v3/analyses/u-dd014af5ed6b38d9130e3f466f850e46d21b951199d53a18ef29ee9341614eaf-1709738102

Links Properties
----------------

.. list-table:: 
   :header-rows: 1

   * - Name
     - Type
     - Examples
   * - self
     - string
     - https://www.virustotal.com/api/v3/analyses/u-dd014af5ed6b38d9130e3f466f850e46d21b951199d53a18ef29ee9341614eaf-1709738102

Error
-----

.. list-table:: 
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - name
     - string
     - Error Name
   * - traceback
     - string
     - Traceback
   * - message
     - string
     - Error Message
   * - status_code
     - number
     - Status Code
   * - response_headers
     - object
     - Response Headers
   * - reason
     - string
     - Error Reason
   * - json_body
     - object
     - JSON Body

.. list-table:: 
   :header-rows: 1

   * - Name
     - Type
     - Examples
   * - name
     - string
     - HTTPError
   * - traceback
     - string
     - 'Traceback (most recent call last): File...'
   * - message
     - string
     - '{''status_code'': 401, ''response_headers'': {...}, ''reason'': ''Unauthorized'',...}'
   * - status_code
     - number
     - 401
   * - response_headers
     - object
     - Content-Type: application/json\n Set-Cookie: VT_SESSION_ID=; Expires=Thu, 01-Jan-1970 00:00:00 GMT; Max-Age=0; Path=/...\n X-Cloud-Trace-Context: 00f69e3bb5f16d7b28b15cda192587b4\n Date: Sat, 27 Jan 2024 19:06:58 GMT\n Server: Google Frontend\n Content-Length: '119'
   * - reason
     - string
     - Unauthorized
   * - json_body
     - object
     - error:\n message: X-Apikey header is missing\n code: AuthenticationRequiredError

Response Headers for Error
--------------------------

.. list-table:: 
   :header-rows: 1

   * - Name
     - Type
     - Examples
   * - Content-Type
     - string
     - application/json
   * - Set-Cookie
     - string
     - VT_SESSION_ID=; Expires=Thu, 01-Jan-1970 00:00:00 GMT; Max-Age=0; Path=/...
   * - X-Cloud-Trace-Context
     - string
     - 00f69e3bb5f16d7b28b15cda192587b4
   * - Date
     - string
     - Sat, 27 Jan 2024 19:06:58 GMT
   * - Server
     - string
     - Google Frontend
   * - Content-Length
     - string
     - '119'

JSON Body for Error
-------------------

.. list-table:: 
   :header-rows: 1

   * - Name
     - Type
     - Examples
   * - error
     - object
     - message: X-Apikey header is missing\n code: AuthenticationRequiredError

Meta
----

- **endpoint**: api/v3/urls
- **method**: POST
