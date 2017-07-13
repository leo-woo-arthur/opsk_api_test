from lettuce import step
from nose.tools import assert_equals

from app.application import app_private
from utils.functions import *


app = app_private


@step(u'I should get a \'(.*)\' response by private v3 interface')
def response_status_code_should_be_expected(step, expected_status_code):
    assert_equals(app.latest_resp_status_code, int(expected_status_code))


@step(u'user_name \'(.*)\' user_pwd \'(.*)\' and domain_name \'(.*)\' is existed by private v3 interface')
def user_should_existed(step, user_name, user_pwd, domain_name):
    response = app.login_v3(user_name, user_pwd, domain_name)
    assert_equals(response.status_code, int(200))


@step(u'login with user_name \'(.*)\' user_pwd \'(.*)\' and domain_name \'(.*)\' by private v3 interface')
def login_by_domain_name(step, user_name, user_pwd, domain_name):
    app.login_v3(user_name, user_pwd, domain_name)


@step(u'call private v3 interface with this login token will success')
def get_users_response_should_be_expected(step):
    assert_equals(app.user_list().status_code, 200)


@step(u'create user with user_name \'(.*)\' user_pwd \'(.*)\' and role_name \'(.*)\' and domain_name \'(.*)\' by private v3 interface')
def user_create(step, user_name, user_pwd, role_name, domain_name):
    app.user_create_v3(user_name, user_pwd, role_name, domain_name)


@step(u'user_name \'(.*)\' existence in the system should be \'(.*)\' by private v3 interface')
def user_name_should_exist(step, user_name, exist_flag):
    assert_equals(app.user_is_exist(user_name), str_flag_to_bool(exist_flag))


@step(u'user_name \'(.*)\' modify role_name to \'(.*)\' by private v3 interface')
def user_modify(step, user_name, role_name):
    app.user_modify(user_name, role_name)


@step(u'delete user_name \'(.*)\' by private v3 interface')
def user_delete(step, user_name):
    app.user_delete(user_name)



