Trace Exchange Messages with Python
===================================

You can ingest security alarm data, such as candidate phishing email
messages, using the sw_microsoft_exchange plugin. The Exchange plugin
targets the `Exchange
EWS <https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/start-using-web-services-in-exchange>`__
APIs via the `Python
exchangelib <https://pypi.org/project/exchangelib/>`__.

The Exchange plugin currently does not offer message tracing. Yet, you
may want to know the answer to a question like, "How many people in an
organization have received a known malicious email message?" This topic
explains how you can discover the answer.

To trace Exchange messages with Python:

#. `Install the Python
   package, <https://swimlane.com/knowledge-center/docs/administrator-guide/integrations/install-and-manage-python-packages>`__\ *pypsrp.*

#. Create a Python task with script similar to this:

   from pypsrp.powershell import PowerShell, RunspacePool from
   pypsrp.wsman import WSMan wsman =
   WSMan(server="outlook.office365.com", port=443, auth="basic",
   username="USERNAME", password="PASSWORD", path="powershell-liveid")
   with RunspacePool(wsman, configuration_name="Microsoft.Exchange") as
   pool: ps = PowerShell(pool) ps.add_cmdlet("Get-MessageTrace") output
   = ps.invoke() print(output[0].adapted_properties)

   The data within *adapted_properties* is a Python dictionary with
   these keys:

   testvar = output[0].adapted_properties print(testvar['StartDate'])
   print(testvar['EndDate']) print(testvar['Received'])
   print(testvar['MessageTraceId']) print(testvar['Size'])
   print(testvar['FromIP']) print(testvar['ToIP'])
   print(testvar['Status']) print(testvar['Subject'])
   print(testvar['RecipientAddress']) print(testvar['SenderAddress'])
   print(testvar['Index']) print(testvar['MessageId'])
   print(testvar['Organization'])

For more information, contact your Swimlane Professional Services
representative.

+> **Note:** Powershell users can accomplish message tracing objectives
with the `Exchange Online PowerShell V2
module <https://docs.microsoft.com/en-us/powershell/exchange/connect-to-exchange-online-powershell?view=exchange-ps>`__
and/or the `Get-MessageTrace
cmdlet <https://docs.microsoft.com/en-us/powershell/module/exchange/get-messagetrace?view=exchange-ps>`__.
