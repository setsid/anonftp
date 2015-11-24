Summary
-------

anonftp - Insecure anonymous FTP server based on pyftpdlib.
Gives full anonymous access (read/write) to the root directory.
Can be very useful and convenient in the DMZ, but not on the Internet.

Requirements
------------

- Python 3
- [pyftpdlib](https://github.com/giampaolo/pyftpdlib)
- setuptools (for installation only)

Installation
------------

```
$ python3 setup.py install
```

Usage
-----

```
$ anonftp [-d] [-a <ADDRRESS] [-p <PORT>] [-u <USER>] [-r <ROOT>]

-d: enable debug mode;
-a <ADDRESS>: listen on address (0.0.0.0 by default);
-p <PORT>: listen on port (2121 by default);
-u <USER>: run program under unprivileged user account;
-r <ROOT>: root directory (current directory by default);
```
