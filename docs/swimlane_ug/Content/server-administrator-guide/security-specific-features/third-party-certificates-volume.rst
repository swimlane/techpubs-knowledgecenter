Third-Party Certificates Volume
===============================

Use the information in this topic if you need to allow Swimlane
integrations and services to trust a custom certificate authority.

The third-party certificates volume can be utilized by commenting out
the ``volumes`` key on the api and tasks containers in
``docker-compose.override.yml``.

Specify the path to a local directory on the host that contains the
files you wish to share with the tasks service.

On each start of the api and tasks services, run
``update-ca-certificates`` to import the certificates.

The api and tasks containers will need to be restarted for the changes
to take affect if new certs are added.

See the following example:

sw_api: volumes: -
/opt/swimlane/ca-certs/:/usr/local/share/ca-certificates/swimlane/
sw_tasks: volumes: -
/opt/swimlane/ca-certs/:/usr/local/share/ca-certificates/swimlane/
