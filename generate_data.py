import csv
import random
from faker import Faker

fake = Faker()

num_rows = 20000000

genders = ["Male", "Female", "Non-Binary", ""]
device_types = ["Desktop", "Mobile", "Tablet", ""]
ad_positions = ["Top", "Bottom", "Side", ""]
browsing_categories = ["Shopping", "Education", "Entertainment", "Social Media", "News", ""]
times_of_day = ["Morning", "Afternoon", "Evening", "Night", ""]

output_file = "advertisement.csv"

# Write CSV
with open(output_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    
    # Write header (added ip_address column)
    writer.writerow([
        "id", "full_name", "age", "gender", "device_type", 
        "ad_position", "browsing_history", "time_of_day", 
        "click", "ip_address"
    ])
    
    for i in range(1, num_rows + 1):
        row = [
            i,
            f"User{i}",
            random.choice([random.randint(18, 65), ""]),  # some rows missing age
            random.choice(genders),
            random.choice(device_types),
            random.choice(ad_positions),
            random.choice(browsing_categories),
            random.choice(times_of_day),
            random.choice([0, 1]),  # click or not
            fake.ipv4()  # generate random IP address
        ]
        writer.writerow(row)

print(f"Random dataset generated with {num_rows} rows -> {output_file}")
