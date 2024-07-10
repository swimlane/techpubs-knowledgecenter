Fix Calculated Formulas
=======================

If your Swimlane instance throws 500 errors when you click on records or
when you try to open an application, you might pull errors similar to
this:

{ "\_id" : ObjectId(“<object-id>"), "Date" : ISODate(“<data>“),
"HostName" : “<host-name>", "LayoutName" : "FullDebug", "Level" :
"Error", "UserName" : “<user-name>”, "MethodName" :
"Core.Engines.Calculation.Calculator.PerformCalculationsForRecord",
"LineNumber" : “<line-number>", "Message" : "Error calculating formula
for field \\”<field-name>\\” on record <“record-id>, "ApplicatonId" :
“<application-id>“, "ExceptionMessage" : "Object reference not set to an
instance of an object.", "ExceptionMethod" : "System.Object
Calculate(Core.Models.Record.Record,
Core.Models.Application.Application, System.String)", "ExceptionType" :
"System.NullReferenceException", "ExceptionStackTrace" : "at
Core.Engines.Calculation.Calculator.Calculate(Record record, Application
app, String formula) in /app/Core/Engines/Calculation/Calculator.cs:line
<line-number>\\n at
Core.Engines.Calculation.Calculator.PerformCalculationsForRecord(Record
record, Application app) in
/app/Core/Engines/Calculation/Calculator.cs:line <line-number>“,
"ExceptionWithInner" : "System.NullReferenceException: Object reference
not set to an instance of an object.\\n at
Core.Engines.Calculation.Calculator.Calculate(Record record, Application
app, String formula) in /app/Core/Engines/Calculation/Calculator.cs:line
<line-number>\\n at
Core.Engines.Calculation.Calculator.PerformCalculationsForRecord(Record
record, Application app) in
/app/Core/Engines/Calculation/Calculator.cs:line <line-number>“ }

More than likely, this error means you have calculated fields that are
not failing because they aren't accounting for empty fields.

For example, you have a calculated field, **Case TT Resolved Min** whose
calculations depend on **Case Created On** and **Case Closed On**
fields. You will get an error if those two files are not populated
correctly.

Chances are these fields are using a formula similar to the following:

``IF ([Case Created On] = [Case Resolved On], 0, TOTALMINUTES([Case Created On],[Case Resolved On]))``

Notice that this formula is only checking if two fields are equal in
order to skip the calculation and return *0*. However, it is not
checking whether **Case Created On** or **Case Resolved On** fields are
empty. The fact that these fields are indeed empty is likely causing the
issue.

To confirm if this is the issue, open the problematic record(s) and
check if all the fields are populated. If they are not, you have found
the problem!

To fix this issue:

#. From the Swimlane global navigation menu, select Applications &
   Applets.

#. Select the application or applet that is causing the error.

#. Select the fields in the Form Layout and select Edit to open the
   Calculation Builder:

#. Change the formula by adding “OR” and “IsBlank" to allow for the
   empty fields, for example:

   IF (OR([Case Created On] = [Case Closed On], IsBlank([Case Created
   On]), IsBlank([Case Closed On])), 0, TOTALMINUTES([Case Created
   On],[Case Closed On]))
