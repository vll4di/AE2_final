def display_header():
    """Task 3: Displays a clear, stylized header for the application."""
    print("-" * 40)
    print("      DISNEYLAND REVIEW ANALYSER")
    print("-" * 40)

def main_menu():
    """Task 4: Displays the main menu and returns the user's choice."""
    print("\nMain Menu:")
    print("[A] View Data")
    print("[B] Visualise Data")
    print("[C] Export Summary")
    print("[X] Exit")
    return input("Selection: ").strip().upper()

def sub_menu_view():
    """Task 5: Displays sub-menu for data viewing options."""
    print("\nView Data Options:")
    print("[A] View Reviews by Park")
    print("[B] Number of Reviews by Park and Location")
    print("[C] Average Score per Year by Park")
    print("[D] Average Score per Park by Reviewer Location")
    return input("Selection: ").strip().upper()

def sub_menu_visual():
    """Task 6: Displays sub-menu for visualisation options."""
    print("\nVisualisation Options:")
    print("[A] Average Score by Location (Bar Chart)")
    print("[B] Total Reviews per Park (Pie Chart)")
    print("[C] Monthly Average Scores (Line Chart)")
    return input("Selection: ").strip().upper()

def get_park_input():
    """Helper: Gets the park name/alias from the user."""
    return input("Enter Park Name (e.g., Paris, California, Hong Kong): ").strip()

def display_available_parks(parks):
    """Visual aid to show the user valid park names."""
    print("\nAvailable Disneyland Parks to search:")
    for park in parks:
        print(f" - {park}")
    print("-" * 40)

def display_reviews(reviews):
    """Task 7: Prints the results of a review search."""
    if not reviews:
        print("\nNo reviews found.")
    else:
        print(f"\nFound {len(reviews)} reviews:")
        for r in reviews[:10]:  # Limit display to 10 for readability
            print(f"- {r['Review_ID']}: {r['Rating']} Stars ({r['Reviewer_Location']})")
        if len(reviews) > 10:
            print(f"... and {len(reviews) - 10} more.")

def confirm_choice(choice):
    """Simple feedback for the user after a menu selection."""
    print(f"\nSelection '{choice}' confirmed.")