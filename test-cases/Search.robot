*** Settings ***
Documentation     Your documentation related to test-cases on this module

Resource            ../modules/search/Keywords.robot

*** Test Cases ***
Scenario: Filter search based on price and validate result
    Given From Home Page
    When Filter Properties By Price
    Then Search Result Should Not Be More Than Maximum And Less Than Minimum