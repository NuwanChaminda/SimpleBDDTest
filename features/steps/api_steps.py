import logging
import time
from behave import *
from config import *
from API_methods.post_method import post_requests
import json
import pandas as pd
use_step_matcher("re")


@given("I have (?P<access_url>.+) to create user with (?P<name>.+) (?P<gender>.+) (?P<email>.+) and (?P<status>.+)")
def step_impl(context, access_url, name, gender, email, status):
    context.url = access_url
    context.name = name
    context.gender = gender
    context.email = email
    context.status = status
    context.body = {"name": "{0}".format(name), "gender": "{0}".format(gender), "email": "{0}".format(email), "status": "{0}".format(status)}


@When("I send the request with header details (?P<accept>.+) (?P<content_type>.+) and valid token")
def step_impl(context, accept, content_type):
    context.token = configarations['API_token']['token']
    context.headers = {'Accept': '{0}'.format(accept), 'Content-Type': '{0}'.format(content_type), 'Authorization': '{0}'.format(context.token)}
    response_status_code, response_json = post_requests().post_request(context.url, context.body, context.headers)
    context.status_code = response_status_code
    context.response = response_json


@Then("I should have expected (?P<status_code_expected>.+) response code")
def step_impl(context, status_code_expected):
    assert context.status_code == int(status_code_expected)


@given("I have (?P<access_url_post>.+) to create post for (?P<user>.+) with (?P<title>.+) and (?P<body_post>.+)")
def step_impl(context, access_url_post, user, title, body_post):
    context.url = access_url_post
    context.user = user
    context.title = title
    context.body_post = body_post
    context.body_for_post = {"user_id": "{0}".format(user), "title": "{0}".format(title), "body": "{0}".format(body_post)}


@When("I send the user post request with header details (?P<accept>.+) (?P<content_type>.+) and valid token")
def step_impl(context, accept, content_type):
    context.token = configarations['API_token']['token']
    context.headers = {'Accept': '{0}'.format(accept), 'Content-Type': '{0}'.format(content_type), 'Authorization': '{0}'.format(context.token)}
    response_status_code_post, response_json = post_requests().post_request(context.url, context.body_for_post, context.headers)
    context.status_code_post = response_status_code_post
    context.response = response_json


@Then("I should have expected (?P<status_code_expected>.+) response code for user post request")
def step_impl(context, status_code_expected):
    assert context.status_code_post == int(status_code_expected)


@given("I have (?P<access_url_post_comment>.+) to create post comment for (?P<post_id>.+) with (?P<name_commenter>.+) (?P<email_commenter>.+) and (?P<body_comment>.+)")
def step_impl(context, access_url_post_comment, post_id, name_commenter, email_commenter, body_comment):
    context.url = access_url_post_comment
    context.post_id = post_id
    context.name_commenter = name_commenter
    context.email_commenter = email_commenter
    context.body_comment = body_comment
    context.body_for_post_comment = {"post_id": "{0}".format(post_id), "name": "{0}".format(name_commenter), "email": "{0}".format(email_commenter), "body": "{0}".format(body_comment)}


@When("I send the user post comment request with header details (?P<accept>.+) (?P<content_type>.+) and valid token")
def step_impl(context, accept, content_type):
    context.token = configarations['API_token']['token']
    context.headers = {'Accept': '{0}'.format(accept), 'Content-Type': '{0}'.format(content_type), 'Authorization': '{0}'.format(context.token)}
    response_status_code_post_comment, response_json = post_requests().post_request(context.url, context.body_for_post_comment, context.headers)
    context.status_code_post_comment = response_status_code_post_comment
    context.response = response_json


@Then("I should have expected (?P<status_code_expected>.+) response code for user post comment request")
def step_impl(context, status_code_expected):
    assert context.status_code_post_comment == int(status_code_expected)


@given("I have (?P<access_url_todo>.+) to create todo for (?P<user_id>.+) with (?P<todo_title>.+) (?P<due_on>.+) and (?P<todo_status>.+)")
def step_impl(context, access_url_todo, user_id, todo_title, due_on, todo_status):
    context.url = access_url_todo
    context.user_id = user_id
    context.todo_title = todo_title
    context.due_on = due_on
    context.todo_status = todo_status
    context.body_for_create_todo = {"user_id": "{0}".format(user_id), "title": "{0}".format(todo_title), "due_on": "{0}".format(due_on), "status": "{0}".format(todo_status)}


@When("I send the todo create request with header details (?P<accept>.+) (?P<content_type>.+) and valid token")
def step_impl(context, accept, content_type):
    context.token = configarations['API_token']['token']
    context.headers = {'Accept': '{0}'.format(accept), 'Content-Type': '{0}'.format(content_type), 'Authorization': '{0}'.format(context.token)}
    response_status_code_todo, response_json = post_requests().post_request(context.url, context.body_for_create_todo, context.headers)
    context.status_code_todo = response_status_code_todo
    context.response = response_json


@Then("I should have expected (?P<status_code_expected>.+) response code for create todo request")
def step_impl(context, status_code_expected):
    assert context.status_code_todo == int(status_code_expected)


# @step("I should have expected response")
# def step_impl(context):
#     df_response = pd.json_normalize(context.response)
#     assert str(df_response[['name']].to_string()) == str(context.name)

