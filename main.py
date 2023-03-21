import pandas as pd
import requests
import json

iterable_update = "https://api.iterable.com/api/users/update"

update_headers = {
    "Content-Type": "application/json",
    "Api-Key": "f435988be541463fb59da3e9d16d0925"
}

df = pd.read_csv("Phone Numbers Need Backfill -- 03-21-23.csv")
# print(df.values)

all_data = {x: "+" + str(y) for x, y in df.values}
# print(all_data)

n = 0
for x, y in all_data.items():
    n += 1
    update = {
        "email": x,
        "dataFields":
            {
                "phoneNumber": y
            }
    }

    update_user = json.dumps(update)
    # print(f"Row {n}:", update_user)

    response = requests.post(url=iterable_update, data=update_user, headers=update_headers)
    print(f"Row {n}: email: {x} phone: {y} Response: ", response.json())

