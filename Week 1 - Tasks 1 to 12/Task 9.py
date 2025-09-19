def holiday(food, trips, presents):
    funds = 50000

    print("Italian Holiday")
    print(f"Funds Remaining: €{"{0:,.2f}".format(funds)}")

    funds -= food + trips + presents

    print(f"Funds Remaining: €{"{0:,.2f}".format(funds)}")
    
food_spend = float(input("Food Spend: £"))
trip_spend = float(input("Trip Spend: £"))
present_spend = float(input("Presents Spend: £"))

holiday(food_spend, trip_spend, present_spend)
