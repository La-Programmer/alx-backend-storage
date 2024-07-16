#!/usr/bin/env python3
"""UPDATE A DOCUMENT"""

import pymongo


def update_topics(mongo_collection, name, topics):
    """Update a document"""
    updated = mongo_collection.update_one(
        {"name": name}, {"$set": {"topics": topics}}
    )
