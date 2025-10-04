"""Garden advice according to season and flower type"""


def get_season_advice(season):
    """Function to get advice based on season"""
    advice = ""
    if season == "summer":
        advice += "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        advice += "Protect your plants from frost with covers.\n"
    else:
        advice += "No advice for this season.\n"
    return advice


def get_plant_advice(plant_type):
    """Function to get advice based on plant type"""
    advice = ""
    if plant_type == "flower":
        advice += "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        advice += "Keep an eye out for pests!"
    else:
        advice += "No advice for this type of plant."
    return advice


if __name__ == "__main__":
    # Main program logic
    # Get user input for the season and plant type
    season = input(
        "Enter the current season (e.g., summer, winter): ").lower()
    plant_type = input(
        "Enter your plant type (e.g., flower, vegetable): ").lower()

    season_advice = get_season_advice(season)
    plant_advice = get_plant_advice(plant_type)

    total_advice = season_advice + plant_advice

    # Print the generated advice
    print(total_advice)
