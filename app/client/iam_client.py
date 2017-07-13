import json

from app.client import reqwithlog
from utils.log_it import *


class IamClient(object):
    def __init__(self, ip, port, protocol):
        self.ip = ip
        self.port = port
        self.protocol = protocol

    def __get_full_url(self, p_url, p_port=None):
        cur_port = self.port
        if p_port is not None:
            cur_port = p_port
        prefix_url = "%s://%s:%s" % (self.protocol, self.ip, cur_port)
        return prefix_url + p_url

    def _log_response(func):
        def log_resp_to_file(*args, **kwargs):
            logger.info('Before calling %s' % func.__name__)
            return func(*args, **kwargs)
        return log_resp_to_file

    # --------------------  private  --------------------

    @_log_response
    def private_keystone_version_get(self):
        url = self.__get_full_url('/api/keystone_version')
        headers = {'Content-type': 'application/json'}

        return reqwithlog.get(url, headers=headers)

    @_log_response
    def private_v2_login(self, user_name, user_pwd):
        url = self.__get_full_url('/api/v1.0/auth/sessions')
        headers = {'Content-type': 'application/json'}
        body = {"username": user_name, "password": user_pwd}

        return reqwithlog.post(url, data=json.dumps(body), headers=headers)

    @_log_response
    def private_v3_login(self, user_name, user_pwd, domain_name):
        url = self.__get_full_url('/api/v1.0/auth/sessions')
        headers = {'Content-type': 'application/json'}
        body = {"username": user_name, "password": user_pwd, 'domainName': domain_name}

        return reqwithlog.post(url, data=json.dumps(body), headers=headers)

    @_log_response
    def private_v2_user_create(self, token, user_name, user_pwd, role_name, is_default='false', email='xxx', description='yyy', telephone='zzz'):
        url = self.__get_full_url('/api/v1.0/auth/users')
        headers = {'Content-type': 'application/json', 'X-Auth-Token': token}
        role_name_list = map(str.strip, map(str, role_name.split(",")))  # role_name.strip()
        body = {"user": {"name": user_name, "password": user_pwd, "isDefault": is_default, "roles": role_name_list,
                "email": email, 'description': description, 'telephone': telephone}}
        return reqwithlog.post(url, data=json.dumps(body), headers=headers)

    @_log_response
    def private_v3_user_create(self, token, user_name, user_pwd, role_name, domain_id, is_default='false', email='xxx', description='yyy', telephone='zzz'):
        url = self.__get_full_url('/api/v1.0/auth/users')
        headers = {'Content-type': 'application/json', 'X-Auth-Token': token}
        role_name_list = map(str.strip, map(str, role_name.split(",")))  # role_name.strip()
        body = {"user": {"name": user_name, "password": user_pwd, "isDefault": is_default, "roles": role_name_list,
                         "email": email, 'description': description, 'telephone': telephone, 'domainId': domain_id}}

        return reqwithlog.post(url, data=json.dumps(body), headers=headers)

    @_log_response
    def private_common_user_list(self, token):
        url = self.__get_full_url('/api/v1.0/auth/users')
        headers = {'Content-type': 'application/json', 'X-Auth-Token': token}

        return reqwithlog.get(url, headers=headers)

    @_log_response
    def private_common_user_modify(self, token, user_id, user_name, role_name):
        url = self.__get_full_url('/api/v1.0/auth/users/%s' % user_id)
        headers = {'Content-type': 'application/json', 'X-Auth-Token': token}
        role_name_list = map(str.strip, map(str, role_name.split(",")))  # role_name.strip()
        body = {"name": user_name, "roles": role_name_list}

        return reqwithlog.put(url, data=json.dumps(body), headers=headers)

    @_log_response
    def private_common_user_delete(self, token, user_id):
        url = self.__get_full_url('/api/v1.0/auth/users/%s' % user_id)
        headers = {'Content-type': 'application/json', 'X-Auth-Token': token}

        return reqwithlog.delete(url, headers=headers)

    # --------------------  v2  --------------------

    @_log_response
    def raw_v2_login_by_tenant_name(self, user_name, user_pwd, tenant_name):
        url = self.__get_full_url('/v2.0/tokens')
        headers = {'Content-type': 'application/json'}
        body = {"auth": {"passwordCredentials": {"username": user_name, "password": user_pwd}, "tenantName": tenant_name}}

        return reqwithlog.post(url, data=json.dumps(body), headers=headers)

    @_log_response
    def raw_v2_login_by_tenant_id(self, user_name, user_pwd, tenant_id):
        url = self.__get_full_url('/v2.0/tokens')
        headers = {'Content-type': 'application/json'}
        body = {"auth": {"passwordCredentials": {"username": user_name, "password": user_pwd}, "tenantId": tenant_id}}

        return reqwithlog.post(url, data=json.dumps(body), headers=headers)

    @_log_response
    def raw_v2_tenant_list(self, token):
        url = self.__get_full_url('/v2.0/tenants')
        headers = {'Content-type': 'application/json', 'X-Auth-Token': token}

        return reqwithlog.get(url, headers=headers)

    @_log_response
    def raw_v2_tenant_get_by_name(self, token, tenant_name):
        url = self.__get_full_url('/v2.0/tenants?name=%s' % tenant_name)
        headers = {'Content-type': 'application/json', 'X-Auth-Token': token}

        return reqwithlog.get(url, headers=headers)

    @_log_response
    def raw_v2_user_create(self, token, user_name, user_pwd, tenant_id, email='', enabled='true'):
        url = self.__get_full_url('/v2.0/users', p_port=36387)
        headers = {'Content-type': 'application/json', 'X-Auth-Token': token}
        body = {"user": {"name": user_name, "password": user_pwd, "tenantId": tenant_id, "email": email, "enabled": bool(enabled)}}

        return reqwithlog.post(url, data=json.dumps(body), headers=headers)

    @_log_response
    def raw_v2_user_list(self, token):
        url = self.__get_full_url('/v2.0/users', p_port=36387)
        headers = {'Content-type': 'application/json', 'X-Auth-Token': token}

        return reqwithlog.get(url, headers=headers)

    @_log_response
    def raw_v2_user_modify(self, token, user_id, email, enabled):
        url = self.__get_full_url('/v2.0/users/%s' % user_id, p_port=36387)
        headers = {'Content-type': 'application/json', 'X-Auth-Token': token}
        body = {"user": {"email": email, "enabled": enabled}}

        return reqwithlog.put(url, data=json.dumps(body), headers=headers)

    @_log_response
    def raw_v2_user_delete(self, token, user_id):
        url = self.__get_full_url('/v2.0/users/%s' % user_id, p_port=36387)
        headers = {'Content-type': 'application/json', 'X-Auth-Token': token}

        return reqwithlog.delete(url, headers=headers)

    # --------------------  v3  --------------------

    @_log_response
    def raw_v3_login_by_name_password(self, user_name, user_pwd, domain_name):
        url = self.__get_full_url('/v3/auth/tokens')
        headers = {'Content-type': 'application/json'}
        body = {"auth": {"identity": {"methods": ["password"], "password": {"user": {"name": user_name, "password": user_pwd, "domain": {"id": domain_name}}}},"scope": {"domain": {"name": domain_name}}}}

        return reqwithlog.post(url, data=json.dumps(body), headers=headers)

    @_log_response
    def raw_v3_login_by_id_password(self, user_id, user_pwd, domain_name):
        url = self.__get_full_url('/v3/auth/tokens')
        headers = {'Content-type': 'application/json'}
        body = {"auth": {"identity": {"methods": ["password"], "password": {"user": {"id": user_id, "password": user_pwd, "domain": {"id": domain_name}}}}, "scope": {"domain": {"name": domain_name}}}}

        return reqwithlog.post(url, data=json.dumps(body), headers=headers)


    @_log_response
    def raw_v3_user_create(self, token, user_name, user_pwd, domain_id, enabled='true'):
        url = self.__get_full_url('/v3/users', p_port=36387)
        headers = {'Content-type': 'application/json', 'X-Auth-Token': token}
        body = {"user": {"domain_id": domain_id, "enabled": bool(enabled), "name": user_name, "password": user_pwd}}  # ToDo[zy]: without "default_project_id": "xxxx"

        return reqwithlog.post(url, data=json.dumps(body), headers=headers)

    @_log_response
    def raw_v3_user_list(self, token):
        url = self.__get_full_url('/v3/users', p_port=36387)
        headers = {'Content-type': 'application/json', 'X-Auth-Token': token}

        return reqwithlog.get(url, headers=headers)

    @_log_response
    def raw_v3_user_modify(self, token, user_id, user_pwd, enabled):
        url = self.__get_full_url('/v3/users/%s' % user_id, p_port=36387)
        headers = {'Content-type': 'application/json', 'X-Auth-Token': token}
        body = {"user": {"password": user_pwd, "enabled": enabled}}

        return reqwithlog.patch(url, data=json.dumps(body), headers=headers)

    @_log_response
    def raw_v3_user_delete(self, token, user_id):
        url = self.__get_full_url('/v3/users/%s' % user_id, p_port=36387)
        headers = {'Content-type': 'application/json', 'X-Auth-Token': token}

        return reqwithlog.delete(url, headers=headers)

    @_log_response
    def raw_v3_user_assign_role(self, token, user_id, role_id, domain_id):
        url = self.__get_full_url('/v3/domains/%s/users/%s/roles/%s' % (domain_id, user_id, role_id), p_port=36387)
        headers = {'Content-type': 'application/json', 'X-Auth-Token': token}

        return reqwithlog.put(url, headers=headers)

    @_log_response
    def raw_v3_role_list(self, token):
        url = self.__get_full_url('/v3/roles', p_port=36387)
        headers = {'Content-type': 'application/json', 'X-Auth-Token': token}

        return reqwithlog.get(url, headers=headers)

    @_log_response
    def raw_v3_domain_list(self, token):
        url = self.__get_full_url('/v3/domains', p_port=36387)
        headers = {'Content-type': 'application/json', 'X-Auth-Token': token}

        return reqwithlog.get(url, headers=headers)






