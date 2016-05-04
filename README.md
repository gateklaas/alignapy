alignapy
========

Basic ontology matching

example
=======
```python
from rdflib import Graph, OWL
from alignapy import alignment

graph1 = Graph()
graph1.parse('vocab.ttl', format='turtle')

graph2 = Graph()
graph2.parse('group15.rdf')

corr_list = alignment.align(graph1, graph2, threshold=0.1)

for corr in corr_list:
    print corr.entity1, corr.relation, corr.entity2, corr.measure
    graph1.add((corr.entity1, OWL.sameAs, corr.entity2))

with open('vocab2.ttl', 'w') as f:
    graph1.serialize(f, format='turtle')
```

install
=======

pip install -e git+https://github.com/gateklaas/alignapy.git#egg=alignapy
