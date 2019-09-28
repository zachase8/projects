#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PageRank

@author: Zach Chase
"""

import numpy as np

class DiGraph:
    """
    What does this class do???
    
    Attributes:
        jfkdal;fjdsakdlfj;as
    """
    
    def __init__(self, A, labels=None):
        """
        Description
        
        Parameters:
            A ((n,n) ndarray): The adjacency matrix of a directed graph
                A[i,j] is the weight of the edge from node j to node i.
            labels (list(str)): Labels for the n nodes in the graph
                If None, defaults to [0,1,...,n-1]
        """
        
        # Find size of adjacency matrix
        self.n = A.shape[0]

        # Save labels as an attribute, set to default if None
        if labels is None:
            self.labels = list(np.arange(self.n))
        else:
            self.labels = labels
            
        #Raise ValueError if lengths of nodes and labels don't match
        if len(self.labels) != self.n:
            raise ValueError("Length of labels must be the same as number of nodes.")
            
        # Eliminate sinks by modifying adjacency matrix
        for i in range(self.n):
            if np.count_nonzero(A[0:,i]) == 0:
                A[0:,i] = 1 # Sinks now connected to all other nodes
        
        # Normalize Columns and save the matrix as an attribute
        self.A = A/A.sum(axis=0)

        