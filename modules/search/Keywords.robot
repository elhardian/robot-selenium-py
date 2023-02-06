*** Settings ***
Documentation       Keywords with robot syntax

Library            ./Usecases.py

*** Keywords ***

From Home Page
    go_to_home_page
    check_visibility_of_home_page

Filter Properties By Price
    click_on_filter_button
    input_filter_minimum_amount
    input_filter_maximum_amount
    submit_search_filter

Search Result Should Not Be More Than Maximum And Less Than Minimum
    validate_price_on_search_result