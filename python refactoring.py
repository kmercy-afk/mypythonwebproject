import sys

# Dictionary to store the refactoring logs
refactoring_logs = []

def get_valid_process():
    """Get a valid process selection from 1 to 3."""
    while True:
        try:
            selection = int(input("Please select the process you wish to perform (1-3): "))
            if 1 <= selection <= 3:
                return selection
            else:
                print("Please enter 1 to 3")
        except ValueError:
            print("Please enter 1 to 3")

def get_valid_rating():
    """Get a valid rating from 1 to 5."""
    while True:
        try:
            rating = int(input("Please enter a rating on a scale of 1 to 5: "))
            if 1 <= rating <= 5:
                return rating
            else:
                print("Please enter a value between 1 and 5")
        except ValueError:
            print("Please enter a value between 1 and 5")

def enter_evaluation():
    """Enter evaluation points and comments for the current entry."""
    try:
        points = float(input("Enter evaluation points: "))
    except ValueError:
        print("Invalid points. Using default 0.")
        points = 0.0
    comments = input("Enter your comments: ")
    return points, comments

def view_results():
    """Display the results so far."""
    if not refactoring_logs:
        print("No results yet.")
        return
    
    print("\n--- Refactoring Results So Far ---")
    for i, log in enumerate(refactoring_logs, 1):
        print(f"{i}. Process: {log['process']}")
        print(f"   Rating: {log['rating']}")
        print(f"   Points: {log['points']}")
        print(f"   Comments: {log['comments']}")
        if log['method_name']:
            print(f"   Suggested Method Name: {log['method_name']}")
        print()

def suggest_method_name(process_desc):
    """Suggest a relevant method name based on process description."""
    words = process_desc.lower().split()
    if any(word in words for word in ['calculate', 'compute']):
        return 'calculate_' + '_'.join(words[:2])
    elif any(word in words for word in ['split', 'extract']):
        return 'extract_' + '_'.join(words[1:3])
    else:
        return 'process_' + '_'.join(words[:2])

def main():
    print("Python Refactoring Helper")
    print("This tool guides you through refactoring steps, focusing on splitting processes into new methods.")
    
    while True:
        print("\nOptions:")
        print("1: Enter evaluation points and comments")
        print("2: Check the results so far.")
        print("3: Terminate")
        
        try:
            choice = int(input("Choose an option (1-3): "))
            if choice == 1:
                # Select process first
                process = get_valid_process()
                process_names = {
                    1: "Extract Method (A new method must be defined and the process must be split.)",
                    2: "Rename Variable",
                    3: "Inline Method"
                }
                print(f"Selected: {process_names[process]}")
                
                # For process 1, handle method naming
                method_name = None
                if process == 1:
                    process_desc = input("Describe the process to split: ")
                    print("Remember: A new method must be defined and the process must be split into it.")
                    suggested_name = suggest_method_name(process_desc)
                    print(f"Suggested relevant method name: {suggested_name}")
                    confirm = input("Use this name? (y/n): ").lower().strip()
                    method_name = suggested_name if confirm == 'y' else input("Enter method name: ").strip()
                
                # Enter rating
                rating = get_valid_rating()
                
                # Enter evaluation
                points, comments = enter_evaluation()
                
                # Store the log
                log = {
                    'process': process_names[process],
                    'rating': rating,
                    'points': points,
                    'comments': comments,
                    'method_name': method_name
                }
                refactoring_logs.append(log)
                print("Entry saved!")
                
            elif choice == 2:
                view_results()
                
            elif choice == 3:
                print("Terminating the process.")
                sys.exit(0)
                
            else:
                print("Please enter 1 to 3")
                
        except ValueError:
            print("Please enter 1 to 3")
        except KeyboardInterrupt:
            print("\nTerminating the process.")
            sys.exit(0)

if __name__ == "__main__":
    main()