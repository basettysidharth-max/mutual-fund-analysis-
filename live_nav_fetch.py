import requests
import pandas as pd

schemes = [119551, 120503, 118632, 119092, 120841]

nav_data = []

for code in schemes:
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        nav_data.append({
            "amfi_code": code,
            "scheme_name": data["meta"]["scheme_name"],
            "latest_nav": data["data"][0]["nav"],
            "date": data["data"][0]["date"]
        })

nav_df = pd.DataFrame(nav_data)

nav_df.to_csv("live_nav_5_schemes.csv", index=False)

print(nav_df)
