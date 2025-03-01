# Postmortem: apache2 not runnig

# Issue Summary
Duration of the Outage: The outage was detected at 08:00 hrs GMT and was resolved by 08:20 hrs GMT. A total downtime of 20 minutes.

Impact: HTTP requests to the apache2 webserver failed.

Root Cause: The `apache2` service was not running

# Timeline of Events
- 08:00 GMT: Curl 0:80 requests to the ALX apache2 server returned "curl: (7) Failed to connect to 0 port 80: Connection refused".
- 08:02 GMT: Checked and found out that the apache server was not running (`ps aux | grep apache2`).
- 08:04 GMT: Checked whether apache2 was installed on the system (`apache2 -v`).
- 08:06 hrs GMT: Checked and confirmed apache2 configuration files had no errors (`sudo apache2ctl configtest`).
- 08:08 GMT: Started the apache2 service
- 08:10 GMT: Checked to see if apache2 service was listening on port 80.
- 08:12 GMT: Sent a request to localhost on port 80 and confirmed the issue resolved, with the site back online. 

# Root Cause and Resolution
## Root Cause:
apache2 service was not running.

## Resolution:
Ensure that apache2 is installed with a valid configuration file, running and listening on TCP port 80.

# Corrective and Preventive Measures
## Improvements/Fixes:
Ensure apache2 is correctly installed and configured. A script was written to be run to ensure a common cofiguration for apache2.

## Checklist
- Create and execute a script to installs apache2
- Validates te configuration file of apache2
- If the configuration file is valid, start apache2 service.
- Ensure apache2 is running and listening on port 80.

[The Script](script)
