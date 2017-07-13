
Feature: user on IAM with raw v2 of openstack



Scenario: Raw v2 interface: Create user will success with user_name/user_pwd/tenant_name
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' and tenant_name 'admin' is existed by raw v2 interface
When login with user_name 'SysAdmin' user_pwd 'SysAdmin_123' and tenant_id of 'admin' by raw v2 interface
  And create user with user_name 'labRatUser_raw_222222' user_pwd 'labRatUser_raw_pwd' and tenant_id of 'admin' and email 'labRatUser1_email' enabled 'true' by raw v2 interface
Then I should get a '200' response by raw v2 interface
  And user_name 'labRatUser_raw_222222' existence in the system should be 'True' by raw v2 interface
  And login with user_name 'labRatUser_raw_222222' user_pwd 'labRatUser_raw_pwd' and tenant_id of 'admin' by raw v2 interface
  And I should get a '200' response by raw v2 interface


Scenario: Raw v2 interface: Created user login will success
Given user_name 'labRatUser_raw_222222' user_pwd 'labRatUser_raw_pwd' and tenant_name 'admin' is existed by raw v2 interface
When login with user_name 'labRatUser_raw_222222' user_pwd 'labRatUser_raw_pwd' and tenant_id of 'admin' by raw v2 interface
Then I should get a '200' response by raw v2 interface


Scenario: Raw v2 interface: Create same user will fail
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' and tenant_name 'admin' is existed by raw v2 interface
  And user_name 'labRatUser_raw_222222' user_pwd 'labRatUser_raw_pwd' and tenant_name 'admin' is existed by raw v2 interface
When login with user_name 'SysAdmin' user_pwd 'SysAdmin_123' and tenant_id of 'admin' by raw v2 interface
  And create user with user_name 'labRatUser_raw_222222' user_pwd 'labRatUser_raw_pwd' and tenant_id of 'admin' and email 'labRatUser1_email' enabled 'true' by raw v2 interface
Then I should get a '409' response by raw v2 interface
  And user_name 'labRatUser_raw_222222' existence in the system should be 'True' by raw v2 interface
  And login with user_name 'labRatUser_raw_222222' user_pwd 'labRatUser_raw_pwd' and tenant_id of 'admin' by raw v2 interface
  And I should get a '200' response by raw v2 interface


Scenario: Raw v2 interface: Modify user will success
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' and tenant_name 'admin' is existed by raw v2 interface
  And user_name 'labRatUser_raw_222222' user_pwd 'labRatUser_raw_pwd' and tenant_name 'admin' is existed by raw v2 interface
When login with user_name 'SysAdmin' user_pwd 'SysAdmin_123' and tenant_id of 'admin' by raw v2 interface
  And user_name 'labRatUser_raw_222222' modify email to 'labRatUser1_email111' enabled 'true' by raw v2 interface
Then I should get a '200' response by raw v2 interface


Scenario: Raw v2 interface: Delete user will success
Given user_name 'SysAdmin' user_pwd 'SysAdmin_123' and tenant_name 'admin' is existed by raw v2 interface
  And user_name 'labRatUser_raw_222222' user_pwd 'labRatUser_raw_pwd' and tenant_name 'admin' is existed by raw v2 interface
When login with user_name 'SysAdmin' user_pwd 'SysAdmin_123' and tenant_id of 'admin' by raw v2 interface
  And delete user_name 'labRatUser_raw_222222' by raw v2 interface
Then I should get a '204' response by raw v2 interface
  And user_name 'labRatUser_raw_222222' existence in the system should be 'False' by raw v2 interface





