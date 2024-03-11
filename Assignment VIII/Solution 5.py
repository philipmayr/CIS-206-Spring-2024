import random

STATE_CAPITALS = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississipi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",
}

correct_response_counter = 0
incorrect_response_counter = 0

states_capitals_thereof_guessed_correctly = []
previous_state = None

while correct_response_counter < 50:
    random_state = random.choice(list(STATE_CAPITALS))
    ## Pick another state if random state happens to be the same as previously guesed at state
    ## or if random state was already guessed correctly before
    while (random_state == previous_state or random_state in states_capitals_thereof_guessed_correctly):
        random_state = random.choice(list(STATE_CAPITALS))
    print("What is the capital of " + random_state + "?")
    input_capital = input("Enter the state's capital: ")
    
    if (STATE_CAPITALS[random_state].lower() == input_capital.lower().strip()):
        correct_response_counter += 1
        print("Correct!" + "(" + str(correct_response_counter) + "/50)")
        states_capitals_thereof_guessed_correctly.append(random_state)
    else:
        incorrect_response_counter += 1
        print("Incorrect!" + "(" + str(incorrect_response_counter) + ")")
    previous_state = random_state
    print()
    
