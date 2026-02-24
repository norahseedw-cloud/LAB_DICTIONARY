phone_book={
    "0568323222": "Amal",
    "0522222232":"Mohammed",
    "0532335983":"Khadijah",
    "0545341144":"Abdullah",
    "0545534556":"Rawan",
    "0560664566":"Faisal",
    "0567917077":"Layla"
}

def find_phone_book(phone_number: str):
    if len(phone_number) == 10 and phone_number.isdigit():
        name = phone_book.get(phone_number)
        if name:
            print(f"The owner of the number is {name}")
        else:
            print("Sorry, the number is not found")
    else:
        print("This is an invalid number")          


user_input=input("Enter the phone number: ")

find_phone_book(user_input)