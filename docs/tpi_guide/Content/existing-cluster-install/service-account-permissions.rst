Service Account Permissions
===========================

If your cluster requires pods to have service accounts defined in order
to run, the following are the necessary role permissions the pod types
that require them.

Swimlane Tools
--------------

This Swimlane Tools deployment requires special permissions in order to
process snapshots and support bundles. Enabling the
``Automatically create the Service Account used by the Swimlane Tools deployment``
option on the config page will automatically create the service account,
role, and role binding named ``swimlane-backup`` with the required
permissions. If you want to use a different service account you can
disable that option and create your own. The following is an example
role with the required permissions to assign to the service account:

kind: Role apiVersion: rbac.authorization.k8s.io/v1 metadata: name:
swimlane-backup rules: - apiGroups: [""] resources: ["pods"] verbs:
["list"] - apiGroups: ["apps"] resources: ["deployments"] verbs:
["create", "update", "patch", "get", "list", "watch"] - apiGroups:
["apps"] resources: ["statefulsets"] verbs: ["list"]
