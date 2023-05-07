Feature: API SDET test

    @Test_02
  Scenario Outline: As a user I could create user account only using valid data
    Given I have <access_url> to create user with <name> <gender> <email> and <status>
    When I send the request with header details <accept> <content_type> and valid token
    Then I should have expected <status_code_expected> response code
#    And I should have expected response

    Examples:
    |access_url|name|gender|email|status|accept|content_type|status_code_expected|
    |https://gorest.co.in/public/v2/users|Tenali Ramakrishna|male|packer2@123c.com|active|application/json|application/json|201|
    |https://gorest.co.in/public/v2/users|Tenali Ramakrishna|male|packer2@123c.com|active|application/json|application/json|422|
    |https://gorest.co.in/public/v2/users|Tenali Ramakrishna|111male|packer1@123c.com|active|application/json|application/json|422|
      |https://gorest.co.in/public/v2/users|Tenali Ramakrishna|male|packer1@@123c.com|active|application/json|application/json|422|


    @Test_03
  Scenario Outline: As a user I could create post for existing user only using valid data
    Given I have <access_url_post> to create post for <user> with <title> and <body_post>
    When I send the user post request with header details <accept> <content_type> and valid token
    Then I should have expected <status_code_expected> response code for user post request
#    And I should have expected response

    Examples:
    |access_url_post|user|title|body_post|accept|content_type|status_code_expected|
    |https://gorest.co.in/public/v2/posts|1452772|new Post|This is anew post|application/json|application/json|201|
    |https://gorest.co.in/public/v2/posts|145277299999999|new Post1|This is anew post1|application/json|application/json|422|
    |https://gorest.co.in/public/v2/posts|1452772|new Post2|This is anew post2|application/json|application/json|201|


    @Test_04
  Scenario Outline: As a user I could create post comment for existing user post only using valid data
    Given I have <access_url_post_comment> to create post comment for <post_id> with <name_commenter> <email_commenter> and <body_comment>
    When I send the user post comment request with header details <accept> <content_type> and valid token
    Then I should have expected <status_code_expected> response code for user post comment request
#    And I should have expected response

    Examples:
    |access_url_post_comment|post_id|name_commenter|email_commenter|body_comment|accept|content_type|status_code_expected|
    |https://gorest.co.in/public/v2/comments|18695|Asha Asan|asan_asha@beahan.test|new comment|application/json|application/json|201|
    |https://gorest.co.in/public/v2/comments|18695|Asha Asan|asan_asha@@beahan.test|new comment1|application/json|application/json|422|

    @Test_05
  Scenario Outline: As a user I could create todo for existing user only using valid data
    Given I have <access_url_todo> to create todo for <user_id> with <todo_title> <due_on> and <todo_status>
    When I send the todo create request with header details <accept> <content_type> and valid token
    Then I should have expected <status_code_expected> response code for create todo request
#    And I should have expected response

    Examples:
    |access_url_todo|user_id|todo_title|due_on|todo_status|accept|content_type|status_code_expected|
    |https://gorest.co.in/public/v2/todos|1440251|Create plan|2023-06-02T00:00:00.000+05:30|completed|application/json|application/json|201|
    |https://gorest.co.in/public/v2/todos|1440251|Attend wedding|2023-06-02T00:00:00.000+05:30|pending|application/json|application/json|201|
      |https://gorest.co.in/public/v2/todos|1440251|Attend wedding|2023-06-02T00:00:00.000+05:30|not started|application/json|application/json|422|