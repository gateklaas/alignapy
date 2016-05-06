import stringdistances
import util

class Correspondence():
    entity1 = None
    entity2 = None
    relation = None
    measure = 0.0
    
    def __init__(self, entity1, entity2, relation, measure):
        self.entity1 = entity1
        self.entity2 = entity2
        self.relation = relation
        self.measure = measure
    
def _correspondence_measure(graph1, graph2, object1, object2, method=stringdistances.equal_distance):
    entity_name1 = util.guess_entity_name(graph1, object1)
    entity_name2 = util.guess_entity_name(graph2, object2)
    if entity_name1 == None or entity_name2 == None:
        return 0.0
    else:
        return 1.0 - method(entity_name1, entity_name2)

def align(graph1, graph2, threshold=1.0, method=stringdistances.equal_distance):
    corr_list = []
    
    # Create properties lists
    prop_list1 = util.load_properties(graph1)
    prop_list2 = util.load_properties(graph2)
     
    # Create class lists
    class_list1 = util.load_classes(graph1)
    class_list2 = util.load_classes(graph2)
    
    # Create individuals lists
    ind_list1 = util.load_individuals(graph1)
    ind_list2 = util.load_individuals(graph2)

    # Calc class correspondence
    for i, class1 in zip(xrange(len(class_list1)), class_list1):
        for j, class2 in zip(xrange(len(class_list2)), class_list2):
            value = _correspondence_measure(graph1, graph2, class1, class2, method=method)
            if value >= threshold:
                corr = Correspondence(class1, class2, '=', value)
                corr_list.append(corr)
            
    # Calc property correspondence
    for i, prop1 in zip(xrange(len(prop_list1)), prop_list1):
        for j, prop2 in zip(xrange(len(prop_list2)), prop_list2):
            value = _correspondence_measure(graph1, graph2, prop1, prop2, method=method)
            if value >= threshold:
                corr = Correspondence(prop1, prop2, '=', value)
                corr_list.append(corr)
            
    # Calc individual correspondence
    for i, ind1 in zip(xrange(len(ind_list1)), ind_list1):
        for j, ind2 in zip(xrange(len(ind_list2)), ind_list2):
            value = _correspondence_measure(graph1, graph2, ind1, ind2, method=method)
            if value >= threshold:
                corr = Correspondence(ind1, ind2, '=', value)
                corr_list.append(corr)

    return corr_list