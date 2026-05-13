## 💧 Department of Water

### Situation

Lakewood’s municipal water system is severely compromised. Broken water mains and contamination from ruptured pipes have left much of the city without reliable tap water. Emergency tankers are distributing potable water to major shelters.

### Mission

Write a Python program to collect and analyze emergency water distribution data for each district and each shelter.

### Data Collected

For each shelter, collect:

- Gallons of water delivered
- Number of people in the shelter
- Number of additional gallons requested

### Requirements

Your program must:

- Use an outer loop to process two districts.
- Use an inner loop to process three shelters per district.
- Validate all input values.

### Input Limits

| Input | Valid Values |
|---|---|
| Gallons delivered | Greater than 0 |
| People in shelter | Greater than 0 |
| Additional gallons requested | 0 or greater |

### Calculations

Gallons per person for each shelter:
```
    gallons_per_person = gallons_delivered / people
```
District gallons per person:
```
    district_gallons_per_person = total_gallons_delivered / total_people
```
Delivery efficiency:
```
    
```delivery_efficiency = total_gallons_delivered / (total_gallons_delivered + total_gallons_requested) * 100
### Outputs

Your program must display:

- Gallons per person for each shelter
- District gallons per person
- Total gallons delivered for each district
- Total gallons requested for each district
- Delivery efficiency for each district

### Metric Reported to City Manager

At the end of the program, your team must report:

| District | Metric |
|---|---|
| Clover Park | District gallons per person |
| Steilacoom | District gallons per person |

### Sample Output
```
*** District 1 (Clover Park) ***

-- Shelter 1 Data --
Enter gallons delivered: 1500
Enter number of people: 100
Enter additional gallons requested: 300
Gallons per person: 15.0

-- Shelter 2 Data --
Enter gallons delivered: 2000
Enter number of people: 150
Enter additional gallons requested: 400
Gallons per person: 13.3

-- Shelter 3 Data --
Enter gallons delivered: 1200
Enter number of people: 80
Enter additional gallons requested: 200
Gallons per person: 15.0

*** District Summary ***
-------------------
Average gallons per person: 14.43
Total gallons delivered: 4700
Total gallons requested: 900
Delivery efficiency: 83.91%


*** District 2 (Steilacoom) ***

-- Shelter 1 Data --
Enter gallons delivered: 1300
Enter number of people: 80
Enter additional gallons requested: 300
Gallons per person: 16.3

-- Shelter 2 Data --
Enter gallons delivered: 2000
Enter number of people: 150
Enter additional gallons requested: 500
Gallons per person: 13.3

-- Shelter 3 Data --
Enter gallons delivered: 1500
Enter number of people: 100
Enter additional gallons requested: 300
Gallons per person: 15.0

*** District Summary ***
-------------------
Average gallons per person: 14.87
Total gallons delivered: 4800
Total gallons requested: 1100
Delivery efficiency: 81.36%


Data collection complete for all districts.
```