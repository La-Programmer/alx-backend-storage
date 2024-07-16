#!/usr/bin/env python3
"""PROVIDES NGINX STATS"""

import pymongo
from typing import List


def get_logs(collection) -> int:
    """Get the number of documents in the collection"""
    docs_count: int = collection.count_documents({})
    return docs_count


def get_document_count_by_type(collection) -> List[int]:
    """Get the number of documents according to post type"""
    method_list: List[List[any]] = [
                ["GET"], ["POST"], ["PUT"], ["PATCH"], ["DELETE"]
            ]

    for method in method_list:
        method: List[any]
        docs_count: int = collection.count_documents({"method": method[0]})
        method.append(docs_count)
    return method_list


def get_status_check_count(collection) -> int:
    """Get the number of documents with POST and path"""
    docs_count: int = collection.count_documents({"$and": [
            {"method": "GET"},
            {"path": "/status"}
        ]})
    return docs_count


def main():
    """Main function"""
    client: pymongo.MongoClient
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    logs_count: int = get_logs(nginx_collection)
    docs_count_by_list: List[List[any]]
    docs_count_by_list = get_document_count_by_type(nginx_collection)
    status_check_count: int
    status_check_count = get_status_check_count(nginx_collection)
    print(f'{logs_count} logs')
    print('Methods:')
    for method in docs_count_by_list:
        print(f'\tmethod {method[0]}: {method[1]}')
    print(f'{status_check_count} status check')


if __name__ == '__main__':
    main()
