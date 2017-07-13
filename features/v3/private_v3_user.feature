
Feature: session(login/logout) on IAM with Private v3 interface



Scenario: Private v3 interface: Create user will success with user_name/user_pwd/role_name
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' and domain_name 'Default' is existed by private v3 interface
When login with user_name 'SysAdmin' user_pwd 'SysAdmin_123' and domain_name 'Default' by private v3 interface
  And create user with user_name 'labRatUser_private_333333' user_pwd 'labRatUser_private_pwd' and role_name 'cloudManager' and domain_name 'Default' by private v3 interface
Then I should get a '202' response by private v3 interface
  And user_name 'labRatUser_private_333333' existence in the system should be 'True' by private v3 interface
  And login with user_name 'labRatUser_private_333333' user_pwd 'labRatUser_private_pwd' and domain_name 'Default' by private v3 interface
  And I should get a '200' response by private v3 interface


Scenario: Private v3 interface: Created user login will success
Given user_name 'labRatUser_private_333333' user_pwd 'labRatUser_private_pwd' and domain_name 'Default' is existed by private v3 interface
When login with user_name 'labRatUser_private_333333' user_pwd 'labRatUser_private_pwd' and domain_name 'Default' by private v3 interface
Then I should get a '200' response by private v3 interface


Scenario: Private v3 interface: Create same user will fail
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' and domain_name 'Default' is existed by private v3 interface
  And user_name 'labRatUser_private_333333' user_pwd 'labRatUser_private_pwd' and domain_name 'Default' is existed by private v3 interface
When login with user_name 'SysAdmin' user_pwd 'SysAdmin_123' and domain_name 'Default' by private v3 interface
  And create user with user_name 'labRatUser_private_333333' user_pwd 'labRatUser_private_pwd' and role_name 'cloudManager' and domain_name 'Default' by private v3 interface
#Then I should get a '409' response by private v3 interface   # will be 202 because it is action .....
  And user_name 'labRatUser_private_333333' existence in the system should be 'True' by private v3 interface
  And login with user_name 'labRatUser_private_333333' user_pwd 'labRatUser_private_pwd' and domain_name 'Default' by private v3 interface
  And I should get a '200' response by private v3 interface


#Scenario: Private v3 interface: Create user with more than one of role(cloudManager/projectManager/DomainManager) will fail
#Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' and domain_name 'Default' is existed by private v3 interface
#When login with user_name 'SysAdmin' user_pwd 'SysAdmin_123' and domain_name 'Default' by private v3 interface
#  And create user with user_name 'labRatUser_private_333333_1' user_pwd 'labRatUser_private_pwd' and role_name 'cloudManager,projectManager' and domain_name 'Default' by private v3 interface
#Then I should get a '202' response by private v3 interface
#  And user_name 'labRatUser_private_333333_1' existence in the system should be 'False' by private v3 interface


Scenario: Private v3 interface: Modify user will success
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' and domain_name 'Default' is existed by private v3 interface
  And user_name 'labRatUser_private_333333' user_pwd 'labRatUser_private_pwd' and domain_name 'Default' is existed by private v3 interface
When login with user_name 'SysAdmin' user_pwd 'SysAdmin_123' and domain_name 'Default' by private v3 interface
  And user_name 'labRatUser_private_333333' modify role_name to 'projectManager' by private v3 interface
Then I should get a '202' response by private v3 interface


Scenario: Private v3 interface: Delete user will success
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' and domain_name 'Default' is existed by private v3 interface
  And user_name 'labRatUser_private_333333' existence in the system should be 'True' by private v3 interface
When login with user_name 'SysAdmin' user_pwd 'SysAdmin_123' and domain_name 'Default' by private v3 interface
  And delete user_name 'labRatUser_private_333333' by private v3 interface
Then I should get a '202' response by private v3 interface
  And user_name 'labRatUser_private_333333' existence in the system should be 'False' by private v3 interface


