# Cowork and Microsoft 365 configuration

Use an authorised Microsoft 365 work account with an Entra tenant. The tenant admin must consent to the Microsoft 365 connector and enable write tools for email. Connect it in Claude **Customize → Connectors**. Personal Outlook.com accounts are not supported by that connector. For a cloud schedule, use connected OneDrive for Business or SharePoint files; a task using local files or apps runs locally.

The native connector can send Outlook mail but cannot attach a workbook. For the required `.xlsx` attachment, create a Power Automate cloud flow with OneDrive for Business **When a file is created** on a dedicated `Approved Reports` folder, then **Get file content**, then Office 365 Outlook **Send an email (V2)** with the approved workbook name and file content in the attachment fields. Restrict recipients to an authorised test mailbox during the lab. Moving a reconciled workbook into `Approved Reports` is the human release gate. Record the flow run ID and Outlook Sent Item.

Current references:
- https://support.claude.com/en/articles/15183774-connect-to-microsoft-365
- https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork
- https://learn.microsoft.com/en-us/connectors/onedriveforbusiness/
- https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/office365outlook
