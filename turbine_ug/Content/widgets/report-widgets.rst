Report Widgets
==============

You create report widgets from within the Charts feature on the Default
Reports page. Click **Charts** from the Default Reports taskbar, then
from **Chart Types,** select the Widgets icon.

|image1|

Report widgets have access to the report's data, in two different
formats: raw (as it is received from the API), and a more user-friendly
format, where the ID's are replaced with values. In addition to the
report's data, the widget also has access to the query.

Example data (in json):

{ "data": [ { "name": "Domain", "value": 1 }, { "name": "Email Address",
"value": 5 }, { "name": "File Hash", "value": 1 }, { "name": "IP
Address", "value": 2 } ], "rawData": [ { "$type":
"System.Dynamic.ExpandoObject, System.Linq.Expressions", "count": 1,
"aAPdorKWs_pxNlGkJ": "5acba8b218d0f6f1c9b89b5a" }, { "$type":
"System.Dynamic.ExpandoObject, System.Linq.Expressions", "count": 1,
"aAPdorKWs_pxNlGkJ": "5acba8b1cfd46fbd9cff863c" }, { "$type":
"System.Dynamic.ExpandoObject, System.Linq.Expressions", "count": 2,
"aAPdorKWs_pxNlGkJ": "5acba8b172178cc2705f0acc" }, { "$type":
"System.Dynamic.ExpandoObject, System.Linq.Expressions", "count": 5,
"aAPdorKWs_pxNlGkJ": "5acba8aa6bd592df69556b07" } ], "query": {
"dimensions": [ { "fieldId": "aAPdorKWs_pxNlGkJ", "groupByType":
"groupBy" } ], "measures": [ { "fieldId": "a98rEPNR5acwbVbVI",
"aggregateType": "count" } ] } }

Once a report with a widget is saved, it can then be placed on a
dashboard, like any other chart or report.

.. |image1| image:: ../Resources/Images/chart-widget.png
