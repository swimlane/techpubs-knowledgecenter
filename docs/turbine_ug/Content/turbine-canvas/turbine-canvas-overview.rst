 

This guide is for Swimlane **INTERNAL USE ONLY** and is provided to
support SKO 2024 and other early adopters of Turbine Canvas. Please use
Slack's # tech-pubs channel to provide feedback on this content.

 

Turbine Canvas
==============

+------------+---------------------------+---------------------------+
| Term       | Definition                | Characteristics           |
+============+===========================+===========================+
|            |                           | -  Create user-made       |
|            |                           |    components             |
| **Canvas** | A modular feature and     |                           |
|            | enhanced playbook         | -  Expand and collapse    |
|            | building UX that          |    components             |
|            | includes, but is not      |                           |
|            | limited to: components,   | -  Ability to group and   |
|            | playbooks, native         |    un-group components    |
|            | actions, actions.         |                           |
|            |                           | -  Can contain multiple   |
|            |                           |    triggers per playbook  |
|            |                           |                           |
|            |                           | -  Configure assets,      |
|            |                           |    actions, triggers in   |
|            |                           |    one place              |
+------------+---------------------------+---------------------------+

Turbine canvas is a human-centric automation builder with an executed
workflow inspired by a business process modeling notation (BPMN). You
create playbooks from canvas using visual programming language
components, triggers, actions, and assets.

Capabilities
------------

Using canvas, you have comprehensive support of flow control
constructions, i.e., native actions such as parallel, wait all, if/else
conditions, forEach loops, and more.

There is an enriched user-experience with mutable variables, which allow
you to modify variables after creation for advanced scenarios, and you
can configure components, actions, and assets from a single location for
better user experience.

After logging in, navigate to the ORCHESTRATION tab via the left-hand
navigation menu to access all of the features of Turbine Canvas. From
there, you can see all of the available canvas features to build and
maintain playbooks.

Terminology
-----------

+---------------------+----------------------+----------------------+
| Term                | Definition           | Defining             |
|                     |                      | Characteristics      |
+=====================+======================+======================+
|                     |                      | -  Pass/process data |
|                     |                      |    inputs            |
| Action              | Individual           |                      |
|                     | capabilities of      | -  Results available |
|                     | connectors, allowing |    in outputs        |
|                     | users to create      |                      |
|                     | automation that      | -  Functionality     |
|                     | interacts with       |    options:          |
|                     | external             |    Conditions,       |
|                     | technologies.        |    Loops, Retries,   |
|                     |                      |    Repeats,          |
|                     |                      |    Discovered        |
|                     |                      |    outputs, testing, |
|                     |                      |    promote items     |
|                     |                      |    (arrays)          |
+---------------------+----------------------+----------------------+
|                     |                      | -  Appended to an    |
|                     |                      |    existing          |
| Applet              | A preconfigured set  |    application form  |
|                     | of fields and layout |    layout and allow  |
|                     | specifications.      |    users to easily   |
|                     |                      |    update and expand |
|                     |                      |    their existing    |
|                     |                      |    applications      |
+---------------------+----------------------+----------------------+
|                     |                      | Examples:            |
|                     |                      |                      |
| Application         | A user-defined       | -  Collaboration     |
|                     | template for         |                      |
|                     | collecting, storing, | -  Case and Incident |
|                     | and organizing your  |    Management        |
|                     | data. All automated  |                      |
|                     | activities and       | -  Threat            |
|                     | decisions are driven |    Intelligence      |
|                     | by how your          |                      |
|                     | application stores   |                      |
|                     | data. You also       |                      |
|                     | manage workflow from |                      |
|                     | within applications. |                      |
+---------------------+----------------------+----------------------+
|                     |                      | -  Can be for a      |
|                     |                      |    specific          |
| Assets              | Saved credentials    |    connector or      |
|                     | and key/value pairs  |    customized, which |
|                     | that help you        |    can be applied to |
|                     | connect to           |    any action        |
|                     | technologies, and    |    inputs.           |
|                     | also serve as a key  |                      |
|                     | store for commonly   | -  Most useful for   |
|                     | used sets of keys    |    standardizing and |
|                     | and values           |    securing          |
|                     |                      |    configurations.   |
+---------------------+----------------------+----------------------+
|                     |                      | Examples:            |
|                     |                      |                      |
| Bundle              | A combination of     | -  SOC solution      |
|                     | playbooks and        |    bundle            |
|                     | applications to      |                      |
|                     | solve a for a        |                      |
|                     | specific outcome.    |                      |
+---------------------+----------------------+----------------------+
|                     |                      | -  Do not have       |
|                     |                      |    triggers          |
| Component           | A modular, reusable  |                      |
|                     | visual programming   | -  May have          |
|                     | playbook building    |    predefined inputs |
|                     | block                |                      |
|                     |                      | -  Requires          |
|                     |                      |    well-defined      |
|                     |                      |    outputs           |
|                     |                      |                      |
|                     |                      | -  Two component     |
|                     |                      |    forms: User-built |
|                     |                      |    and               |
|                     |                      |    Swimlane-built    |
+---------------------+----------------------+----------------------+
|                     |                      |                      |
|                     |                      |                      |
| Component Interface | Interface is the     | Components with the  |
|                     | data shape that can  | same interface can   |
|                     | be applied to        | be easily swapped    |
|                     | Turbine components.  | out for one another  |
|                     | It prescribes the    | when used on the     |
|                     | schema of the        | canvas because they  |
|                     | component. It can    | have the same        |
|                     | specify what kind of | defined inputs and   |
|                     | data the component   | output. So the data  |
|                     | accepts as inputs    | that was already     |
|                     | and what kind of     | mapped, doesn't need |
|                     | data the component   | to be re-mapped.     |
|                     | can produce as       |                      |
|                     | outputs.             |                      |
+---------------------+----------------------+----------------------+
|                     |                      | -  Each flow can     |
|                     |                      |    only have one     |
| Flow                | A single work stream |    trigger           |
|                     | within a playbook    |                      |
|                     | that has one trigger | -  There can be      |
|                     | which initiates      |    multiple flows in |
|                     | subsequent           |    one playbook      |
|                     | automation.          |                      |
+---------------------+----------------------+----------------------+
|                     |                      | Examples:            |
|                     |                      |                      |
| Logic               | Security safeguards  | -  Password access   |
|                     |                      |                      |
|                     |                      | -  Authentication    |
|                     |                      |                      |
|                     |                      | -  Access rights     |
|                     |                      |                      |
|                     |                      | -  Authority levels  |
+---------------------+----------------------+----------------------+
|                     |                      | -  User-friendly     |
|                     |                      |    canvas to build   |
| Playbook            | A set of operational |    playbook          |
|                     | flows that automate  |                      |
|                     | triggers, logic,     | -  Can contain       |
|                     | actions, and         |    triggers,         |
|                     | components, as       |    actions, native   |
|                     | defined              |    actions,          |
|                     |                      |    components,       |
|                     |                      |    assets, inputs,   |
|                     |                      |    outputs           |
|                     |                      |                      |
|                     |                      | -  Automate          |
|                     |                      |    workflows         |
+---------------------+----------------------+----------------------+
|                     |                      | Example:             |
|                     |                      |                      |
| Solution            | A combination of     | -  Alert triage      |
|                     | playbooks and        |                      |
|                     | applications to      | -  Phishing triage   |
|                     | solve a complete     |                      |
|                     | end-to-end use case. | -  Early detection   |
|                     |                      |    and response      |
|                     |                      |                      |
|                     |                      | -  Vulnerability     |
|                     |                      |    management        |
+---------------------+----------------------+----------------------+
|                     |                      | Current triggers:    |
|                     |                      |                      |
| **Triggers**        | A trigger initiates  | -  Webhook           |
|                     | playbook processes.  |                      |
|                     | While a playbook can | -  Schedule          |
|                     | only have one        |                      |
|                     | trigger per flow, it | -  Record Event      |
|                     | can have more than   |                      |
|                     | one trigger and/or   | -  Playbook Button   |
|                     | trigger type.        |                      |
|                     | Turbine currently    |                      |
|                     | uses several types   |                      |
|                     | of triggers to       |                      |
|                     | retrieve and/or      |                      |
|                     | ingest data.         |                      |
+---------------------+----------------------+----------------------+

Continue through the Orchestration section and sub-sections to learn how
to use Turbine Canvas to:

-  Create and modify playbooks with a single source location for
   configuring actions, components, and assets.

-  Select and configure playbook trigger types.

-  Add, configure, and test actions.

-  Add, configure, create, and publish components.

-  Configure assets and connectors.

-  View events.

-  Access classic playbooks/playbook runs.

-  View the Library and access Swimlane Content.

 
