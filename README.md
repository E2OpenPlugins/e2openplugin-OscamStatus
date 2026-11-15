# e2openplugin-OscamStatus

## OscamStatus Plugin by puhvogel modified by Pr2 2011-2018 v.1.0

This is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free
Software Foundation; either version 2, or (at your option) any later
version.

Version 1.0
* Add french translation
* Support for Full HD skin (full screen log)

Version 1.1
* Autoconfiguration: it will retrieve the running OScam setup automatically when no config file found
* configuration file moved and renamed to /etc/enigma2/oscamstatus.cfg

Version 1.2
* Improve Autodetect
* Autodetected server name is not saved nor read from configuration file

Version 1.3
* Fully adapted screens for Full HD
* Provid is now also displayed (useful for Nagra, Seca & Viaccess)
* Support E2 picons by name

Version 1.3.1
* Small cosmetic fixes in Full HD
Remark: to have a nice looking Full HD logging screen it is advised to define a multiple of 43
in your **oscam.conf** section *global* parameter *loghistorylines* (exemple to have 4 pages of logging)
```
[global]
loghistorylines               = 172
```
Version 1.3.2
* Fix in source text

Version 1.3.3
* SSL Fix (Thanks Token for it)

Version 1.4.0
* Add a green "Display Entitlements" button to the locally connected readers screen. Will display the active entitlements and limit the expired ones to the last 2 more recent (some cards keep a full list of all expired entitlements, it's useless to display them all).
* Fix the connected client screen that remains empty due to OScam layout changes. Also fix the information displayed on the yellow button.
* Fix crash with connected readers yellow - yellow - yellow key press.
* Some Python 2 to Python 3 improvements.
* Strenghten the configuration file creation and reading.

Version 1.4.1
Improve picon & FullHD layouts, and fix Python 3 issues

Features & UI improvements:
* Overhaul FullHD ReaderstatsScreen picon skin (1480px width, larger fonts, 110x55 scaled picons, and wider caid:provid:srvid column for Nagra).
* Improve Connected Clients view by falling back to userstats when <client> nodes are absent, enriching online clients with live channel/reader data from part=status, highlighting active clients in green, and displaying channel duration.
* Fetch live client details (CAID, ProvID, SrvID, service, ECM history) from part=status when opening ClientDataScreen.

Picon & Python 3 bugfixes:
* Add UTF-8 Service Name Picon (UTF-8 SNP via sanitizeFilename) support alongside classic ASCII SNP, strip CAID@PROVID and provider prefixes, search additional mount points, and add multi-step picon fallback for Connected Readers.
* Replace async ePicLoad with synchronous cached LoadPixmap and add BT_SCALE|BT_KEEP_ASPECT_RATIO flags for reliable picon rendering under Python 3.
* Improve SNP picon resolution (strip CAID@PROVID and provider prefixes, search additional mount points) and add multi-step picon fallback for Connected Readers.
* Replace deprecated Python 2 cmp() sorting in ReaderServiceDataScreen with key=lambda sorting.
* Replace string identity comparisons (is / is not) with equality operators (== / !=) and None checks with is / is not None.
* Sanitize invalid XML tokens and unescaped ampersands before minidom parsing, and guard against closed screen sessions in DownloadXMLScreen.gotThreadMsg.
