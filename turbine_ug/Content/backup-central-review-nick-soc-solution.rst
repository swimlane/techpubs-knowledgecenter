backup-central-review-nick-soc-solutionSOC Solution
===================================================

The SOC Solution is a solution bundle that is made of four smaller,
interconnected solutions: Phishing Triage (PT), Alert Triage (AT),
Threat Intelligence (TI), and Case and Incident Management (CIM).
Phishing Triage and Alert Triage are the primary ingestion workflows,
processing incoming events into casesignals in the CIM application. The
TI solution is used to enrich observables extracted from incoming cases.
Combined, the four solutions create a powerful set of workflows to
efficiently and effectively triage and manage critical security events.

Important! Turbine customers on +> 23.2.0 can install the SOCSolution,
whether they are on cloud or on-prem. Turbine customers on 11.8 should
NOT attempt to install the SOC Solution due to the Turbine Record
actions connector and APIs in +> 23.2.0.

Let's dive in to what these solutions do as part of the SOC Solution.

Alert Triage

How it Works

The Alert Triage solution is composed of several playbooks for triaging
events from a SIEM, EDR, or other security alert source. You can use
either a webhook to push alerts from your source into Turbine, or a bulk
ingestion component in the solution to ingest alerts. Each alert is
processed to identify and extract the important observables. A
signalcase is created in the Case and Incident Management (CIM)
application and populates relevant alert data. Then the threat
intelligence (TI)application evaluates observables discovered in your
alert to categorize, evaluate, and prioritize the event before
mitigation or remediation.

You can configure the solution to work with any number of SIEMs, EDRs,
or other security tools. Similarly, the you can customize playbook
actions to fit any company’s existing or preferred SOC processes.

Capabilities

The Alert Triage solution has the following capabilities:

Provides connectors, assets, and playbooks for triaging alerts from
security information and event management (SIEM), XDR(extended detection
and response), or Endpoint detection and response (EDR), etc. products

Automates ingestion of alerts via webhook or API request

Summarizes alert data

Enriches observables and identifies actionable data

Feeds into CIMSolution

Workflow

Phishing Triage

How it Works

The Phishing (Email) Triage solution is composed of several playbooks
for processing user-submitted emails that they suspect to be phishing
attempts. The solution extracts the critical information from the email
(such as observables) and attaches them to a new signalcase in the CIM
application. Then TI providers, configured with the TI solution
application, evaluate the observables discovered in the suspected
phishing email. A rendered image of the suspected phishing email is also
generated, to provide a safe way to view the contents of the email. For
security reasons, an image of the original email is saved as part of the
case rather than the original content.

Turbine users can customize the phishing triage playbooks to fit any
company’s existing or preferred SOC processes.

Capabilities

The Phishing Triage solution has the following capabilities:

Provides connectors, assets, and playbooks for triaging reported
phishing emails

Automates ingestion of emails with reported phishing emails attached

Summarizes reported phishing email data

Enriches observables and identifies actionable data

Feeds into Case and Incident Management Solution

Workflow

Threat Intelligence

How it Works

The TI solution works with one or more threat intelligence providers
(TIPs) to enrich the observable evidence extracted in the Phishing
Triage and Alert Triage solutions. When a TI Record is created, several
playbooks evaluate the observables against the intelligence provided by
the intelligence providers TIPs. The results are used to update the TI
Record, which is associated with the signalcase being triaged.

Capabilities

The TI threat Intelligence solution has the following capabilities:

Provides connectors, assets, and playbooks for enriching TI observables

Allows configuration of multiple threat intelligence providers,
including a configurable primary trusted intelligence provider per
observable type (domain, IP, etc.)

Allows automated enrichment of observables identified from Alert and
Phishing Triage playbooks and adhoc searches through the CIMsolution

[Workflow

Case and Incident Management

How it Works

The CIM solution works with the Alert Triage and Phishing Triage
solutions to create and manage cases signals for each event being
investigated. The created signalcases serve as the primary interaction
point dashboard for investigations, showing the details, status, and
next steps for each signalcase. Signals that are identified as true
positive or important can be escalated to case status. If cases are
deemed to be important impactful to security, they can be promoted to
incidents.

Turbine users can customize the CIM playbooks to fit any company’s
existing or preferred SOC processes.

Capabilities

The Case and Incident Management solution has the following
capabilities:

Provides an interactive user interface for:

Triaging reported phishing emails from the Phishing Triage Solution

Triaging alerts from the Alert Triage Solution

Viewing, interacting with, enriching, and adding observables via the
Threat Intelligence Solution

Documenting research and notes regarding an investigation

Collecting granular metrics such as MTTR, MTTD, Dwell Time, etc.

Identifying MITRE ATT&CK Phases

Working an investigation through its entire lifecycle, from Signal
ingestion through Case and Incident escalations, remediation, and
resolution

Triaging reported phishing emails from the Phishing Triage Solution

Triaging alerts from the Alert Triage Solution

Viewing, interacting with, enriching, and adding observables via the
Threat Intelligence Solution

Documenting research and notes regarding an investigation

Collecting granular metrics such as MTTR, MTTD, Dwell Time, etc.

Identifying MITRE ATT&CK Phases

Working an investigation through its entire lifecycle, from ingestion
through Case and Incident escalations, remediation, and resolution

[Workflow
