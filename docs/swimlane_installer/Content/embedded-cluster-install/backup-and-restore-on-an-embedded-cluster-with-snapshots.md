Backup and Restore on an Embedded Cluster with Snapshots
##############

The Swimlane Platform Installer (SPI) uses snapshots to backup and
restore your Swimlane platform and data.

| __Important!__ Note the following items that list limitations with
  snapshots:
| By default, snapshots are stored locally on the cluster. For
  production environments, snapshots should be changed to be stored
  externally so that a total cluster outage does not result in the loss
  of snapshots.
| Taking a snapshot requires enough free disk space for a compressed
  archive of the Swimlane database to be saved in ephemeral storage
  before it is uploaded to the snapshot destination. Free disk space on
  the cluster at `/var/lib/kubelet` should be greater than or equal to
  the size of the uncompressed database to ensure there is no disk
  pressure during the snapshot process.
| Instance snapshots are considered complete and are usable in disaster
  recovery scenarios. Application snapshots are the legacy snapshot
  method and are not usable for disaster recovery. Instance snapshots
  can be used in place of the legacy application snapshots.
| Snapshots cannot be restored to a different Operating System than when
  the snapshot was taken. For example, cluster snapshots based on CentOS
  cannot be restored to clusters based on Ubuntu.
| Snapshots cannot be restored to different installation methods. For
  example, online cluster snapshots cannot be restored to offline
  clusters.
| AWS S3 buckets with a bucket policy that requires the server-side
  encryption header are not supported. If you need to require
  server-side encryption for objects, Swimlane recommends that you
  enable default encryption on the bucket itself instead.
| Cleanup and removal of snapshots can only be done through the SPI
  admin console snapshots tab. Removing data from the snapshot storage
  itself will result in data corruption and loss of snapshots.

Configure Snapshot Storage
############--

From the top-level SPI UI, click the __Snapshots__ section and then
click __Settings__ (on the lower right side of the screen).

|image1|

Storing Snapshots on Amazon S3
##############--

|image2|

Requirements
#########

Storing snapshots on Amazon S3 requires:

-  An IAM user or IAM role to authenticate.

-  The bucket cannot have a bucket policy that requires the server-side
   encryption header. The recommended method to require server side
   encryption for objects is to enable default encryption on the bucket
   itself instead.

-  The following sample policy can be used after replacing `${BUCKET}`
   with the AWS ARN of your bucket:

   Sample IAM Policy

   { "Version": "2012-10-17", "Statement": [ { "Effect": "Allow",
   "Action": [ "s3:GetObject", "s3:DeleteObject", "s3:PutObject",
   "s3:AbortMultipartUpload", "s3:ListMultipartUploadParts" ],
   "Resource": [ "arn:aws:s3:::${BUCKET}/\_" ] }, { "Effect": "Allow",
   "Action": [ "s3:ListBucket" ], "Resource": [ "arn:aws:s3:::${BUCKET}"
   ] } ] }

Instructions
#########

#. Change the __Destination__ drop down to __Amazon S3__.

#. Set __Bucket__ to the name of the Amazon S3 bucket to store snapshots
   in.

#. Set __Region__ to the name of the AWS region that the S3 bucket is
   in.

#. Set __Path__ to the path in the S3 bucket that the snapshots should
   be stored under.

#. If your cluster nodes are AWS EC2 instances and you want the AWS
   permissions to access the S3 bucket managed by an IAM instance role,
   check the __Use IAM Instance Role__ checkbox and leave the __Access
   Key ID__ and __Access Key Secret__ fields blank.

#. If you need to use IAM credentials to access the S3 bucket then set
   __Access Key ID__ and __Access Key Secret__ to the IAM user's API
   credentials.

Storing Snapshots on Azure Blob Storage
##################---

|image3|

- _requirements-1:

Requirements
#########

Storing snapshots on Azure Blog Storage requires:

-  An Azure service principal and client secret to authenticate.
-  The storage account and service principal must be in the same
   subscription, tenant, and resource group.
-  Required service principal permissions:

   -  The service principal must have the
      `Storage Account Key Operator Service Role` role on the storage
      account.
   -  The service principal must have the
      `Storage Blob Data Contributor` role on the storage container.

- _instructions-1:

Instructions
#########

#. Change the __Destination__ drop down to __Azure Blob Storage__.

#. Configure your Azure settings:

Storing Snapshots on Google Cloud Storage
####################-

|image4|

- _requirements-2:

Requirements
#########

Storing snapshots on Google Cloud Storage requires:

-  Requires a Google Cloud service account to authenticate.
-  The service account should have the `storage.objectAdmin` role on
   the bucket.

- _instructions-2:

Instructions
#########

#. Change the __Destination__ drop down to __Google Cloud Storage__.

#. Set __Bucket__ to the name of the Google storage bucket to store
   snapshots in.

#. Set __Path__ to the path in the bucket that the snapshots should be
   stored under.

#. If your cluster nodes are Google Cloud VMs and you want the AWS
   permissions to access the Google Cloud Storage bucket managed by an
   IAM instance role, check the __Use IAM Instance Role__ checkbox and
   leave the __JSON File__ field blank.

#. If you need to use IAM credentials to access the Google Cloud Storage
   bucket then set __JSON File__ to the JSON key for the service
   account.

Storing Snapshots on a Host Path
################

|image5|

- _requirements-3:

Requirements
#########

Storing snapshots on a Host Path requires:

-  The host path storage destination should not be used for production
   environments. They provide a security risk and the snapshots are not
   stored externally. Restoration will not be possible in the event of a
   total cluster loss.
-  The host path must be a dedicated directory. Do not use a partition
   used by a service like Docker or Kubernetes for ephemeral storage.
-  The host path directory specified must exist on every node that the
   SPI pods can be scheduled on to ensure snapshots work even if pod
   scheduling changes.
-  The host path directory must be read-writable by the user:group
   1001:1001
-  Host path cannot be used if your cluster requires pods to have
   resources, service account, affinity, node selectors, or tolerations
   defined.

   -  This option creates a Minio deployment in the namespace that
      Swimlane is installed under to handle passing the snapshot data to
      the host path. Swimlane does not support changing any of those
      settings for this deployment.

- _instructions-3:

Instructions
#########

#. Change the __Destination__ drop down to __Host Path__.
#. Set __Host Path__ to the directory on the cluster nodes that the
   snapshots should be stored under.

Storing Snapshots on NFS
############

|image6|

- _requirements-4:

Requirements
#########

Storing snapshots on NFS requires:

-  Supports NFSv3 and NFSv4.
-  Host/IP authentication must be used as username and password
   authentication is not supported.
-  The NFS server must be configured to allow access from all the nodes
   in the cluster.
-  The NFS directory must be owned by the user:group 1001:1001.
-  The target directory needs to be read-writable by the user:group
   1001:1001
-  All the nodes in the cluster must have the necessary NFS client
   packages installed to be able to communicate with the NFS server. For
   example, the nfs-common package is a common package used on Ubuntu.
-  Any firewalls must allow traffic between the NFS server and clients
-  NFS cannot be used if your cluster requires pods to have resources,
   service account, affinity, node selectors, or tolerations defined.

   -  This option creates a Minio deployment in the namespace that
      Swimlane is installed under to handle passing the snapshot data to
      the host path and it is not currently supported to change any of
      those settings for this deployment.

- _instructions-4:

Instructions
#########

#. Change the __Destination__ drop down to __Network File System
   (NFS)__.
#. Set __Server__ to the hostname or IP of the NFS server.
#. Set __Path__ to the path on the NFS server that the snapshots should
   be stored under.

Storing Snapshots on Other S3-compatible Provider
########################-

|image7|

- _requirements-5:

Requirements
#########

Storing snapshots on an S3-Compatible Provider requires:

-  An S3-compatible provider like `min.io <https://min.io/>`__.
-  The S3-compatible provider should be installed separately from the
   cluster nodes that Swimlane is installed on to ensure that snapshots
   are stored externally from the cluster so they can be retrieved in
   the event of a total cluster loss.

- _instructions-5:

Instructions
#########

#. Change the __Destination__ drop down to __Other S3-Compatible
   Storage__.

#. Set __Bucket__ to the name of the S3-compatible bucket to store
   snapshots in.

#. Set __Path__ to the path in the S3-compatible that the snapshots
   should be stored under.

#. Set __Access Key ID__ and __Access Key Secret__ to the credentials
   required to access the storage provider.

#. Set __Endpoint__ to the required value for your storage provider.

6. Set __Region__ to the required value for your storage provider.

Configure Snapshots Schedule and Retention
####################--

#. From the Platform Installer UI, click the Snapshots tab.

|image8|

The first time you access the Snapshots tab you are prompted to either
schedule a snapshot or to begin creating one. After you have taken your
first snapshot the schedule settings are available from the __Schedule__
link on the snapshots tab.

2. Click __Schedule Snapshots__. If you want to schedule automatic
   snapshots, click __Enable automatic scheduled snapshots__.

   |image9|

   You can schedule automatic snapshots hourly, daily, weekly, monthly,
   or you can setup a custom snapshot schedule using a cron expression.

   __Important!__ The SPI uses server time to schedule automatic
   snapshots.

3. Under __Retention policy__ you can specify to have the SPI to
   automatically delete older snapshots. Specify by a number of days,
   weeks, months, or years, and then click __Update schedule__.

   |image10|

Restore from a Partial (Application) Snapshot
######################-

#. On the Snapshots page, you can review a list of all of your
   Application Snapshots under the "Partial Snapshots (Application)"
   menu. Click the circular icon to restore a certain snapshot to your
   Swimlane instance.

   |image11|

#. If you want to restore to the version of the Snapshot, click
   __Restore from snapshot__. You are then prompted to enter the slug of
   the snapshot (confirming the slug name). Enter `swimlane-platform`.

   __Important!__ Restoring to the version you've selected will remove
   any data since the snapshot was made. In addition, during
   restoration, your Swimlane instance will not be available and you
   will not be able to use the Swimlane Installer UI until the restore
   completes.

#. Return to the main UI. Once your Application Status displays _Ready_,
   then you know that both the UI and your Swimlane instance are back up
   and available again.

   |image12|

Restore from a Full (Instance) Snapshot in a non-DR scenario
##############################

Instance snapshots can act as both instance-level snapshots and as
application-level snapshots. This section covers restoring the Swimlane
application with an instance snapshot.

#. On the Snapshots page, you can review a list of all of your instance
   snapshots under the "Full Snapshots (Instance)" menu. Click the
   circular icon and select "Partial Restore" to restore a certain
   snapshot to your Swimlane instance.

   |image13|

#. You are then prompted to enter the slug of the snapshot (confirming
   the slug name). Enter `swimlane-platform`.

   __Important!__ Restoring to the version you've selected removes any
   data since the snapshot was made. In addition, during restoration,
   your Swimlane instance is not available and you will not be able to
   use the SPI until the restore completes.

#. Return to the main UI. Once your Application Status displays _Ready_,
   then you know that both the SPI UI and your Swimlane instance are
   back up and available again.

   |image14|

Restore from a Full (Instance) Snapshot in a DR scenario
############################

#. After your new destination cluster nodes are installed, run the
   following command to configure your storage location:

2. A process takes place after configuring the snapshot storage location
   that discovers which snapshots are available for restore. After a few
   minutes, you can run the following to show the backups that are
   available:

3. Select the backup you want to restore from the list and restore it
   via this command:

- |image1| image:: ../Resources/Images/snapshot_settings_default.png
- |image2| image:: ../Resources/Images/snapshot_settings_s3.png
   :width: 50.0%
- |image3| image:: ../Resources/Images/snapshot_settings_azure.png
   :width: 50.0%
- |image4| image:: ../Resources/Images/snapshot_settings_google.png
   :width: 50.0%
- |image5| image:: ../Resources/Images/snapshot_settings_hostpath.png
   :width: 50.0%
- |image6| image:: ../Resources/Images/snapshot_settings_nfs.png
   :width: 50.0%
- |image7| image:: ../Resources/Images/snapshot_settings_s3-compatible.png
   :width: 50.0%
- |image8| image:: ../Resources/Images/no_snapshots.png
- |image9| image:: ../Resources/Images/enable_automatic_snapshots.png
- |image10| image:: ../Resources/Images/schedule_snapshots.png
- |image11| image:: ../Resources/Images/restore_from_application_snapshot.png
- |image12| image:: ../Resources/Images/swimlane_ready.png
- |image13| image:: ../Resources/Images/restore_from_instance_snapshot.png
- |image14| image:: ../Resources/Images/swimlane_ready.png
