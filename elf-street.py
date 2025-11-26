import csv
import random
from datetime import datetime, timedelta

# Configuration
start_time = datetime(2025, 12, 1, 0, 0, 0)  # Midnight Nov 1, 2025
end_time = start_time + timedelta(hours=24)    # 6 hours later
locations = ['Santa`s Workshop']

# Generate CSV
with open('elf-street-1csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)

    # Write header
    writer.writerow(['timestamp', 'location', 'Temperature', 'light'])

    current_time = start_time

    while current_time < end_time:

        selected_locations = random.sample(locations, 1)

        for location in selected_locations:
            # Generate random whole-number temperature between 0 and 4 (inclusive)
            temperature = random.randint(0, 2)
#             light = round(random.random() * 10)
            light= 0

            # Write record
            writer.writerow([
                f"{current_time.timestamp():.3f}",
                location,
                temperature,
                light
            ])

        # Increment time by 1 second
        current_time += timedelta(seconds=1800)

total_seconds = (end_time - start_time).total_seconds()
print(f"CSV file generated for {total_seconds} seconds with multiple locations per second")