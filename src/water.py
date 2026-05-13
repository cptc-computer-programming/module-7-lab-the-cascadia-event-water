# Lakewood Emergency Operations Center
# Department of Water

DISTRICT_COUNT = 2
SHELTER_COUNT = 3

MIN_GALLONS_DELIVERED = 1
MIN_PEOPLE = 1
MIN_GALLONS_REQUESTED = 0

DISTRICT_NAMES = [
    "Clover Park",
    "Steilacoom"
]

for i, district_name in enumerate(DISTRICT_NAMES): # enumerate() returns the [index, value] from the list
    print(f"*** District {i + 1} ({district_name}) ***") # format string for the index and name

    # Set the district totals as zero before checking the shelters
    total_gallons_district = 0
    total_people = 0
    district_gallons_requested = 0

    for shelter in range(SHELTER_COUNT): # Check over all shelters in the district
        print(f"-- Shelter {shelter + 1} Data --")

        gallons_delivered = float(input("Enter gallons delivered (>0): "))
        while gallons_delivered < MIN_GALLONS_DELIVERED: # While it's invalid try again
            gallons_delivered = float(input("Enter gallons delivered (>0): "))

        people_in_shelter = int(input("Enter people in shelter (>0): "))
        while people_in_shelter < MIN_PEOPLE:
            people_in_shelter = int(input("Enter people in shelter (>0): "))

        additional_gallons = float(input("Additional gallons requested (>=0): "))
        while additional_gallons < MIN_GALLONS_REQUESTED:
            additional_gallons = float(input("Additional gallons requested (>=0): "))

        print(f"Gallons per person: {(gallons_delivered / people_in_shelter):.1f}\n") # \n adds another line at the end

        # Add to the district totals
        total_gallons_district += gallons_delivered
        total_people += people_in_shelter
        district_gallons_requested += additional_gallons

    # Calculated District Totals
    district_gallons_per_person = total_gallons_district / total_people
    delivery_efficiency = total_gallons_district / (total_gallons_district + district_gallons_requested) * 100

    print("*** District Summary ***")
    print(f"Average per person: {district_gallons_per_person:.1f}")
    print(f"Total gallons delivered: {total_gallons_district:.1f}")
    print(f"Total gallons requested: {district_gallons_requested:.1f}")
    print(f"Delivery efficiency: {delivery_efficiency:.1f}\n")