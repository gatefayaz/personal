Feature Azure_Inrastructure

    Scenario: Test if expected resources are provisioned in the Subscription
        Given I have access to Azure
        When I list available resources
        Then I can find expected resources

    Scenario: Test if DataFactory has right linked services
        Given I have DataFactory provisioned
        When I list available linked services
        Then I can find expected linked services
