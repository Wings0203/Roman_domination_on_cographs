from Trees import Tree
from sage.all import Graph,graphs
import itertools

def is_cograph(g):
	P4 = graphs.PathGraph(4)
	return not g.subgraph_search(P4, induced=True)

def create_cotree(g):
	"""
 	function that computes the cotree of a given graph

 	input:
 	sage graph / python dictionary, with the nodes and ALL their neighbors
	"""
	if is_cograph(g)==False:
		return
	cotree=Tree('1')
	# the root of the tree is always '1'
	i=0
	for node in g:
		if i==0:
			first_node=node
			i+=1
		elif i==1:
			if g.has_edge(node,first_node):
				# first and second node are adjacent
				Tree.add_child(cotree,Tree(first_node))
				Tree.add_child(cotree,Tree(node))
			else:
				# first and second node are not adjacent
				tree0=Tree('0',[Tree(first_node),Tree(node)])
				Tree.add_child(cotree,tree0)
			i+=1
		else:
			# add incrementally nodes 3,...,end to the cotree
			flag_mixed=[0]
			Tree.is_cograph(cotree,node,g[node],flag_mixed)
			if flag_mixed[0]==0:
				Tree.update_cotree(cotree,node,g[node],0,0)
			elif flag_mixed[0]==2:
				print ("The input graph is not a co-graph. Execution terminated!")
				return
			# initialize tree info for the next iteration
			cotree.reset_info()
	return cotree
