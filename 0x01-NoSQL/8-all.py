#!/usr/bin/env python3
"""
MongoDB module. Defines function to list all documents in a collection
"""


def list_all(mongo_collection):
    """
    Returns a list of all documents in a collection
    """
    return mongo_collection.find()
