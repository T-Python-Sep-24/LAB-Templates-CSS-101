# Blood Bank Management System

class BloodBank:
    def __init__(self):
        self.donors = {}  # Dictionary to store donor information

    def add_donor(self, name, blood_type, quantity):
        donor_id = len(self.donors) + 1
        self.donors[donor_id] = {
            'name': name,
            'blood_type': blood_type,
            'quantity': quantity
        }
        print(f"Donor {name} added successfully!")

    def view_donors(self):
        if not self.donors:
            print("No donors found.")
        else:
            for donor_id, details in self.donors.items():
                print(f"ID: {donor_id}, Name: {details['name']}, Blood Type: {details['blood_type']}, Quantity: {details['quantity']}")

    def search_donor(self, donor_id):
        if donor_id in self.donors:
            details = self.donors[donor_id]
            print(f"ID: {donor_id}, Name: {details['name']}, Blood Type: {details['blood_type']}, Quantity: {details['quantity']}")
        else:
            print("Donor not found.")

    def total_blood_quantity(self):
        total = sum(details['quantity'] for details in self.donors.values())
        return total

def display_menu():
    print("\n--- Blood Bank Management System ---")
    print("1. Add Donor")
    print("2. View Donors")
    print("3. Search Donor")
    print("4. Total Blood Quantity")
    print("5. Exit")

def main():
    blood_bank = BloodBank()
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            name = input("Enter donor name: ")
            blood_type = input("Enter blood type (A, B, AB, O): ")
            quantity = float(input("Enter quantity of blood (in liters): "))
            blood_bank.add_donor(name, blood_type, quantity)
        elif choice == '2':
            blood_bank.view_donors()
        elif choice == '3':
            donor_id = int(input("Enter donor ID to search: "))
            blood_bank.search_donor(donor_id)
        elif choice == '4':
            total_quantity = blood_bank.total_blood_quantity()
            print(f"Total blood quantity in the bank: {total_quantity} liters")
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
