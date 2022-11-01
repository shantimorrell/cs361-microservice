# cs361-microservice


HOW TO REQUEST DATA

Request data by accessing the file "calculate_goals.txt" and writing to the file "run" followed by the user's maintenance calories and the user's goal calories. It should follow the format:

run</br>
user maintenance calories</br>
user goal calories</br>

and there should be no blank line before "run." An example call is:

run</br>
1000</br>
1200</br>

</br></br>

HOW TO RECEIVE DATA

The microservice will write the protein, fat, and carb goals to the file in the following format:

protein goal</br>
fat goal</br>
carbs goal</br>

with no blank line at the beginning of the file. An example of the returning state is:

60.0</br>
40.0</br>
150.0</br>

</br></br>

UML SEQUENCE DIAGRAM
![Microservice UML Sequence Diagram](https://user-images.githubusercontent.com/91344787/199148814-dd0bdf68-cc95-4005-9921-02f1dfcd60e2.jpeg)


