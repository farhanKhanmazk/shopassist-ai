from agents.return_agent import process_message

print("ShopAssist AI Started")

while True:
    message = input("Customer: ")

    response = process_message(message)

    print("Agent:", response)