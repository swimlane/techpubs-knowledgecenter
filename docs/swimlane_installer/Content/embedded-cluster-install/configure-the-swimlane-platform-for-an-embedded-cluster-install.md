Configure the Swimlane Platform for an Embedded Cluster Install
###############===

When you need to access the SPI UI after the initial install you can
access it by access port 8800 over HTTPS on any node IP (e.g.
https://:8800).

__Note:__ All configuration of the Swimlane Platform Installer and
Swimlane platform must be done through the SPI admin console config
page. Editing or manipulating the underlying Kubernetes resources is not
supported and will not be permanent since they are managed and
controlled by the Swimlane Platform Installer.

To configure the Swimlane platform for an embedded cluster install:

#. On Swimlane Settings, you'll begin setting up your configuration for
   Swimlane. Review and set the following fields as necessary:

-  __Expose the Swimlane Web Service Externally?__ - Enable this option
   when using a Layer 7 load balancer. The Swimlane web service will be
   directly exposed from each node in the cluster on TCP port 4443.
-  __Enable the Ingress Controller__ - Enable this option when using a
   Layer 4 load balancer or for single node lab/test environments. The
   included ingress controller will be used for routing web requests to
   Swimlane on TCP port 443.

   -  __Swimlane Hostname__ - The DNS record pointing to the Swimlane
      Platform Installer and Swimlane platform load balancer.
   -  __Upload a certificate for Swimlane Web?__ - Enable this option to
      upload a certificate and key to be used for the included ingress
      controller. If no certificate is uploaded a self-signed one will
      be generated and used. The certificate must be ASCII encoded X.509
      format. The private key cannot be password protected.

-  __Upload a certificate for Swimlane Web backend?__ - Enable this
   option to upload a certificate and key to be used by the backend
   Swimlane web service. If no certificate is uploaded a self-signed one
   will be used.
-  __Swimlane Web CORS Headers__ - Enable this option to set HTTP
   Cross-Origin Resource Sharing Headers for Swimlane Web. A list of
   options relevant to CORS Headers will appear below and if left blank,
   they will be set with the default values specified next to each
   option. If this option is disabled, no CORS headers will be set for
   Swimlane Web.

   -  __Swimlane Web CORS Header Access-Control-Allow-Origin__ -
      Determine whether to override the value for the `HTTP
      Access-Control-Allow-Origin
      header <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin>`__.
   -  __Swimlane Web CORS Header Access-Control-Allow-Headers__ -
      Determine whether to override the value for the `HTTP
      Access-Control-Allow-Headers
      header <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Headers>`__.
   -  __Swimlane Web CORS Header Access-Control-Allow-Methods__ -
      Determine whether to override the value for the `HTTP
      Access-Control-Allow-Methods
      header <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Methods>`__.

-  __Swimlane Web CSP Header__ - Enable this option to set the HTTP
   Content Security Policy Header for Swimlane Web. A new option will
   appear below to override the CSP header, if left blank it will get
   set to the default value. If this option is disabled, no CSP header
   will be set for Swimlane Web.

   -  __Swimlane Web Content-Security-Policy Header__ - Determine
      whether to override the value for the `HTTP
      Content-Security-Policy
      header <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy>`__.

2. Next, set the logging settings.

   -  __ASP.NET Hosting Environment__ - Set this option to Development
      to have stack traces sent to the browser for 500 errors. Set this
      option to Production to not send them.

   -  __Enable Swimlane Audit Logging__ - Enable this option to log raw
      Swimlane API requests and responses into Swimlane pods.

   -  __Swimlane Logging Level__ - Set this option to specify the
      logging level for Swimlane pods.

3. Determine whether to override the OpenSSL settings for CipherString
   and MinProtocol for outgoing secure connections that originate from
   API and tasks pods.

4. Next, determine whether to enable the Swimlane Syslog Receiver and
   the Selenium ChromeDriver.

5. Next, determine whether you want Mongo to be exposed for external
   access, and whether to upload pip config for API and tasks.

6. If you have third-party certificates for API and tasks, click
   __Upload Additional Trusted Certificates for API and Tasks?__ and
   then browse for and upload your certificates.

7. Next, choose whether to enable or disable a pod liveness probe for
   the API and Tasks pods. The default liveness probe setting for API
   pods is disabled and for Tasks pods is enabled.

8. On Initial MongoDB Settings, enter the appropriate encryption keys
   and passwords for your Swimlane database and MongoDB.

9. Next, if you have 3 or more nodes in your cluster, click __HA
   Environment__ and set the number of pods for each type.

10. If you have an HA cluster, confirm the recommended default settings
    for Web/API/Tasks/Reports AntiAffinity (Soft) and MongoDB Pod
    AntiAffinity (Hard). Then, click __Save config__.

11. When you save the configuration, preflight checks for your
    installation begin.

12. Once the preflight checks process, the Swimlane Installer Admin
    Console opens.
