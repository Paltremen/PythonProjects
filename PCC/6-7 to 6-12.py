phil = {
    "first name": "philip",
    "last name": "varlamov",
    "age": 26,
    "city": "bobruisk",
    }

yura = {
    "first name": "yuri",
    "last name": "zenko",
    "age": 25,
    "city": "volozhin",
    }

kolya = {
    "first name": "nikolai",
    "last name": "mineev",
    "age": 22,
    "city": "minsk",
    }

friends = [phil, yura, kolya]
for friend in friends:
    print(f"The name is {friend["first name"].title()}, he is {friend["age"]} and lives in {friend["city"].title()}.")

favorite_things = {
    "phil": ["me", "gaming", "game design"],
    "yura": ["pokemon", "Japan", "gaming"],
    "kolya": ["French", "teaching", "cats"]
    }
for name, things in favorite_things.items():
    print(f"\n{name.title()}'s favorite things are:")
    for thing in things:
        print(thing)

cities = {
    "minsk": {"population": 2_000_000, "country": "belarus"},
    "london": {"population": 7_000_000, "country": "united kingdom"},
    "moscow": {"population": 10_000_000, "country": "russia"},
    }
for city, facts in cities.items():
    print(f"The name of the city is {city.title()}, its population is {facts["population"]}, "
          f"\nand it's located in {facts["country"].title()}")