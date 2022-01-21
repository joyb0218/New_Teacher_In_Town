from roster import student_roster
from itertools import combinations, chain

class ClassroomOrganizer:
  def __init__(self):
    self.sorted_names = self._sort_alphabetically(student_roster)

# 3a. Define the iterator protocol for our ClassroomOrganizer class.
  def __iter__(self):
    self.index = 0
    return self

  def __next__(self):
    each_student = self.sorted_names[self.index]
    self.index += 1
    if self.index >= 10:
      raise StopIteration
    return each_student

  def _sort_alphabetically(self, students):
    names = []
    for student_info in students:
      name = student_info['name']
      names.append(name)
    return sorted(names)

  def get_students_with_subject(self, subject):
    selected_students = []
    for student in student_roster:
      if student['favorite_subject'] == subject:
        selected_students.append((student['name'], subject))
    return selected_students

# 4. Using the itertools module, define a method within ClassroomOrganizer that will retrieve a
# final list of all tuple combinations of 2 students that can be seated at each table.
  def table_seating(self):
    names = []
    for student_info in student_roster:
      name = student_info['name']
      names.append(name)
      table_list = list(combinations(names, 2))
    return table_list

# 5. Retrieve a list of all 4 combinations of students whose favorite subjects are Math and Science.
# print the final list of combinations
  def two_subjects_tables(self):
    math = []
    science = []
    for student_info in student_roster:
      fav_subject = student_info['favorite_subject']
      if fav_subject == 'Math':
        math.append(student_info['name'])
      if fav_subject == 'Science':
        science.append(student_info['name'])
      two_subjects_list = list(chain(math, science))
      two_subjects_combos = list(combinations(two_subjects_list, 4))
    return two_subjects_combos

#3b. Create a way to run through morning roll call, by ordering all students by first name alphabetically
# student_roll = ClassroomOrganizer()
# student_roll_iter = iter(student_roll)
# # for student in student_roll_iter:
# #   print(student)

# tables = ClassroomOrganizer()
# student_tables = tables.table_seating()
# #print(student_tables)

#Test
two_subjects = ClassroomOrganizer()
two_subjects_combo = two_subjects.two_subjects_tables()
#print(two_subjects_combo)







