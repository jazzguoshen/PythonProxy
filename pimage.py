import requests
import json
import os 
d = {
        "master": {
        'image': '10.11.66.139/py3_locust_1:0.3',
        'ports': ["5558/tcp", '5557/tcp', '5559/tcp', "8089/tcp"],
        "env": ['CELERY_QUEUE=%(name)', 'task_default_queue=%(name)']},
    "python2":{
        'image': '10.11.66.139/py3_locust_1:0.3',
        'ports': ["5558/tcp", '5557/tcp', '5559/tcp', "8089/tcp"],
        "env": ['CELERY_QUEUE=%(name)', 'task_default_queue=%(name)']},
    "python3":{
        'image': '10.11.66.139/py3_locust_1:0.3',
        'ports': ["5558/tcp", '5557/tcp', '5559/tcp', "8089/tcp"],
        "env": ['CELERY_QUEUE=%(name)', 'task_default_queue=%(name)']},
    "pypy":{
        'image': '10.11.66.139/py3_locust_1:0.3',
        'ports': ["5558/tcp", '5557/tcp', '5559/tcp', "8089/tcp"],
        "env": ['CELERY_QUEUE=%(name)', 'task_default_queue=%(name)']},
    "pypy_python2":{
        'image': '10.11.66.139/py3_locust_1:0.3',
        'ports': ["5558/tcp", '5557/tcp', '5559/tcp', "8089/tcp"],
        "env": ['CELERY_QUEUE=%(name)', 'task_default_queue=%(name)']
    },
        "slaver": {
        'image': '10.11.66.139/py3_locust_1:0.3',
        'ports': ["5558/tcp", '5557/tcp', '5559/tcp', "8089/tcp"],
        "env": ['CELERY_QUEUE=%(name)', 'task_default_queue=%(name)']},
    "python2":{
        'image': '10.11.66.139/py3_locust_1:0.3',
        'ports': ["5558/tcp", '5557/tcp', '5559/tcp', "8089/tcp"],
        "env": ['CELERY_QUEUE=%(name)', 'task_default_queue=%(name)']},
    "python3":{
        'image': '10.11.66.139/py3_locust_1:0.3',
        'ports': ["5558/tcp", '5557/tcp', '5559/tcp', "8089/tcp"],
        "env": ['CELERY_QUEUE=%(name)', 'task_default_queue=%(name)']},
    "pypy":{
        'image': '10.11.66.139/py3_locust_1:0.3',
        'ports': ["5558/tcp", '5557/tcp', '5559/tcp', "8089/tcp"],
        "env": ['CELERY_QUEUE=%(name)', 'task_default_queue=%(name)']},
    "pypy_python2":{
        'image': '10.11.66.139/py3_locust_1:0.3',
        'ports': ["5558/tcp", '5557/tcp', '5559/tcp', "8089/tcp"],
        "env": ['CELERY_QUEUE=%(name)', 'task_default_queue=%(name)']}

}

r = requests.post("http://10.11.65.105/docker/type/info/5c20cae6", data=json.dumps(d))
print r
print r.text



