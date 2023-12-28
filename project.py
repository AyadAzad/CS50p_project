import string
from fpdf import FPDF
import random
import re


class PasswordGenerator:
    def __init__(self):
        pass

    def add_name(self):
        name = input("Enter your name :")
        return name.capitalize()

    def add_platform(self):
        platform = input("Enter your platform :")
        return platform.capitalize()

    def generate_random_password(self, length=12):
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:'<>,.?/"
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def generate_custom_password(self, text):
        # Remove non-alphanumeric characters
        clean_text = re.sub(r'[^a-zA-Z0-9]', '', text)

        while len(clean_text) < 8:
            clean_text += clean_text

        random_chars = ''.join(
            random.choices(string.ascii_letters + string.digits + string.punctuation, k=len(clean_text)))

        password = ''.join(random.sample(clean_text + random_chars, len(clean_text + random_chars)))
        return password

    def rate_password_strength(self, password):
        # criteria
        has_lowercase = any(char.islower() for char in password)
        has_uppercase = any(char.isupper() for char in password)
        has_numbers = any(char.isdigit() for char in password)
        has_symbols = any(char in string.punctuation for char in password)
        length = len(password)

        # Calculate strength based on criteria
        strength = sum([has_lowercase, has_uppercase, has_numbers, has_symbols, min(length // 4, 3)])

        # Rate password strength from 1 to 10 based on the criteria
        return min(strength, 10)

    def generate_password_card(self, name, password, platform, filename='password_card.pdf'):
        pdf = FPDF("P", "mm", "A4")  # Specify page format and units
        pdf.add_page()

        pdf.image(r"C:\Users\Anton\PycharmProjects\CS50p_project\background.png", x=0, y=0, w=pdf.w, h=pdf.h)
        pdf.image(r"C:\Users\Anton\PycharmProjects\CS50p_project\blue_key.jpg", x=12, y=172, w=12, h=12)

        if platform.lower() == 'facebook':
            pdf.image(r"C:\Users\Anton\PycharmProjects\CS50p_project\facebook_logo.png", x=12, y=172 + 17, w=12, h=12)
        elif platform.lower() == 'linkedin':
            pdf.image(r"C:\Users\Anton\PycharmProjects\CS50p_project\linkedin_logo.png", x=12, y=172 + 17, w=12, h=12)
        elif platform.lower() == 'instagram':
            pdf.image(r"C:\Users\Anton\PycharmProjects\CS50p_project\instagram_logo.jpg", x=12, y=172 + 17, w=12, h=12)

        pdf.set_font("Arial", size=28)

        pdf.set_text_color(219, 35, 51)
        pdf.text(10, 120, f"{name}")
        pdf.set_font("Arial", size=16)
        pdf.set_text_color(0, 0, 0)
        pdf.text(26, 180, f"{password}")
        pdf.text(26, 197, f"{platform}")
        pdf.output(filename)


def main():
    try:
        generator = PasswordGenerator()
        while True:
            user_input = input("choose an option \n"
                               "1- Generate random password \n"
                               "2- Generate custom password \n"
                               "3- Check password strength \n"
                               "\n"
                               "Options :")
            try:
                user_input = int(user_input)
                if user_input not in [1, 2, 3]:
                    print(f"please enter a value between 1 to 3")
                    continue
            except ValueError:
                print("Enter an Integer.")
                continue

            if user_input == 1:
                random_password = generator.generate_random_password()
                name = generator.add_name()
                platform = generator.add_platform()
                generator.generate_password_card(name, random_password, platform, 'random_password_card.pdf')
                print("Random password generated successfully !")
                break
            elif user_input == 2:
                user_input = input("Enter text for custom password: ")
                name = generator.add_name()
                platform = generator.add_platform()
                custom_password = generator.generate_custom_password(user_input)
                generator.generate_password_card(name, custom_password, platform, 'custom_password_card.pdf')
                print("Custom password generated successfully !")
                break
            elif user_input == 3:
                user_password = input("Enter password to check its strength: ")
                strength = generator.rate_password_strength(user_password)
                print(f"Password Strength: {strength}/10")
                break
    except Exception as e:
        print(f"error occurred {e}")


if __name__ == "__main__":
    main()
