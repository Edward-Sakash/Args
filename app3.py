import argparse

def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="Greet the user and calculate age")

    # Add positional arguments
    parser.add_argument("first_name", nargs="?", default="Larry", help="First name")
    parser.add_argument("last_name", nargs="?", default="Hanson", help="Last name")
    parser.add_argument("age", nargs="?", type=int, default=100, help="Age")

    # Add optional argument
    parser.add_argument("--fast", action="store_true", help="Enable fast mode")

    # Parse the command line arguments
    args = parser.parse_args()

    # Print "fast mode enabled" if --fast option is used
    if args.fast:
        print("fast mode enabled")

    # Calculate age + 1
    age_next_year = args.age + 1

    # Output the greeting with provided or default values
    print(f"Hello {args.first_name} {args.last_name}! I see that you have had {age_next_year} birthdays.")

if __name__ == "__main__":
    main()
