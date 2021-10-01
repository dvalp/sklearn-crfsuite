"""
allow to build docs without scikit-learn installed
"""

try:
    from sklearn.base import BaseEstimator
except ImportError:
    class BaseEstimator(object):
        pass
