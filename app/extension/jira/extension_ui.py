import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jira.pages.pages import Login
from util.conf import JIRA_SETTINGS


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)
    if datasets['custom_issues']:
        issue_key = datasets['custom_issue_key']

    # To run action as specific user uncomment code bellow.
    # NOTE: If app_specific_action is running as specific user, make sure that app_specific_action is running
    # just before test_2_selenium_z_log_out action
    #
    # @print_timing("selenium_app_specific_user_login")
    # def measure():
    #     def app_specific_user_login(username='admin', password='admin'):
    #         login_page = Login(webdriver)
    #         login_page.delete_all_cookies()
    #         login_page.go_to()
    #         login_page.set_credentials(username=username, password=password)
    #         if login_page.is_first_login():
    #             login_page.first_login_setup()
    #         if login_page.is_first_login_second_page():
    #             login_page.first_login_second_page_setup()
    #         login_page.wait_for_page_loaded()
    #     app_specific_user_login(username='admin', password='admin')
    # measure()

    @print_timing("selenium_app_custom_action")
    def measure():
        @print_timing("selenium_app_custom_action:view_issue")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/browse/{issue_key}")
            page.wait_until_visible((By.ID, "summary-val"))  # Wait for summary field visible
            page.wait_until_visible((By.ID, "ID_OF_YOUR_APP_SPECIFIC_UI_ELEMENT"))  # Wait for you app-specific UI element by ID selector
        sub_measure()
    measure()


def app_specific_action_view_admin_contacts_table(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("app_specific_action_view_admin_contacts_table")
    def measure():
        @print_timing("selenium_app_custom_action:view_admin_contacts_table")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/ContactsBook!default.jspa")
            page.wait_until_visible((By.ID, "contacts-book-table-body"))

        sub_measure()

    measure()


def app_specific_action_view_issue_contacts_table(webdriver, datasets):
    page = BasePage(webdriver)
    if datasets['custom_issues']:
        issue_key = datasets['custom_issue_key']

    @print_timing("app_specific_action_view_issue_contacts_table")
    def measure():
        @print_timing("selenium_app_custom_action:view_issue_contacts_table")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/browse/" + issue_key)
            page.get_element((By.ID, "ts-contacts-tabpanel")).click()
            page.wait_until_visible((By.ID, "contacts-table-body"))

        sub_measure()

    measure()


def app_specific_action_add_issue_contact(webdriver, datasets):
    page = BasePage(webdriver)
    if datasets['custom_issues']:
        issue_key = datasets['custom_issue_key']

    @print_timing("app_specific_action_add_issue_contact")
    def measure():
        @print_timing("selenium_app_custom_action:add_issue_contact")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/browse/" + issue_key)
            page.wait_until_visible((By.ID, "ts-add-contact-button"))
            page.get_element((By.ID, "ts-add-contact-button")).click()
            # page.wait_until_visible((By.ID, "add-new-contact-dialog"))
            # page.get_element((By.ID, "first-name")).text == "First Name"
            # page.get_element((By.ID, "last-name")).text == "Last Name"
            # page.get_element((By.ID, "default-phone-number-code")).text == "+961"
            # page.get_element((By.ID, "default-phone-number")).text == "76853593"
            # page.get_element((By.ID, "email")).text == "thinksoft@thinksoft.live" + issue_key
            # page.get_element((By.ID, "add-contact-submit")).click()
            # page.wait_until_visible((By.ID, "view-hide-company-info"))
            # page.get_element((By.ID, "company-name")).text == "Company Name"
            # page.get_element((By.ID, "add-contact-submit")).click()
        sub_measure()

    measure()


def app_specific_action_view_project_contacts(webdriver, datasets):
    page = BasePage(webdriver)
    if datasets['custom_issues']:
        issue_key = datasets['custom_issue_key']
    project_key = issue_key[:issue_key.index("-")]

    @print_timing("app_specific_action_view_project_contacts")
    def measure():
        @print_timing("selenium_app_custom_action:view_project_contacts")
        def sub_measure():
            # page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/ProjectContacts!default.jspa?projectKey=" + project_key)
            # page.wait_until_visible((By.ID, "project-contacts-table"))
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/ProjectContacts!default.jspa?projectKey=" + project_key)
            page.wait_until_visible((By.ID, "project-contacts-actions"))
            page.get_element((By.ID, "project-contacts-actions")).click()

        sub_measure()

    measure()


def app_specific_action_view_unlinked_project_contacts(webdriver, datasets):
    page = BasePage(webdriver)
    if datasets['custom_issues']:
        issue_key = datasets['custom_issue_key']
    project_key = issue_key[:issue_key.index("-")]

    @print_timing("app_specific_action_view_unlinked_project_contacts")
    def measure():
        @print_timing("selenium_app_custom_action:view_unlinked_project_contacts")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/ProjectContacts!default.jspa?projectKey=" + project_key)
            page.wait_until_visible((By.ID, "project-contacts-actions"))
            page.get_element((By.ID, "project-contacts-actions")).click()
            page.wait_until_visible((By.ID, "ts-view-unlinked-contacts-buttons"))
            page.get_element((By.ID, "ts-view-unlinked-contacts-buttons")).click()
            page.wait_until_visible((By.ID, "link-contacts-to-issue-dialog"))
            page.wait_until_visible((By.ID, "link-contacts-to-issue-dialog-close-button"))
            page.get_element((By.ID, "link-contacts-to-issue-dialog-close-button")).click()

        sub_measure()

    measure()


def app_specific_action_delete_project_contact(webdriver, datasets):
    page = BasePage(webdriver)
    if datasets['custom_issues']:
        issue_key = datasets['custom_issue_key']
    project_key = issue_key[:issue_key.index("-")]

    @print_timing("app_specific_action_delete_project_contact")
    def measure():
        @print_timing("selenium_app_custom_action:delete_project_contact")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/ProjectContacts!default.jspa?projectKey=" + project_key)
            page.wait_until_visible((By.ID, "contacts-project-table-body"))
            # Select(driver.find_element(By.TAG_NAME, "select")).select_by_index(2)
            page.get_element((By.ID, "project-contacts-delete-button-")).click()
            page.wait_until_visible((By.ID, "delete-contact-confirmation-dialog"))
            page.get_element((By.ID, "delete-contact-dialog-submit-button")).click()

        sub_measure()

    measure()
