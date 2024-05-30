.. _designated-cloud-architecture:

Dedicated Cloud Architecture
============================

Access to Swimlane dedicated cloud is over HTTPS encrypted with TLS 1.2.
Web application firewall (WAF) protects inbound traffic. Data are then
load balanced across dedicated infrastructure in multiple zones for high
availability. An egress firewall protects outbound traffic to external
integrations and data stored in Swimlane are encrypted at-rest using the
AES-256 algorithm.
