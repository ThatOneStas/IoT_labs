class Conference:
    # Constructor
    def __init__(
              self,
              title: str = "",
              participants_number: int = 0,
              price: float = 0.0,
              place: str = ""
    ):
            # Initializing private fields
            self.__title = title
            self.__participants_number = participants_number
            self.__price = price
            self.__place = place
            # Initializing public fields
            self.property_one = "Property One"
            self.property_two = "Property Two"
    # Destructor
    def __del__(self):
        print(f"Deleting: {self.__title}")

    # Accessors
    def get_title(self):
        return self.__title
    def set_title(self, title):
        self.__title = title

    def get_participants_number(self):
        return self.__participants_number
    def set_participants_number(self, participants_number):
        self.get_participants_number = participants_number

    def get_price(self):
        return self.__price
    def set_price(self, price):
        self.__price = price

    def get_place(self):
        return self.__place
    def set_place(self, place):
        self.__place = place

    # Overridden methods
    def __str__(self):
        return (f"Title: {self.__title}\n"
                f"- Participants count: {self.__participants_number}\n"
                f"- Price: {self.__price}\n"
                f"- Place: {self.__place}\n"
                f"- Property one: {self.property_one}\n"
                f"- Property two: {self.property_two}"
                )
    def __repr__(self):
        return (f"Conference(title={self.__title}, "
                f"participants_number={self.__participants_number}, "
                f"price={self.__price}, "
                f"place={self.__place})"
                )

def main():
    # 1
    print("Example 1_1:")
    conf = Conference("Python Conference", 100, 299.99, "New York")
    print(conf)
    print(repr(conf))
    conf.set_title("Advanced Python Conference")
    conf.set_participants_number(150)
    conf.set_price(399.99)
    conf.set_place("San Francisco")
    print("\nExample 1_2:")
    print(conf)
    print(repr(conf))
    # 2
    print("\nExample 2:")
    conf2 = Conference()
    print(conf2)
    print(repr(conf2))
    # 3
    print("\nExample 3:")
    conf3 = Conference("Data Science Conference", 200, 499.99, "Los Angeles")
    print(conf3)
    print(repr(conf3))

main()