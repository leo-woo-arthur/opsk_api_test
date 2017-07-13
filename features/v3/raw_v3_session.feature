
Feature: session(login) on IAM with raw v3 of openstack



Scenario: Raw v3 interface: Login will success with user_name/user_pwd/domain_name
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' and domain_name 'Default' is existed by raw v3 interface
When login with user_name 'SysAdmin' user_pwd 'SysAdmin_123' and domain_name 'Default' by raw v3 interface
Then I should get a '201' response by raw v3 interface
  And call raw v3 interface with this login token will success


Scenario: Raw v3 interface: Login will success with user_name/user_pwd/domain_name
Given user_name 'admin' user_pwd 'keystone' and domain_name 'Default' is existed by raw v3 interface
When login with user_name 'admin' user_pwd 'keystone' and domain_name 'Default' by raw v3 interface
Then I should get a '201' response by raw v3 interface
  And call raw v3 interface with this login token will success


Scenario: Raw v3 interface: Login will fail with wrong user_name
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' and domain_name 'Default' is existed by raw v3 interface
When login with user_name 'SysAdmin_Wrong' user_pwd 'SysAdmin_123' and domain_name 'Default' by raw v3 interface
Then I should get a '401' response by raw v3 interface


Scenario: Raw v3 interface: Login will fail with wrong user_pwd
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' and domain_name 'Default' is existed by raw v3 interface
When login with user_name 'SysAdmin' user_pwd 'SysAdmin_Wrong' and domain_name 'Default' by raw v3 interface
Then I should get a '403' response by raw v3 interface


Scenario: Raw v3 interface: Login will fail with wrong domain_name
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' and domain_name 'Default' is existed by raw v3 interface
When login with user_name 'SysAdmin' user_pwd 'SysAdmin_123' and domain_name 'Default_Wrong' by raw v3 interface
Then I should get a '401' response by raw v3 interface




