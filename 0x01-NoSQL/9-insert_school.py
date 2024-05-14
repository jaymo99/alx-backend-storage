#!/usr/bin/env python3
"""
9-insert_school module. Inserts a new document in a collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    Returns the new _id
    """
    return mongo_collection.insert(kwargs)
