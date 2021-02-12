host = 'csr01'

nodes = set()
nodes.add(host)

for node in nodes: 
    # dict1 = { 
    #     'id': node
    # }
    
    print(dict(id=node))

# import ipdb;ipdb.set_trace()