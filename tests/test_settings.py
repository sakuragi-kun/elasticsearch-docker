from .fixtures import elasticsearch
import pytest


def test_setting_node_name_with_an_environment_variable(elasticsearch):
    # The fixture for this test comes from tests/docker-compose.yml
    assert elasticsearch.get_root_page()['name'].startswith('docker-test-node')


def test_setting_heapsize_with_an_environment_variable(elasticsearch):
    # The fixture for this test comes from tests/docker-compose.yml
    heap_max_in_bytes = 1
    for jvmstat in elasticsearch.get_nodes_heap_max_in_bytes():
        heap_max_in_bytes *= (int(jvmstat['mem']['heap_max_in_bytes']) == 1037959168)
    assert bool(heap_max_in_bytes)


def test__ess__cluster__name_with_an_environment_variable(elasticsearch):
    # The fixture for this test comes from tests/docker-compose.yml
    assert elasticsearch.get_root_page()['cluster_name'] == ('docker-test-cluster')


def test_non_whitelisted_setting_without_dot_with_an_environment_variable(elasticsearch):
    # The fixture for this test comes from tests/docker-compose.yml
    assert 'irrelevantsetting' not in elasticsearch.es_cmdline()
