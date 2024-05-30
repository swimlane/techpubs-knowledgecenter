Turbine Canvas Terminology
==========================

The following terms and definitions will be introduced/used as part of
the new Turbine Canvas builder and TC/TP 23.5.0 release:

Orange = Needs further clarification

Audience for this page: EMs, PMs, TechPubs, Design - This is for
internal use and so that work and documentation can be aligned

+----------------+-------------------------+-------------------------+
| Term           | Definition              | Characteristics         |
+================+=========================+=========================+
| Turbine Canvas | A modular feature and   | -  Expand & collapse    |
|                | enhanced playbook       |    components           |
|                | building UX that        |                         |
|                | include, but not        | -  multiple triggers    |
|                | limited to: components, |    per playbook         |
|                | playbooks, native       |                         |
|                | actions, interfaces,    | -  group & ungroup      |
|                | actions                 |    components           |
|                |                         |                         |
|                |                         | -  record actions &     |
|                |                         |    triggers w/          |
|                |                         |    dependency           |
|                |                         |    highlighting         |
+----------------+-------------------------+-------------------------+
| Solution       | A combination of        | Example:                |
|                | playbooks and           |                         |
|                | applications to solve a | -  AT                   |
|                | complete end-to-end use |                         |
|                | case.                   | -  PT                   |
|                |                         |                         |
|                |                         | -  EDR                  |
|                |                         |                         |
|                |                         | -  VM                   |
+----------------+-------------------------+-------------------------+
| Playbook       | A set of operational    | -  Have multiple        |
|                | flows that automate     |    triggers, which are  |
|                | triggers, logic,        |    clearly              |
|                | actions, and            |    differentiated by    |
|                | components, as defined  |    individual flows     |
|                |                         |                         |
|                |                         | -  Are built with a     |
|                |                         |    visual programming   |
|                |                         |    language             |
|                |                         |    (components)         |
|                |                         |                         |
|                |                         | -  Contain x            |
+----------------+-------------------------+-------------------------+
| Bundle         | A combination of        | Examples:               |
|                | playbooks and           |                         |
|                | applications to solve a | -  SOC solution bundle  |
|                | for a specific outcome. |                         |
+----------------+-------------------------+-------------------------+
| Application    | (current definition) A  | Collaboration           |
|                | user-defined template   |                         |
|                | for collecting,         | CIM                     |
|                | storing, and organizing |                         |
|                | your data. All          | TI                      |
|                | automated activities    |                         |
|                | and decisions are       |                         |
|                | driven by how your      |                         |
|                | application stores      |                         |
|                | data. You also manage   |                         |
|                | workflow from within    |                         |
|                | applications.           |                         |
+----------------+-------------------------+-------------------------+
| Applet         | (current definition) A  |                         |
|                | preconfigured set of    |                         |
|                | fields and layout       |                         |
|                | specifications. Applets |                         |
|                | are appended to an      |                         |
|                | existing application    |                         |
|                | form layout and allow   |                         |
|                | users to easily update  |                         |
|                | and expand their        |                         |
|                | existing applications.  |                         |
+----------------+-------------------------+-------------------------+
| Component      | A modular, reusable     | -  Do not have triggers |
|                | visual programming      |                         |
|                | playbook building block | -  May have predefined  |
|                |                         |    inputs               |
|                |                         |                         |
|                |                         | -  Requires             |
|                |                         |    well-defined outputs |
|                |                         |                         |
|                |                         | -  Two component        |
|                |                         |    forms: User-built    |
|                |                         |    and Swimlane-built   |
+----------------+-------------------------+-------------------------+
| Assets         | Saved credentials and   | -  Can be for a         |
|                | key/value pairs that    |    specific connector   |
|                | help you connect to     |    or customized, which |
|                | technologies, and also  |    can be applied to    |
|                | serve as a key store    |    any action inputs.   |
|                | for commonly used sets  |                         |
|                | of keys and values      | -  Most useful for      |
|                |                         |    standardizing and    |
|                |                         |    securing             |
|                |                         |    configurations.      |
+----------------+-------------------------+-------------------------+
| Action         | Individual capabilities | -  Passes/processes     |
|                | of connectors, allowing |    data inputs          |
|                | users to create         |                         |
|                | automation that         | -  Results available in |
|                | interacts with external |    outputs              |
|                | technologies.           |                         |
|                |                         | -  Functionality        |
|                |                         |    options: Conditions, |
|                |                         |    Loops, Retries,      |
|                |                         |    Repeats, Discovered  |
|                |                         |    outputs, testing,    |
|                |                         |    promote items        |
|                |                         |    (arrays)             |
+----------------+-------------------------+-------------------------+
| Triggers       | A trigger initiates     |                         |
|                | playbook processes.     |                         |
|                | While a playbook can    |                         |
|                | only have one trigger   |                         |
|                | per flow, it can have   |                         |
|                | more than one trigger   |                         |
|                | and/or trigger type.    |                         |
|                | Turbine currently uses  |                         |
|                | several types of        |                         |
|                | triggers to retrieve    |                         |
|                | and/or ingest data.     |                         |
+----------------+-------------------------+-------------------------+
| Flow           | A single workstream     | -  Each flow can only   |
|                | within a playbook that  |    have one trigger     |
|                | has one trigger which   |                         |
|                | initiates subsequent    | -  There can be         |
|                | automation.             |    multiple flows in    |
|                |                         |    one playbook         |
+----------------+-------------------------+-------------------------+
| Logic          | Security safeguards     |                         |
|                | like user               |                         |
|                | identification and      |                         |
|                | password access,        |                         |
|                | authenticating, access  |                         |
|                | rights and authority    |                         |
|                | levels                  |                         |
+----------------+-------------------------+-------------------------+

Definitions - TBA
-----------------

+---------------------+----------------------+----------------------+
| Term                | Definition           | Characteristics      |
+=====================+======================+======================+
| Component Interface | TBA                  | Components with the  |
|                     |                      | same interface can   |
|                     | Suggestion:          | be easily swapped    |
|                     | Interface is the     | out for one another  |
|                     | data “shape” that    | when used on the     |
|                     | can be applied to    | canvas because they  |
|                     | Turbine components.  | have the same        |
|                     | It prescribes the    | defined inputs and   |
|                     | schema of the        | output. So the data  |
|                     | component: It can    | that was already     |
|                     | specify what kind of | mapped, doesn't need |
|                     | data the component   | to be re-mapped.     |
|                     | accepts as inputs    |                      |
|                     | and what kind of     |                      |
|                     | data the component   |                      |
|                     | can produce as       |                      |
|                     | outputs.             |                      |
+---------------------+----------------------+----------------------+

 
