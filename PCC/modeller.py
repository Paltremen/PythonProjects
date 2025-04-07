def car_profile(manufacturer, model, **details):
    profile = {
        "manufacturer": manufacturer,
        "model": model
    }
    profile.update(details)
    return profile