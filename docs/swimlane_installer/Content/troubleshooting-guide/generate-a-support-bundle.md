Generate a Support Bundle
######=

If you're having issues with the Swimlane Platform Installer (SPI), your
Swimlane support representative will likely ask you to generate a
support bundle to identify the diagnostics for your issue.

Support bundles contain logs from all relevant pods, as well as other
useful information from your deployment.

Airgapped Deployments
##########-

Use these instructions for an airgapped deployment.

Before you begin generating a support bundle you must first ensure that
you have the support-bundle command installed.

Install the Support-Bundle Command
########################~~

If you have already installed the support-bundle command, you can skip
these steps.

To install the support-bundle command:

#. From a computer that is connected to the internet run:

   curl -o support-bundle https://krew.sh/support-bundle curl -o
   spec.yaml https://kots.io -H
   'User-agent:Replicated_Troubleshoot/v1beta1'

#. Move the files to the server:

   scp support-bundle <server>:/path/ scp spec.yaml <server>:/path/

#. Next, connect to the airgapped server and make the support-bundle
   file executable:

   chmod 777 support-bundle

#. Execute the installer for support-bundle:

   ./support-bundle

#. Finally, generate the support bundle:

   kubectl support-bundle /path/to/spec.yaml

   A support bundle is created in the directory from which you ran the
   command:

   support-bundle-2021-01-19T17_20_56.tar.gz

#. Give this support bundle to Swimlane support.

Generating a Support Bundle with CLI (Airgap)
#################################~

To generate a support bundle with CLI (Airgap):

#. Log in to SPI, and connect to the server.

#. Run this support-bundle command:

   kubectl support-bundle
   secret/default/kotsadm-swimlane-platform-supportbundle
   --redactors=configmap/default/kotsadm-redact-spec/redact-spec,configmap/default/kotsadm-swimlane-platform-redact-spec/redact-spec

   If this command throws the following error, it means that a
   support-bundle file has been saved in the directory from which the
   commands were run:

   $ kubectl support-bundle
   secret/default/kotsadm-swimlane-platform-supportbundle \_ failed to
   run collector "run/ping-google": timeout \_ Failed to upload support
   bundle: execute request: Put
   "https://<swimlane-url>:8800/api/v1/troubleshoot/1n7plYfeeXJCdYH31LhYACWdVun/xjt595pdcr6m6fvts8wnbpbltbms6hhb":
   dial tcp [::1]:8800: connect: connection refused

   If you do not have the support-bundle command, see `Install the
   Support-Bundle Command <#Install>`__.

3. The support bundle uploads to your Swimlane Platform Installer UI.

4. From the Swimlane Platform Installer UI, click Dashboard and then
   open the Troubleshoot tab.

5. On Troubleshoot, click __Download bundle__.

6. Deliver the downloaded file to Swimlane support.

Online Deployments
########--

Use these instructions for an online deployment that is connected to the
internet.

Before you begin generating a support bundle you must first ensure that
you have the support-bundle command installed. See `Install the
Support-Bundle Command <#Install>`__ for details.

Generating a Support Bundle with CLI (Online)
#################################~

To generate a support bundle with CLI (Online):

#. Log in to SPI, and connect to the server.

#. | Run this support-bundle command:

#. curl https://krew.sh/support-bundle \| bash

3. Generate the support bundle by running this command: kubectl
   support-bundle secret/default/kotsadm-swimlane-platform-supportbundle

4. The support bundle uploads to your Swimlane Platform Installer UI.

5. From the Swimlane Platform Installer UI, click Dashboard and then
   open the Troubleshoot tab.

6. On Troubleshoot, click __Download bundle__.

7. Deliver the downloaded file to Swimlane support.

Generating a Support Bundle Through the SPI UI
######################--

Use these instructions to get a support bundle from the SPI UI.

#. Log in to the Swimlane Platform Installer UI.

#. From the Swimlane Platform Installer UI, click Dashboard and then
   open the Troubleshoot tab.
   If you do not have the support-bundle command, see `Install the
   Support-Bundle Command <#Install>`__.

#. On the Troubleshoot tab, click __Analyze Swimlane__.

4. To view the content of the support bundle, click the File Inspector
   tab.

5. To download the support bundle, click __Download bundle__.

6. Deliver the downloaded file to Swimlane support.
