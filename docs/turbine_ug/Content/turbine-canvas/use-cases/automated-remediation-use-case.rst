Automated Remediation Use Case
==============================

Below is an example playbook. Let's break down how it's built and follow
the flow to the desired outcome.

-  **Desired Outcome:** Update an existing case with remediation
   actions.

-  **Native Actions:** Create Variables, Loop, Script, and Condition.

-  **Additional playbook tools:** Connectors and component.

The desired outcome is to create a playbook that filters through the
Alexa traffic site, searches for specific variables, then based on
conditions set, either adds the site to a domain block list or to a
decrypt list. You already have created a playbook that has a record
event trigger. Turbine initiates this playbook every time a record is
updated in the Case and Incident Management application.

|image1|

Use the Create Variables native action to add the Block Exception List
and configure to add the sites you want to filter for by adding them as
array items. For the example, we've entered Google and Swimlane's URLs
as string property types and applied the changes.

For efficiency, the Loop action to apply more than one action to each
item in the array. The following steps show a forEach parallel loop
added downstream. Inside the loop the Script and Condition native
actions are added to filter top traffic sites, then set TRUE/FALSE
condition criteria. First, configure the loop.

#. Drag-and-drop the **Loop** action downstream from your variable and
   click **Configure** to select a playbook property.

Next, configure the Script action using inputs.

#. Drag-and-drop the **Script** action into the loop.

#. From the Action panel, click **Configure**.

#. From the Scripts tab, add the array and string property types.

|image2|

The following steps show the Create Variables array the forEach Domain
value inputs.

The Python script sets up the execution paths for what will be the next
downstream action: Condition native action. If the criteria used from
the playbook property from the Script action is true, the TRUE flow
executes and adds the domain to a block list. If the criteria used from
the playbook property from the Script action is not true, then the FALSE
flow executes and adds the domain to a decrypt list. Use the `Swimlane
Python Chatbot <../../native-actions/swimlane-python-chatbot.htm>`__ to
assist with writing Python.

#. Add the Condition native action after the script.

This use case uses Palo Alto connectors. Use desired connectors, as
needed.

#. On the TRUE flow, add **Edit Custom Url Category** connector.

#. On the FALSE flow, add the **Edit Custom Url Category** connector.

Your loop is complete! Now, you have the information but need
remediation. In the playbook, drag and drop the Create Variable native
action and Update Record native action downstream after the loop to
ensure the case is updated with remediation actions. Here's a quick look
at their configurations:

 

**Tip:** If you want to combine the final two actions, group them into a
component and save. In the Add panel, the component is now available.

 

If you want to publish and access the component in the User Content
library, see `Components. <../orchestration/canvas-components.htm>`__

 

.. |image1| image:: ../../Resources/Images/canvas-ar-1.png
.. |image2| image:: ../../Resources/Images/canvas-ar-3.png
