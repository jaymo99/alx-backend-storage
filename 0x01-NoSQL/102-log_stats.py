#!/usr/bin/env python3
"""
102-log_stats module.
Provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    filter = [
        {'$group': {'_id': '$ip', 'count': {'$sum': 1}}},
        {'$sort': {'count': -1}},
        {'$limit': 10}
    ]

    print(logs.count_documents({}), "logs")
    print("Methods:")

    for method in methods:
        print(
            "\tmethod {}:".format(method),
            logs.count_documents({"method": "{}".format(method)})
            )
    print(logs.count_documents({"method": "GET", "path": "/status"}),
          "status check")

    print('IPs:')
    popular_ips = logs.aggregate(filter)
    for ip in popular_ips:
        print('\t{}: {}'.format(ip['_id'], ip['count']))
