import sys #

def main():
    # Check if "--help" option is present in the command line arguments
    if "--help" in sys.argv:
        # Print usage and options help text
        print("Usage: app1.py [--fast]")
        print("Options:")
        print("  --fast     Enable fast mode")
        print("  --help     Show this help message")
    # Check if "--fast" option is present in the command line arguments
    elif "--fast" in sys.argv:
        # Print message indicating fast mode is enabled
        print("fast mode enabled")
    else:
        # Print message indicating slow mode is enabled
        print("slow mode enabled")

if __name__ == "__main__":
    # Call the main function when the script is executed
    main()

#