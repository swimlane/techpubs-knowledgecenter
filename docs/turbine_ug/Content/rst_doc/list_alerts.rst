List Alerts
===========
Retrieve a list of alerts.


Inputs
~~~~~~


*Parameters*                    (*object*)  

  *ID*                    (*array*)

    :Description: One or more alert identifiers to resolve. Must provide between 1 and 100 items

    ..

    :Example: ['e5aeafc5-fbc7-42f8-9594-fc7f23adcb78', 'd7f4b588-1ffb-452c-8425-f2ea9abcfb6a']

    ..  

  *Offset*                    (*number*)

    :Description: The (zero-based) offset of the first item in the collection to return. Must be any value between 0 and 100.

    ..

    :Example: 0

    ..  

  *Limit*                    (*number*)

    :Description: The maximum number of items to return. Will default to 10 unless using id which will default to the number of ids provided. Must be any value between 0 and 100.

    ..

    :Example: 10

    ..
Outputs
~~~~~~~~~~~~


*Status Code*                    (*number*)

  :Example: 200

  ..

*Response Headers*                    (*object*)  

  *Date*                    (*string*)

    :Example: Fri, 12 Jul 2024 07:48:57 GMT

    ..  

  *Content-Type*                    (*string*)

    :Example: application/json

    ..  

  *Transfer-Encoding*                    (*string*)

    :Example: chunked

    ..  

  *Connection*                    (*string*)

    :Example: keep-alive

    ..  

  *X-Correlation-Id*                    (*string*)

    :Example: EKP5QDRJ8TRRJ

    ..  

  *Vary*                    (*string*)

    :Example: Origin, Access-Control-Request-Method, Access-Control-Request-Headers

    ..  

  *Ratelimit Limit*                    (*string*)

    :Example: 100

    ..  

  *Ratelimit Remaining*                    (*string*)

    :Example: 99

    ..  

  *Ratelimit Reset*                    (*string*)

    :Example: 2

    ..  

  *Retry After*                    (*string*)

    :Example: 2

    ..  

  *X-Content-Type-Options*                    (*string*)

    :Example: nosniff

    ..  

  *X-XSS-Protection*                    (*string*)

    :Example: 1; mode=block

    ..  

  *Cache-Control*                    (*string*)

    :Example: no-cache, no-store, max-age=0, must-revalidate

    ..  

  *Pragma*                    (*string*)

    :Example: no-cache

    ..  

  *Expires*                    (*string*)

    :Example: 0

    ..  

  *X-Frame-Options*                    (*string*)

    :Example: DENY

    ..

*Reason*                    (*string*)

  :Example: 

  ..

*JSON Body*                    (*array*)

  :Example: [{'id': 'd7f4b588-1ffb-452c-8425-f2ea9abcfb6a', 'portal-id': 'BBCBBK', 'risk-type': 'exposed-access-key', 'classification': 'exposed-access-key-alert', 'risk-assessment': {'risk-level': 'medium'}, 'risk-factors': ['Asset mentioned in source', 'Author/repo owner linked to your organization', 'Exposed on your public code repo', 'Exposed on public code repo'], 'title': None, 'description': 'Each alert risk type will have a templated description intended for display, or ingest by a freetext indexing system.\n\nThis template can change at any time, so the description must NOT be parsed based on the assumption that the format cannot change.', 'assets': [{'id': '485d2681-87a9-4a4e-b691-aef596be0c17'}, {'id': '99081ae2-381e-43fb-aa5f-a61dbf8302df'}, {'id': '52e8b12f-2bcc-443a-9c79-5bcf2533fbd9'}, {'id': '2a641291-b10f-4b7c-9d30-87aaa6b2e974'}, {'id': 'c835dc1a-7be0-4257-bffa-262357616f4c'}], 'raised': '2024-06-17T13:59:40.370331470Z', 'updated': '2024-06-17T13:59:40.370281282Z', 'mitre-attack-mapping': None}]

  ..