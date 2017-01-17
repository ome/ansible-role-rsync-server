import testinfra.utils.ansible_runner

import re

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_rsync_running(Service):
    assert Service('rsyncd').is_running
    assert Service('rsyncd').is_enabled


def test_connect_rsync(Command):
    out = Command.check_output('rsync rsync://localhost')
    assert re.match('dataset-1\s+Public datasets', out)
