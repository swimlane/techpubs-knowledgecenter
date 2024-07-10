Transport Encryption
====================

Care should be taken to ensure Swimlane traffic cannot be intercepted in
transit. Swimlane web traffic should be secured in transit using TLS/SSL
in IIS.

If a single Swimlane server deployment is used, the database ports of
2424, 2480, and 27017 can be blocked to restrict external database
access. If MongoDB is located on a separate server, or if multiple
database servers are used, consider using TLS/SSL for transport
encryption of data in transit between the database servers and the
Swimlane servers.

**More Information**

-  MongoDB's TLS/SSL documentation
