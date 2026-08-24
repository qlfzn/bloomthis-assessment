import json


def get_total_completed():
    # read json file
    # parse them into a list of dict
    # get the amount for all completed transaction
    # sum up the amount to get the total
    # return the total
    with open("./transactions.json") as json_file:
        records = json.load(json_file)

    total_amount = 0
    for txn in records:
        if txn["status"] == "completed":
            total_amount += txn["amount"]

    print(f"Total amount for completed orders: {total_amount}")
    
get_total_completed()