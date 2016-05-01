alignapy
========

Basic ontology matching

example
=======
```python
from rdflib import Graph
from alignapy import alignment

graph1 = Graph()
graph1.parse('vocab.ttl', format='turtle')

graph2 = Graph()
graph2.parse('group15.rdf')

corr_list = alignment.align(graph1, graph2, threshold=0.9)

for corr in corr_list:
    print corr.entity1, corr.relation, corr.entity2, corr.measure
```

install
=======

pip install -e git+https://github.com/gateklaas/alignapy.git#egg=alignapy
