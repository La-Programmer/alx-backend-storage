#!/usr/bin/env python3
"""INSERT A DOCUMENT"""

import pymongo


def insert_school(mongo_collection, **kwargs) -> str:
    """Insert a document into a collection"""
    insert_object: pymongo.InsertOneResult
    insert_object = mongo_collection.insert_one(kwargs)
    return insert_object.inserted_id
