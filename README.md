# cs361-microservice


HOW TO REQUEST DATA

Request data by accessing the file "calculate_goals.txt" and writing to the file "run" followed by the user's maintenance calories and the user's goal calories. It should follow the format:

run
user maintenance calories
user goal calories

and there should be no blank line before "run." An example call is:

run
1000
1200



HOW TO RECEIVE DATA

The microservice will write the protein, fat, and carb goals to the file in the following format:

protein goal
fat goal
carbs goal

with no blank line at the beginning of the file. An example of the returning state is:

60.0
40.0
150.0



UML SEQUENCE DIAGRAM
![Microservice UML Sequence Diagram](https://user-images.githubusercontent.com/91344787/199148814-dd0bdf68-cc95-4005-9921-02f1dfcd60e2.jpeg)


