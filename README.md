# content-host-d
A Docker-ized RHEL 7 Hypervisor Guest for Red Hat Satellite 6

Installation
------------
```docker build -t ch-d:guest <path-to-this-directory>```

Usage
-----
```docker run <arguments> ch-d:guest```

Additonally, a fully-automated flood script is provided that will create fake hypervisors and guests.

```python flood.py -s my.sat.host.com --hypervisors 5 --guests 5 --limit 20``` 

Accepted Arguments
------------------
-e  (e.g. ```-e "SATHOST=my.hostname.domain.com"```)
 * AK - Name of the Activation Key to use.
 * AUTH - Satellite username and password. (AUTH=username/password)
 * ENV - Name of the Environment to use.
 * KILL - If this is not passed, then the container will be kept alive and goferd running.
 * ORG - Name of the Organization to use.
 * SATHOST(Required) - Hostname of the Satellite (not url).
 ^ UUID - Will set a virt uuid for subscription manager to report.

Note
----
If you want to be able to use katello-agent, you must mount your /dev/log to the container at runtime. (i.e. -v /dev/log:/dev/log)

Examples
--------
```docker run -e "SATHOST=my.host.domain.com" -e "UUID=my-long-uuid" ch-d:guest```

```docker run -e "SATHOST=my.host.domain.com" -e "ORG=Dev" -e "AUTH=username/password" -e "UUID=my-long-uuid" ch-d:guest```

```python flood.py -s my.host.domain.com --hypervisors 5 --guests 5 --limit 10```
