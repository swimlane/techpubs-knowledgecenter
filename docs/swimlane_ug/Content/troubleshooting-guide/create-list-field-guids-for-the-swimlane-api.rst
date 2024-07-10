Create List Field GUIDs for the Swimlane API
============================================

To use the Swimlane API to create or update list fields in an
application record you must first generate a Globally Unique Identifier
(GUID) to add to the API PUT/POST request.

Here are two examples:

-  POST or PUT requests to the */app//record* endpoint for Text or
   Numeric List record field values

-  POST or PUT requests to the */app/* endpoint for creating/updating
   Selection field definitions

When Swimlane saves a record with Text or Numeric List fields, it
generates a GUID for each of the values in the list, for example:

"values": { "$type":
"System.Collections.Generic.Dictionary`2[[System.String,
System.Private.CoreLib],[System.Object, System.Private.CoreLib]],
System.Private.CoreLib", "ail82": [ { "$type":
"Core.Models.Record.ListItem`1[[System.String]], Core", "value": "1",
"id": "5f2d4a05d1f737f282b679f6" }, { "$type":
"Core.Models.Record.ListItem`1[[System.String]], Core", "value": "2",
"id": "5f2d4a07bc0744013faeb137" }, { "$type":
"Core.Models.Record.ListItem`1[[System.String]], Core", "value": "3",
"id": "5f2d4a09b5051c345cc94842" } ], "ae5v9": [ { "$type":
"Core.Models.Record.ListItem`1[[System.Double]], Core", "value": 4,
"id": "5f2d4a0de779783a09497131" }, { "$type":
"Core.Models.Record.ListItem`1[[System.Double]], Core", "value": 5,
"id": "5f2d4a0e8f92749bc9132b9b" }, { "$type":
"Core.Models.Record.ListItem`1[[System.Double]], Core", "value": 6,
"id": "5f2d4a0fb51a4e0cb7c88db0" } ] },

+> **Note:** The GUID is the value listed as the ID for each field.

You must provide these GUIDs when creating or updating list types of
record fields with the API. To do so, use this Python code to generate a
GUID. A new GUID must be generated for each field:

import time import binascii import os def random_objectid(): """Returns
a randomly generated MongoDB ObjectId.""" timestamp =
'{0:x}'.format(int(time.time())) rest =
binascii.b2a_hex(os.urandom(8)).decode('ascii') return timestamp + rest
