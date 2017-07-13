import requests
import time
import uuid
from utils.log_it import *


def restful_api(method, url, params=None, data=None, json=None, **kwargs):
    cur_id = uuid.uuid1()
    time_before = time.time()
    logger.info('Before:[%s] -- method:[%s], url:[%s], data:[%s], json:[%s]' % (cur_id, method, url, "", ""))

    # Terrible
    if method == "get":
        resp = requests.get(url, params, **kwargs)
    elif method == "options":
        resp = requests.options(url, **kwargs)
    elif method == "head":
        resp = requests.head(url, **kwargs)
    elif method == "post":
        resp = requests.post(url, data, json, **kwargs)
    elif method == "put":
        resp = requests.put(url, data, **kwargs)
    elif method == "patch":
        resp = requests.patch(url, data, **kwargs)
    elif method == "delete":
        resp = requests.delete(url, **kwargs)

    used_time = time.time() - time_before
    logger.info('After:[%s] --  timing:[%s], code:[%s], result:[%s]' % (cur_id, used_time, resp.status_code, resp.text))
    return resp


def get(url, params=None, **kwargs):
    resp = restful_api("get", url, params=params, **kwargs)
    return resp


def options(url, **kwargs):
    resp = restful_api("options", url, **kwargs)
    return resp


def head(url, **kwargs):
    resp = restful_api("head", url, **kwargs)
    return resp


def post(url, data=None, json=None, **kwargs):
    resp = restful_api("post", url, data=data, json=json, **kwargs)
    return resp


def put(url, data=None, **kwargs):
    resp = restful_api("put", url, data=data, **kwargs)
    return resp


def patch(url, data=None, **kwargs):
    resp = restful_api("patch", url, data=data, **kwargs)
    return resp


def delete(url, **kwargs):
    resp = restful_api("delete", url, **kwargs)
    return resp

