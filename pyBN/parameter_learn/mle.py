"""
*****************************
Maximum Likelihood Estimation
Parameter Learning
*****************************

"""

__author__ = """Nicholas Cullen <ncullen.th@dartmouth.edu>"""

import numpy as np

def mle_estimator(bn, data):
	"""
	Maximum Likelihood Estimation is a frequentist
	method for parameter learning, where there is NO
	prior distribution. Instead, the frequencies/counts
	for each parameter start at 0 and are simply incremented
	as the relevant parent-child values are observed in the
	data. 

	This can be a risky method for small datasets, because if a 
	certain parent-child instantiation is never observed in the
	data, then its probability parameter will be ZERO (even if you
	know it should at least have a very small probability). 

	Note that the Bayesian and MLE estimators essentially converge
	to the same set of values as the size of the dataset increases.

	Also note that, unlike the structure learning algorithms, the
	parameter learning functions REQUIRE a passed-in BayesNet object
	because there MUST be some pre-determined structure for which
	we can actually learn the parameters. You can't learn parameters
	without structure - so structure must always be there first!

	Arguments
	---------
	*bn* : a BayesNet object
		The associated network structure for which
		the parameters will be learned

	*data* : a nested numpy array

	Returns
	-------
	None

	Effects
	-------
	- modifies/sets bn.data to the learned parameters

	Notes
	-----
	data attributes:
		"numoutcomes" : an integer
	    "vals" : a list
	    "parents" : a list or None
	    "children": a list or None
	    "cprob" : a nested python list

	- Do not want to alter bn.data directly!

	"""
	# set empty conditional probability table for each RV
	for rv in bn.V:
		p_idx = int(np.prod([len(bn.data[p]['vals']) for p in bn.data[rv]['parents']]))
		bn.data[rv]['cprob'] = [[0]*len(bn.data[rv]['vals']) for _ in range(p_idx)]

	# loop through each row of data
	for row in data:
		obs_dict = dict([(rv,row[bn.node_idx(rv)]) for rv in bn.nodes()]) # key=node, val=row value

		# loop through each RV and increment its observed parent-self value
		for rv in bn.nodes():

			value_indices = np.empty(bn.scope_size(rv))
			value_indices[0] = bn.value_idx(rv, obs_dict[rv])

			strides = np.empty(bn.scope_size(rv))
			stride[0] = bn.stride(rv,rv)

			for i,p in enumerate(bn.parents(rv)):
				value_indices[i+1] = bn.value_idx(p,obs_dict[p])
				strides[i+1] = bn.stride(rv, p)
			
			offset = np.sum(np.prod(value_indices,strides)) # get cprob offset
			bn.data[rv]['cprob'][offset] += 1

	













