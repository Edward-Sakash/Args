import getopt
import sys

def main():
    try:
        # Define the valid short and long options
        short_options = "hn:"
        long_options = ["help", "name="]

        # Get the command line arguments and options using getopt
        opts, args = getopt.getopt(sys.argv[1:], short_options, long_options)
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)
    
    name = None  # Initialize the name variable

    # Process the parsed options and arguments
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("Usage: app2.py [-n NAME] [--name=NAME]")
            print("Options:")
            print("  -h, --help           Show this help message")
            print("  -n NAME, --name=NAME Set the name")
            sys.exit()
        elif opt in ("-n", "--name"):
            name = arg
    
    if name:
        print(f"Good Morning {name}!")
    else:
        print("Good Morning folks!")

if __name__ == "__main__":
    main()
