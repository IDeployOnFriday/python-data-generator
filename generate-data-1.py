import csv
import random
from datetime import datetime, timedelta

# Configuration
start_time = datetime(2025, 11, 1, 0, 0, 0)  # Midnight Nov 1, 2025
end_time = start_time + timedelta(days=2)    # x days later
locations = ['light A', 'light B', 'light C', 'light D', 'light E']

# Generate CSV
with open('light_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)

    # Write header
    writer.writerow(['timestamp', 'location', 'red_score', 'green_score', 'blue_score'])

    current_time = start_time

    while current_time < end_time:
        num_locations_this_second = random.randint(2, 5)
        selected_locations = random.sample(locations, num_locations_this_second)

        for location in selected_locations:
            # Generate random scores between 0.000 and 1.000
            red_score = round(random.random() * 10, 2)
            green_score = round(random.random() * 10, 2)
            blue_score = round(random.random() * 10, 2)

            # Write record
            writer.writerow([
                f"{current_time.timestamp():.3f}",
                location,
                red_score,
                green_score,
                blue_score
            ])

        # Increment time by 1 second
        current_time += timedelta(seconds=30)

total_seconds = (end_time - start_time).total_seconds()
print(f"CSV file generated for {total_seconds} seconds with multiple locations per second")