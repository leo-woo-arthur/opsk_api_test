import time

from app.provider.iam_provider_base import *
from utils.log_it import *


class IamProvider4Private(IamProviderBase):
    def __init__(self, p_ip, p_port, p_protocol):
        super(IamProvider4Private, self).__init__(p_ip, p_port, p_protocol)

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
                self.login_token_id = response.json()['access_token']
                self.login_user_id = response.json()['id']
                self.login_user_name = response.json()['username']
            return response
        return extract_info

    @_extract_info_from_login_resp
    @_extract_info_from_each_resp
    def login_v2(self, user_name, user_pwd):
        return self.iam.private_v2_login(user_name, user_pwd)

    @_extract_info_from_login_resp
    @_extract_info_from_each_resp
    def login_v3(self, user_name, user_pwd, domain_name):
        return self.iam.private_v3_login(user_name, user_pwd, domain_name)

    @_extract_info_from_each_resp
    def user_create_v2(self, user_name, user_pwd, role_name):
        response = self.iam.private_v2_user_create(self.login_token_id, user_name, user_pwd, role_name)
        time.sleep(3)  # [zy] todo: private v2 interface is action .....
        return response

    def domain_get_id_by_name(self, domain_name):
        resp_login = self.iam.raw_v3_login_by_name_password("admin", "keystone", "Default")
        raw_login_token_id = resp_login.headers['X-Subject-Token']
        response = self.iam.raw_v3_domain_list(raw_login_token_id)

        domain_id = 'domain_id_unknown'
        if response.status_code == 200:
            for cur_domain in response.json()['domains']:
                if cur_domain['name'] == domain_name:
                    domain_id = cur_domain['id']
        return domain_id

    @_extract_info_from_each_resp
    def user_create_v3(self, user_name, user_pwd, role_name, domain_name):
        domain_id = self.domain_get_id_by_name(domain_name)
        response = self.iam.private_v3_user_create(self.login_token_id, user_name, user_pwd, role_name, domain_id)
        time.sleep(3)  # [zy] todo: private v3 interface is action .....
        return response

    @_extract_info_from_each_resp
    def user_list(self):
        return self.iam.private_common_user_list(self.login_token_id)

    def user_get_id_by_name(self, user_name):
        response = self.iam.private_common_user_list(self.login_token_id)

        user_id = 'user_id_unknown'
        if response.status_code == 200:
            for cur_user in response.json()['users']:
                logger.info('user_is_exist - user_name [%s]' % user_name)
                if cur_user['name'] == user_name:
                    user_id = cur_user['id']

        return user_id

    def user_is_exist(self, user_name):
        time.sleep(3)
        return self.user_get_id_by_name(user_name) != "user_id_unknown"

    @_extract_info_from_each_resp
    def user_modify(self, user_name, role_name):
        user_id = self.user_get_id_by_name(user_name)
        return self.iam.private_common_user_modify(self.login_token_id, user_id, user_name, role_name)

    @_extract_info_from_each_resp
    def user_delete(self, user_name):
        user_id = self.user_get_id_by_name(user_name)
        response = self.iam.private_common_user_delete(self.login_token_id, user_id)
        time.sleep(3)  # [zy] todo: private v2 interface is action .....
        return response

    def user_clean_by_name_like(self, name_like):
        response = self.iam.private_common_user_list(self.login_token_id)
        if response.status_code == 200:
            for cur_user in response.json()['users']:
                if -1 != cur_user['name'].find(name_like):
                    self.user_delete(cur_user['name'])
        time.sleep(3)  # [zy] todo: private v2 interface is action .....


