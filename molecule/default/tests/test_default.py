import os
import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_rsync_running(host):
    assert host.service('rsyncd').is_running
    assert host.service('rsyncd').is_enabled


def test_connect_rsync(host):
    out = host.check_output('rsync rsync://localhost')
    assert re.match('dataset-1\s+Public datasets', out)
