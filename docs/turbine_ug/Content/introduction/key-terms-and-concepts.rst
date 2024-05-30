Key Terms and Concepts
======================

Swimlane Turbine uses a variety of terms throughout this documentation
and the platform itself. The table below contains high-level definitions
of some of the key terms and concepts you will encounter using Turbine.

.. table:: Key Terms and Concepts
    :class: tight-table
    
    +----------------------------------+----------------------------------+
    | Term                             | Definition                       |
    +==================================+==================================+
    | **Administrator**                | An account created to enable     |
    |                                  | access to the Turbine UI or API. |
    |                                  | The administrator role in        |
    |                                  | Turbine has access to all        |
    |                                  | tenants, roles, groups,          |
    |                                  | permissions, applications,       |
    |                                  | reports, records, etc. The       |
    |                                  | administrator role and           |
    |                                  | permissions can be narrowed to   |
    |                                  | meet business needs.             |
    +----------------------------------+----------------------------------+
    | **Agents**                       | Agents perform actions from      |
    |                                  | playbooks, and then send those   |
    |                                  | results back to the Turbine      |
    |                                  | engine. Agents wait to accept    |
    |                                  | jobs to execute actions from     |
    |                                  | Turbine but will not initiate    |
    |                                  | actions themselves to simplify   |
    |                                  | network configuration.           |
    +----------------------------------+----------------------------------+
    | **Applet**                       | A preconfigured set of fields    |
    |                                  | and layout specifications for    |
    |                                  | Turbine. Applets are appended to |
    |                                  | an existing application form     |
    |                                  | layout and are designed to allow |
    |                                  | users to easily update and       |
    |                                  | expand their existing            |
    |                                  | applications.                    |
    +----------------------------------+----------------------------------+
    | **Applet Builder**               | A form layout in Turbine for     |
    |                                  | configuring applets.             |
    +----------------------------------+----------------------------------+
    | **Application**                  | A user-defined template for      |
    |                                  | collecting, storing, and         |
    |                                  | organizing your data. All        |
    |                                  | automated activities and         |
    |                                  | decisions are driven by how your |
    |                                  | application stores data. You     |
    |                                  | also manage workflow from within |
    |                                  | applications.                    |
    +----------------------------------+----------------------------------+
    | **Application Builder**          | A form layout in Turbine for     |
    |                                  | configuring applications.        |
    +----------------------------------+----------------------------------+
    | **Assets**                       | Reusable, structured, and        |
    |                                  | vendor-specific collections of   |
    |                                  | data that contribute to the      |
    |                                  | success of Turbine actions.      |
    |                                  | Assets allow users to create a   |
    |                                  | reusable set of values that can  |
    |                                  | be applied to actions as inputs  |
    |                                  | in playbooks. Assets can be for  |
    |                                  | a specific connector, or created |
    |                                  | as a custom asset which can be   |
    |                                  | applied to any action inputs.    |
    |                                  | Assets are most useful for       |
    |                                  | standardizing and securing       |
    |                                  | configurations.                  |
    +----------------------------------+----------------------------------+
    | **Arrays**                       | An ordered collection of values  |
    |                                  | of the same data type. Values    |
    |                                  | vary based on the action         |
    |                                  | connector and/or assets, and may |
    |                                  | include, but are not limited to: |
    |                                  | IP addresses, file names, URLs,  |
    |                                  | etc.                             |
    +----------------------------------+----------------------------------+
    | **Card**                         | A report or HTML object that is  |
    |                                  | associated with a dashboard. You |
    |                                  | can have multiple cards on a     |
    |                                  | single dashboard.                |
    +----------------------------------+----------------------------------+
    | **Charts**                       | A visual, graphic representation |
    |                                  | of record and application data.  |
    +----------------------------------+----------------------------------+
    | **Comparison Operators**         | Compare the values on either     |
    |                                  | side of the operator.            |
    +----------------------------------+----------------------------------+
    | Concatenation                    | The ability to add context to a  |
    |                                  | playbook input property.         |
    +----------------------------------+----------------------------------+
    | Condition (Workflow)             | Decision-points in the business  |
    |                                  | processes programmed into        |
    |                                  | workflow.                        |
    +----------------------------------+----------------------------------+
    | Connectors                       | Stable, reliable connections for |
    |                                  | any API in a customer's          |
    |                                  | environment.                     |
    +----------------------------------+----------------------------------+
    | Context Variables                | Variables that hold a variety of |
    |                                  | contextual information relating  |
    |                                  | to the current playbook, its     |
    |                                  | invocation parameters, and       |
    |                                  | executed actions.                |
    +----------------------------------+----------------------------------+
    | **Dashboard**                    | A visual display of records,     |
    |                                  | reports, and charts associated   |
    |                                  | with the applications in the     |
    |                                  | workspace. A workspace can have  |
    |                                  | multiple dashboards.             |
    +----------------------------------+----------------------------------+
    | **Default Dashboard**            | The dashboard available to a     |
    |                                  | user upon log in. The default is |
    |                                  | administrator-defined.           |
    +----------------------------------+----------------------------------+
    | **Dynamic Value**                | A dynamic value for string       |
    |                                  | property types allows you to add |
    |                                  | context and/or repeats to a      |
    |                                  | playbook property or expression. |
    +----------------------------------+----------------------------------+
    | **Endpoint Detection and         | Case management, low-code        |
    | Response (EDR)**                 | playbooks, solutions, and        |
    |                                  | components that increase         |
    |                                  | security operation center (SOC)  |
    |                                  | team efficiently at              |
    |                                  | machine-speed.                   |
    +----------------------------------+----------------------------------+
    | **Field**                        | A value, or series of values,    |
    |                                  | stored in an application.        |
    +----------------------------------+----------------------------------+
    | **Group**                        | A collection of defined users.   |
    +----------------------------------+----------------------------------+
    | **Integration**                  | One-way or bidirectional         |
    |                                  | communication between two or     |
    |                                  | more systems.                    |
    +----------------------------------+----------------------------------+
    | **Job**                          | The execution of a programmed    |
    |                                  | action, including the inputs and |
    |                                  | resulting outputs from that      |
    |                                  | action. A job is to an action    |
    |                                  | what a playbook run is to a      |
    |                                  | playbook.                        |
    +----------------------------------+----------------------------------+
    | **Swimlane Content**             | Turbine's integrated content     |
    |                                  | distribution platform. Content   |
    |                                  | includes solutions, components,  |
    |                                  | and connectors.                  |
    +----------------------------------+----------------------------------+
    | **Mean-time-to-detect (MTTD)**   | A measure of the average time it |
    |                                  | takes for an organization to     |
    |                                  | detect a security breach or      |
    |                                  | incident.                        |
    +----------------------------------+----------------------------------+
    | **Mean-time-to-respond (MTTR)**  | The time it takes to fully       |
    |                                  | resolve an incident or a         |
    |                                  | security concern and restore     |
    |                                  | systems.                         |
    +----------------------------------+----------------------------------+
    | **Orchestration**                | Security orchestration is the    |
    |                                  | integration of disparate         |
    |                                  | security tools and platforms to  |
    |                                  | enable automated incident        |
    |                                  | response.                        |
    +----------------------------------+----------------------------------+
    | **Playbook**                     | A playbook is a set of rules     |
    |                                  | describing a series of actions   |
    |                                  | to be executed and the set of    |
    |                                  | triggers that should execute     |
    |                                  | those actions.                   |
    +----------------------------------+----------------------------------+
    | **Playbook Action**              | A single task within a playbook. |
    |                                  | The action includes all details  |
    |                                  | necessary for the execution of   |
    |                                  | the task.                        |
    +----------------------------------+----------------------------------+
    | **Playbook Condition**           | Conditional statements coded     |
    |                                  | into an action or trigger within |
    |                                  | a playbook.                      |
    +----------------------------------+----------------------------------+
    | Playbook Input                   | A set of inputs to a playbook    |
    |                                  | that map action properties or    |
    |                                  | triggers.                        |
    +----------------------------------+----------------------------------+
    | Playbook (Nested)                | A playbook that calls another    |
    |                                  | playbook as an action.           |
    +----------------------------------+----------------------------------+
    | Playbook Output                  | Playbook outputs are the         |
    |                                  | promoted responses and/or        |
    |                                  | results from a playbook's        |
    |                                  | actions.                         |
    +----------------------------------+----------------------------------+
    | Playbook (Parent)                | A playbook that calls another    |
    |                                  | playbook.                        |
    +----------------------------------+----------------------------------+
    | Playbook Run                     | The outcome, as well as the      |
    |                                  | activity, of a single execution  |
    |                                  | of a playbook.                   |
    +----------------------------------+----------------------------------+
    | **Pod**                          | A Turbine component that hosts   |
    |                                  | sensors and is capable of        |
    |                                  | funneling issues detected from   |
    |                                  | sensors.                         |
    +----------------------------------+----------------------------------+
    | **Property Types**               | Data types in playbook actions:  |
    |                                  | string, number, integer,         |
    |                                  | Boolean, object, array, null,    |
    |                                  | date, date & time, password,     |
    |                                  | code.                            |
    +----------------------------------+----------------------------------+
    | **Record**                       | A single entry within an         |
    |                                  | application. In Turbine          |
    |                                  | terminology individual cases,    |
    |                                  | events, alarms, alerts, etc. are |
    |                                  | generalized as application       |
    |                                  | records.                         |
    +----------------------------------+----------------------------------+
    | **Remote Agents**                | Allows customers to connect      |
    |                                  | internal applications and        |
    |                                  | systems to Turbine without the   |
    |                                  | need to configure multiple VPNs  |
    |                                  | or complex networks.             |
    +----------------------------------+----------------------------------+
    | **Report**                       | A consolidated list of records.  |
    +----------------------------------+----------------------------------+
    | **Role**                         | A user-defined set of user       |
    |                                  | and/or group permissions.        |
    +----------------------------------+----------------------------------+
    | **Sensor**                       | A conduit programmed to receive  |
    |                                  | and forward event information.   |
    +----------------------------------+----------------------------------+
    | **Security Information and Event | Collects, aggregates, and then   |
    | Management (SIEM)**              | identifies, categorizing and     |
    |                                  | analyzing incidents and events.  |
    +----------------------------------+----------------------------------+
    | **Swimlane Solution Packages     | Use Swimlane Solution Packages   |
    | (SSPs)**                         | (SSPs, file extension .ssp) to   |
    |                                  | import or export a collection of |
    |                                  | playbooks, assets, applications, |
    |                                  | etc. into a Swimlane Turbine     |
    |                                  | system.                          |
    +----------------------------------+----------------------------------+
    | **Trigger**                      | A rule in a playbook describing  |
    |                                  | which events and under what      |
    |                                  | conditions a playbook should     |
    |                                  | execute.                         |
    +----------------------------------+----------------------------------+
    | **User**                         | An account created to enable     |
    |                                  | access to the Turbine UI or API. |
    |                                  | The user role differs from the   |
    |                                  | administrator role in Turbine    |
    |                                  | and typically has limited access |
    |                                  | to administrator role            |
    |                                  | functionality.                   |
    +----------------------------------+----------------------------------+
    | Webhooks                         | Expand actionability by enabling |
    |                                  | products, vendors, and services  |
    |                                  | to push real-time communication  |
    |                                  | into Turbine                     |
    +----------------------------------+----------------------------------+
    | WebSockets                       | Communications between Swimlane  |
    |                                  | Turbine (RabbitMQ) and the       |
    |                                  | remote agents are over           |
    |                                  | TLS-secured WebSockets on port   |
    |                                  | 443. This streamlines the        |
    |                                  | deployment of Turbine and        |
    |                                  | prevents the need for additional |
    |                                  | hostnames or infrastructure.     |
    +----------------------------------+----------------------------------+
    | **Workflow**                     | A series of conditional decision |
    |                                  | points and resulting actions     |
    |                                  | that automate the presentation   |
    |                                  | of record fields and layout.     |
    +----------------------------------+----------------------------------+
    | **Workflow Action**              | A single task within workflow,   |
    |                                  | manually defined to respond to a |
    |                                  | conditional decision point.      |
    +----------------------------------+----------------------------------+
    | **Workflow Condition**           | Decision-points programmed into  |
    |                                  | workflow.                        |
    +----------------------------------+----------------------------------+
    | **Workspace**                    | A customizable area within the   |
    |                                  | Turbine platform where you can   |
    |                                  | organize and access the Turbine  |
    |                                  | tools and features you use on a  |
    |                                  | regular basis. Workspaces can    |
    |                                  | include applications,            |
    |                                  | dashboards, records, reports,    |
    |                                  | and charts.                      |
    +----------------------------------+----------------------------------+
