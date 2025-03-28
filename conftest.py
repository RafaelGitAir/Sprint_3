import pytest

#фикстура логин/пароль
@pytest.fixture(scope='session')
def login_password():
    login_password = {'email': 'aaaaa@bbb.cc', 'password': '111223'}
    return login_password