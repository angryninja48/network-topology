# import logging
import json

from collections import defaultdict

from nornir.core.task import Result

from norntool.drivers.base import BaseHandler as Base
from nornir_netmiko.tasks.netmiko_send_command import netmiko_send_command

TOPOLOGY_FILE='static/data.json'

def show_cdp_neighbours(task):

    cdp = task.run(
        task=netmiko_send_command,
        command_string="show cdp neighbors", 
        use_textfsm=True
    )

    # if cdp.failed:
    #     for host in cdp.failed_hosts.keys():
    #         logger.warning(f'{host}: Failed to run cdp')

    if not cdp.failed:
        if isinstance(cdp.result, list):
            task.host['cdp_data'] = cdp.result
        # else:
        #     logger.debug(f'{host}: No neighbours found')

    return Result(result=task.host['cdp_data'], host=task.host)

def show_interfaces(task):

    interfaces = task.run(
        task=netmiko_send_command,
        command_string="show interfaces", 
        use_textfsm=True
    )

    # if cdp.failed:
    #     for host in cdp.failed_hosts.keys():
    #         logger.warning(f'{host}: Failed to run cdp')

    if not interfaces.failed:
        if isinstance(interfaces.result, list):
            task.host['interfaces'] = interfaces.result
        else:
            logger.debug(f'{host}: No interfaces found')

    return Result(result=task.host['interfaces'], host=task.host)


        

def transform_data(data):

    topology = {
        'nodes': list(),
        'links': list()
    }

    links = defaultdict(tuple)

    for host,values in data.items():
        # import ipdb;ipdb.set_trace()
        
        topology['nodes'].append({'id':host})

        for link in values.result:

            # Dedup tuples
            if links.get((link['neighbor'], link['neighbor_interface'])):
                continue

            local_link = (host, link['local_interface'])
            neighbour_link = (link['neighbor'], link['neighbor_interface'])

            # Map links
            links[local_link] = neighbour_link
    

    for source, target in links.items():

        (source_host, source_int) = source
        (target_host, target_int) = target
        

        topology['links'].append({
            'source': source_host,
            # 'source_interface': source_int,
            # 'target_int': target_int,
            'target': target_host

        })

    topology['type'] = "NetworkGraph"
    topology['label'] = "Lab"

    return topology

def main():

    nr = Base(
        host_file='inventory/hosts.yml',
        group_file='inventory/groups.yml',
        defaults_file='inventory/defaults.yml'
    )

    cdp_result = nr.nornir.run(
        task=show_cdp_neighbours
    )

    toplogy = transform_data(data=cdp_result)
    
    f = open(TOPOLOGY_FILE, 'w')
    f.write(json.dumps(toplogy, indent=4, sort_keys=True))


if __name__ == '__main__':
    main()
