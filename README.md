Report for Assignment 1 - resit

Chosen project:

Name: cookiecutter-django

URL: https://github.com/cookiecutter/cookiecutter-django.git

Number of lines of code: 4129

Tool used for counting lines: Lizard

Programming language: Python

Coverage measurement:

In order to test my project I used the measurement tool: Coverage.py. To be able to test cookiecutter-django, I had to create another separate django project following the README_original.md setup. After accomplishing a functioning setup, I used the following command to test my project: pytest --cov=django_project.
The coverage report was completed as follows: coverage html.
![coverage_report_1](https://github.com/ionm28/Assignment1/assets/113595239/34ebc163-ac37-41f0-9c48-a528ac3d8971)

Coverage improvement:

The first function I approached is called: 	AccountAdapter.is_open_for_signup.

Commit link to prove the enhanced tests: https://github.com/cookiecutter/cookiecutter-django/commit/5a03c78631d3f8cc980613a2bae0bfe939f413e3

Old coverage result: ![first_function_unimproved](https://github.com/ionm28/Assignment1/assets/113595239/ce3caddf-a715-46f0-a4a5-1a27c760a4a9)

New coverage result: ![first_function_improved](https://github.com/ionm28/Assignment1/assets/113595239/4bae58bb-bcfe-4c6c-8042-abe58aea4557)

The coverage was improved by a 100 precent. The first test case ensures that if ACCOUNT_ALLOW_REGISTRATION is TRUE than the tested function returns the same value. Similarly, the second test case the function returns false if ACCOUNT_ALLOW_REGISTRATION is false.

The second function I approached is called: SocialAccountAdapter.is_open_for_signup

Commit link to prove the enhanced tests: https://github.com/cookiecutter/cookiecutter-django/commit/b512c18c26f596a011b11027d7f9e917983126ec

Old coverage result: ![second_function_unimproved](https://github.com/ionm28/Assignment1/assets/113595239/38bfe228-5d2f-4396-bf97-23098eee2948)

New coverage result: ![second_function_improved](https://github.com/ionm28/Assignment1/assets/113595239/487b20f6-166c-4ae5-a3ad-69b299cd23a4)

The coverage of this function was improved by 100 precent. All the test cases check if sociallogin is provided correctly and whether ACCOUNT_ALLOW_REGISTRATION is TRUE or FALSE.

Summary:

The overall coverage was improved by 10 precent.

Old coverage result: ![coverage_report_1](https://github.com/ionm28/Assignment1/assets/113595239/34ebc163-ac37-41f0-9c48-a528ac3d8971)

New coverage result: ![coverage_report_2](https://github.com/ionm28/Assignment1/assets/113595239/f97577cb-d669-48c8-879a-f055c829b53e)




