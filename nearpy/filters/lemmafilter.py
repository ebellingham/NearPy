from __future__ import print_function

import numpy

from nearpy.filters.vectorfilter import VectorFilter

class LemmaFilter(VectorFilter):
    """
    Assumes that the data argument of the vector is a string in the format LEMMA_UNIQUEKEY
    e.g. take_993343
    
    Given a particular lemma, filters candidates to check that they are assigned the target lemma
    
    Also filters for uniqueness (by 'data').
    
    Makes sure that each vectors is only once in the vector list. Works on
    both types of vector listst - (vector, data, distance) and
    (vector, data).

    This filter uses the 'data' as key for uniqueness. If you need some
    other feature for uniqueness, you can implement your own filter.

    You only need a uniqueness filter if your hash-configuration makes it
    possible that one vector is saved in many buckets.
    """

    def __init__(self):
        pass

    def filter_vectors(self, input_list, lemma):
        """
        Returns subset of specified input list.
        """
        unique_dict = {}
        for v in input_list:
            vlemma = v[1].split('_')[0]
            if vlemma == lemma:
                unique_dict[v[1]] = v
        return list(unique_dict.values())