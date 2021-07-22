import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jira.pages.pages import Login
from util.conf import JIRA_SETTINGS


def app_specific_action_currency_table(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_app_custom_action_view_currency_table")
    def measure():
        @print_timing("selenium_app_custom_action:view_currency_table")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/jira/secure/Currency!default.jspa")
            page.wait_until_visible((By.ID, "project-cost-currency-table-spinner"))
        sub_measure()
    measure()


def app_specific_action_cost_category_table(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_app_custom_action_cost_category_table")
    def measure():
        @print_timing("selenium_app_custom_action:cost_category_table")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/jira/secure/IssueCostCategory!default.jspa")
            page.wait_until_visible((By.ID, "cost-category-table-spinner"))
        sub_measure()
    measure()


def app_specific_action_project_cost_report(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_app_custom_action_project_cost_report")
    def measure():
        @print_timing("selenium_app_custom_action:project_cost_report")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/jira/secure/ProjectCostReport!default.jspa")
            page.wait_until_visible((By.ID, "project-cost-report-spinner"))
        sub_measure()
    measure()


def app_specific_action_permission_form(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_app_custom_action_permission_form")
    def measure():
        @print_timing("selenium_app_custom_action:permission_form")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/jira/secure/Permissions!default.jspa")
            page.wait_until_visible((By.ID, "pcfj-permissions-form-container"))
        sub_measure()
    measure()


def app_specific_action_issue_cost_details(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_app_custom_action_permission_form")
    def measure():
        @print_timing("selenium_app_custom_action:permission_form")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/jira/secure/browse/SIP-25")
            page.wait_until_visible((By.ID, "issue-cost-details"))
        sub_measure()
    measure()

