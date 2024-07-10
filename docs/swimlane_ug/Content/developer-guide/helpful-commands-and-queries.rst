Helpful Commands and Queries
============================

This topic is a compilation of commands and queries that you can utilize
with Swimlane.

MongoDB Swimlane Database
-------------------------

Once you’ve connected to MongoDB’s Swimlane database, you can use some
of the queries listed here. The queries are organized in this section by
the collections targeted within them.

**Note:** Be sure to backup your Swimlane data before using these
commands: \_update\_, \_remove\_, \_delete\_, \_deleteOne\_,
\_deleteMany\_, or \_drop\_.

**Important**! There is a file size limit of 500MB.

Logs
~~~~

To find diagnostic information for the most recently encountered errors:

db.Logs.find({Level:'Error'}).sort({Date:-1}).limit(30)

To find diagnostic information for errors not strictly related to task
execution:

db.Logs.find({Level:'Error', TaskName: {$exists:
false}}).sort({Date:-1})

To find diagnostic information for errors strictly related to task
execution, or for any recently executed tasks:

db.Logs.find({Level:'Error', TaskName: {$exists: true}}).sort({Date:-1})

To find recent execution history (start time, end time, outcome):

db.Logs.find({TaskName:'GravityZone Host Details Daily
Sync'}).sort({Date:-1}).limit(50)

To find instances of specific error messages or print-statement
diagnostic messages:

db.Logs.find({Message:/update existing SOC
record/i}).sort({Date:-1}).limit(50)

To find multiple instances of specific error messages:

// separately db.getCollection('Logs').find({Message:/Create Task from
Alerts/i}).sort({Date:-1}).limit(10)
db.getCollection('Logs').find({Message:/validationexception/i}).count()
// together db.getCollection('Logs').find({$and:
[{Message:/validationexception/i}, {Message:/create task from
alert/i}]}).sort({Date:-1}).limit(20)\` // find one but exclude the
other db.getCollection('Logs').find({$and:
[{Message:/validationexception/i}, {Message:{$not:/create task from
alert/i}}]}).sort({Date:-1}).limit(20)

To find log entries using regular expression searching:

db.Logs.find({'Message':{'$regex':'^Failed to process the job .\* an
exception occurred. Job was automatically deleted'},
'Exception.Text':/EmailImportRetrievalJob/i, Date:{$gt:new
ISODate('2017-06-06T17:25:00.000Z')}}).sort({Date:-1}).limit(5)

To find all log entries within a certain span of time:

db.Logs.find({Date:{$gte: ISODate('2017-11-28T14:00:00.000Z'), $lte:
ISODate('2017-11-28T15:00:00.000Z')}}).count()
db.Logs.find({Level:'Error', Date:{$gte:
ISODate('2018-09-11T22:00:00.000Z'), $lte:
ISODate('2018-09-18T17:20:00.000Z')}}).sort({Date:-1}).limit(100)

You can also combine several of the above needs (time span inclusion,
specific message exclusion):

db.getCollection('Logs').aggregate( [ { $project: { Date:{$and: [{$gte:
ISODate('2017-11-20T21:00:00.000Z')}, {$lte:
ISODate('2017-11-20T21:07:00.000Z')}]}, Message:{$and: [{$not:/Email
asset/i}, {$not:/GetNewMail/i}]} } } ] ).sort({Date:-1})

To extract a large set of JSON documents to the console:

var cursor = db.Logs.find({Date:{$gte:
ISODate('2017-09-18T00:00:00.000Z')}}).sort({Date:-1});
while(cursor.hasNext()) { records.push(cursor.next()) }
print(tojson(records)); // This can be done for any collection: Logs,
Records, Tasks, etc.

Records
~~~~~~~

**Important!** MongoDB limits the size of a record to 16MB.

To inspect an individual Swimlane record’s properties and field values
(after connecting to the Swimlane database):

\`db.Records.find({TrackingFull:'CASE-6'})\`

To edit a field value in a Swimlane record:

**Note:** This requires two commands because every field value is stored
in two places within the underlying record.

db.Records.update( { "TrackingFull" : "RC-1", "Values.k":
'a5YCKOsVt6sXZ' }, { $set: { "Values.$.v": "not applicable" } } )

and

db.Records.update( { "TrackingFull" : "RC-1" }, { $set: {
"ValuesDocument.a5YCKOsVt6sXZ": "not applicable" } } )

To find all records in given application with a malformation (incorrect
null) in a certain field, and repair the affected records:

// find effected records db.Records.find({ApplicationId:
'578aa3a50f1b8814c4556a7b', 'Values.k': '578aa43c1b095222d1ad4d49',
'Values.v': null}) // fix one db.Records.update({ApplicationId:
'578aa3a50f1b8814c4556a7b', TrackingFull:'ALRT-XXXXX', 'Values.k':
'578aa43c1b095222d1ad4d49', 'Values.v': null}, {$pull: {'Values': {'k':
'578aa43c1b095222d1ad4d49'}}}, {$unset:
{'ValuesDocument.578aa43c1b095222d1ad4d49': ''}}) // fix all
db.Records.update({ApplicationId: '578aa3a50f1b8814c4556a7b',
'Values.k': '578aa43c1b095222d1ad4d49', 'Values.v': null}, {$pull:
{'Values': {'k': '578aa43c1b095222d1ad4d49'}}}, {$unset:
{'ValuesDocument.578aa43c1b095222d1ad4d49': ''}}, {multi:true})

To find all parent records in a given application that does not have any
children:

db.Records.find({ApplicationId: '578aa3a50f1b8814c4556a7b',
'ReferencedRecordIds': {$eq: []}})

To find records with corrupted field values or other malformation:

db.Records.find({"$text": {"$search": "JArray"}})
db.Records.find({"$text": {"$search": "JToken"}})

To find distinct values within a collection, e.g. to get the list of all
values for a given record field in a given application:

db.getCollection('Records').distinct("ValuesDocument.ajs1o")

To count records by application:

db.Records.aggregate([{$group: {\_id: "$ApplicationId", count: {$sum:
1}}},{$sort: {count: -1}}])

To unlock all records:

db.getCollection('Records').update({Locked: true}, { $unset: { Locked:
1, LockedDate: 1, LockingUser: 1}})

To determine the count of records that are restricted or not yet
restricted:

db.getCollection('Records').find( { 'ApplicationId': {$eq:
'APPLICAION_ID_HERE'}, 'Allowed._id': {$eq: []} // 'Allowed._id': {$eq:
'USER_ID_HERE'} Can also check for records that have specific user/group
id restrictions } ).count()

To find records with text and/or numeric list fields whose values were
improperly created via the RESTful API:

// Find records whose List field values were not given any identifiers
db.getCollection('Records').find({ "Values": { $elemMatch: { $and:[ {
"v._t": { $regex: "Core.Models.Record.ListItem\*" } }, { $or: [ {
"v._v": { $elemMatch: { "\_id": { $exists: false } } } }, { "v._v": {
$elemMatch: { "\_id": null } } } ] } ] }} }) // Find records whose List
field values have identifiers, but these are identifiers are not unique
within a given field in a given record db.Records.aggregate([ {$unwind:
"$Values"}, {$unwind: "$Values.v._v"}, {$group: {\_id: {valueId:
"$Values.v._v._id", recordId: "$_id", fieldId: "$Values.k", type:
"$Values.v._t"}, count: {$sum: 1}} }, {$match: { "\_id.type": { $regex:
/^Core.Models.Record.ListItem*/ }, "\_id.valueId": {$exists: true},
"\_id.valueId": {$ne: null}, count: {$gt: 1} } }, {$project: {
"\_id.valueId" : 1, "\_id.recordId" : 1, "\_id.fieldId" : 1, "count": 1
} } ])

To delete a record and its history:

**Note:**  This should only be used when record deletion through the
Swimlane UI has failed. You can run this command after connecting to the
Swimlane database.

db.Records.deleteOne({TrackingFull:'CASE-1'})

Next, connect to the SwimlaneHistory database and run:

db.Records.deleteMany({'Version.TrackingFull':'CASE-1'})

See other SwimlaneHistory queries below.

Settings
~~~~~~~~

To extend password expiration:

db.Settings.update({}, {$set: {'SecurityParameters.PasswordExpiration':
180}})

To disable Active Directory sync:

db.Settings.update({}, {$set: {'Directory.Enabled': 'false'}})

Reports
~~~~~~~

To detect report filter corruption:

db.Reports.find({"Filters": {"$elemMatch": {"Value._v.name._t":
"JValue"}}}).count()

To inspect report filter corruption:

db.Reports.find({"Filters": {"$elemMatch": {"Value._v.name._t":
"JValue"}}}).pretty()

To purge report filter corruption:

db.Reports.update({"Filters": {"$elemMatch": {"Value._v.name._t":
"JValue"}}}, {$set: {Filters:[]}})

Hangfire
~~~~~~~~

To purge the Hangfire job queue:

// unfortunately, there is no method for clearing only specifically
chosen tasks // delete all task execution data
db.hangfire.jobGraph.drop() // delete all task execution data (more
thorough) db.hangfire.job.remove({}); db.hangfire.jobQueue.drop();
db.hangfire.aggregatedcounter.drop(); db.hangfire.jobGraph.drop()

Tasks
~~~~~

To find all e-mail ingest tasks of type built-in IMAP import:

db.Tasks.find({'Action.Descriptor.Name':/Email Import/})
db.Tasks.find({'Trigger.Type':/email/})

To find all integration tasks that rely on a specific asset:

db.getCollection('Tasks').find({'Action.AssetId':'aTDGoDcW1mTxX'}) //
for most tasks do this
db.getCollection('Tasks').find({'Triggers.AssetId':'aTDGoDcW1mTxX'}) //
for built-in tasks do this

To find all e-mail ingest tasks relying on the sw\\_microsoft\\_exchange
plugin:

db.Tasks.find({'Action.Descriptor.Name':'Exchange Get Email Metadata'})

To remove ghost task menu entries (which result from creating a task
with the same name as a task that was previously deleted by application
deletion):

// Option 1 // Swimlane UI: Navigate to Swimlane > Collections > Menu
Items: Find by task name > Delete // Option 2
db.getCollection('MenuItems').find({Name: 'ARS - Submit v3 Vector
String' }) // Option 3 (as a Python script to find and delete all ghost
entries) from pymongo import MongoClient import ssl
mongo_connection_string =
'mongodb://Swimlane:UR4Swimlane!@192.168.56.121:27017/Swimlane' client =
MongoClient(mongo_connection_string, ssl=True,
ssl_cert_reqs=ssl.CERT_NONE) db = client['Swimlane'] tasks = db['Tasks']
menu = db['MenuItems'] menu_items = menu.find({'Type': 2}) for item in
menu_items: task_id = item['TaskId'] try: task = tasks.find_one({'\_id':
task_id}) if not task: menu.delete_one({'\_id': item['\_id']}) except:
pass

To find all tasks where the script includes the value ‘pendulum’:

db.getCollection('Tasks').aggregate([ { $project: { Name: 1, \_id: 1,
match: { $gt: [{ $indexOfBytes: [ "$Action.Script", "pendulum"] }, -1] }
} }, { $match: { match: true } } ]);

The next two queries list tasks that ran in the last 90 days for MongoDB
and with Python.

For a MongoDB query:

db.hangfire.jobGraph.aggregate([{ "$match": {"Parameters.Task Name":
{"$exists": true, "$ne": "null"}, "CreatedAt": { "$exists": true,
"$lte": new Date(ISODate().getTime() - 90 \* 24 \* 60 \* 60000)}}},
{"$group": {"\_id": "$Parameters.Task Name"}}, ])

For a Python script:

# List tasks that ran in the last 90 days import datetime from pymongo
import MongoClient import ssl client = MongoClient(host='localhost',
port=27017, username='Admin', password='nowayjose', authSource='admin',
authMechanism='SCRAM-SHA-1', ssl=True,
ssl_cert_reqs=ssl.CERT_NONE).Swimlane # <class
'pymongo.collection.Collection'> tasksExecuted =
client.get_collection("hangfire.jobGraph") # <class
'pymongo.command_cursor.CommandCursor'> tasks_executed_docs =
tasksExecuted.aggregate([{ "$match": {"Parameters.Task Name":
{"$exists": True, "$ne": "null"}, "CreatedAt": { "$exists": True,
"$lte": datetime.datetime.today() + datetime.timedelta(-90)}}},
{"$group": {"\_id": "$Parameters.Task Name"}}, ]) # <class 'list'>
tasks_executed = list(tasks_executed_docs) for taskId in tasks_executed:
taskId['Task Name'] = taskId.pop('\_id') print(taskId['Task Name'])

Integration States
~~~~~~~~~~~~~~~~~~

To clear the state store (the data persisted by \_sw\\_context.state\_)
for a given integration task:

db.IntegrationStates.deleteOne( { "\_id" : "INTEGRATION-TASK-ID"} );

AspNetUsers
~~~~~~~~~~~

To disable 2FA for a given user:

#Find user id first db.getCollection('AspNetUsers').find({},
{'UserName':1}).pretty() #Then use id to unset values
db.getCollection('AspNetUsers').update({"\_id": "USER_ID"}, {$unset: {
"OneTimePasswordSecretBytes": 1, "IsOTPVerified": 1, "IsOtpEnforced":
1}})

GridFS (fs.files and fs.chunks)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To detect orphaned plugin artifacts (often the result of failed plugin
upgrades):

​db.fs.files.find({filename:/sw_microsoft_exchange/})

To find and/or delete the byte stream for an unnecessary plugin:

db.getCollection('fs.chunks').find({'files_id': 'UPLOADED_FILE_ID'}) //
the UPLOADED_FILE_ID is the \_id value from the spurious entry(ies)
resulting from the above query, if present

To detect large and/or orphaned files that were added to a Swimlane
record's attachments fields:

db.fs.chunks.aggregate([{$group:{\_id: "$files_id", chunks: {$sum: 1}}},
{$sort:{chunks:-1}}]).forEach(function(f){ if (f.chunks > 15) {
print(f._id + "\\t" + f.chunks) } })

Applications
~~~~~~~~~~~~

To find all of the fields in a given application of a given type:

db.Applications.find( { Fields: { $elemMatch: {FieldType: 8, TargetId:
null } } }, {'Fields.$.Name':1}) // field types are: 1- Text, 2-
Numeric, 3- Selection, 4- Date, 5- User/Group, 6- Attachments 7-
Tracking Id, 8- Reference, 10- Comments, 11- History, 12- List // there
is no 9

SignalRMessages
~~~~~~~~~~~~~~~

Setting a timeout on SignalR (web socket) messages:

db.getCollection('SignalRMessages').createIndex({ "CreatedDate": 1 }, {
expireAfterSeconds: 300 } )

MongoDB SwimlaneHistory Database
--------------------------------

The queries in this section are useful after connecting to MongoDB’s
SwimlaneHistory database.

.. _records-1:

Records
~~~~~~~

To retrieve every historic revision of a given record:

db.Records.find({'Version.TrackingFull':'CASE-6'}) // alternate:
db.Records.find({'ReferenceId': 'my-record-id'})

Kubernetes
~~~~~~~~~~

To ascertain the MongoDB connection string:

kubectl -n $ns get secrets kubectl -n $ns get secrets swimlane-tasks -o
yaml echo "[the value of \*_Data_Mongo_SwimlaneConnectionString]” \|
base64 -d

To recover MongoDB usernames and/or passwords from secrets:

kubectl -n $ns get secrets # select desired secret (eg. mongo-admin in
example) kubectl -n $ns get secrets swimlane-sw-mongo-admin -o yaml echo
"[the value of user and/or password]” \| base64 -d

Python
------

This section provides you with some easy methods to inspect JSON data
returned from callees.

For a small amount of data, use \_json.dumps\_ in combination with
\_print\_ to inspect the data in the console:

from swimlane import Swimlane swimlane = Swimlane('https://HOST',
'USER', 'PASSWORD', verify_ssl=False) app = swimlane.apps.get(name='Doug
SA Change Selection Field') selection_field_def =
app.get_field_definition_by_name('Selection')
print(json.dumps(selection_field_def, sort_keys=True, indent=4,
separators=(",", ": ")))

For a larger JSON object, write it out to a file and then inspect the
text file:

with open('C:\\temp\\inspect_json.txt', 'a') as f:
json.dump(selection_field_def, f, sort_keys=True, indent=4,
separators=(",", ": "))

 
