from app.provider.iam_provider_base import *


class IamProvider4RawV2(IamProviderBase):
    def __init__(self, p_ip, p_port, p_protocol):
        super(IamProvider4RawV2, self).__init__(p_ip, p_port, p_protocol)

    def _extract_info_from_each_resp(func):
        def extract_info(self, *args, **kwargs):
            response = func(self, *args, **kwargs)
            self.latest_resp_status_code = response.status_code
            return response

        return extract_info

    def _extract_info_from_login_resp(func):
        def extract_info(self, *args, **kwargs):
            response = func(self, *args, **kwargs)
            self.login_cur_status_code = response.status_code
            if response.status_code == 200:
                self.login_token_id = response.json()['access']['token']['id']
                self.login_user_id = response.json()['access']['user']['username']
                self.login_user_name = response.json()['access']['user']['id']
            return response
        return extract_info

    @_extract_info_from_login_resp
    @_extract_info_from_each_resp
    def login_by_tenant_name(self, user_name, user_pwd, tenant_name):
        response = self.iam.raw_v2_login_by_tenant_name(user_name, user_pwd, tenant_name)
        return response


    @_extract_info_from_login_resp
    @_extract_info_from_each_resp
    def login_by_tenant_id(self, user_name, user_pwd, tenant_id):
        response = self.iam.raw_v2_login_by_tenant_id(user_name, user_pwd, tenant_id)
        return response

    @_extract_info_from_each_resp
    def tenant_list(self):
        response = self.iam.raw_v2_tenant_list(self.login_token_id)
        return response

    def tenant_get_id_by_name(self, tenant_name):
        response = self.iam.raw_v2_tenant_get_by_name(self.login_token_id, tenant_name)
        tenant_id = "tenant_id_unknown"
        if response.status_code == 200:
            for cur_tenant in response.json()['tenants']:
                if cur_tenant['name'] == tenant_name:
                    tenant_id = cur_tenant['id']
        elif response.status_code == 401:
            tenant_id = "tenant_id_401"
        return tenant_id

    @_extract_info_from_each_resp
    def user_create(self, user_name, user_pwd, tenant_name, email='', enabled='true'):
        tenant_id = self.tenant_get_id_by_name(tenant_name)
        response = self.iam.raw_v2_user_create(self.login_token_id, user_name, user_pwd, tenant_id, email, enabled)
        return response

    @_extract_info_from_each_resp
    def user_list(self):
        response = self.iam.raw_v2_user_list(self.login_token_id)
        return response

    def user_get_id_by_name(self, user_name):
        response = self.iam.raw_v2_user_list(self.login_token_id)
        user_id = 'user_id_unknown'
        if response.status_code == 200:
            for cur_user in response.json()['users']:
                if cur_user['username'] == user_name:
                    user_id = cur_user['id']

        return user_id

    def user_is_exist(self, user_name):
        response = self.iam.raw_v2_user_list(self.login_token_id)
        is_exist = False
        if response.status_code == 200:
            for cur_user in response.json()['users']:
                if cur_user['username'] == user_name:
                    is_exist = True
        return is_exist

    @_extract_info_from_each_resp
    def user_modify(self, user_name, email, enabled):
        user_id = self.user_get_id_by_name(user_name)
        response = self.iam.raw_v2_user_modify(self.login_token_id, user_id, email, enabled)
        return response

    @_extract_info_from_each_resp
    def user_delete(self, user_name):
        user_id = self.user_get_id_by_name(user_name)
        response = self.iam.raw_v2_user_delete(self.login_token_id, user_id)
        return response

    def user_clean_by_name_like(self, name_like):
        response = self.iam.raw_v2_user_list(self.login_token_id)
        if response.status_code == 200:
            for cur_user in response.json()['users']:
                if -1 != cur_user['name'].find(name_like):
                    self.user_delete(cur_user['name'])



