from utils import Personalized, generic


def main():
    while True:
        sender_name = input("What is your name: ").strip().title()
        receiver_name = input("What is the name of the receiver: ")
        msg = "What type of card you want to send:\n\n"
        msg += "Please choose one of the available options\n"
        msg += "1 - Generic Card\n"
        msg += "2 - Personalized Card\n: "
        while True:
            choice = input(msg)
            if choice not in ["1", "2"]:
                print(
                    "Sorry enter a digit number: 1 - for generic, 2 - for personalized"
                )
            else:
                break

        if choice == "1":
            print("You have selected Generic Card!")
            msg = "Please choose one of the available templates: \n"
            msg += "1 - Happy Birthday Template Card\n"
            msg += "2 - Thank You Template Card\n:"
            while True:
                select_card = input(msg)
                if select_card not in ["1", "2"]:
                    print(
                        "Sorry enter a digit number: 1 - for birthday, 2 - for thank you"
                    )
                else:
                    break

            if select_card == "1":
                with generic(
                    "happy_bday.txt", sender_name, receiver_name
                ) as generic_card:
                    print("Your 'Happy Birthday Card' has been generated!")
                    break
            elif select_card == "2":
                with generic_card(
                    "thank_you.txt", sender_name, receiver_name
                ) as generic_card:
                    print("Your 'Thank You Card' has been generated!")
                    break

        elif choice == "2":
            msg = "You have selected Personalized Card!"
            msg += "\n Please enter your message for the receiver\n: "
            text = input(msg)
            with Personalized(sender_name, receiver_name) as personalized_card:
                personalized_card.write(txt)
            break


if __name__ == "__main__":
    main()
