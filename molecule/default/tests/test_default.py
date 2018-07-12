# -*- coding: utf-8 -*-
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service_deployed(host):
    runit_running = host.service("runit").is_running
    runsvdir_running = host.service("runsvdir").is_running
    assert (runit_running or runsvdir_running)
