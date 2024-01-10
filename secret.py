import random
import string
from colorama import init, Fore, Style
import os

# Initialize colorama
init(autoreset=True)

# Function to set text color
def set_color(color):
    print(f"{color}", end="")
    
def set_color(color):
    print(f"{color}", end="")

# Function to reset text color
def reset_color():
    os.system("COLOR 07")

# Function to print validation result
def print_validation_result(code, is_good):
    reset_color()
    if is_good:
        set_color(Fore.GREEN)  # Green text
        print(f"Validation result for code {code}: GOOD")
    else:
        set_color(Fore.RED)  # Red text
        print(f"Validation result for code {code}: NOT GOOD")
    reset_color()


    
def generate_random_code(format_choice):
    code = ""

    def generate_block(length):
        block = random.sample(string.ascii_uppercase, 1) + random.sample(string.digits, 1)
        block += random.sample(string.ascii_uppercase + string.digits, length - 2)
        random.shuffle(block)
        return ''.join(block)

    if format_choice == 1:
        code += ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
        code += '-'
        code += ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        code += '-'
        code += ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    elif format_choice == 2:
        code += ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
        code += '-'
        code += ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        code += '-'
        code += ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    elif format_choice == 3:
        code += ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
        code += '-'
        code += ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        code += '-'
        code += ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    else:
        print("Invalid format choice. Using default format: xxxx-xxxxx-xxxxx")
        code += ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
        code += '-'
        code += ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
        code += '-'
        code += ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))

    return code

def save_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content + '\n')

def is_good_code(code, format_choice):
    dissimilarities = [calculate_dissimilarity(code, existing_code) for existing_code in existing_codes]
    unique_percentage = sum(dissimilarity >= 0.95 * len(code) for dissimilarity in dissimilarities) / len(existing_codes) if len(existing_codes) > 0 else 0

    # Introduce a 10% chance of a code being "good" if unique percentage is 95% or above
    is_good = random.random() < 0.1 or unique_percentage >= 0.95

    if is_good and format_choice == 2:
        save_to_file('amazon_gift_card.txt', code)

    return is_good

def calculate_dissimilarity(code1, code2):
    return sum(c1 != c2 for c1, c2 in zip(code1, code2))

existing_codes = []

# Display introductory message in blue
# Display introductory message with warning
print(f"{Fore.BLUE}********************************************")
print(f"{Fore.BLUE}*                                          *")
print(f"{Fore.BLUE}*   THX FOR USING THIS PROGRAM. DON'T STEAL *")
print(f"{Fore.BLUE}*   WARNING: NOT ALL GOOD CODES WILL WORK   *")
print(f"{Fore.BLUE}*                                          *")
print(f"{Fore.BLUE}********************************************")

while True:
    # Get user input for the number of codes to generate
    num_codes_to_generate = int(input("Enter the number of codes to generate (enter '0' to exit): "))
    
    if num_codes_to_generate == 0:
        print("Exiting program. Goodbye!")
        break

    format_choice = int(input("Enter the format choice (1 for amazon vouchers xxxx-xxxxxx-xxxxxxxx, 2 for amazon gift card xxxx-xxxxxx-xxxxx, 3 for xxxxx-xxxxx-xxxxx-xxxxx-xxxxx): "))

    for i in range(num_codes_to_generate):
        random_code = generate_random_code(format_choice)
        save_to_file('generated_codes.txt', random_code)
        is_good = is_good_code(random_code, format_choice)
        print(f"Generated code: {random_code} - {'Good' if is_good else 'Not Good'}")
