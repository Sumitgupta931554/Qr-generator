import qrcode
from PIL import Image

def generate_qr_code(data, size, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    img.save(f"{file_name}.png")
    print(f"QR Code saved as {file_name}.png")

def main_menu():
    while True:
        print("\nQR Code Generator Menu")
        print("1. Generate a QR Code")
        print("2. Exit")
        choice = input("Choose an option (1 or 2): ")

        if choice == '1':
            data = input("Enter the text or URL to generate the QR code: ")
            while True:
                try:
                    size = int(input("Enter the size of the QR code (e.g., 10): "))
                    break
                except ValueError:
                    print("Please enter a valid integer for the size.")

            file_name = input("Enter the file name to save the QR code (without extension): ")
            generate_qr_code(data, size, file_name)

        elif choice == '2':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    main_menu()
