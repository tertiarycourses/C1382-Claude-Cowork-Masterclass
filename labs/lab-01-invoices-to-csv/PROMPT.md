# Lab 01 prompt — Extract the invoice data and file the PDFs

Copy everything in the block below into Claude.

```text
In this folder are all my invoices from 2025. I need you to process
these so I can send them to my accountant.

Read each invoice and extract the following data points:

- invoice number
- invoice sender
- invoice sender address
- invoice date
- invoice due date
- total amount due
- currency

Then create a CSV called invoices_2025.csv where you store all this
information as well as the filename.

After you have extracted the information, move each invoice PDF into
sub folders based on the YEAR-MONTH of the invoice date, using the
naming convention 2025-01, 2025-02 and so on.

Flag anything that does not look like a normal supplier invoice, or
that you think I should check. Do not delete any file.
```

> **Note:** Work on a copy of the folder — tell Claude to move files, never to delete them.
