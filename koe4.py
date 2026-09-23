
autot = [
    {"merkki": "Toyota", "vuosi": 2018},
    {"merkki": "Ford", "vuosi": 2020},
    {"merkki": "VW", "vuosi": 2023}
]
for auto in autot:
    if auto["vuosi"] > 2019:
        print(auto["merkki"])