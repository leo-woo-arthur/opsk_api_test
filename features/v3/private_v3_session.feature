from steps import *



Feature: session(login/logout) on IAM with Private v3 interface



Scenario: Private v3 interface: Login will success with user_name/user_pwd/domain_name
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' and domain_name 'Default' is existed by private v3 interface
When login with user_name 'SysAdmin' user_pwd 'SysAdmin_123' and domain_name 'Default' by private v3 interface
Then I should get a '200' response by private v3 interface
  And call Private v3 interface with this login token will success


Scenario: Private v3 interface: Login will fail with wrong user_name
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' and domain_name 'Default' is existed by private v3 interface
When login with user_name 'SysAdmin_Wrong' user_pwd 'SysAdmin_123' and domain_name 'Default' by private v3 interface
Then I should get a '406' response by private v3 interface


Scenario: Private v3 interface: Login will fail with wrong user_pwd
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' and domain_name 'Default' is existed by private v3 interface
When login with user_name 'SysAdmin' user_pwd 'SysAdmin_Wrong' and domain_name 'Default' by private v3 interface
Then I should get a '406' response by private v3 interface



