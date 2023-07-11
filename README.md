# Fix DB WiFi

`fix-db-wifi` is a simple command-line tool to resolve IP address conflicts between Deutsche Bahn WiFi and Docker
networks. Both Deutsche Bahn WiFi and Docker use the `172.18.0.0/16` address space by default, which can cause
connectivity issues.

## Modes

This tool has two modes:

### `--temporary` (default)

remove all Docker networks in the conflicting address space 

### `--permanent`

When run in permanent mode, the tool will modify Docker's configuration file (`/etc/docker/daemon.json`) to change the
default address pool to `192.168.0.0/16`, and then restart Docker.

## Usage

To install `fix-db-wifi`, use pip in your terminal:

```bash
pip install fix_db_wifi
```

Afterwards you can run the tool using

```bash
fix_db_wifi
```

or

```bash
fix_db_wifi --permanent
```

Please note that because of the changes it makes, fix-db-wifi must be run with root privileges.
If you have any problems, feel free to open an issue.
Original solution pulled from [here](https://forum.ubuntuusers.de/topic/probleme-mit-dem-wifionice/)
