Collaboration Extension
=======================

Overview
--------

The Collaboration Extension is a collection of bundled components to
create context-aware messages from predefined templates to send to
external messaging systems, such as email, Slack, and/or Microsoft Teams
for processing by Swimlane, or non-Swimlane, users. These messages can
trigger an action based on an arbitrary amount of user-defined choices,
such as **Approve**, **Confirm**, **Deny**, or **Request Contact**. In
this way, non-Swimlane users can participate in security workflows by
responding to Turbine generated messages.

Capabilities
------------

The Collaboration Extension can: 

-  | Craft message templates in the **Collaboration Template Manager**
     application using mustache syntax.
   | Example: {{Field Display Name}}

-  Drag and drop the **Collaboration Extension Applet** into any
   application for your use case.

-  Load, modify, and manage the resulting message in the **Collaboration
   Extension Applet** before sending (or send) the message automatically
   after loading.

-  Use the dedicated and re-usable **Collaboration Message Sender**
   application designed to send messages over a variety of communication
   channels (Slack, MS Teams, email) and handle action-button responses
   from the recipient.

-  Send messages to one or multiple recipients across one or multiple
   communication channels.

Common Use Case Examples
------------------------

Some common use cases for Collaboration Extension include:

**Practitioner Event Notification**

Notify a team of practitioners (e.g., security analysts, vulnerability
analysts) across a desired communication channel (Slack, MS Teams,
email) that an activity has occurred. Examples of possible activities
are: specific alerts being generated, cases reaching desired
checkpoints, or a new vulnerability being detected.

**User-Centric Triage**

Practitioners can automatically, or on an ad-hoc basis, send details of
some observed activity to non-Swimlane users. The message can include
buttons that the recipient may choose between. Clicking these buttons
informs the invoking record in Turbine and facilitates further
automation as desired.

**Action Approvals**

When approval is required to perform an impactful automated action, the
Collaboration Extension provides for a pathway to request and receive
that approval from a decision-maker, without additional Swimlane
practitioner intervention.

**Sending Confirmation of Receipt Messages**

Send a message to a non-Swimlane user that something has been received
in Turbine. For example, this can be useful to auto-reply when a
phishing email is submitted to the security team.

.. toctree::
   :titlesonly:
   :caption: Children:

   /Content/marketplace/install-and-configure-collaboration-extension
   /Content/marketplace/configure-webhooks
   /Content/marketplace/configure-collaboration-extension-template
   /Content/marketplace/select-template-and-send-a-message
