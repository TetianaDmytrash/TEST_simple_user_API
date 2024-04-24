"""
    attempt to divide into classes
"""
import pytest
from connect import *
from constants import *


class TestCreateUserPositive:
    """
        method for checking answers
    """

    @pytest.fixture()
    def setup(self, request):
        """
            setup and cleanup fir test create user positive scenarios
        :param request:
        :return:
        """
        try:
            firstName, lastName, email, completed, username, password, summary = request.param
            yield (configure_headers(),
                   configure_payload(firstName, lastName, email, completed, username, password, summary))
        finally:
            try:
                delete_all_users(GET_ALL_USERS_LINK, DELETE_USER_LINK)
            except requests.exceptions.RequestException as e:
                logging.error(f"Error occurred during deletion all users: {e}")
            logging.info("\nCleanup - Cleaning up resources after the test")

    @pytest.mark.parametrize("setup", [
        (generate_random_string(6, DIGITS_LETTERS_CHARS), "surname1", "test1@example.com", False, "test1", "password123", "simple text 1"),
    ], indirect=True)
    def test_positive_create_user_status_code(self, setup):
        """
        Title:
        Check status code after create user.

        Description:
        After POST request check that response has status code - 201.

        Test pre-requisites:
        Setup type: COSM
        Setup topology: ROADM, P2P
        ONC VM type: NXF
        Browser supported: Firefox, Chrome
        Condition of the target setup:

        Test Steps:
        1. prepare valid data (json format).
        2. Send POST request to the (http://127.0.0.1:5000/user) with details created in step 1.
        3. verify that the response status code is 201 OK.

        Test pass/fail criteria:
        1. test pass: receiving expected status code.
        2. test pass: created valid user.
        3. test fail: user doesn`t create.

        Test exceptions:
        1.
        :param setup:
        :return:
        """
        headers, payload = setup
        try:
            response = create_user(POST_USER_LINK, headers, payload)
            assert response.status_code == 201, f"status code: {response.status_code}"
        except requests.exceptions.RequestException as e:
            logging.error(f"Error occurred during registration: {e}")

    @pytest.mark.parametrize("setup", [
        ("name222", "surname1", "test1@example.com", False, "test1", "password123", "simple text 1"),
    ], indirect=True)
    def test_positive_create_user_message(self, setup):
        """
        Title:
        Check expected message after create user.

        Description:
        After POST request check that response message is "success create user".

        Test pre-requisites:
        Setup type: COSM
        Setup topology: ROADM, P2P
        ONC VM type: NXF
        Browser supported: Firefox, Chrome
        Condition of the target setup:

        Test Steps:
        1. prepare valid data (json format).
        2. Send POST request to the (http://127.0.0.1:5000/user) with details created in step 1.
        3. verify that the response message is "success create user".

        Test pass/fail criteria:
        1. test pass: receiving expected message.
        2. test pass: created valid user.
        3. test fail: user doesn`t create.

        Test exceptions:
        1.
        :param setup:
        :return:
        """
        headers, payload = setup
        try:
            response = create_user(POST_USER_LINK, headers, payload)
            response_data = response.json()
            print(response_data["message"])
        except requests.exceptions.RequestException as e:
            logging.error(f"Error occurred during registration: {e}")


class TestCreateUserFieldPositive:
    """
        class for checking fields
    """

    @pytest.fixture()
    def setup(self):
        """
            Start setup: configure headers and payload for this class "TestCreateUserFieldPositive"
        """
        try:
            yield configure_headers()
        finally:
            try:
                delete_all_users(GET_ALL_USERS_LINK, DELETE_USER_LINK)
            except requests.exceptions.RequestException as e:
                logging.error(f"Error occurred during deletion all users: {e}")
            logging.info("\nCleanup - Cleaning up resources after the test")

    @pytest.mark.parametrize("firstName, lastName, email, completed, username, password, summary", [
        (generate_random_string(2, DIGITS_LETTERS_CHARS), "surname1", "test1@example.com", False, "test1", "password123", "simple text 1"),
        (generate_random_string(10, DIGITS_LETTERS_CHARS), "surname1", "test1@example.com", False, "test1", "password123", "simple text 1"),
        (generate_random_string(5, DIGITS_LETTERS_CHARS), "surname1", "test1@example.com", False, "test1", "password123", "simple text 1"),
        ("name-Na", "surname1", "test1@example.com", False, "test1", "password123", "simple text 1"),
    ])
    def test_positive_firstName(self, firstName, lastName, email, completed, username, password, summary, setup):
        """
        Title:
        Check the length of the "first name" field.

        Description:
        Check that if field "first name" has permissible length, user created correct.

        Test pre-requisites:
        Setup type: COSM
        Setup topology: ROADM, P2P
        ONC VM type: NXF
        Browser supported: Firefox, Chrome
        Condition of the target setup:

        Parametrize:
        name - 2 symbols
        name - 5 symbols
        name - 10 symbols
        name - hyphen


        Test Steps:
        1. prepare valid data (json format).
        2. Send POST request to the (http://127.0.0.1:5000/user) with details created in step 1.
        3. verify that the response status code is 201 OK.


        Test pass/fail criteria:
        1. test pass: receiving expected status code.
        2. test pass: created valid user.
        3. test fail: user doesn`t create.

        Test exceptions:
        1.
        """
        headers = setup
        payload = configure_payload(firstName, lastName, email, completed, username, password, summary)
        try:
            response = create_user(POST_USER_LINK, headers, payload)
        except requests.exceptions.RequestException as e:
            logging.error(f"Error occurred during registration: {e}")
        assert response.status_code == 201, f" status code not valid - {response.status_code} "

    @pytest.mark.parametrize("firstName, lastName, email, completed, username, password, summary", [
        ("name1", "su", "test1@example.com", False, "test1", "password123", "simple text 1"),
        ("name1", "surnameSur", "test1@example.com", False, "test1", "password123", "simple text 1"),
        ("name1", "surname1", "test1@example.com", False, "test1", "password123", "simple text 1"),
    ])
    def test_positive_lastName(self, firstName, lastName, email, completed, username, password, summary, setup):
        headers = setup
        payload = configure_payload(firstName, lastName, email, completed, username, password, summary)
        try:
            response = create_user(POST_USER_LINK, headers, payload)
        except requests.exceptions.RequestException as e:
            logging.error(f"Error occurred during registration: {e}")
        response_data = convert_response_to_json(get_all_users(GET_ALL_USERS_LINK))
        list_user_uid = get_users_uid(response_data)
        get_user_by_uid(GET_USER_LINK, list_user_uid[0]) # тут по идеи надо обыграть то, что я знаю, что там может прийти только один юзер
        # делать это через нулевой элемент массива как-то максимально странно та и забудется оно

    @pytest.mark.parametrize("firstName, lastName, email, completed, username, password, summary", [
        ("name1", "surname1", "test1@example.com", False, generate_random_string(2, DIGITS_LETTERS_CHARS), "password123", "simple text 1"),
        ("name1", "surname1", "test1@example.com", False, generate_random_string(10, DIGITS_LETTERS_CHARS), "password123", "simple text 1"),
        ("name1", "surname1", "test1@example.com", False, generate_random_string(5, DIGITS_LETTERS_CHARS), "password123", "simple text 1"),
    ])
    def test_positive_userName(self, firstName, lastName, email, completed, username, password, summary, setup):
        """
        Title:
        Check the length of the "username" field.

        Description:
        Check that if field "username" has permissible length, user created correct.

        Test pre-requisites:
        Setup type: COSM
        Setup topology: ROADM, P2P
        ONC VM type: NXF
        Browser supported: Firefox, Chrome
        Condition of the target setup:

        Parametrize:
        username - 2 symbols
        username - 5 symbols
        username - 10 symbols
        username - hyphen


        Test Steps:
        1. prepare valid data (json format).
        2. Send POST request to the (http://127.0.0.1:5000/user) with details created in step 1.
        3. verify that the response status code is 201 OK.


        Test pass/fail criteria:
        1. test pass: receiving expected status code.
        2. test pass: created valid user.
        3. test fail: user doesn`t create.

        Test exceptions:
        1.
        """
        headers = setup
        payload = configure_payload(firstName, lastName, email, completed, username, password, summary)
        try:
            response = create_user(POST_USER_LINK, headers, payload)
        except requests.exceptions.RequestException as e:
            logging.error(f"Error occurred during registration: {e}")
        assert response.status_code == 201, f" status code not valid - {response.status_code} "


class TestCreateUserFieldNegative:
    """
        class for checking fields -> user doesn`t create
    """

    @pytest.fixture()
    def setup(self):
        """
            Start setup: configure headers and payload for this class "TestCreateUserFieldNegative"
        """
        try:
            yield configure_headers()
        finally:
            try:
                delete_all_users(GET_ALL_USERS_LINK, DELETE_USER_LINK)
            except requests.exceptions.RequestException as e:
                logging.error(f"Error occurred during deletion all users: {e}")
            logging.info("\nCleanup - Cleaning up resources after the test")

    @pytest.mark.parametrize("firstName, lastName, email, completed, username, password, summary", [
        ("name1", "surname1", "test1@example.com", False, generate_random_string(0, DIGITS_LETTERS_CHARS), "password123", "simple text 1"),
        ("name1", "surname1", "test1@example.com", False, generate_random_string(11, DIGITS_LETTERS_CHARS), "password123", "simple text 1"),
        ("name1", "surname1", "test1@example.com", False, generate_random_string(5, LETTERS_SPECIAL_CHARS),
         "password123", "simple text 1"),
        ("name1", "surname1", "test1@example.com", False, random.randint(0, 100), "password123", "simple text 1"),
        ("name1", "surname1", "test1@example.com", False, random.choice([True, False]), "password123", "simple text 1"),
        ("name1", "surname1", "test1@example.com", False, None, "password123", "simple text 1"),
    ])
    def test_negative_userName(self, firstName, lastName, email, completed, username, password, summary, setup):
        """
        Title:
        unacceptable value in first name.

        Description:
        Check that user doesn`t create and return status code 400 if field "first name" has unacceptable value.

        Test pre-requisites:
        Setup type: COSM
        Setup topology: ROADM, P2P
        ONC VM type: NXF
        Browser supported: Firefox, Chrome
        Condition of the target setup:

        Parametrize:
        name - empty
        name - 11 symbols
        name - , | / \ ; < > ! ? . {} [] * - + () :
        name - \n || \r (not implemented)
        name - \x00 (not implemented)
        name - null (not implemented) -> None
        name - NaN
        name - "integer" - 123456
        name - "boolean" - True


        Test Steps:
        1. prepare invalid data (json format).
        2. Send POST request to the (http://127.0.0.1:5000/user) with details created in step 1.
        3. verify that the response status code is 400.


        Test pass/fail criteria:
        1. test pass: receiving expected status code.
        2. test pass: created valid user.
        3. test fail: user doesn`t create.

        Test exceptions:
        1.
        """
        headers = setup
        payload = configure_payload(firstName, lastName, email, completed, username, password, summary)
        try:
            response = create_user(POST_USER_LINK, headers, payload)
        except requests.exceptions.RequestException as e:
            logging.error(f"Error occurred during registration: {e}")
        assert response.status_code == 400, f" status code not valid - {response.status_code} "


# method for complex fast deletion all created users
def test_delete_all_users():
    try:
        delete_all_users(GET_ALL_USERS_LINK, DELETE_USER_LINK)
    except requests.exceptions.RequestException as e:
        logging.error(f"Error occurred during deletion all users: {e}")