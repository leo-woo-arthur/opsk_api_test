
Feature: session(login) on IAM with raw v2 of openstack


Scenario: Raw v2 interface: Login will success with user_name/user_pwd/tenant_name
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' and tenant_name 'admin' is existed by raw v2 interface
When login with user_name 'SysAdmin' user_pwd 'SysAdmin_123' and tenant_name 'admin' by raw v2 interface
Then I should get a '200' response by raw v2 interface
  And call Raw v2 interface with this login token will success


Scenario: Raw v2 interface: Login will success with user_name/user_pwd/tenant_id
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' and tenant_name 'admin' is existed by raw v2 interface
When login with user_name 'SysAdmin' user_pwd 'SysAdmin_123' and tenant_id of 'admin' by raw v2 interface
Then I should get a '200' response by raw v2 interface
  And call Raw v2 interface with this login token will success


#Scenario: Raw v2 interface: Login will success with user_name/user_pwd/tenant_name
#Given user_name 'admin' user_pwd 'keystone' and tenant_name 'admin' is existed by raw v2 interface
#When login with user_name 'admin' user_pwd 'keystone' and tenant_name 'admin' by raw v2 interface
#Then I should get a '200' response by raw v2 interface
#  And call Raw v2 interface with this login token will success


Scenario: Raw v2 interface: Login will fail with wrong user_name
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' and tenant_name 'admin' is existed by raw v2 interface
When login with user_name 'SysAdmin_Wrong' user_pwd 'SysAdmin_123' and tenant_name 'admin' by raw v2 interface
Then I should get a '406' response by raw v2 interface


Scenario: Raw v2 interface: Login will fail with wrong user_pwd
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' and tenant_name 'admin' is existed by raw v2 interface
When login with user_name 'SysAdmin' user_pwd 'SysAdmin_Wrong' and tenant_name 'admin' by raw v2 interface
Then I should get a '403' response by raw v2 interface


Scenario: Raw v2 interface: Login will fail with wrong tenant_name
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' and tenant_name 'admin' is existed by raw v2 interface
When login with user_name 'SysAdmin' user_pwd 'SysAdmin_123' and tenant_name 'admin_Wrong' by raw v2 interface
Then I should get a '401' response by raw v2 interface


Scenario: Raw v2 interface: Login will fail with wrong tenant_id
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' and tenant_name 'admin' is existed by raw v2 interface
When login with user_name 'SysAdmin' user_pwd 'SysAdmin_123' and tenant_id of 'admin111' by raw v2 interface
Then I should get a '401' response by raw v2 interface









