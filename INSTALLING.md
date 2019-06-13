# INSTALLING

## Installing uWSGI Service

The following instructions target Ubuntu 18.04 LTS

* Rename `uwsgi.dist.ini` to `uwsgi.ini`
* Copy `uwsgi.dist.service` to `/etc/systemd/system/<API Service Name>.service`
* Run:

```bash
    sudo systemctl start <API Service Name>
    sudo systemctl enable <API Service Name>
```

* Verify service status

```bash
    sudo systemctl status <API Service Name>
```
