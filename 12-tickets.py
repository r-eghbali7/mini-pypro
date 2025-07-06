from datetime import datetime

meghdar_avaliye = {
    "person": {
        "beni": {"id": "1", "age": 28, "maney": 1000000},
        "ariya": {"id": "2", "age": 38, "maney": 1000000},
        "yas": {"id": "3", "age": 18, "maney": 1000000},
    },

    "airplan": {
        "mahan": {"air_id": "1", "air_tadad": 10, "air_hazine": 10000},
        "iranAir": {"air_id": "2", "air_tadad": 50, "air_hazine": 20000},
        "saba": {"air_id": "3", "air_tadad": 30, "air_hazine": 30000},
    },

    "transactions": []  # اینجا تراکنش‌ها ثبت می‌شوند
}


def buying():
    karbar = input("Enter User Name: ")

    if karbar in meghdar_avaliye["person"]:
        print(f" -------------- Welcome {karbar} ------------------\n")
        print("Choose an airline:\n")

        for aircompany in meghdar_avaliye["airplan"]:
            print(aircompany)

        name_air_company = input("\nEnter airline name: ")

        if name_air_company in meghdar_avaliye["airplan"]:
            tadad_blit = int(input("How many tickets? "))

            available = meghdar_avaliye["airplan"][name_air_company]["air_tadad"]
            price = meghdar_avaliye["airplan"][name_air_company]["air_hazine"]
            total_cost = price * tadad_blit

            if tadad_blit > available:
                print("❌ Not enough tickets available.")
                return

            if meghdar_avaliye["person"][karbar]["maney"] < total_cost:
                print("❌ Not enough money.")
                return

            # Update ticket count and user balance
            meghdar_avaliye["airplan"][name_air_company]["air_tadad"] -= tadad_blit
            meghdar_avaliye["person"][karbar]["maney"] -= total_cost

            # Save transaction
            meghdar_avaliye["transactions"].append({
                "type": "buy",
                "name": karbar,
                "airline": name_air_company,
                "count": tadad_blit,
                "cost": total_cost,
                "phone": input("Enter phone number: "),
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

            print(f"✅ Thank you {karbar} for your purchase.\n")
        else:
            print("❌ Airline not found.")
    else:
        print("❌ User not found.")


def selling():
    karbar = input("Enter User Name: ")

    if karbar in meghdar_avaliye["person"]:
        print("Which airline ticket do you want to return?")
        for aircompany in meghdar_avaliye["airplan"]:
            print(aircompany)

        name_air_company = input("Enter airline name: ")

        if name_air_company in meghdar_avaliye["airplan"]:
            tadad_blit = int(input("How many tickets to return? "))

            price = meghdar_avaliye["airplan"][name_air_company]["air_hazine"]
            total_refund = price * tadad_blit

            # بازگشت بلیت به سیستم
            meghdar_avaliye["airplan"][name_air_company]["air_tadad"] += tadad_blit
            meghdar_avaliye["person"][karbar]["maney"] += total_refund

            # ذخیره تراکنش فروش
            meghdar_avaliye["transactions"].append({
                "type": "sell",
                "name": karbar,
                "airline": name_air_company,
                "count": tadad_blit,
                "refund": total_refund,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

            print(f"✅ {tadad_blit} tickets returned by {karbar}. {total_refund} refunded.\n")
        else:
            print("❌ Airline not found.")
    else:
        print("❌ User not found.")


def reporting():
    print("********** All Data ************")
    print(meghdar_avaliye["person"])
    print(meghdar_avaliye["airplan"])
    
    print("\n********** All Transactions ************")
    for trans in meghdar_avaliye["transactions"]:
        print(trans)


# منو ساده برای تست
while True:
    print("\n1. Buy Ticket\n2. Sell Ticket\n3. Show Report\n4. Exit")
    choice = input("Select an option: ")

    if choice == "1":
        buying()
    elif choice == "2":
        selling()
    elif choice == "3":
        reporting()
    elif choice == "4":
        break
    else:
        print("❌ Invalid choice.")
