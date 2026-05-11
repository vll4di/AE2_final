import matplotlib.pyplot as plt

def display_pie_chart(labels, values):
    """Task 9: Displays a pie chart showing the distribution of reviews per park."""
    plt.figure(figsize=(10, 7))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Total Number of Reviews per Disneyland Park")
    plt.axis('equal')  # Ensures the pie chart is a circle
    plt.show()

def display_bar_chart(park_name, labels, values):
    """Task 11: Displays a bar chart showing average scores by reviewer location."""
    plt.figure(figsize=(12, 6))
    plt.bar(labels, values, color='skyblue')
    plt.xlabel('Reviewer Location')
    plt.ylabel('Average Rating (1-5)')
    plt.title(f'Top 10 Average Reviewer Scores for {park_name}')
    plt.xticks(rotation=45, ha='right')
    plt.ylim(0, 5) # Ratings are between 1 and 5
    plt.tight_layout()
    plt.show()

def display_monthly_avg_chart(park_name, months, averages):
    """Task 12: Displays a line chart showing monthly average score trends."""
    plt.figure(figsize=(12, 6))
    plt.plot(months, averages, marker='o', linestyle='-', color='orange')
    plt.xlabel('Month (Year_Month)')
    plt.ylabel('Average Rating')
    plt.title(f'Monthly Average Rating Trend: {park_name}')
    plt.xticks(rotation=90)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()