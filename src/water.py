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

# TODO: Process water distribution data for both districts.
total_gallons_delivered = 0
for i, district_name in enumerate(DISTRICT_NAMES): # enumerate() returns the [index, value] from the list
    print(f"*** District {i + 1} ({district_name}) ***") # format string for the index and name
    total_gallons_district = 0
    total_people = 0
    for shelter in range(SHELTER_COUNT):
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

        total_gallons_district += gallons_delivered

        total_people += people_in_shelter
    
    district_gallons_per_person = total_gallons_district / total_people
   
    print("*** District Summary ***")
    print("Average per person: " + str(district_gallons_per_person))
    print("Total gallons delivered:" + str(total_gallons_district ))

 
# TODO: For each district, process all shelters.

# TODO: Validate all user input.

# TODO: Calculate and display shelter-level and district-level results.

# TODO: Print a final completion message.