from ordeq_project import gather_nodes
from resources.gather.example import catalog_1, catalog_2
from resources.gather.example import nodes, nodes_relative_import
from resources.gather import example

print(gather_nodes(catalog_1))
print(gather_nodes(catalog_2))
print(gather_nodes(nodes))
print(gather_nodes(nodes_relative_import))
print(gather_nodes(example))
