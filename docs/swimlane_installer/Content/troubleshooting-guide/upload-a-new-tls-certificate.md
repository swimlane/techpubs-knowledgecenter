Upload a New TLS Certificate
#######

If you've already gone through the setup process once, and you want to
upload new TLS certificates, run this command to restore the ability to
upload new TLS certificates:

kubectl -n default annotate secret kotsadm-tls acceptAnonymousUploads=1

__Important!__ Adding this annotation temporarily creates a
vulnerability for an attacker to maliciously upload TLS certificates.
Once TLS certificates have been uploaded again, the vulnerability goes
away.

After adding the annotation, you will need to restart the kurl proxy
server. The simplest way to do that is to delete the kurl-proxy pod (the
pod will automatically get restarted) with this command:

kubectl delete pods PROXY_SERVER

This command provides you with the name of the kurl-proxy server:

kubectl get pods -A \| grep kurl-proxy \| awk '{print $2}'

After the pod has been restarted, re-direct your browser to
`http://<your_ip>:8800/tls` to see the same page that you did during
the initial installation. Then, load your TLS certificate:

|image1|

Swimlane recommends that you complete this process as soon as possible
in order to avoid anyone from nefariously uploading TLS certificates.
After this process is complete, the vulnerability is closed, and
uploading new TLS certificates will be disallowed again. Please repeat
the steps above in order to upload new TLS certificates.

- |image1| image:: ../Resources/Images/ssl_certificate.png
