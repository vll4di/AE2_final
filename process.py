import csv


def load_data(file_path):
    """Task 2: Loads the CSV data into a list of dictionaries."""
    data = []
    try:
        with open(file_path, mode='r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    return data


def get_unique_parks(data):
    """Extracts unique Disneyland branch names for the user guide."""
    return sorted(list({row['Branch'] for row in data if row['Branch']}))


def get_reviews_by_park(data, park_name):
    """Task 7: Returns all reviews for a specific park alias."""
    search_term = park_name.strip().lower()
    return [row for row in data if search_term in row['Branch'].lower()]


def count_reviews_by_location(data, park_name, location):
    """Task 8: Counts reviews from a specific country for a park."""
    search_park = park_name.strip().lower()
    search_loc = location.strip().lower()
    return len([row for row in data if search_park in row['Branch'].lower()
                and search_loc == row['Reviewer_Location'].lower()])


def get_average_score_by_year(data, park_name, year):
    """Task 8.2: Calculates average rating for a park in a specific year."""
    search_park = park_name.strip().lower()
    scores = []
    for row in data:
        if search_park in row['Branch'].lower() and row['Year_Month'].startswith(str(year)):
            try:
                scores.append(int(row['Rating']))
            except ValueError:
                continue
    return round(sum(scores) / len(scores), 2) if scores else 0


def get_average_score_by_location(data, park_name, location):
    """Task 8.3: Calculates average rating for a park by reviewer location."""
    search_park = park_name.strip().lower()
    search_loc = location.strip().lower()
    scores = [int(row['Rating']) for row in data if search_park in row['Branch'].lower()
              and search_loc == row['Reviewer_Location'].lower()]
    return round(sum(scores) / len(scores), 2) if scores else 0


def count_reviews_per_park(data):
    """Task 9: Counts reviews for each park for a Pie Chart."""
    counts = {}
    for row in data:
        park = row['Branch']
        counts[park] = counts.get(park, 0) + 1
    return list(counts.keys()), list(counts.values())


def get_location_averages(data, park_name):
    """Task 11: Gets average scores by location for a Bar Chart."""
    search_park = park_name.strip().lower()
    loc_data = {}
    for row in data:
        if search_park in row['Branch'].lower():
            loc = row['Reviewer_Location']
            rating = int(row['Rating'])
            if loc not in loc_data:
                loc_data[loc] = []
            loc_data[loc].append(rating)

    labels = list(loc_data.keys())[:10]  # Limit to top 10 for readability
    values = [round(sum(loc_data[l]) / len(loc_data[l]), 2) for l in labels]
    return labels, values


def get_monthly_averages(data, park_name):
    """Task 12: Gets average scores per month for a Line Chart."""
    search_park = park_name.strip().lower()
    month_data = {}
    for row in data:
        if search_park in row['Branch'].lower() and row['Year_Month'] != 'missing':
            month = row['Year_Month']
            rating = int(row['Rating'])
            if month not in month_data:
                month_data[month] = []
            month_data[month].append(rating)

    sorted_months = sorted(month_data.keys())
    averages = [round(sum(month_data[m]) / len(month_data[m]), 2) for m in sorted_months]
    return sorted_months, averages