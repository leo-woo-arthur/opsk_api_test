from steps import *



Feature: session(login/logout) on IAM with Private v2 interface



Scenario: Private v2 interface: Login will success with user_name/user_pwd
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' is existed by private v2 interface
When login with user_name 'SysAdmin' user_pwd 'SysAdmin_123' by private v2 interface
Then I should get a '200' response by private v2 interface
  And call Private v2 interface with this login token will success


Scenario: Private v2 interface: Login will fail with wrong user_name
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' is existed by private v2 interface
When login with user_name 'SysAdmin_Wrong' user_pwd 'SysAdmin_123' by private v2 interface
Then I should get a '406' response by private v2 interface


Scenario: Private v2 interface: Login will fail with wrong user_pwd
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' is existed by private v2 interface
When login with user_name 'SysAdmin' user_pwd 'SysAdmin_Wrong' by private v2 interface
Then I should get a '406' response by private v2 interface












