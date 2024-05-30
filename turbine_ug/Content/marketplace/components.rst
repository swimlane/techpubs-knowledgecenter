.. _vendor-interaction-components:

Components
==========

Components, also known as vendor interaction components (VICs), focus on
the intent of the vendor action. Vendor APIs send data in differing
formats. That data needs to be in common data formats for best
practices. Use components to set an intent, then configure
vendor-specific details.

Turbine components focus on:

-  Ingestion

-  Enrichment

**Why Use Ingestion Components**

Turbine ingestion components get data from third-party tools and
transform that data into appropriate Open Cybersecurity Schema Framework
(OSCF)/Swimlane Object Schema (SOS) objects.

Using ingestion components:

-  Provides preconfigured intents for your playbook framework to reduce
   time building

-  Allows mass data ingestion

-  Uses ingested data downstream in the playbook and/or the promoted
   results for use outside the playbook

**Why Use Enrichment Components**

Turbine enrichment components ingest data from third-party tools and
transform data into appropriate OSCF/SOS objects to improve incident
response investigations for threat hunting.
