Testing Connections in Directory Services
=========================================

If Test Connection fails when you're setting up Active Directory or Open
LDAP Directory Services, you can troubleshoot to establish TCP/IP and
LDAP connectivity to the directory server. This involves double-checking
the validity of all four of the Server Settings parameters, and it may
also involve repeated trial-and-error connection attempts until the test
connection operation succeeds.

Remember, you can't access the **Test Connection** button until after
you save!

It may also be necessary to:

-  Confirm that the chosen directory user has sufficient privilege for
   the Swimlane Platform’s need to connect and traverse the Directory
   tree.

-  Disable any firewall that is blocking access to the directory server.

**Note:** If your Directory Services domain name collides with a name
that is registered publicly on the Internet (e.g. example.com), then the
test connection may report a false-positive success.
