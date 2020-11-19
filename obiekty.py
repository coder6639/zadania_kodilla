from faker import Faker

fake = Faker()


class BaseContact:
    def __init__(self, name, surname, number, email):
        self.name = name
        self.surname = surname
        self.number = number
        self.email = email

        # Variables
        self._label_length = 0

    def __str__(self):
        return f"{self.name}, {self.surname}, {self.email}"

    def contact(self):
        print(f"Wybieram numer {self.number} i dzwonię do {self.name} {self.surname}")

    @property
    def label_length(self):
        self._label_length = len(self.name) + len(self.surname)
        return self._label_length


class BusinessContact(BaseContact):
    def __init__(self, job, company, work_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.work_number = work_number

        # Variables
        self._label_length = len(self.name) + len(self.surname)

    def contact(self):
        print(f"Wybieram numer {self.work_number} i dzwonię do {self.name} {self.surname}")

    @property
    def label_length(self):
        return self._label_length


def create_contacts(item, quantity: int):
    if item == BaseContact:
        for j in range(quantity):
            entry = BaseContact(name=fake.first_name(),
                                surname=fake.last_name(),
                                number=fake.phone_number(),
                                email=fake.email())
            print(entry)
            people.append(entry)
    elif item == BusinessContact:
        for j in range(quantity):
            entry = BusinessContact(name=fake.first_name(),
                                    surname=fake.last_name(),
                                    number=fake.phone_number(),
                                    email=fake.email(),
                                    job=fake.job(),
                                    company=fake.company(),
                                    work_number=fake.phone_number())
            people.append(entry)


people = []

create_contacts(BusinessContact, 4)

for i in range(4):
    print(people[i].number)
    print(people[i].work_number)
    BaseContact.contact(self=people[i])
    BusinessContact.contact(self=people[i])
    print(people[i].label_length)
