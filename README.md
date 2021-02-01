Rsync Server
============

[![Actions Status](https://github.com/ome/ansible-role-rsync-server/workflows/Molecule/badge.svg)](https://github.com/ome/ansible-role-rsync-server/actions)
[![Ansible Role](https://img.shields.io/ansible/role/41886.svg)](https://galaxy.ansible.com/ome/rsync_server/)

Setup rsync as a server.


Role Variables
--------------

Defaults: `defaults/main.yml`

- `rsync_server_timeout`: Timeout for connections, default `300` seconds
- `rsync_server_max_connections`: Maximum number of connections, default `10`
- `rsync_server_shares`: A list of dictionaries of shares with fields:
  - `name`: The published name of the share, required
  - `path`: Filesystem path of the share, required
  - `comment`: Description of the share, default is the same as `name`
  - `readonly`: Whether the share is read-only, default `True`
  - `uid`: User name or ID when access the share, default `nobody`
  - `gid`: Group name or ID when access the share, default `nobody`
  - `excludes`: A list of exclusions, default `['lost+found', '.*']`


Log rotation:
- `rsync_server_logrotate_interval`: Rotate log files at this interval, default `weekly`
- `rsync_server_logrotate_backlog_size`: Number of backlog files to keep, default `52`


Example Playbook
----------------

    - hosts: localhost
      roles:
      - role: ome.rsync_server
        rsync_server_shares:
        - name: dataset-1
          comment: Public datasets
          path: /data/1


Related roles
-------------

This role was originally written with the OME's minimal requirements in mind.
Please also take a look at [@stejoo's fork](https://github.com/stejoo/ansible-role-rsync-server/tree/stejoo) which has additional features.


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
