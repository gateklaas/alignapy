import alignment
import stringdistances
import util
from nltk.corpus import wordnet as wn
from nltk.tokenize import wordpunct_tokenize

def jwnl_basic_synonym_distance(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    
    dist_subs = stringdistances.substring_distance(string1, string2)
    synsets = wn.synsets(string1, wn.NOUN)
    if len(synsets) == 0:
        tokens = wordpunct_tokenize(string1)
        for token in tokens:
            synsets = wn.synsets(string1, wn.NOUN)
            if len(synsets) > 0:
                break
    if len(synsets) > 0:
        for synset in synsets:
            for lemma in synset.lemmas():
                dist = stringdistances.substring_distance(lemma.name(), string2)
                if (dist < dist_subs):
                    dist_subs = dist
    return dist_subs

graph1 = util.graph_from_uri('http://purl.org/dc/elements/1.1/')
graph2 = util.graph_from_uri('http://purl.org/dc/terms/')

print 'graph sizes:', len(graph1), len(graph2)
print 'num classes:', len(util.load_classes(graph1)), len(util.load_classes(graph2))

corr_list = alignment.align(graph1, graph2, threshold=0.9, method=jwnl_basic_synonym_distance)

print 'num correspondences:', len(corr_list)

for corr in corr_list:
    print corr.entity1, corr.relation, corr.entity2, corr.measure
