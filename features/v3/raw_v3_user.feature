
Feature: user on IAM with raw v3 of openstack



Scenario: Raw v3 interface: Create user will success with user_name/user_pwd/domain_name
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' and domain_name 'Default' is existed by raw v3 interface
When login with user_name 'SysAdmin' user_pwd 'SysAdmin_123' and domain_name 'Default' by raw v3 interface
  And create user with user_name 'labRatUser_raw_333333' user_pwd 'labRatUser_raw_pwd' and domain_name 'Default' and enabled 'true' by raw v3 interface
Then I should get a '200' response by raw v3 interface
  And user_name 'labRatUser_raw_333333' existence in the system should be 'True' by raw v3 interface
  And assign user_name 'labRatUser_raw_333333' a role with role_name 'admin' in domain_name 'Default' by raw v3 interface
  And login with user_name 'labRatUser_raw_333333' user_pwd 'labRatUser_raw_pwd' and domain_name 'Default' by raw v3 interface
  And I should get a '201' response by raw v3 interface


Scenario: Raw v3 interface: Created user and login with user_id will success
Given user_name 'labRatUser_raw_333333' user_pwd 'labRatUser_raw_pwd' and domain_name 'Default' is existed by raw v3 interface
When login with user_id of 'labRatUser_raw_333333' user_pwd 'labRatUser_raw_pwd' and domain_name 'Default' by raw v3 interface
Then I should get a '201' response by raw v3 interface


Scenario: Raw v3 interface: Create same user will fail
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' and domain_name 'Default' is existed by raw v3 interface
  And user_name 'labRatUser_raw_333333' user_pwd 'labRatUser_raw_pwd' and domain_name 'Default' is existed by raw v3 interface
When login with user_name 'SysAdmin' user_pwd 'SysAdmin_123' and domain_name 'Default' by raw v3 interface
  And create user with user_name 'labRatUser_raw_333333' user_pwd 'labRatUser_raw_pwd' and domain_name 'Default' and enabled 'true' by raw v3 interface
Then I should get a '409' response by raw v3 interface
  And user_name 'labRatUser_raw_333333' existence in the system should be 'True' by raw v3 interface
  And login with user_name 'labRatUser_raw_333333' user_pwd 'labRatUser_raw_pwd' and domain_name 'Default' by raw v3 interface
  And I should get a '201' response by raw v3 interface


Scenario: Raw v3 interface: Modify user will success
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' and domain_name 'Default' is existed by raw v3 interface
  And user_name 'labRatUser_raw_333333' user_pwd 'labRatUser_raw_pwd' and domain_name 'Default' is existed by raw v3 interface
When login with user_name 'SysAdmin' user_pwd 'SysAdmin_123' and domain_name 'Default' by raw v3 interface
  And user_name 'labRatUser_raw_333333' modify password to 'labRatUser_raw_pwd_11' enabled 'true' by raw v3 interface
Then I should get a '200' response by raw v3 interface
  And login with user_name 'labRatUser_raw_333333' user_pwd 'labRatUser_raw_pwd_11' and domain_name 'Default' by raw v3 interface
  And I should get a '201' response by raw v3 interface


Scenario: Raw v3 interface: Delete user will success
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' and domain_name 'Default' is existed by raw v3 interface
  And user_name 'labRatUser_raw_333333' user_pwd 'labRatUser_raw_pwd_11' and domain_name 'Default' is existed by raw v3 interface
When login with user_name 'SysAdmin' user_pwd 'SysAdmin_123' and domain_name 'Default' by raw v3 interface
  And delete user_name 'labRatUser_raw_333333' by raw v3 interface
Then I should get a '204' response by raw v3 interface
  And user_name 'labRatUser_raw_333333' existence in the system should be 'False' by raw v3 interface





