Feature: Search in Sogou WebSite
    In order to Search in Sogou WebSite
    As a tester
    We will test the Sogou WebSite using the word 'NBA players'

    Scenario: Search the NBA players
        Given I have the english name "<search_name>"
        When I search it in Sogou website
        Then I see the entire name "<search_result>"

    Examples:
        | search_name | search_result |
        | Jordan | Michael |
        | Curry | Stephen |
        | Kobe | Bryant |
