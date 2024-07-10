JSONpath in Python Tasks
========================

This topic contains JSONpath examples.

Examples
--------

See the following JSON document. It shows how JSONpath expressions can
be added to it.

\```json { "json_response": { "entities": [ { "id":
"email:android@android.com", "name": "android@android.com", "type":
"EmailAddress", "count": 12 }, { "id":
"email:creative-review@mopub.com", "name": "creative-review@mopub.com",
"type": "EmailAddress", "count": 2 }, { "id":
"email:firebase-database-client@google.com", "name":
"firebase-database-client@google.com", "type": "EmailAddress", "count":
5 }, { "id": "idn:firebase.com", "name": "firebase.com", "type":
"InternetDomainName", "count": 9 }, { "id": "idn:mopub.com", "name":
"mopub.com", "type": "InternetDomainName", "count": 1 }, { "id":
"ip:23.2.3.3", "name": "23.2.3.3", "type": "IpAddress", "count": 27 }, {
"id": "ip:123.1.1.1", "name": "123.1.1.1", "type": "IpAddress", "count":
2 }, { "id": "ip:123.4.5.6", "name": "123.4.5.6", "type": "IpAddress",
"count": 1 } ] } } \``\`

You can form expressions to suit your requirement using the supported
JSONpath syntax and filters.

+----------------------------------+----------------------------------+
| Expression                       | Result                           |
+==================================+==================================+
| $                                | Entire object                    |
+----------------------------------+----------------------------------+
| $.json_response                  | Entire json_response object      |
+----------------------------------+----------------------------------+
| $.json_response.entities[0]      | First entity                     |
+----------------------------------+----------------------------------+
| $.                               | First entity                     |
| ['json_response']['entities'][0] |                                  |
+----------------------------------+----------------------------------+
| $.json_response.entities[0,2]    | First and third entity           |
+----------------------------------+----------------------------------+
| $.json_response.entities[:2]     | First two entities               |
+----------------------------------+----------------------------------+
| $.json_response.entities[-2:]    | Last two entities                |
+----------------------------------+----------------------------------+
| $                                | The name of all the entities     |
| .json_response.entities[\*].name |                                  |
+----------------------------------+----------------------------------+
| $..id                            | All the ids                      |
+----------------------------------+----------------------------------+
| $.                               | All entities with count greater  |
| json_response.entities[?(@.count | than 6                           |
| > 6)]                            |                                  |
+----------------------------------+----------------------------------+
| $..entities[?(@.type ==          | All entities with type           |
| "InternetDomainName")]           | InternetDomainName               |
+----------------------------------+----------------------------------+
