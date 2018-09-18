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

