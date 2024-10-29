#import predefined page sizes 
#create and manipulate PDF documents
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Custom Exception for handling receipt errors
class ReceiptError(Exception):
    pass

# Class for Payment Receipt
class PaymentReceipt:
    def __init__(self, receipt_id, customer_name, items):
        self.receipt_id = receipt_id
        self.customer_name = customer_name
        self.items = items  # List of tuples (item_name, item_price)

    def calculate_total(self):
        """Calculate the total amount for the receipt."""
        return sum(price for _, price in self.items)

    def generate_receipt(self):
        """Generate the receipt as a dictionary."""
        return {
            'Receipt ID': self.receipt_id,
            'Customer Name': self.customer_name,
            'Items': self.items,
            'Total Amount': self.calculate_total()
        }

# Function to save receipt to a PDF file
def save_receipt_to_pdf(receipt):
    """Save the receipt as a PDF file."""
    filename = f"receipt_{receipt['Receipt ID']}.pdf"
    try:
        c = canvas.Canvas(filename, pagesize=letter)
        c.drawString(100, 750, f"Receipt ID: {receipt['Receipt ID']}")
        c.drawString(100, 730, f"Customer Name: {receipt['Customer Name']}")
        c.drawString(100, 710, "Items:")
        
        y = 690
        for item in receipt['Items']:
            c.drawString(100, y, f"{item[0]}: ${item[1]:.2f}")
            y -= 20
        
        c.drawString(100, y, f"Total Amount: ${receipt['Total Amount']:.2f}")
        c.save()
    except Exception as e:
        raise ReceiptError(f"Error saving receipt to PDF: {e}")

# Function to get items from user input
def get_items():
    """Get items from user input and return as a list of tuples."""
    items = []
    while True:
        item_name = input("Enter item name (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        item_price = float(input(f"Enter price for {item_name}: "))  # Data type casting
        items.append((item_name, item_price))
    return items

# Main function
def main():
    """Main function to create and save a payment receipt."""
    # Using variables and data type casting
    receipt_id = input("Enter Receipt ID: ")
    customer_name = input("Enter Customer Name: ")
    
    # Get items from user
    items = get_items()

    # Creating a PaymentReceipt object
    receipt = PaymentReceipt(receipt_id, customer_name, items)

    # Generating receipt
    generated_receipt = receipt.generate_receipt()
    print("\nGenerated Receipt:")
    print(generated_receipt)

    # Saving receipt to PDF
    save_receipt_to_pdf(generated_receipt)
    print(f"Receipt saved as {generated_receipt['Receipt ID']}.pdf")

if __name__ == "__main__":
    main()