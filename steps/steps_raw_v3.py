from lettuce import step
from nose.tools import assert_equals

from app.application import app_raw_v3
from utils.functions import *


app = app_raw_v3


@step(u'I should get a \'(.*)\' response by raw v3 interface')
def response_status_code_should_be_expected(step, expected_status_code):
    assert_equals(app.latest_resp_status_code, int(expected_status_code))


@step(u'user_name \'(.*)\' user_pwd \'(.*)\' and domain_name \'(.*)\' is existed by raw v3 interface')
def user_should_existed(step, user_name, user_pwd, domain_name):
    response = app.login_by_name_password(user_name, user_pwd, domain_name)
    assert_equals(response.status_code, int(201))


@step(u'login with user_name \'(.*)\' user_pwd \'(.*)\' and domain_name \'(.*)\' by raw v3 interface')
def login_by_name_password(step, user_name, user_pwd, domain_name):
    app.login_by_name_password(user_name, user_pwd, domain_name)


@step(u'login with user_id of \'(.*)\' user_pwd \'(.*)\' and domain_name \'(.*)\' by raw v3 interface')
def login_by_id_password(step, user_name, user_pwd, domain_name):
    app.login_by_id_password(user_name, user_pwd, domain_name)


@step(u'call raw v3 interface with this login token will success')
def get_tenants_response_should_be_expected(step):
    assert_equals(app.user_list().status_code, 200)


@step(u'create user with user_name \'(.*)\' user_pwd \'(.*)\' and domain_name \'(.*)\' and enabled \'(.*)\' by raw v3 interface')
def user_create(step, user_name, user_pwd, domain_name, enabled='true'):
    app.user_create(user_name, user_pwd, domain_name, enabled)


@step(u'user_name \'(.*)\' existence in the system should be \'(.*)\' by raw v3 interface')
def user_name_should_exist(step, user_name, exist_flag):
    assert_equals(app.user_is_exist(user_name), str_flag_to_bool(exist_flag))


@step(u'assign user_name \'(.*)\' a role with role_name \'(.*)\' in domain_name \'(.*)\' by raw v3 interface')
def user_assign_role(step, user_name, role_name, domain_name):
    app.user_assign_role(user_name, role_name, domain_name)


@step(u'user_name \'(.*)\' modify password to \'(.*)\' enabled \'(.*)\' by raw v3 interface')
def user_modify(step, user_name, user_pwd, enabled):
    app.user_modify(user_name, user_pwd, str_flag_to_bool(enabled))


@step(u'delete user_name \'(.*)\' by raw v3 interface')
def user_delete(step, user_name):
    app.user_delete(user_name)

