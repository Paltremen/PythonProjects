def describe_city(city, country = "the UK"):
    print(f"{city.title()} is in {country}")

describe_city("leeds")
describe_city(city = "york")
describe_city(country = "Russia", city = "moscow")