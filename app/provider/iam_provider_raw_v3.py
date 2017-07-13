from app.provider.iam_provider_base import *
from utils.log_it import *


class IamProvider4RawV3(IamProviderBase):
    def __init__(self, p_ip, p_port, p_protocol):
        super(IamProvider4RawV3, self).__init__(p_ip, p_port, p_protocol)

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
            if response.status_code == 201:
                self.login_token_id = response.headers['X-Subject-Token']
                self.login_user_id = response.json()['token']['user']['name']
                self.login_user_name = response.json()['token']['user']['id']
            logger.info("X-Auth-Token: " + self.login_token_id)
            return response
        return extract_info

    @_extract_info_from_login_resp
    @_extract_info_from_each_resp
    def login_by_name_password(self, user_name, user_pwd, domain_name):
        return self.iam.raw_v3_login_by_name_password(user_name, user_pwd, domain_name)

    @_extract_info_from_login_resp
    @_extract_info_from_each_resp
    def login_by_id_password(self, user_name, user_pwd, domain_name):
        user_id = self.user_get_id_by_name(user_name)
        return self.iam.raw_v3_login_by_id_password(user_id, user_pwd, domain_name)

    def domain_get_id_by_name(self, domain_name):
        response = self.iam.raw_v3_domain_list(self.login_token_id)

        domain_id = 'domain_id_unknown'
        if response.status_code == 200:
            for cur_domain in response.json()['domains']:
                if cur_domain['name'] == domain_name:
                    domain_id = cur_domain['id']
        return domain_id

    @_extract_info_from_each_resp
    def user_create(self, user_name, user_pwd, domain_name, enabled='true'):
        domain_id = self.domain_get_id_by_name(domain_name)
        return self.iam.raw_v3_user_create(self.login_token_id, user_name, user_pwd, domain_id, enabled)

    @_extract_info_from_each_resp
    def user_list(self):
        return self.iam.raw_v3_user_list(self.login_token_id)

    def user_get_id_by_name(self, user_name):
        response = self.iam.raw_v3_user_list(self.login_token_id)

        user_id = 'user_id_unknown'
        if response.status_code == 200:
            for cur_user in response.json()['users']:
                if cur_user['name'] == user_name:
                    user_id = cur_user['id']

        return user_id

    def user_is_exist(self, user_name):
        return self.user_get_id_by_name(user_name) != "user_id_unknown"

    @_extract_info_from_each_resp
    def user_modify(self, user_name, user_pwd, enabled):
        user_id = self.user_get_id_by_name(user_name)
        response = self.iam.raw_v3_user_modify(self.login_token_id, user_id, user_pwd, enabled)

        return response

    def role_get_id_by_name(self, role_name):
        response = self.iam.raw_v3_role_list(self.login_token_id)

        role_id = 'role_id_unknown'
        if response.status_code == 200:
            for cur_role in response.json()['roles']:
                if cur_role['name'] == role_name:
                    role_id = cur_role['id']

        return role_id

    def user_assign_role(self, user_name, role_name, domain_name):
        domain_id = self.domain_get_id_by_name(domain_name)
        role_id = self.role_get_id_by_name(role_name)
        user_id = self.user_get_id_by_name(user_name)

        return self.iam.raw_v3_user_assign_role(self.login_token_id, user_id, role_id, domain_id)

    @_extract_info_from_each_resp
    def user_delete(self, user_name):
        user_id = self.user_get_id_by_name(user_name)
        return self.iam.raw_v3_user_delete(self.login_token_id, user_id)

    def user_clean_by_name_like(self, name_like):
        response = self.iam.raw_v3_user_list(self.login_token_id)
        if response.status_code == 200:
            for cur_user in response.json()['users']:
                if -1 != cur_user['name'].find(name_like):
                    self.user_delete(cur_user['name'])

