#!/usr/bin/env python3
"""LIST ALL DOCUMENTS IN A COLLECTION IN A LIST"""

import pymongo
from typing import List


def list_all(mongo_collection) -> List:
    """Returns all documents in a collection in a list"""
    documents: List = mongo_collection.find({})
    return documents
