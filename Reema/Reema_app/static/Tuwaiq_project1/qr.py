import qrcode
import os

# Function to generate QR code
def generate_qr_code(link, filename):
    try:
        # Create QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(link)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
        print(f"QR code saved as {filename}")
    except Exception as e:
        print(f"Error generating QR code: {e}")

# Main function to handle user input and QR code generation
def main():
    links = []  # List to store links
    while True:
        link = input("Enter a link to generate QR code (or 'exit' to quit): ")
        if link.lower() == 'exit':
            break
        elif link.startswith("http://") or link.startswith("https://"):
            links.append(link)
        else:
            print("Invalid link. Please enter a valid URL starting with http:// or https://")

    # Generate QR codes for all valid links
    for index, link in enumerate(links):
        filename = f"qr_code_{index + 1}.png"
        generate_qr_code(link, filename)

# Run the main function
if __name__ == "__main__":
    main()