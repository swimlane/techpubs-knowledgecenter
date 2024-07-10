Server Architecture Overview
============================

Swimlane is an advanced modern application that makes use of leading
database and server technology. The Swimlane server is made up of
several services which can be installed on a single server or separate
servers. Additionally, each component can be distributed across multiple
servers for increased throughput and high availability. For more
information about distributing Swimlane, contact Swimlane support.

The components of the Swimlane server are:

-  **MongoDB:** document storage database, permissions database
-  **Swimlane Web Server:** serves the Swimlane web application and API
   via IIS
-  **Swimlane Tasks Service**: processes background Swimlane jobs such
   as integrations, outgoing email, and Active Directory sync

+> **Note:** For more information on a secure MongoDB deployment,
consult `MongoDB's security
documentation <https://docs.mongodb.com/manual/security/>`__.
