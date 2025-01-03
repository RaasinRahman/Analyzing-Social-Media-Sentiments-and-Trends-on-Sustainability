mock_tweets = [
    # Sustainability-related
    {
        "text": "Sustainability is the key to our future! #Sustainability #EcoFriendly",
        "created_at": "2024-12-02T10:00:00Z",
        "user": "User1",
        "likes": 150,
        "retweets": 45,
    },
    {
        "text": "We need to do more to reduce our carbon footprint. #ClimateAction #Sustainability",
        "created_at": "2024-12-01T15:30:00Z",
        "user": "User2",
        "likes": 200,
        "retweets": 60,
    },
    {
        "text": "Our planet needs us. Take action now! #EcoFriendly #Sustainability",
        "created_at": "2024-12-03T09:20:00Z",
        "user": "User3",
        "likes": 175,
        "retweets": 55,
    },
    # Climate Change-related
    {
        "text": "Cutting down our carbon footprint one step at a time. #CarbonFootprint #ClimateChange",
        "created_at": "2024-12-01T12:00:00Z",
        "user": "User6",
        "likes": 300,
        "retweets": 90,
    },
    {
        "text": "It's time to fight climate change together. #ClimateChange #ActNow",
        "created_at": "2024-12-02T14:10:00Z",
        "user": "User4",
        "likes": 110,
        "retweets": 25,
    },
    {
        "text": "Join the movement against climate change! #ClimateAction #ClimateChange",
        "created_at": "2024-12-04T15:00:00Z",
        "user": "User5",
        "likes": 180,
        "retweets": 80,
    },
    # Renewable Energy-related
    {
        "text": "Solar energy is a game-changer for a greener future. #RenewableEnergy #SolarPower",
        "created_at": "2024-12-03T10:00:00Z",
        "user": "User7",
        "likes": 240,
        "retweets": 70,
    },
    {
        "text": "Using renewable energy is the future of energy consumption. #GreenEnergy #RenewableEnergy",
        "created_at": "2024-12-01T13:15:00Z",
        "user": "User10",
        "likes": 220,
        "retweets": 60,
    },
    {
        "text": "Wind energy can power our planet sustainably. #WindEnergy #RenewableEnergy",
        "created_at": "2024-12-04T18:45:00Z",
        "user": "User8",
        "likes": 150,
        "retweets": 50,
    },
    # Zero Waste-related
    {
        "text": "Zero waste is not just a goal; it’s a lifestyle. #ZeroWaste #EcoFriendly",
        "created_at": "2024-12-01T10:30:00Z",
        "user": "User7",
        "likes": 100,
        "retweets": 25,
    },
    {
        "text": "Plastic-free July was a success! Let’s keep it going year-round. #ZeroWaste #PlasticFree",
        "created_at": "2024-12-03T09:30:00Z",
        "user": "User9",
        "likes": 130,
        "retweets": 40,
    },
    {
        "text": "Going zero waste will change how we interact with the environment. #ZeroWaste",
        "created_at": "2024-12-04T12:45:00Z",
        "user": "User11",
        "likes": 90,
        "retweets": 20,
    },
    # Plastic Free
    {
        "text": "Say no to single-use plastics! #PlasticFree #GoGreen",
        "created_at": "2024-12-02T17:00:00Z",
        "user": "User12",
        "likes": 70,
        "retweets": 25,
    },
    {
        "text": "Let's commit to a plastic-free future. #PlasticFree #ZeroWaste",
        "created_at": "2024-12-03T20:00:00Z",
        "user": "User13",
        "likes": 85,
        "retweets": 30,
    },
    # Eco-Friendly
    {
        "text": "Eco-friendly products are changing the market! #EcoFriendly #Sustainability",
        "created_at": "2024-12-02T10:15:00Z",
        "user": "User14",
        "likes": 120,
        "retweets": 40,
    },
    {
        "text": "Make eco-friendly choices every day. #EcoFriendly",
        "created_at": "2024-12-04T15:00:00Z",
        "user": "User15",
        "likes": 95,
        "retweets": 35,
    },
    # Miscellaneous
    {
        "text": "Water conservation is vital for our planet. #WaterConservation #SaveWater",
        "created_at": "2024-12-04T08:00:00Z",
        "user": "User16",
        "likes": 110,
        "retweets": 30,
    },
    {
        "text": "Trees are the lungs of the Earth. Plant more! #PlantTrees #GoGreen",
        "created_at": "2024-12-03T14:30:00Z",
        "user": "User17",
        "likes": 125,
        "retweets": 45,
    },
    {
        "text": "Act now to save our planet. #ActNow #ClimateCrisis",
        "created_at": "2024-12-02T19:00:00Z",
        "user": "User18",
        "likes": 150,
        "retweets": 60,
    },
   
    {
        "text": "Switching to solar power has reduced my bills by 50%! #SolarPower #RenewableEnergy",
        "created_at": "2024-12-05T09:00:00Z",
        "user": "User19",
        "likes": 180,
        "retweets": 40,
    },
    {
        "text": "Wind farms are the backbone of clean energy. #WindPower #GreenEnergy",
        "created_at": "2024-12-05T11:30:00Z",
        "user": "User20",
        "likes": 220,
        "retweets": 65,
    },
    {
        "text": "Hydropower is sustainable and reliable. #HydroPower #CleanEnergy",
        "created_at": "2024-12-06T13:45:00Z",
        "user": "User21",
        "likes": 200,
        "retweets": 50,
    },
    # Zero Waste Movement
    {
        "text": "A zero-waste kitchen is easier than you think! #ZeroWaste #SustainableLiving",
        "created_at": "2024-12-06T08:30:00Z",
        "user": "User22",
        "likes": 150,
        "retweets": 35,
    },
    {
        "text": "Refill stations are popping up everywhere. Goodbye plastic waste! #ZeroWaste #PlasticFree",
        "created_at": "2024-12-07T10:15:00Z",
        "user": "User23",
        "likes": 170,
        "retweets": 45,
    },
    # Climate Action
    {
        "text": "Governments need to prioritize climate action. #ClimateAction #NetZero",
        "created_at": "2024-12-05T14:00:00Z",
        "user": "User24",
        "likes": 250,
        "retweets": 90,
    },
    {
        "text": "Individual efforts can help tackle climate change. #ActOnClimate #EcoFriendly",
        "created_at": "2024-12-06T16:45:00Z",
        "user": "User25",
        "likes": 130,
        "retweets": 30,
    },
    {
        "text": "The time to act is now. #ClimateCrisis #ClimateJustice",
        "created_at": "2024-12-07T18:30:00Z",
        "user": "User26",
        "likes": 290,
        "retweets": 100,
    },
    # Biodiversity
    {
        "text": "Protecting forests means protecting biodiversity. #SaveForests #Biodiversity",
        "created_at": "2024-12-05T12:30:00Z",
        "user": "User27",
        "likes": 120,
        "retweets": 25,
    },
    {
        "text": "Wildlife conservation is critical to our ecosystem. #Wildlife #Conservation",
        "created_at": "2024-12-06T14:20:00Z",
        "user": "User28",
        "likes": 200,
        "retweets": 55,
    },
    {
        "text": "Marine life is under threat. We must act now! #OceanConservation #SaveTheOceans",
        "created_at": "2024-12-07T09:45:00Z",
        "user": "User29",
        "likes": 150,
        "retweets": 35,
    },
    # Miscellaneous Green Initiatives
    {
        "text": "Electric vehicles are revolutionizing transportation. #EV #CleanTransportation",
        "created_at": "2024-12-05T08:00:00Z",
        "user": "User30",
        "likes": 210,
        "retweets": 75,
    },
    {
        "text": "Tree planting initiatives are making a real difference. #PlantTrees #Reforestation",
        "created_at": "2024-12-06T12:00:00Z",
        "user": "User31",
        "likes": 140,
        "retweets": 40,
    },
    {
        "text": "Green rooftops are transforming urban cities. #UrbanGreenery #GreenLiving",
        "created_at": "2024-12-07T15:15:00Z",
        "user": "User32",
        "likes": 180,
        "retweets": 60,
    },
    {
        "text": "Composting at home reduces waste and helps the soil. #Composting #SustainableLiving",
        "created_at": "2024-12-05T17:30:00Z",
        "user": "User33",
        "likes": 130,
        "retweets": 25,
    },
    # Miscellaneous Trending
    {
        "text": "Supporting local farmers supports sustainability. #BuyLocal #SustainableAgriculture",
        "created_at": "2024-12-06T16:30:00Z",
        "user": "User34",
        "likes": 110,
        "retweets": 20,
    },
    {
        "text": "Energy-efficient homes save money and the planet. #EnergyEfficiency #GreenHomes",
        "created_at": "2024-12-07T10:45:00Z",
        "user": "User35",
        "likes": 125,
        "retweets": 30,
    }
]
