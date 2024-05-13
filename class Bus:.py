
#Task 1

class Vehicle:
    def __init__(self, registration_number, type, owner):
        self.registration_number = registration_number
        self.type = type
        self.owner = owner

new_owner = Vehicle(1545, "Jeep", "New Owner")
print(new_owner.owner)

# Task 2
class Event:
    def __init__(self, name, date, participants):
        self.name = name
        self.date = date
        self.participants = participants

    def add_participant(self):
        print("Adding new participant")
        self.participants += 1
        print(f"There are currently {self.participants} participants")

    def get_participant_count(self):
        print(f"There are currently {self.participants} participants")

new_event = Event ("Reunion", "Saturday", 30)
new_event.add_participant()
new_event.get_participant_count()
        