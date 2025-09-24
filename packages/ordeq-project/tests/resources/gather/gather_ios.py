from ordeq_project import gather_ios
from resources.gather.example import catalog_1, catalog_2
from resources.gather.example import nodes, nodes_relative_import
from resources.gather import example

print(gather_ios(catalog_1))
print(gather_ios(catalog_2))
print(gather_ios(nodes))
print(gather_ios(nodes_relative_import))
print(gather_ios(example))
