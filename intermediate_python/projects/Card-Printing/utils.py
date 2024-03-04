from contextlib import contextmanager


class Personalized:
    def __init__(self, sender_name, receiver_name):
        self.sender_name = sender_name
        self.receiver_name = receiver_name
        self.file = f"{self.sender_name}_personalized.txt"

    def __enter__(self):
        self.opened_file = open(self.file, "w")
        self.opened_file.write(f"Dear {self.receiver_name}\n")
        return self.opened_file

    def __exit__(self, *exec):
        self.opened_file.write(f"Sincerely, \n\n{self.sender_name}")
        print("Your 'Personalized Card' has been generated!")
        self.opened_file.close()


@contextmanager
def generic(card_type, sender_name, recipient):
    template_generic_card = open(card_type, "r")
    new_generic_card = open(f"{sender_name}_generic.txt", "w")
    try:
        new_generic_card.write(f"Dear {recipient}\n\n")
        new_generic_card.write(f"{template_generic_card.read()}\n")
        new_generic_card.write(f"Sincerely, \n\n{sender_name}")
        yield new_generic_card
    finally:
        template_generic_card.close()
        new_generic_card.close()
