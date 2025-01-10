# Simple-Crypto-Hex-Generator
This python script is to generate hex in certain range, (example: puzzle 67 of BTC challenges) 
Just change the part:

if __name__ == "__main__":
    start_range = int("40000000000000000", 16)
    end_range = int("7ffffffffffffffff", 16)
    total_hex_numbers = 15000000  # Change this to the desired number of random hex values
    output_filename = "hex.txt"

With you own range. the results file will be save in hex.txt
