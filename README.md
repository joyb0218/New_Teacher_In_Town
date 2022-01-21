# New_Teacher_In_Town
Codecademy's intermediate project utilizing iterables and iterators using custom, combinations, and chains.

In roster.py., you have been provided a roster of students for the 10 children in your class. Each child’s record contains name, age, height (in inches), favorite classroom subject, and favorite animal to help you get to know them better.

There are 6 tasks to complete:

1. Navigate to script.py and import the student_roster list from roster.py. Create an iterator for the student_roster list and print out each student’s information using next().
2. You’ve been provided a file called classroom_organizer.py. Start defining out your custom ClassroomOrganizer class by importing the student_roster list from the roster.py file so that we can utilize it within our custom class. 
3. Create a simple way to run through morning roll call, by ordering all students by first name alphabetically. It should return each student’s name one at a time on each next() call or for loop iteration. Define the iterator protocol for our ClassroomOrganizer class and then use either next() calls or a for loop on the ClassroomOrganizer object to print out the next student on the roll call.
4. Using the itertools module, define a method within ClassroomOrganizer that will retrieve a final list of all tuple combinations of 2 students that can be seated at 5 tables. Then, from script.py, print out the result to see all the possible combinations.
5. Retrieve a list of all 4 combinations of students whose favorite subjects are Math and Science. The get_students_with_subject() method can be used to retrieve iterables for each of the subjects, then print from script.py.
6. OPTIONAL: You can use the remaining dictionary info within the student roster list (favorite animal, height, age) to practice more with itertools or custom iterators.
