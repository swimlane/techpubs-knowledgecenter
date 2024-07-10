Working with Files in Python Scripts
====================================

Attachments as Input
--------------------

Python integrations can accept attachment fields as input. Attachment
fields are stored as a list of dictionary objects. Since an attachment
field may have many attachments each element of the list will be a
dictionary that contains the keys 'base64' and 'filename'. The 'base64'
key contains the base64 encoding of the file contents. The 'filename'
key contains the file name in plain text.

Example attachment object passed from Swimlane to a python task:

``attachments = [{"base64": "aGV5IGhvdydzIGl0IGdvaW5nPw==", "filename": "file1.txt"},{"base64": "aHR0cDovL3d3dy5zd2ltbGFuZS5jb20=", "filename": "file2.jpg"}]``

For example, to get the file name of the first file in an attachment
field:

``sw_context.inputs['attachments'][0]['filename']``

To get the file contents of the first file in an attachment field:

``import base64``

``base64.b64decode(sw_context.inputs['attachments'][0]['base64'])``

Attaching Files from Python
---------------------------

Python integrations can add attachments to attachment fields in Python
by returning the attachment as a base 64 encoded string using
``sw_outputs``. The value from ``sw_outputs`` is then mapped into an
attachment field using the integrations output tab, just like any other
integration field value.

For example:
``sw_outputs.append({"attachment": base64.b64encode(fileContent)})``

Specifying a File Name
~~~~~~~~~~~~~~~~~~~~~~

By default the attachment file name is the MD5 hash of the file
contents. The file name can be specified by using an inner dictionary to
specify both the file name and base 64 file contents.

For example:
``sw_outputs.append({"attachment": { "filename": "myFile.txt", "base64": base64.b64encode(fileContent)}})``
