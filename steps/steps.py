from lettuce import step, world, before, after
from nose.tools import assert_equals

from app.application import app_private, app_raw_v2, app_raw_v3


@before.all
def before_all():
    tear_down()


@after.all
def after_all(total):
    tear_down()


def tear_down():
    app_raw_v2.login_by_tenant_name('SysAdmin', 'SysAdmin_123', 'admin')
    app_raw_v2.user_clean_by_name_like("labRatUser")

    app_raw_v3.login_by_name_password('SysAdmin', 'SysAdmin_123', 'Default')
    app_raw_v3.user_clean_by_name_like("labRatUser")

    app_private.login_v2('SysAdmin', 'SysAdmin_123')
    app_private.user_clean_by_name_like("labRatUser")

    app_private.login_v3('SysAdmin', 'SysAdmin_123', 'Default')
    app_private.user_clean_by_name_like("labRatUser")


@before.each_feature
def setup_some_feature(feature):
    app_raw_v2.login_by_tenant_name('SysAdmin', 'SysAdmin_123', 'admin')
    if -1 != feature.name.find("v3"):
        assert_equals(get_keystone_version(app_raw_v3), "v3")


def get_keystone_version(provider):
    response = provider.get_keystone_version()
    version = "unknown"
    if response.status_code < 300:
        version = response.json()['version']
    return version

