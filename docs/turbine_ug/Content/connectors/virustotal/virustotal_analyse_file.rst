.. _action_1_analyse_file:

Analyse File
============

Initiates a comprehensive threat analysis on specified files using VirusTotal, requiring the 'files' input.

Inputs
------

.. list-table:: 
   :header-rows: 1

   * - Property
     - Title
     - Description
     - Type
     - Default / Format
   * - **files**
     - Attachments
     - File to be analysed
     - object
     - 
       - **file**
         - Type: string
         - Format: binary
       - **file_name**
         - Type: string

Required
--------

.. list-table:: 
   :header-rows: 1

   * - Property
   * - files

Output
------

.. list-table:: 
   :header-rows: 1

   * - Property
     - Title
     - Examples
     - Type
     - Properties
   * - **status_code**
     - Status Code
     - 200
     - number
     - 
   * - **response_headers**
     - Response Headers
     - Cache-Control: no-cache, Content-Type: application/json; charset=utf-8, X-Cloud-Trace-Context: a5acdfac6cf89cdca49f7b3fbc7f5a51, Date: Fri, 21 Oct 2022 23:00:30 GMT, Server: Google Frontend, Content-Length: '128'
     - object
     - 
       - **Cache-Control**
         - Title: Cache Control
         - Examples: no-cache
         - Type: string
       - **Content-Type**
         - Title: Content Type
         - Examples: application/json; charset=utf-8
         - Type: string
       - **X-Cloud-Trace-Context**
         - Title: X Cloud Trace Context
         - Examples: a5acdfac6cf89cdca49f7b3fbc7f5a51
         - Type: string
       - **Date**
         - Title: Date
         - Examples: Fri, 21 Oct 2022 23:00:30 GMT
         - Type: string
       - **Server**
         - Title: Server
         - Examples: Google Frontend
         - Type: string
       - **Content-Length**
         - Title: Content Length
         - Examples: '128'
         - Type: string
   * - **reason**
     - Reason
     - OK
     - string
     - 
   * - **json_body**
     - JSON Body
     - data: type: analysis, id: MGIyNmUzMTNlZDRhN2NhNjkwNGIwZTkzNjllNWI5NTc6MTY2NjM5MzIzMA==
     - object
     - 
       - **data**
         - Title: Data
         - Examples: type: analysis, id: MGIyNmUzMTNlZDRhN2NhNjkwNGIwZTkzNjllNWI5NTc6MTY2NjM5MzIzMA==
         - Type: object
         - 
           - **type**
             - Title: Type
             - Examples: analysis
             - Type: string
           - **id**
             - Title: ID
             - Examples: MGIyNmUzMTNlZDRhN2NhNjkwNGIwZTkzNjllNWI5NTc6MTY2NjM5MzIzMA==
             - Type: string

Error
-----

.. list-table:: 
   :header-rows: 1

   * - Property
     - Title
     - Examples
     - Type
     - Properties
   * - **name**
     - Error Name
     - HTTPError
     - string
     - 
   * - **traceback**
     - Traceback
     - 'Traceback (most recent call last): File...'
     - string
     - 
   * - **message**
     - Error Message
     - '{''status_code'': 401, ''response_headers'': {...}, ''reason'': ''Unauthorized'',...}'
     - string
     - 
   * - **status_code**
     - Status Code
     - 401
     - number
     - 
   * - **response_headers**
     - Response Headers
     - Content-Type: application/json, Set-Cookie: VT_SESSION_ID=; Expires=Thu, 01-Jan-1970 00:00:00 GMT; Max-Age=0; Path=/..., X-Cloud-Trace-Context: 00f69e3bb5f16d7b28b15cda192587b4, Date: Sat, 27 Jan 2024 19:06:58 GMT, Server: Google Frontend, Content-Length: '119'
     - object
     - 
       - **Content-Type**
         - Title: Content Type
         - Examples: application/json
         - Type: string
       - **Set-Cookie**
         - Title: Set Cookie
         - Examples: VT_SESSION_ID=; Expires=Thu, 01-Jan-1970 00:00:00 GMT; Max-Age=0; Path=/...
         - Type: string
       - **X-Cloud-Trace-Context**
         - Title: X Cloud Trace Context
         - Examples: 00f69e3bb5f16d7b28b15cda192587b4
         - Type: string
       - **Date**
         - Title: Date
         - Examples: Sat, 27 Jan 2024 19:06:58 GMT
         - Type: string
       - **Server**
         - Title: Server
         - Examples: Google Frontend
         - Type: string
       - **Content-Length**
         - Title: Content Length
         - Examples: '119'
         - Type: string
   * - **reason**
     - Error Reason
     - Unauthorized
     - string
     - 
   * - **json_body**
     - JSON Body
     - error: message: X-Apikey header is missing, code: AuthenticationRequiredError
     - object
     - 
       - **error**
         - Title: Error Detail
         - Examples: message: X-Apikey header is missing, code: AuthenticationRequiredError
         - Type: object
         - 
           - **message**
             - Title: Error Message
             - Examples: X-Apikey header is missing
             - Type: string
           - **code**
             - Title: Error Code
             - Examples: AuthenticationRequiredError
             - Type: string

Meta
----

.. list-table:: 
   :header-rows: 1

   * - Property
     - Value
   * - **endpoint**
     - api/v3/files
   * - **method**
     - POST
