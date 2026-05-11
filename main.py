import process
import tui
import visual


def handle_view_data(choice, data):
    """Coordinates Section B viewing tasks."""
    if choice == 'A':
        park = tui.get_park_input()
        results = process.get_reviews_by_park(data, park)
        tui.display_reviews(results)
    elif choice == 'B':
        park = tui.get_park_input()
        location = input("Enter Reviewer Location: ").strip()
        count = process.count_reviews_by_location(data, park, location)
        print(f"\nResult: There are {count} reviews for {park} from {location}.")
    elif choice == 'C':
        park = tui.get_park_input()
        year = input("Enter Year (e.g., 2019): ").strip()
        avg = process.get_average_score_by_year(data, park, year)
        print(f"\nResult: The average score for {park} in {year} was: {avg}")
    elif choice == 'D':
        park = tui.get_park_input()
        location = input("Enter Reviewer Location: ").strip()
        avg = process.get_average_score_by_location(data, park, location)
        print(f"\nResult: The average score for {park} from {location} was: {avg}")


def handle_visuals(choice, data):
    """Section C visualisation tasks."""
    if choice == 'A':
        park = tui.get_park_input()
        labels, values = process.get_location_averages(data, park)
        if labels:
            visual.display_bar_chart(park, labels, values)
    elif choice == 'B':
        labels, values = process.count_reviews_per_park(data)
        visual.display_pie_chart(labels, values)
    elif choice == 'C':
        park = tui.get_park_input()
        labels, values = process.get_monthly_averages(data, park)
        if labels:
            visual.display_monthly_avg_chart(park, labels, values)


def run():
    """Main program loop."""
    tui.display_header()
    data = process.load_data("Disneyland_reviews.csv")

    # Show valid park names to help with the parks aliases
    parks = process.get_unique_parks(data)
    tui.display_available_parks(parks)

    while True:
        selection = tui.main_menu()

        # ALL lines below must be indented to be part of the while loop
        if selection == 'A':
            sub_choice = tui.sub_menu_view()
            handle_view_data(sub_choice, data)
        elif selection == 'B':
            sub_choice = tui.sub_menu_visual()
            handle_visuals(sub_choice, data)
        elif selection == 'C':
            # Task 13: Export Summary
            with open("summary.txt", "w") as f:
                f.write("Disneyland Data Summary\n" + "=" * 25 + "\n")
                for p in parks:

                    avg = process.get_average_score_by_year(data, p, "")
                    f.write(f"{p}: Overall Average = {avg}\n")
            print("Summary exported to summary.txt!")
        elif selection == 'X':
            print("Exiting. Goodbye!")
            break

if __name__ == "__main__":
    run()