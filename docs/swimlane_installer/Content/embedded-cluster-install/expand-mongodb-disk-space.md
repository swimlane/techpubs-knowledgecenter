Expand MongoDB Disk Space
######=

The MongoDB pods store data in the `/var/openebs/` directory of the
node that the pod is running on. In order to increase the disk space
available to the MongoDB pods, you must expand the volume/partition this
directory is mounted on and expand the file system. The steps to do this
vary based on your storage provider and file system type.

__Important!__ You must resize the volume on each node in the cluster
since each MongoDB pod contains the full dataset.If your storage
provider or file system doesn't support online resizing then you must
ensure only one node is offline at a time to ensure proper cluster
operation.

Cloud Service Storage Resizing
##############--

+####--+############################--+
| Provider | Documentation                                            |
+##==+##############==+
| AWS      | `EBS                                                     |
|          | Volumes <https://docs.aws.amazon.com/AWSEC2/lates        |
|          | t/UserGuide/requesting-ebs-volume-modifications.html>`__ |
+####--+############################--+
| Azure    | `Azure                                                   |
|          | Disks <https://docs.microsoft                            |
|          | .com/en-us/azure/virtual-machines/linux/expand-disks>`__ |
+####--+############################--+
| GCP      | `GCP Zonal Persistent                                    |
|          | Disks <https://cloud.google.                             |
|          | com/compute/docs/disks/add-persistent-disk#resize_pd>`__ |
+####--+############################--+

File System Resizing
##########

Every file system type (EXT3, EXT4, XFS, etc.) will have different
instructions for resizing. See the documentation for your file system
type for expanding your file system after increasing the size of the
volume/partition.
