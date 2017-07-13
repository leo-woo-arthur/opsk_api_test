from app.client.iam_client import IamClient


class IamProviderBase(object):
    def __init__(self, p_ip, p_port, p_protocol):
        self.iam = IamClient(ip=p_ip, port=p_port, protocol=p_protocol)
        self.login_token_id = '0'
        self.login_user_id = '0'
        self.login_user_name = '0'
        self.latest_resp_status_code = '0'
        # self.login_status_code = 0
        # self.latest_resp_text = '0'

    def get_keystone_version(self):
        response = self.iam.private_keystone_version_get()
        return response

