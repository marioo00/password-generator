import secrets 
import string

#Pool of characters used in the generated password
alphabet = string.ascii_letters + string.digits + string.punctuation

def generate_password(length = 16):
    # Generates a random password of a specified length, default is 16, minimum is 8.
    password = ""
    for _ in range(length):
        password += secrets.choice(alphabet)
    return password

def main():
    print("Secure Password Generator")
    try:
        length = int(input("Enter desired password legth: "))
    except ValueError:
        print("Invalid input. Using default length of 16.")
        length = 16

    #Makes sure password is minimum length 
    if length < 8:
        print("For security, minimum recommended length is 8. Using 8.")
        length = 8

    pwd = generate_password(length)
    print(f"\nGenerated Password: {pwd}")

if __name__ == "__main__":
    main()
