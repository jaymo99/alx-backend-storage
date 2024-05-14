#!/usr/bin/env python3
"""
10-update_topics module.
"""


def insert_school(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name

    Returns the new _id
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
