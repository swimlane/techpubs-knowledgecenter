Agents
======

Remote agents are used to control where actions are run. By assigning
remote agents to pools, then an action to that pool, actions execute on
the remote agent. This allows for actions to execute on remote networks
with access to local resources, without opening networks and firewalls
to remote connections.

**Important!** By default, remote agents are automatically assigned to
the $remote pool during installation. However, when creating an action
in a playbook, the pool that is assigned to the action is $default. To
successfully run an action on a remote agent, you will need to update
the pool from the playbook action. Click `Assigning Agent Pools on the
Playbook Action <#Assignin>`__ for instructions.

Remote agents:

-  Are deployed through a simple bash script.

-  Are configured with arguments to customize functionality.

-  Use Secure Websockets for communication, with event-based job
   dispatching and queueing.

Prerequisites
~~~~~~~~~~~~~

**Note:** Swimlane offers standard install support. However, we cannot
provide OS-level support.

 

Before working with remote agents, ensure you have the following
required software and hardware.

Due to its containerized nature, remote agents may run on many operating
systems. Swimlane directly tests these operating systems for remote
agents:

-  **Ubuntu** 18.04, 20.04, 22.04 (Recommended)

-  **CentOS** 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8-stream

-  **RHEL** 7.4, 7.5, 7.6, 7.7, 7.8,, 8.7, 9.2 7.4, 7.5, 7.6, 7.7, 7.8,
   7.9, 8.0, 8.2, 8.7

-  **Oracle Linux** (with docker) 7.9

-  **Oracle Linux** (with podman) 8.8, 9.2 7.4, 7.5, 7.6, 7.7, 7.8, 7.9
   (`Common Issue
   FAQs <https://docs.oracle.com/en/operating-systems/oracle-linux/podman/podman-KnownIssues.rstl#podman-issues>`__)

-  **Amazon Linux** 2

 

**Note:** Oracle 7.9 does not allow install of podman 4.2+, and cannot
use podman.

Required Software
-----------------

-  Docker (latest version) or Podman 4.2 (or above)

   -  Docker service and client. This does *not* require a license.

   -  `Install for Docker <https://docs.docker.com/engine/install/>`__

   -  `Install for
      Podman <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html-single/building_running_and_managing_containers/index#proc_getting-container-tools_assembly_starting-with-containers>`__

      **Important!** When installing using the podman package, both the
      Podman and Podman-plugins packages are required.!

-  Python 3 (latest)

**Note:** You do not need to perform manual upgrades for remote agents.
The cron job installed when you run the script checks the connected
turbine instance for a new version and updates, if necessary.\ `
 <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html-single/building_running_and_managing_containers/index#proc_getting-container-tools_assembly_starting-with-containers>`__

Minimum Specifications for Remote Agent Work
--------------------------------------------

Remote agent requirements vary depending on the customer’s automation
needs.

Minimum specifications:

-  2 CPUs (x64 architecture)

-  2 GB (or more) ram

-  Disk size will be the minimum needed for your OS choice + 20 GB.

| 

**Tip:** For heavier workloads, more CPU, RAM, and/or disk size may need
to be assigned.

 

-  VM needs outbound access to the Turbine instance and to Quay.io over
   HTTPS (443)

 

**Important!** Whitelist all of quay.io, so you do not restrict images
from access.

Set Up an Argument and Install a Script
---------------------------------------

To set up an argument and install a script:

#. From the navigation menu, click **SETTINGS.**

#. Click **Tenant-Specific**, and then click the Agents tab.

|image1|\ The Agents home page opens and displays the number of agents
and pools.

#. Click **View Agents**.

#. You can filter by name to search for an agent.

   You can toggle **Enabled** to enable or disable the agent.

   | A green circle next to an agent's name indicates the agent is
     online.
   | |image2|

   | A red circle next to an agent's name indicates the agent is
     offline.
   | |image3|

#. From Agents, click **Deploy Agent**.
   |image4|

#. The **Install an agent** window opens.

   **Important!** If you click out of the **Install an agent** window,
   the window closes and you will have to start from **Deploy Agent**
   again.

#. Enter the required and/or customizable fields. The table below
   provides the field names and supplemental information to complete the
   script install process.

Install Agent Fields Table
~~~~~~~~~~~~~~~~~~~~~~~~~~

At the top, you can see the install command. Here are the fields that
you can configure to build your install script:

+-----------------------------------+-----------------------------------+
| **Only Required Field**           | **Information**                   |
+===================================+===================================+
| AGENT_NAME                        | The name of the agent, will       |
|                                   | prompt if not provided (This      |
|                                   | value is prefixed with            |
|                                   | ``agent-``.) Agent name can only  |
|                                   | contain letters, numbers,         |
|                                   | underscores, or hyphens. Do not   |
|                                   | use spaces.                       |
+-----------------------------------+-----------------------------------+
| **Customizable Fields**           | **Information**                   |
+-----------------------------------+-----------------------------------+
| CA_CERT_PATH                      | Path to a folder of CA Certs to   |
|                                   | be mounted for certificate        |
|                                   | validation (helpful for           |
|                                   | self-signed or internal certs).   |
+-----------------------------------+-----------------------------------+
| DOCKER_BIN                        | Path to the Docker executable,    |
|                                   | this script tries to find Docker  |
|                                   | but you can help it if it cannot. |
+-----------------------------------+-----------------------------------+
| AGENT_IMAGE_NAME                  | The Docker Image to use. By       |
|                                   | default it uses the               |
|                                   | publicly-hosted Docker image with |
|                                   | the same version as your          |
|                                   | deployment. Example:              |
|                                   | swimlane/turbine-agent:11.0.      |
+-----------------------------------+-----------------------------------+
| AGENT_HEARTBEAT_INTERVAL          | How often the agent sends a       |
|                                   | heartbeat message. When the       |
|                                   | threshold for the heartbeat is    |
|                                   | exceeded, it is marked unhealthy. |
+-----------------------------------+-----------------------------------+
| AGENT_INITIAL_POOLS               | The initial pools to join. You    |
|                                   | can add more than one.            |
+-----------------------------------+-----------------------------------+
| AGENT_JOB_MAX                     | The maximum number of jobs the    |
|                                   | agent can handle at once.         |
+-----------------------------------+-----------------------------------+
| AGENT_JOB_QUEUE_EXPIRES           | **Seconds** to wait until a job   |
|                                   | on the queue expires. Example: 5  |
|                                   | hours = 18000 seconds.            |
+-----------------------------------+-----------------------------------+
| HTTP_PROXY                        | Add HTTP proxy support for remote |
|                                   | agents. Example:                  |
|                                   | h                                 |
|                                   | ttp://username:password@host:port |
+-----------------------------------+-----------------------------------+
| HTTPS_PROXY                       | Add HTTPS proxy support for       |
|                                   | remote agents. Example:           |
|                                   | ht                                |
|                                   | tps://username:password@host:port |
+-----------------------------------+-----------------------------------+
| NO_PROXY                          | | Comma-delimited list of URLs    |
|                                   |   which may bypass the above      |
|                                   |   proxy settings.                 |
|                                   | | Example:                        |
|                                   |   swimlane.com,google.com         |
+-----------------------------------+-----------------------------------+
| CRON_USER                         | The user that will execute the    |
|                                   | cron job that performs updates to |
|                                   | the agent images. The user needs  |
|                                   | to be able to execute docker      |
|                                   | commands and curl requests. For   |
|                                   | assistance creating a cron user,  |
|                                   | please contact your Linux first   |
|                                   | line of support.                  |
+-----------------------------------+-----------------------------------+
| Join Default Pool                 | Joins the remote agent to the     |
|                                   | $default pool, in addition to the |
|                                   | $remote pool.                     |
+-----------------------------------+-----------------------------------+
| Ignore Insecure Certificates      | Instructs the agent and its       |
|                                   | connectors to ignore insecure     |
|                                   | certificates while connecting to  |
|                                   | HTTPS sources.                    |
+-----------------------------------+-----------------------------------+
| Allow Insecure Certificates for   | Allows an insecure certificate    |
| Gateway Communication             | when connecting to the host       |
|                                   | Turbine instance’s gateway.       |
+-----------------------------------+-----------------------------------+

Example: Blank Agent Window

|image5|

#. To copy the install script, click **Copy install script**, open a
   command prompt/terminal, paste, and run the script.

   **Tip:** The **Ignore Insecure Certificates** turns off certificate
   validation. You can toggle this feature off if you have self-signed
   certs.

   Once you have copied the install script, you can close the window.

   Example: Install Agent Window

   In the video, notice that the AGENT_NAME field is entered because it
   is required. Additional information can be entered but is not
   required. After clicking \**Copy Install Script*\* you can close the
   window.

   |image6|

Log In to the Remote Agent
--------------------------

To log in to the remote agent:

#. Open a cmd/terminal window.

#. The login is root, which is the default, or you can log in as a
   member of the docker group.

**Important!** Systems may require additional configuration with a
non-root user to keep Docker or Podman running after the user’s session
is terminated. Please make sure to consult post-install instructions for
your OS and container engine.

#. `Docker
   Post-Install <https://docs.docker.com/engine/install/linux-postinstall/>`__

   `Podman set
   linger <https://github.com/containers/podman/blob/main/troubleshooting.md#17-rootless-containers-exit-once-the-user-session-exits>`__

#. To set up max_user_namespaces enter this command:

sudo sysctl user.max_user_namespaces=65536

| 

Ensure you do this prior to adding the curl script command in the next
step.

**Important!** User namespaces are used with containers to allow a
container to be set up without privileged operations. Setting up the
maximum allows a normal user to act as root inside a container to
perform administrative tasks, without being root on the host outside.

#. Copy and paste the curl script command into your cmd/terminal window.

**Warning!** If using RHEL or another system using SELinux, use the -R
argument to set the container engine internal user to root, due to
security restrictions.

**Tip:** Reading the curl script can be tricky! Here's some helpful
information: The full copied string contains two commands: The "curl +
K" + the https …” downloads the installation script from your server.
The “bash – “ executes the script with the options you have selected.
These commands may be separated and run separately if you encounter any
connectivity issues that need to be debugged.

#. Click **Enter**.

#. The script runs in the cmd/terminal window.

#. During installation you will be prompted for your Turbine username
   and password. This will authenticate the remote agent to your
   installation and join it using generated keys. Your credentials will
   not be saved.

**Warning!** If you see errors, **read** them! The text communicates any
errors that you need to resolve before successfully running the remote
agent.

#. If there are no errors, the logs display **Done**.

Validate the Remote Agent with Docker commands
----------------------------------------------

Want to ensure your install is successful? Use the docker commands to
validate the remote agent.

+----------------------------------+----------------------------------+
| **Command**                      | **Action**                       |
+==================================+==================================+
| docker ps                        | Lists all running docker         |
|                                  | containers.                      |
+----------------------------------+----------------------------------+
| docker logs --follow             | Gets and follows the logs of a   |
| **container-id** or **name**     | container. Checks for connectors |
|                                  | requesting and installing (do    |
|                                  | not be alarmed if this takes     |
|                                  | some time) CTRL + C = exit       |
+----------------------------------+----------------------------------+
| docker restart **container-id**  | Restarts a container.            |
| or **name**                      |                                  |
+----------------------------------+----------------------------------+
| docker stop **container-id** or  | Stops a container.               |
| **name**                         |                                  |
+----------------------------------+----------------------------------+
| docker rm **container-id** or    | Removes a container.             |
| **name**                         |                                  |
+----------------------------------+----------------------------------+
| check the agent endpoint:        | Verifies the agent endpoint.     |
| https://**installation           |                                  |
| name**/agent                     |                                  |
+----------------------------------+----------------------------------+

**Tip:** When using podman, ensure validation using podman--not Docker.

**Tip:** You can pull logs at anytime using the cmd/terminal window to
see what the agent is doing or verify the relay by running the docker
logs command.

**What if you want to start over completely?**

-  Use the docker stop **container-id** or **name**, then docker rm
   **container-id** or **name** commands.

Assigning Agent Pools on the Playbook Action
--------------------------------------------

Pools allow control over which agents run an action. Pools may contain
multiple agents, and agents may belong to multiple pools.

**Common Scenarios:**

-  You have several isolated networks. Network A has a database required
   for an action, Network B has a SIEM system that needs to be queried.
   By installing two remote agents, and assigning them to separate
   pools, the actions that require those resources will be available to
   the actions running on the remote agents

-  You want to be sure that your remote agents are highly available. By
   installing several remote agents on different VMs across availability
   zones, then assigning those to the same pool, actions requiring those
   agents will be able to run in several availability zones.

You can assign a pool to an action. To create an action, see
`Actions <../playbooks/actions/actions.rst>`__. To assign a pool at the
action-level:

#. From ACTION, click the **Show advanced settings** drop-down.
   |image7|

#. | **$default** is the default pool.
   | |image8|

#. To change the pool, click the drop-down and select from the available
   pool options.
   |image9|

#. Now the action will run in the selected pool.

   **Important!** Transformation and Python actions do not function with
   remote agents.

WebSockets
----------

Communications between Swimlane Turbine (RabbitMQ) and the remote agents
are over TLS-secured WebSockets on port 443. This streamlines the
deployment of Turbine and prevents the need for additional hostnames or
infrastructure.

.. |image1| image:: ../Resources/Images/admin_panel.png
.. |image2| image:: ../Resources/Images/agents-online-agent.png
.. |image3| image:: ../Resources/Images/agents-offline-agent.png
.. |image4| image:: ../Resources/Images/deploy-agent-button.png
.. |image5| image:: ../Resources/Images/blank-install-agent-window.gif
.. |image6| image:: ../Resources/Images/example-install-agent-window.gif
.. |image7| image:: ../Resources/Images/show-advanced-settings-dropdown.png
.. |image8| image:: ../Resources/Images/default-pool-option.png
.. |image9| image:: ../Resources/Images/pool-options-list.png
