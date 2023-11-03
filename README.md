# Project notes
This project contains two Python 3 programs - jirareport and lsFields.  To run these programs, you'll need the following information:
* Jira Cloud URL (like _https://yourcompany.atlassian.com_)
* Your Jira username (like _me@mycompany.com_)
* Your Jira API Key.

If you don't have an API key already
1. In Jira, click your picture in the upper right and choose _manage account_
2. In the profile page, choose the Security tab on the top.
3. Under Security, go to Create and manage API tokens

## lsFields
This program will take the above input and produce a list of fields and field IDs used in your instance of Jira Cloud.  In our instance, we've added fields and the ID shows as _customfield\_00000_.  I'm positive that you'll want to change the fields I print in the report, since some of mine are custom.  Use this tool to list the fields in your instance and replace the fields that I use.

## JiraReport2
This is the one that does the work.  JiraReport will take the above inputs plus a JQL query to produce a report.  I use the Filters page in Jira Cloud to produce and test my queries as needed, then just paste JQL into the report.  Finally, it will ask for an output filename.  If you press enter, it will just use _jira_report.docx_.

The report includes story keys that are hyperlinks back to the story in Jira Cloud.  The Assignee field also displays the persons name and is a hyperlink to their email address.

### Jirastuff
You can automate the answers to the report.  Create a file called jirastuff.py.  In the file, define four variables.  v1 is for your Jira URL, v2 is username, v3 is API Key, and v4 is the query you want to use.

v1="https://me.atlassian.net"
v2="me@example.com"
v3="Replace with API Key"
v4="type in (epic) and status not in (done, resolved, closed, canceled)"

### Help welcome
This is a pretty simple project, but I don't do a lot of Python.  I'd welcome any suggestions.

My intention is to continue to develop this.  I'd like to be able to have a text file with my answers to URL, username, and API key.  If that file is present, the program would pull the answers from there and not prompt for them.  I'd like to have a web front end, so that my bash-averse colleagues can use this.  Finally, it needs to email the docx out when complete, but I think I'm going to do outside the program through bash.

Bon chance!