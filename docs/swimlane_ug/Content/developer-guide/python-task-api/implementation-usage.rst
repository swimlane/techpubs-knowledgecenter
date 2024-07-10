Implementation Usage
====================

For ease of use, Swimlane has two different APIs for interacting with
Python scripts: a global and class level.

Global
------

The global usage was designed for scripters to be able to drop scripts
into Swimlane, configure a few variables, and be operational with little
effort. In this scenario, users will find anywhere they had arguments
passed to the script via CLI/etc and replace them with the Swimlane
context object sw_context. Additionally, Swimlane inserts a list of
dictionaries (called sw_outputs) into each script that can be used to
return data to Swimlane.

Take the following demo script:

import urllib import sys ipToLookup = sys.argv[1] # example:
'90.156.201.27' yourAPIKey = 'asdfasd3452dsfasdfasdasdf' url =
'https://www.virustotal.com/vtapi/v2/ip-address/report' parameters =
{'ip': ipToLookup, 'apikey': yourAPIKey} response =
urllib.urlopen('%s?%s' % (url, urllib.urlencode(parameters))).read()
print response

This script would be migrated by replacing the apiKey and the ipToLookup
variables with variables from the context object. Additionally, the
standard output printing can be removed to use the sw_outputs object.

import json import urllib ipToLookup = sw_context.inputs["IP"]
yourAPIKey = sw_context.inputs["API_KEY"] url =
'https://www.virustotal.com/vtapi/v2/ip-address/report' parameters =
{'ip': ipToLookup, 'apikey': yourAPIKey} response =
urllib.urlopen('%s?%s' % (url, urllib.urlencode(parameters))).read()
sw_outputs.append({'output': response})

Since we can capture messages from the standard output, moving the
output to the outputs object is not necessary.

Class
-----

Developers who are familiar with object-oriented programming concepts
can leverage the class architecture pattern.

**Note:** Class applies to plugin tasks only, and not to custom scripts.
Custom scripts do not contain plugin-specific behaviors like being able
to use SwMain class.

class SwMain: def \__init\_\_(self, context): # setup pass def
\__del\_\_(): # on done pass def execute(self): # do job and return
output pass

When a developer defines a class with the name of SwMain, it will be
automatically invoked with the sw_context object context argument. After
the class is initialized, the execute method is invoked on that instance
of the class. The execute method is where the 'work' of the task will be
done. When finished, the execute method returns an array of dictionaries
as the output.

With this pattern, the context is encapsulated into the SwMain singleton
rather than accessing the global sw_context or sw_outputs objects and
enforce a single exit point return object. This rigid API helps to
create more predictable, more maintainable, and easier readability
plugin pattern. Swimlane’s internal plugins are authored in this format.
