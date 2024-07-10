Introduction to the Python Task API
===================================

The Swimlane REST API and Python Driver allow you to connect to and
interact with the Swimlane platform from external entities (other
programs acting as Swimlane clients). The Swimlane Python Script task
type and the Python Task API allow you to customize and extend
functionality within the platform.

Swimlane offers these task types:

-  **Built-in tasks** such as the Email Import task that uses Swimlane
   platform code to retrieve email message data from an IMAP inbox.

-  **Plugin tasks** that vary depending on which Plugins you have
   installed.

-  **Powershell script tasks**

-  **Python script tasks**

   See `Create or Edit a
   Task <../../administrator-guide/integrations/create-or-edit-a-task.htm>`__
   for more information on creating Python script tasks.

Authoring and Testing the Script
--------------------------------

To author a Python script that will be executed within Swimlane:

#. From the left-navigation menu, select Integrations.

#. On the Tasks tab, click **New Task** and then click **Create a
   Task**.

#. On New Task, filter for **Script** and then select Python (either
   version, 2.7 or 3.6).

#. Select that task type, and then click **Create**.

#. In the New Task \\ Python form enter a task name and optionally
   specify the application to which this task will be affiliated. Then
   click the Save button in the upper-right.

#. In the resulting page displaying the newly formed task, click the
   Configuration tab. Type or paste in the desired python script code.

#. Click the Triggers tab and explore options for defining the times and
   conditions in which the new task's script will be executed.

Inputs and Outputs
------------------

The Swimlane Task API provides the primary means of conveying input data
into the task's script and retrieving output values from the script. In
addition, the script can interact with the Swimlane REST API and its
Python Driver, which gives this task type even greater power and
flexibility. Many scripts use both the Task API and the REST API/Driver.

Task API Inputs
~~~~~~~~~~~~~~~

The Python Task API provides the script with input values via several
objects, all of which are Python dictionaries:

-  **sw_context.config**

-  **sw_context.inputs**

-  **sw_context.user**

-  **sw_context.state**

These inputs are marshalled together and injected into the script by the
platform whenever a Python script task is executed as a background job.
They are not present within the script when it is executed from the
task’s debugger console.

The **sw_context.config** object has the following keys/values:

-  sw_context.config['SwimlaneUrl'] is the base URL of the Swimlane
   server (e.g. https://swimlane.yourdomain.com) that launched the task.

-  sw_context.config['InternalSwimlaneUrl'] is the internal URL used in
   opening a connection through the Swimlane Python driver.

-  sw_context.config['ApplicationId'] is, if applicable, the ID of the
   Swimlane application with which the task is affiliated. (This value
   is not available in debug mode.)

-  sw_context.config['RecordId'] is, if applicable, the ID of the
   Swimlane record upon which the task was launched to operate. (This
   value is not available in debug mode.)

The **sw_context.inputs** object contains keys and values defined within
the task's Inputs tab (in the lower pane of the Configuration tab). The
developer can create an arbitrary number of input values specified by
user-chosen name and input type/value pairs. The available input types
are shown in task_script_intputs.jpg. For example, assuming the task's
application has a field named "File Hash", you can define a script input
named "file_hash" whose type is Record, sub-type Field: File Hash. Then,
to access the value of the record's "File Hash" field at run-time the
script would simply:

``hash_value = sw_context.inputs['file_hash']``

The **sw_context.user** object contains values pertaining to the user
account under which the task is executed. For example, if the task is
triggered by changing a record and saving the change, then
sw_context.user will contain information about the Swimlane user whose
record modification triggered the script's execution.

``modified_by_user_name = sw_context.user['display_name']``

You can inspect the properties within the sw_context.user by:

-  Following the instructions in Debugging Python Script tasks, and
   forked Plugin tasks, with print statements or Debugging Python Script
   tasks, and forked Plugin tasks, with custom log files.

-  Using the guidance within the Python section in Helpful Commands and
   Queries add the following diagnostic code:

print(json.dumps(sw_context.user, sort_keys=True, indent=4,
separators=(",", ": ")))

This code also works well for print statement debugging.

For log file debugging use:

json.dump(sw_context.user, log_file_object, sort_keys=True, indent=4,
separators=(",", ": "))

The **sw_context.state** object exists to provide the developer with a
place to store values between script executions, in other words, the
script code itself. For example:

from datetime import datetime if 'last_access_datetime' in
sw_context.state: # do something with last_access_datetime, the value
assigned on the previous script execution
sw_context.state['last_access_datetime'] =
datetime.now().strftime('%Y-%m-%d %H:%M:%S')

The key-value pairs added to sw_context.state are available within the
platform for future use after the script executes. They can be found
within the Swimlane.IntegrationStates collection which you can access by
querying MongoDB.

This allows each Python script task its own data store which is a very
useful feature.

Consider the following example:

updated_since = '' if 'last_updated_since' in sw_context.state:
updated_since = sw_context.state['last_updated_since'] else:
updated_since = '2020-06-04T00:00:00Z' logfile.write('Querying Third
Party API for updated alarms starting: ' + updated_since + '\\n') #
Query for and process the updated alarms... new_updated_since =
pendulum.now().to_rfc3339_string().replace('+00:00', 'Z')
sw_context.state['last_updated_since'] = new_updated_since
logfile.write('Retrospective date-and-time for the next run: ' +
new_updated_since + '\\n')

The above script, when run with a scheduled trigger launching it every
20 minutes, for example, can know to fetch and act upon only those
alarms updated within the prior 20 minutes.

The added benefit, however, is that if the Swimlane deployment hosting
the script goes down for 2 hours for maintenance, the script will do the
right thing the next time that it executes. Specifically, the first time
that it runs, it will know to query for all of alarms updated within the
prior two hours. The second time that it runs after the maintenance
window it will resume its typical behavior of launching every 20 minutes
and fetching/processing only those alarms updated within the prior 20
minute span.

You can also test Swimlane workflow. This code is not well-suited for
production use, but it does make testing nuanced worfklow behavior
easier:

count = 0 per_record_key = sw_context.config['RecordId'] + '
execution_count' if per_record_key in sw_context.state: count =
sw_context.state[per_record_key] sw_context.state[per_record_key] =
count + 1 if count == 0: sw_outputs = [{'data':'First output'}] print
'Count is {0} and record id is {1}'.format(str(count),
sw_context.config['RecordId']) else: sw_outputs = [{'data':', second
output'}] print 'Count is {0} and record id is {1}'.format(str(count),
sw_context.config['RecordId'])

This creates a new entry in the script’s state store for every record
upon which it operates. This wouldn’t scale for an application with
thousands or tens of thousands of records, but it is useful in
pre-production scenarios for determining how many times a script is
invoked by the workflow feature upon a given record, and under what
circumstances.

Task API Outputs
~~~~~~~~~~~~~~~~

To make assignments to a record's fields using the TASK API:

#. Add the desired values to sw_outputs.

For example:

import json import urllib ipToLookup = sw_context.inputs["IP"]
yourAPIKey = sw_context.inputs["API_KEY"] url =
'https://www.virustotal.com/vtapi/v2/ip-address/report' parameters =
{'ip': ipToLookup, 'apikey': yourAPIKey} response =
urllib.urlopen('%s?%s' % (url, urllib.urlencode(parameters))).read()
sw_outputs.append({'vt_result': response})

2. Then, make corresponding changes to the task's output mappings.

For the example above, that would involve setting up an output mapping
from "vt_result" to a chosen destination field.

Retrieving Files from an Attachment Field
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To retrieve files from an attachment field, configure a task input named
"Attachment_Field_1", and then add the following lines to your task's
script:

files = context.inputs['Attachment_Field_1'] for file in files: name =
file['filename'] data = file['base64'] # do something with the file #
e.g. decode the file data and submit name and decoded data to a threat
intel service...
