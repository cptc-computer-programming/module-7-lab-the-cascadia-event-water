# Lakewood Emergency Operations Center
# Department of Water

DISTRICT_COUNT = 2
SHELTER_COUNT = 3

MIN_GALLONS_DELIVERED = 0
MIN_PEOPLE = 1
MIN_GALLONS_REQUESTED = 0

DISTRICT_NAME = [
    "Clover Park",
    "Steilacoom"
]

# TODO: Process water distribution data for both districts.
for district in range(DISTRICT_COUNT):
    print(f"*** District {district + 1} ({DISTRICT_NAME[district]}) ***")
    for shelter in range(SHELTER_COUNT):
        print(f"-- Shelter {shelter + 1} Data --")

# TODO: For each district, process all shelters.

# TODO: Validate all user input.

# TODO: Calculate and display shelter-level and district-level results.

# TODO: Print a final completion message.