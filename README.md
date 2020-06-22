# Unofficial Python Implementation of GFLasso

This is a Python implementation of graph-guided fused lasso (GFLasso) based on the following paper,
```
Chen, Xi, et al. 
"Graph-structured multi-task regression and an efficient optimization method for general fused lasso." 
arXiv preprint arXiv:1005.3579 (2010).
```

## Installation
```
python setup.py install
```
or
```
pip install -e .
```

## Usage
See [example.ipynb](./example.ipynb).

## Bug?
- ~~Estimated weights are not be sparse.~~
    - Added soft thresholding operator
