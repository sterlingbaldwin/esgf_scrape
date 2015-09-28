import sys
from pyesgf.search import SearchConnection
from debug import print_debug
import json

#dev imports
import pdb
import pprint

nodes = {
	'ornl': {
		'hostname': 'esg.ccs.ornl.gov'
		},
	'anl': {
		'hostname': 'dev.esg.anl.gov'
		}
}

pp = pprint.PrettyPrinter(indent=4)

def load_facets(node):

    facets = {}
    try:
        conn = SearchConnection(
            'http://' + node + '/esg-search/', distrib=True)
        context = conn.new_context()
        for facet in context.get_facet_options():
            facets[facet] = context.facet_counts[facet]
    except Exception as e:
        print_debug(e)

    return facets


if __name__ == '__main__':

	for node in nodes:
		facets = load_facets(nodes[node]['hostname'])
		for i in facets:
			nodes[node][i] = i
			for j in facets[i]:
				#pdb.set_trace()
				nodes[node][i] = facets[i]
	
	pp.pprint(nodes)	