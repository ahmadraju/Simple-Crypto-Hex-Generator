import random

def generate_random_hex(start, end, count, output_file):
    """
    Generate random hexadecimal numbers within a given range and save them to a file.

    :param start: Starting hexadecimal range (inclusive)
    :param end: Ending hexadecimal range (inclusive)
    :param count: Number of hex numbers to generate
    :param output_file: File to save the generated hex numbers
    """
    with open(output_file, 'w') as file:
        for _ in range(count):
            random_hex = hex(random.randint(start, end))[2:].zfill(64)  # Remove '0x' and zero pad if needed
            file.write(random_hex + '\n')

if __name__ == "__main__":
    start_range = int("40000000000000000", 16)
    end_range = int("7ffffffffffffffff", 16)
    total_hex_numbers = 15000000  # Change this to the desired number of random hex values
    output_filename = "hex.txt"

    generate_random_hex(start_range, end_range, total_hex_numbers, output_filename)
    print(f"Random hex numbers saved to {output_filename}")

