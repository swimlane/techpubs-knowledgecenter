List Triage Item Events
--------------
Retrieve a list of triage item events.


Inputs
------


Parameters                    (object)  

  Event Num After                    (number)

    :Description: Return events with an event-num greater than this value Must be greater than or equal to 0.

    ..  

  Event Created Before                    (string)

    :Description: Return events with a created time equal-to or before this value.

    ..

    :Example: * 2024-07-11T06:02:23.321588Z

    ..  

  Event Created After                    (string)

    :Description: Return events with a created time equal-to or after this value.

    ..  

  Limit                    (number)

    :Description: The maximum number of items to return. If unset, the default value will be 200. Must be any value between 0 and 1000.

    ..

    :Example: * 20

    ..  

  Risk Type                    (array)

    :Description: Return events with a risk type in the provided list. Must provide between 1 and 100 items. Must provide between 1 and 100 items.

    ..  

  Risk Type Exclusion                    (array)

    :Description: Return events with a risk type not in the provided list. Must provide between 1 and 100 items. Must provide between 1 and 100 items.

    ..  

  State                    (array)

    :Description: Return events with a state in the provided list. Must provide between 1 and 100 items.

    ..

    :Example: * ['open']

    ..

    :Possible Values: * open
      * unread
      * rejected
      * resolved
      * closed

    ..
Outputs
------


Status Code                    (number)

  :Example: * 200

  ..

Response Headers                    (object)  

  Date                    (string)

    :Example: * Fri, 12 Jul 2024 06:17:04 GMT

    ..  

  Content-Type                    (string)

    :Example: * application/json

    ..  

  Transfer-Encoding                    (string)

    :Example: * chunked

    ..  

  Connection                    (string)

    :Example: * keep-alive

    ..  

  X-Correlation-Id                    (string)

    :Example: * 4V34QLUF9536T

    ..  

  Vary                    (string)

    :Example: * Origin, Access-Control-Request-Method, Access-Control-Request-Headers

    ..  

  Ratelimit Limit                    (string)

    :Example: * 100

    ..  

  Ratelimit Remaining                    (string)

    :Example: * 99

    ..  

  Ratelimit Reset                    (string)

    :Example: * 55

    ..  

  Retry After                    (string)

    :Example: * 55

    ..  

  X-Content-Type-Options                    (string)

    :Example: * nosniff

    ..  

  X-XSS-Protection                    (string)

    :Example: * 1; mode=block

    ..  

  Cache-Control                    (string)

    :Example: * no-cache, no-store, max-age=0, must-revalidate

    ..  

  Pragma                    (string)

    :Example: * no-cache

    ..  

  Expires                    (string)

    :Example: * 0

    ..  

  X-Frame-Options                    (string)

    :Example: * DENY

    ..

Reason                    (string)

  :Example: * 

  ..

JSON Body                    (array)

  :Example: * [{'event-num': 1455, 'event-created': '2024-07-07T14:59:40.940410965Z', 'event-action': 'create', 'triage-item-id': 'c10407f2-1aec-4b35-b6c3-086b396eb824', 'risk-type': 'weak-certificate', 'classification': 'domain-certificate-issue-incident', 'state': 'unread', 'risk-level': 'very-low'}]

  ..
