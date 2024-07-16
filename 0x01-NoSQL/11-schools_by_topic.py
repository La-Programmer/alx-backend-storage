#!/usr/bin/env python3
"""FECTCH AND FILTER ACCORDING TO TOPICS"""

import pymongo
from typing import List


def schools_by_topic(mongo_collection, topic) -> List:
    """Function to fetch and filter"""
    result_list: List = mongo_collection.find({"topics": {"$in": [topic]}})
    return result_list
