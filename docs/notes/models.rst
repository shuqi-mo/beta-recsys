Models
=================================

MF
---------------------------------
`Matrix Factorization (MF) <https://beta-recsys.readthedocs.io/en/stable/modules/models.html#module-beta_rec.models.mf>`__ used in recommender systems decomposes user-item interaction matrix :math:`D \in R^{m \times n}` into the product of two lower dimensionality rectangular matrices :math:`U \in R^{m \times k}` and :math:`V \in R^{n \times k}`, making the product of  :math:`UV^T` close to the real :math:`D` matrix as much as possible. Matrix Factorization is the mainstream algorithm based on implicit factors.

GMF
---------------------------------
`Generalized Matrix Factorization (GMF) <https://beta-recsys.readthedocs.io/en/stable/modules/models.html#module-beta_rec.models.gmf>`__ is the weighted output of dot product of the embedding vectors of user and item after activation function. Let :math:`f` denote active function, :math:`e_u` denote the embedding vector of user, :math:`e_i` denote the embedding vector of item, $h$ denote the weights of linear function, then the result of GMF is :

.. math::
	z^{GMF}=f(h^T(e_u · e_i))

GMF usually deals with the problem of linear interaction.

MLP
---------------------------------
`Multi-Layer Perceptrons (MLPs) <https://beta-recsys.readthedocs.io/en/stable/modules/models.html#module-beta_rec.models.mlp>`__ is a class of feedforward artificial neural network, consisting at least an input layer, a hidden layer and an output layer. Assume a MLP model has :math:`L` layers, :math:`W_i (0<i < L)` denotes the weight matrix of :math:`i` layer, :math:`b_i` denotes the :math:`i` bias of MLPs, :math:`f_i` denotes the activate function of :math:`i` layer, then the result of MLPs is :

.. math::
	z^{MLP}=f_L(W_{L}^{T}(f_{L-1}(\dots f_1(W_1^TE(e_u,e_i)+b_1)\dots))+b_L)

:math:`E(e_u,e_i)` denotes the concatenation of embedding vectors of user and item. MLPs usually deals with the problem of non-linear interaction.

NCF
---------------------------------
`Neural Collaborative Filtering (MCF) <https://beta-recsys.readthedocs.io/en/stable/modules/models.html#module-beta_rec.models.ncf>`__ is based on **GMF** and **MLP**. Let :math:`z^{GMF}` denote the result vector of **GMF**, :math:`z^{MLP}` denote the result vector of **MLP**, then the result of **NCF** is :

.. math::
	z^{NCF}=\sigma(h^T \begin{bmatrix} z^{GMF} \\ z_{MLP} \end{bmatrix})

where :math:`h` denotes the weights of **NCF**.

NGCF
---------------------------------
`Neural Graph Collaborative Filtering (NGCF) <https://beta-recsys.readthedocs.io/en/stable/modules/models.html#module-beta_rec.models.ngcf>`__ is a recommender systems framework that exploits the user-item graph structure by propagating embeddings on it, which leads to the expressive modeling of high-order connectivity in user-item graph, effectively injecting the collaborative signal into the embedding process in an explicit manner. You can find more details in the origin `NGCF-paper <http://staff.ustc.edu.cn/~hexn/papers/sigir19-NGCF.pdf>`_.

LIGHT_GCN
---------------------------------
`LightGCN <https://beta-recsys.readthedocs.io/en/stable/modules/models.html#beta-rec-models-lightgcn-module>`__ is a model containing only the most essential component in Graph Convolution Network for collaborative filtering, it learns user and item embeddings by linearly propagating them on the user-item interaction graph, and uses the weighted sum of the embeddings learned at all players as the final embedding. You can find more details in the origin `LIGHT_GCN-paper <https://arxiv.org/pdf/2002.02126v4.pdf>`_.

CMN
---------------------------------
`Collaborative Memory Network (CMN) <https://beta-recsys.readthedocs.io/en/stable/modules/models.html#module-beta_rec.models.cmn>`__ is a deep architecture to unify the two classes of Collaborative Filtering models capitalizing on the strengths of the global structure of latent factor model and local neighborhood-based structure in a nonlinear fashion. You can find more details in the origin `CMN-paper <http://www.cse.scu.edu/~yfang/Collaborative_Memory_Network.pdf>`_.

Triple2Vec
---------------------------------
`Triple2Vec <https://beta-recsys.readthedocs.io/en/stable/modules/models.html#module-beta_rec.models.triple2vec>`__ A model that learns user and item embeddings by training a Skip-gram model based on sampled triples. Triple2vec uses the Skip-gram model to recover the sampled triples (i.e. a user and two items occurring in the same basket of that user) from the users' baskets for product representations and purchase prediction. `Triple2Vec-paper <https://www.microsoft.com/en-us/research/uploads/prod/2019/01/cikm18_mwan.pdf>`_.

VBCAR
---------------------------------
`Variational Bayesian Context-aware Representation for Grocery Recommendation (VBCAR) <https://beta-recsys.readthedocs.io/en/stable/modules/models.html#module-beta_rec.models.vbcar>`__ is a novel variational Bayesian model that learns the user and item latent vectors by leveraging basket context information from past user-item interactions. You can find more details in the origin `VBCAR-paper <https://arxiv.org/pdf/1909.07705v1.pdf>`_.

NARM
---------------------------------
`Neural Attentive Session Based Recommendation Model (NARM) <https://beta-recsys.readthedocs.io/en/stable/modules/models.html#beta-rec-models-narm-module>`__ is a neural networks framework that tackle problem that not only considers the user's sequential behavior in the current session but also emphasizing the user's main purpose in the current session. You can find more details in the origin `NARM-paper <https://arxiv.org/pdf/1711.04725.pdf>`_.

VLML
---------------------------------
`Variable Length Memory Layer (VLML) <https://beta-recsys.readthedocs.io/en/stable/modules/models.html#module-beta_rec.models.vlml>`__

PAIRWISE_GMF
---------------------------------
