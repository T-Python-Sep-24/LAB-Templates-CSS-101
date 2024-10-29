import random

class Customer:
    def __init__(self, customer_id, age, balance, has_credit_card, is_active_member, estimated_salary):
        self.customer_id = customer_id
        self.age = age
        self.balance = balance
        self.has_credit_card = has_credit_card
        self.is_active_member = is_active_member
        self.estimated_salary = estimated_salary

    def predict_churn(self):
        """Predict churn based on customer attributes."""
        if self.balance < 5000 and not self.is_active_member:
            return True
        elif self.age > 60 and self.balance < 10000:
            return True
        elif self.has_credit_card and self.balance > 20000:
            return False
        else:
            return random.choice([True, False])  # Random prediction for other cases

def get_customer_data():
    """Get customer data from user input."""
    customer_data = {}
    try:
        customer_data['customer_id'] = input("Enter customer ID: ")
        customer_data['age'] = int(input("Enter customer age: "))
        customer_data['balance'] = float(input("Enter account balance: "))
        customer_data['has_credit_card'] = input("Has credit card? (yes/no): ").strip().lower() == 'yes'
        customer_data['is_active_member'] = input("Is active member? (yes/no): ").strip().lower() == 'yes'
        customer_data['estimated_salary'] = float(input("Enter estimated salary: "))
        
        return customer_data
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None

def main():
    """Main function to run churn prediction."""
    customers = []
    
    while True:
        customer_data = get_customer_data()
        if customer_data is None:
            continue
        
        customer = Customer(**customer_data)
        churn_prediction = customer.predict_churn()
        
        if churn_prediction:
            print(f"Customer {customer.customer_id} is likely to churn.")
        else:
            print(f"Customer {customer.customer_id} is not likely to churn.")
        
        customers.append(customer)
        
        another = input("Do you want to check another customer? (yes/no): ").strip().lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()