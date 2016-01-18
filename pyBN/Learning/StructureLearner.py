import pandas as pd
import numpy as np

class StructureLearner(object):

	def __init__(self,
				data=None,
				dtype=None):
		"""
		Class for structure learning.

		Attributes
		----------

		data : a Pandas dataframe or numpy 3D array
			The data from which the user wants to learn

		dtype : 'pandas' | 'numpy'
			The type of data

		Methods
		-------


		Notes
		-----

		Structure Learning Algorithms in "bnlearn":

			constraint-based structure learning algorithms:

				Grow-Shrink (GS);
				Incremental Association Markov Blanket (IAMB);
				Fast Incremental Association (Fast-IAMB);
				Interleaved Incremental Association (Inter-IAMB);
			
			score-based structure learning algorithms:

				Hill Climbing (HC);
				Tabu Search (Tabu);
			
			hybrid structure learning algorithms:

				Max-Min Hill Climbing (MMHC);
				General 2-Phase Restricted Maximization (RSMAX2);
			
			local discovery algorithms:

				Chow-Liu;
				ARACNE;
				Max-Min Parents & Children (MMPC);
				Semi-Interleaved Hiton-PC (SI-HITON-PC);

		Conditional Independence Tests in "bnlearn"
			
			constraint-based tests:

				mutual information (parametric, semiparametric and permutation tests);
				shrinkage-estimator for the mutual information;
				Pearson's X^2 (parametric, semiparametric and permutation tests);

			score-based tests:

				the multinomial log-likelihood;
				the Akaike Information Criterion (AIC);
				the Bayesian Information Criterion (BIC);
				a score equivalent Dirichlet posterior density (BDe);
				a modified Bayesian Dirichlet for mixtures of interventional and observational data;
				the K2 score;

		"""
		if is_instance(data, 'pd.DataFrame'):
			self.dtype = 'pandas'
		elif is_instance(data, 'np.ndarray'):
			self.dtype = 'numpy'

		self.data = data






