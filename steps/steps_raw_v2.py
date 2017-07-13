from lettuce import step
from nose.tools import assert_equals

from app.application import app_raw_v2
from utils.functions import *


app = app_raw_v2


@step(u'I should get a \'(.*)\' response by raw v2 interface')
def response_status_code_should_be_expected(step, expected_status_code):
    assert_equals(app.latest_resp_status_code, int(expected_status_code))


@step(u'user_name \'(.*)\' user_pwd \'(.*)\' and tenant_name \'(.*)\' is existed by raw v2 interface')
def user_should_existed(step, user_name, user_pwd, tenant_name):
    response = app.login_by_tenant_name(user_name, user_pwd, tenant_name)
    assert_equals(response.status_code, int(200))


@step(u'login with user_name \'(.*)\' user_pwd \'(.*)\' and tenant_name \'(.*)\' by raw v2 interface')
def login_by_tenant_name(step, user_name, user_pwd, tenant_name):
    app.login_by_tenant_name(user_name, user_pwd, tenant_name)


@step(u'login with user_name \'(.*)\' user_pwd \'(.*)\' and tenant_id of \'(.*)\' by raw v2 interface')
def login_by_tenant_id(step, user_name, user_pwd, tenant_name):
    tenant_id = app.tenant_get_id_by_name(tenant_name)
    app.login_by_tenant_id(user_name, user_pwd, tenant_id)


@step(u'call raw v2 interface with this login token will success')
def get_tenants_response_should_be_expected(step):
    assert_equals(app.tenant_list().status_code, 200)


@step(u'create user with user_name \'(.*)\' user_pwd \'(.*)\' and tenant_id of \'(.*)\' and email \'(.*)\' enabled \'(.*)\' by raw v2 interface')
def user_create(step, user_name, user_pwd, tenant_name, email='', enabled='true'):
    app.user_create(user_name, user_pwd, tenant_name, email, enabled)


@step(u'user_name \'(.*)\' existence in the system should be \'(.*)\' by raw v2 interface')
def user_name_should_exist(step, user_name, exist_flag):
    assert_equals(app.user_is_exist(user_name), str_flag_to_bool(exist_flag))


@step(u'user_name \'(.*)\' modify email to \'(.*)\' enabled \'(.*)\' by raw v2 interface')
def user_modify(step, user_name, email, enabled):
    app.user_modify(user_name, email, str_flag_to_bool(enabled))


@step(u'delete user_name \'(.*)\' by raw v2 interface')
def user_delete(step, user_name):
    app.user_delete(user_name)

