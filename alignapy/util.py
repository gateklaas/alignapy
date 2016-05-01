from rdflib import Graph, RDF, OWL, RDFS
import requests
import uuid

class UriNotFound(Exception):
    def __init__(self, uri, reason):
        Exception.__init__(self, 'URI <%s> not found: %s' % (uri,reason))
        self.uri = uri

class UnsupportedContent(Exception):
    def __init__(self, uri, content):
        Exception.__init__(self, 'Unsupported content in <%s>: %s' % (uri,content))
        self.uri = uri

def load_properties(graph):
    properties = set(uri for uri in graph.subjects(RDF.type, OWL.ObjectProperty))\
     | set(uri for uri in graph.subjects(RDF.type, OWL.DatatypeProperty))\
     | set(uri for uri in graph.subjects(RDF.type, OWL.AnnotationProperty))
    if len(properties) == 0:
        return set(uri for uri in graph.subjects(RDF.type, RDF.Property))
    else:
        return properties
    
def load_classes(graph):
    classes = set(uri for uri in graph.subjects(RDF.type, OWL.Class)) | set(uri for uri in graph.subjects(RDF.type, OWL.Restriction))
    if len(classes) == 0:
        return set(uri for uri in graph.subjects(RDF.type, RDFS.Class))
    else:
        return classes
    
def load_individuals(graph):
    return set(uri for uri in graph.subjects(RDF.type, OWL.NamedIndividual))

def guess_entity_name(graph, entity):
    label = graph.value(entity, RDFS.label)
    if label != None:
        return label
    
    if '#' in entity:
        root = entity.defrag()
        return entity.split(root)[1][1:]
    
    splitted_uri = entity.split('/')
    return splitted_uri[len(splitted_uri) - 1]

def guess_base_uri(graph):
    uris = set(uri for uri in graph.subjects())
    if len(uris) == 0:
        raise UriNotFound(None, 'Empty graph')
    canon_num = 0
    for uri in uris:
        tuples = [(pred, obj) for (pred, obj) in self.graph.predicate_objects(uri)]
        num = len(tuples)
        if num > canon_num:
            canon_num = num
            canon_uri = uri
    return canon_uri
        
def graph_from_uri(uri, timeout=30):
    headers={'Accept': 'application/rdf+xml'}
    r = requests.get(uri, headers=headers, timeout=timeout)
    if r.status_code == 404:
        raise UriNotFound(uri, 'Status code 404')

    try:
        content = r.headers['content-type']
    except KeyError as e:
        content = 'application/rdf+xml'

    data = r.text.encode('utf-8')
    graph = Graph()
    
    if 'text/html' in content:
        raise UnsupportedContent(uri, content)  
    elif 'application/rdf+xml' in content or 'application/rdf\\+xml' in content or 'application/owl+xml' in content:
        graph.parse(data=data, format='xml')
    elif 'text/plain' in content:
        try:
            graph.parse(data=data, format='nt')
        except:
            try:
                graph.parse(data=data, format='turtle')
            except:
                graph.parse(data=data, format='xml')
    elif 'text/turtle':
        graph.parse(data=data, format='turtle')
    else:
        raise UnsupportedContent(uri, content)
    
    graph.bind('owl', 'http://www.w3.org/2002/07/owl#')
    return graph
