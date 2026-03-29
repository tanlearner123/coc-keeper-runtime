Feature: Combat Round Resolution
  Scenario: Keeper resolves a combat round with initiative order
    Given a campaign session with 3 ready players in SCENE_ROUND_OPEN
    And the active adventure is loaded
    When the keeper initiates a combat round
    And all players submit combat actions
    Then the rules engine resolves each action in initiative order
    And SAN or HP effects are applied to relevant characters
    And the narration service generates outcome descriptions
