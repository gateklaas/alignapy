alignapy
========

Basic ontology matching

example
=======
```python
from rdflib import Graph, OWL
from alignapy import alignment

# Load graphs
graph1 = Graph()
graph1.parse('vocab.ttl', format='turtle')

graph2 = Graph()
graph2.parse('group15.rdf')

# Find correspondences
corr_list = alignment.align(graph1, graph2)

# Print correspondences
for corr in corr_list:
    print corr.entity1, corr.relation, corr.entity2, corr.measure
```

Another example:
https://github.com/gateklaas/alignapy/blob/master/alignapy/test.py

install
=======

pip install -e git+https://github.com/gateklaas/alignapy.git#egg=alignapy
