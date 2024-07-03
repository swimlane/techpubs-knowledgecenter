Install and Configure SOC Solutions Bundle
==========================================

The SOC Solutions Bundle is a solution bundle that is made of four
smaller, interconnected solutions: Phishing Triage, Alert Triage, Threat
Intelligence (TI), and Case and Incident Management (CIM). For
additional information, navigate to `SOC Solutions
Bundle <https://docs.swimlane.com/turbine/marketplace/soc-solutions-bundle.htm>`__.

**Note:** This installation and configuration documentation is for the
Canvas version of the SOC Solutions Bundle only.

Important Definitions
---------------------

-  Ingestion Component - A component or set of components that:

   -  Interact with a vendor endpoint, such as run a SIEM search, look
      up observable reputation, or initiate a remediation action

   -  Normalize inputs and outputs using interfaces to enable swappable
      component usage

   -  Convert various 3rd-party alerts, reputations, emails, and so on
      to a common schema for use in Turbine solutions such as SOC
      Solutions

-  Turbine Extendable Data Schema (TEDS) - Turbine's native common
   schema for interacting with alerts, emails, reputations, and so on.

Install from Library
--------------------

Follow these steps:

#. Navigate to the **Swimlane Content Library**

   a. From your desired tenant, click Library

   b. Click Swimlane Content

#. Install SOC Solutions Bundle

   a. Select SOC Solutions Bundle from the list of Solutions

   b. Click **Install** on the solution

      |image1|

   c. You may be prompted to overwrite content if some content already
      exists in your environment.

      i. You can avoid overwriting content by deselecting the items you
         do not wish to overwrite, and it will still work. But if you
         deselect too many items that are not being overwritten, you
         will not import the full solution.

Once you have installed the SOC Solutions Bundle, it is time to
configure it to ingest data from your tools for your use cases.

#. For SIEM, XDR, or EDR Alert Triage, see `Configure Alert
   (SIEM/XDR/EDR/etc.) Ingestion <#_1mxsclv3kib0>`__.

#. For Phishing Triage, see `Configure Phishing Email
   Ingestion <#_1wzxmulze8zo>`__.

#. Once you have configured one or more alert sources, you will want to
   add Threat Intelligence to enhance your observables. See `Configure
   Threat Intelligence Enrichment Integration <#_kn9nuvdd2wax>`__.

#. Now that you have events flowing into the Case and Incident
   Management (CIM) application, you will want to configure advanced
   Hero AI features. See `Configure Hero AI <#_hr8226vbbdts>`__.

#. Lastly, you may want to configure CIM for your particular needs. See
   `Case and Incident Management
   Application <https://docs.swimlane.com/turbine/marketplace/case-and-incident-management-application.htm>`__.

Configure Alert (SIEM/XDR/EDR/etc.) Ingestion
---------------------------------------------

Alert ingestion is performed either by a `pull
action <#_6t597gg3xine>`__ using a `Ingestion
Component <#_ac3f7v1gtcsz>`__, or using a push action using a webhook.
Ingestion Components use Turbine connectors, assets, and Turbine logic
to ingest alerts from various products, and then format those alerts as
`Turbine Extendable Data Schema <#_ac3f7v1gtcsz>`__ (TEDS) objects. TEDS
provides a standardized set of common fields used by most products that
generate alerts. `Webhook ingestion <#_j9e640gooiil>`__ usually does not
use connectors or assets, but uses Turbine logic to convert a webhook
sent to Turbine into a TEDS alert.

Configuring the Default Alert Ingestion Flow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To configure the default Alert Ingestion Flow, perform the following
steps:

#. Install your product's Alert Ingestion Component from the Content
   Library.

#. Navigate to Playbooks.

#. Open the PT - Bulk Ingest Alerts playbook.

#. Find the Placeholder action node and select it.

#. | Select the **Component** dropdown menu and choose your Component.
   | |image2|

#. Save the Playbook.

Adding a New Alert Ingestion Component (Pull Alerts)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Navigate to Playbooks

   If your tenant has both Classic and Canvas playbooks, this menu will
   be “Playbooks (NEW)”.

   .

#. Open the Bulk Ingest Alerts Playbook.

#. Add a schedule/cron trigger .

#. From the Components menu, drag an ingestion component below the
   scheduled trigger.

#. Click Edit on the component to edit input variables, such as start
   time and organization.

   a. | start_time takes human-readable parameters, such as "-1 day" or
        "10 minutes ago".
      | |image3|

#. Add the Process Bulk Alerts component beneath the ingestion
   component.

#. Click Edit on the Process Bulk Alerts component.

#. | Choose the component’s "Alerts" output and map into the "Alerts"
     field on Process Bulk Alerts.
   | |image4|

#. Ensure that your ingestion source's asset is configured on the Assets
   page.

|image5|

Adding a New Alert Ingestion Webhook (Push Alert)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Splunk Webhooks
^^^^^^^^^^^^^^^

Splunk webhooks work differently from most webhooks in that they send
information about a saved search that you then have to query in Splunk
to get individual alerts. To ingest Splunk webhooks, use the Splunk
Webhook Ingestion component.

Most Other Webhooks
^^^^^^^^^^^^^^^^^^^

#. Open the Webhook Ingest Alert playbook and retrieve the Webhook URL.

#. In your SIEM, configure the webhook option to point at the Webhook
   URL.

#. Edit the Process Webhook Data action and perform the following:

   a. Map any locations in your event.body that contain observables you
      wish to extract to the Identify Observable Locations array block.

   b. For all other action blocks, map the value from your webhook event
      body to the appropriate block, e.g., Alert Categories, Alert
      Description, Alert Risk Score, Alert Rules, and so on.

      #. | Each block tells you what data type it expects in the comment
           section, i.e. String, Attack Array, Detection Rule Array,
           Number.

|image6|

Configure Phishing Email Ingestion
----------------------------------

Phishing Email Ingestion is performed with a Pull action against a
monitored inbox. Users forward suspicious emails to the monitored inbox
and Turbine will pull it from there. The expected format of an ingested
phishing email is an email from a user reporting the phishing attempt
with a RFC822-compliant attachment containing the phishing email itself.

Configuring the Default Phishing Email Ingestion Flow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To configure the default Phishing Email Ingestion Flow, perform the
following steps:

#. Install your product's Phishing Component from the Content Library.

#. Navigate to Playbooks.

#. Open the PT - Bulk Ingest Phishing Emails playbook.

#. Find the Placeholder action node and select it.

#. | Select the Component dropdown menu and choose your Component.
   | |image7|

#. Save the playbook.

Configuring a New Phishing Email Ingestion Flow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To create a new Phishing Email Ingestion flow, perform the following
steps:

#. Navigate to Playbooks.

#. Open the PT - Bulk Ingest Phishing Emails playbook.

#. Create a cron trigger.

#. Drag and drop a Phishing Triage component under the cron trigger.

   a. Don't forget to configure the asset for your Phishing Triage
      component and edit its inputs.

      |image8|

   b. The Phishing Triage components default to extracting the phishing
      email from an RFC822 .eml attachment on a reporting email.

#. Drag and drop the Execute - Process Bulk Phishing Emails component
   beneath the Phishing Triage component.

   a. | Map the Phishing Email Reports object from the Phishing Triage
        component to the Emails input of this component.
      | |image9|
      | |image10|
      | |image11|

Configure Threat Intelligence Enrichment Integration
----------------------------------------------------

Threat Intelligence Enrichment gathers reputation information from
observables, such as IP addresses, domains, URLs, hashes, email
addresses, and so on from one or more enrichment providers using
enrichment components. Results are aggregated in Threat Intelligence
records, and displayed in Case and Incident Management records as
well. Every observable type has a Primary Intelligence Provider (PIP),
which is the canonical source of truth for reputation verdict,
permalinks, and so on for that observable type.

#. Navigate to Components.

#. Open the Enrich - Enrich Observable component.

#. Edit the components under the Parallel node:

   a. Remove any enrichment sources you are not using.

   b. Add new enrichment sources from the Components menu.

      #. | Click "Edit" and map in "inputs.observable" as a playbook
           property for each new enrichment source.
         | |image12|

   c. | After removing or adding new enrichment sources, edit the
        Aggregate Enrichments action to reflect the changes you have
        made. Each component's Enrichments property should be mapped to
        an append action in the Aggregate Enrichments action.
      | |image13|

      #. Hint: Any append action whose target is $DELETED must be
         removed.

#. Ensure that your enrichment assets are configured on the Assets page.

Configure Hero AI Asset
-----------------------

Before using the Hero AI features that use the Swimlane LLM, such as
`Case Summarization and Recommended
Actions <https://docs.swimlane.com/turbine/marketplace/case-and-incident-management-application.htm>`__,
you must configure the Hero AI Asset with your account credentials.

#. Navigate to **Orchestration** -> **Assets**.

#. Open the Swimlane Hero AI asset.

#. Input the following:

   a. URL.

      i. This should be the same URL as your Turbine Cloud instance, for
         example,
         `https://us1.swimlane.app. <https://us1.swimlane.app/>`__

   b. Account ID (for example, 2604b9cd-38d8-450e-9e6d-e5338fa7d265).

   c. PAT (Turbine user `Personal Access
      Token <https://docs.swimlane.com/turbine/introduction/customize-your-user-profile.htm#:~:text=Creating%20a%20Personal%20Access%20Token>`__
      from the admin console).

|image14|

Configure Included Assets
-------------------------

In order to use 3rd party tools for ingestion, enrichment, and so on,
you must configure the assets for the tools you wish to use:

#. Navigate to **Orchestration** -> **Assets**.

#. Configure all supplied assets for 3rd-party technologies you wish to
   use, i.e. VirusTotal, Recorded Future, Abuse.ch URLHaus,
   IPQualityScore.

Configure Custom Assets
-----------------------

The SOC Solutions Bundle contains a number of custom assets whose
purpose is to allow you to configure variables used in one or more
playbooks or components without having to edit those playbooks or
components directly:

#. Open the Observable Parser Ignore Lists asset.

   a. Enter CSV lists of IP CIDR ranges and Domains you wish to exclude
      from observable ingestion, for example.:

      i.  mycompany.com, outlook.com, swimlane.com, o365.com.

      ii. 10.0.0.0/8, 192.168.0.0/16, 172.16.0.0/12.\ |image15|

#. Open the TI Primary Intelligence Providers asset.

   a. | If you wish to change the primary provider for any TI types, do
        so here.
      | |image16|

**Note:** These must be valid and configured enrichment sources. For
more information, see `Configure Threat Intelligence Enrichment
Integration. <#_kn9nuvdd2wax>`__

Configure Custom Case and Incident Management Data Mappings
-----------------------------------------------------------

Because TEDS relies on the most common attributes for a given object
type, such as alerts, there are vendor-specific fields that are not
mapped in TEDS objects. In order to map these fields to Case and
Incident Management (CIM) records, you will need to use the SOC -
Extract Raw Alert Fields to CIM playbook to pluck values from the raw
alert object included in the TEDS object and record, and write those
values to fields you have created in the CIM application. There are two
ways to do this:

Option 1 - Discrete Mappings (Native Transformations)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For each vendor-specific field you wish to add to CIM:

#. Create a new field of the appropriate type in the CIM application.

#. Edit the Extract Raw Alert Fields to CIM playbook.

#. Edit the Extract Fields action and, for each field you wish to
   extract to CIM:

   a. Create a Transformation Block.

   b. Use the Get Value By Key transformation to extract the data from
      the raw alert body.

      i. For Property, select the Evaluate Raw Alert > Raw Alert
         playbook data.

   c. Add your created fields into the Write to CIM Record action under
      Update Fields and map the appropriate transformation values for
      each field.

| |image17|
| |image18|

Option 2 - Bulk Mappings (Advanced Transformations)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Create fields of the appropriate types in `the CIM
   application <https://docs.swimlane.com/turbine/marketplace/case-and-incident-management-application.htm>`__
   to store your mappings.

#. Create an advanced Transformation Block in the Extract Fields action.

#. | Create a JSON object that follows the format:
   | ``"key-name": actions.Evaluate_Raw_Alert.result.raw_alert.'key-name'``
   | for each key you wish to map to the CIM record.

#. Map this object as a playbook property to Write to CIM Record ->
   Update Fields.

| |image19|
| |image20|

Case and Incident Management Data Mappings - Walk through
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: iframe

   You need to enable JavaScript to run this app.

   .. container::
      :name: root

.. |image1| image:: ../Resources/Images/Install%20and%20Configure%20SOC%20Solutions%20for%20Canvas/Install%20and%20Configure%20SOC.png
   :class: img_1
.. |image2| image:: ../Resources/Images/Install%20and%20Configure%20SOC%20Solutions%20for%20Canvas/Install%20and%20Configure%20SOC_1.png
   :class: img_2
.. |image3| image:: ../Resources/Images/Install%20and%20Configure%20SOC%20Solutions%20for%20Canvas/Install%20and%20Configure%20SOC_2.png
   :class: img_3
.. |image4| image:: ../Resources/Images/Install%20and%20Configure%20SOC%20Solutions%20for%20Canvas/Install%20and%20Configure%20SOC_3.png
   :class: img_4
.. |image5| image:: ../Resources/Images/Install%20and%20Configure%20SOC%20Solutions%20for%20Canvas/Install%20and%20Configure%20SOC_4.png
   :class: img_5
.. |image6| image:: ../Resources/Images/Install%20and%20Configure%20SOC%20Solutions%20for%20Canvas/Install%20and%20Configure%20SOC_5.png
   :class: img_6
.. |image7| image:: ../Resources/Images/Install%20and%20Configure%20SOC%20Solutions%20for%20Canvas/Install%20and%20Configure%20SOC_6.png
   :class: img_7
.. |image8| image:: ../Resources/Images/Install%20and%20Configure%20SOC%20Solutions%20for%20Canvas/Install%20and%20Configure%20SOC_7.png
   :class: img_8
.. |image9| image:: ../Resources/Images/Install%20and%20Configure%20SOC%20Solutions%20for%20Canvas/Install%20and%20Configure%20SOC_8.png
   :class: img_9
.. |image10| image:: ../Resources/Images/Install%20and%20Configure%20SOC%20Solutions%20for%20Canvas/Install%20and%20Configure%20SOC_9.png
   :class: img_10
.. |image11| image:: ../Resources/Images/Install%20and%20Configure%20SOC%20Solutions%20for%20Canvas/Install%20and%20Configure%20SOC_10.png
   :class: img_11
.. |image12| image:: ../Resources/Images/Install%20and%20Configure%20SOC%20Solutions%20for%20Canvas/Install%20and%20Configure%20SOC_11.png
   :class: img_12
.. |image13| image:: ../Resources/Images/Install%20and%20Configure%20SOC%20Solutions%20for%20Canvas/Install%20and%20Configure%20SOC_12.png
   :class: img_13
.. |image14| image:: ../Resources/Images/Install%20and%20Configure%20SOC%20Solutions%20for%20Canvas/Install%20and%20Configure%20SOC_13.png
   :class: img_14
.. |image15| image:: ../Resources/Images/Install%20and%20Configure%20SOC%20Solutions%20for%20Canvas/Install%20and%20Configure%20SOC_14.png
   :class: img_15
.. |image16| image:: ../Resources/Images/Install%20and%20Configure%20SOC%20Solutions%20for%20Canvas/Install%20and%20Configure%20SOC_15.png
   :class: img_16
.. |image17| image:: ../Resources/Images/Install%20and%20Configure%20SOC%20Solutions%20for%20Canvas/Install%20and%20Configure%20SOC_16.png
   :class: img_17
.. |image18| image:: ../Resources/Images/Install%20and%20Configure%20SOC%20Solutions%20for%20Canvas/Install%20and%20Configure%20SOC_17.png
   :class: img_18
.. |image19| image:: ../Resources/Images/Install%20and%20Configure%20SOC%20Solutions%20for%20Canvas/Install%20and%20Configure%20SOC_18.png
   :class: img_19
.. |image20| image:: ../Resources/Images/Install%20and%20Configure%20SOC%20Solutions%20for%20Canvas/Install%20and%20Configure%20SOC_19.png
   :class: img_20
