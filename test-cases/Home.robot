*** Settings ***
Documentation     Login Test Cases

Resource            ../modules/home/Keywords.robot

*** Test Cases ***
Health Check : Check Search Page Availability
    Given From Home Page
    When User Click On Search Button
    Then Should Redirect To Search Page