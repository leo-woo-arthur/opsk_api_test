
Feature: session(login/logout) on IAM with Private v2 interface



Scenario: Private v2 interface: Create user will success with user_name/user_pwd/role_name
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' is existed by private v2 interface
When login with user_name 'SysAdmin' user_pwd 'SysAdmin_123' by private v2 interface
 And create user with user_name 'labRatUser_private_222222' user_pwd 'labRatUser_private_pwd' and role_name 'cloudManager,projectManager' by private v2 interface
Then I should get a '202' response by private v2 interface
 And user_name 'labRatUser_private_222222' existence in the system should be 'True' by private v2 interface
 And login with user_name 'labRatUser_private_222222' user_pwd 'labRatUser_private_pwd' by private v2 interface
 And I should get a '200' response by private v2 interface


Scenario: Private v2 interface: Created user login will success
Given user_name 'labRatUser_private_222222' user_pwd 'labRatUser_private_pwd' is existed by private v2 interface
When login with user_name 'labRatUser_private_222222' user_pwd 'labRatUser_private_pwd' by private v2 interface
Then I should get a '200' response by private v2 interface


Scenario: Private v2 interface: Create same user will fail
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' is existed by private v2 interface
  And user_name 'labRatUser_private_222222' user_pwd 'labRatUser_private_pwd' is existed by private v2 interface
When login with user_name 'SysAdmin' user_pwd 'SysAdmin_123' by private v2 interface
  And create user with user_name 'labRatUser_private_222222' user_pwd 'labRatUser_private_pwd' and role_name 'cloudManager,projectManager' by private v2 interface
#Then I should get a '409' response by private v2 interface
  And user_name 'labRatUser_private_222222' existence in the system should be 'True' by private v2 interface
  And login with user_name 'labRatUser_private_222222' user_pwd 'labRatUser_private_pwd' by private v2 interface
  And I should get a '200' response by private v2 interface


Scenario: Private v2 interface: Modify user will success
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' is existed by private v2 interface
  And user_name 'labRatUser_private_222222' user_pwd 'labRatUser_private_pwd' is existed by private v2 interface
When login with user_name 'SysAdmin' user_pwd 'SysAdmin_123' by private v2 interface
  And user_name 'labRatUser_private_222222' modify role_name to 'cloudManager' by private v2 interface
Then I should get a '202' response by private v2 interface


Scenario: Private v2 interface: Delete user will success
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' is existed by private v2 interface
#And user_name 'labRatUser_private_222222' user_pwd 'labRatUser_private_pwd' is existed by private v2 interface
When login with user_name 'SysAdmin' user_pwd 'SysAdmin_123' by private v2 interface
  And delete user_name 'labRatUser_private_222222' by private v2 interface
Then I should get a '202' response by private v2 interface
  And user_name 'labRatUser_private_222222' existence in the system should be 'False' by private v2 interface





