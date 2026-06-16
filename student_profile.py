Full_Name = input("Enter full name")
Age = int(input("Enter your age"))
GPA = float(input("Enter your gpa"))
Courses = input("Enter your courses").split(",")

student_profile = {
    "name": Full_Name,
    "age": Age,
    "gpa": GPA,
    "courses": Courses,
    "num_courses": num_courses
}
on_Dean_list = GPA >= 3.5 # True or False
is_adult = Age >= 18  # True or False

print(f"Name:{student_profile["name"]}")
print(f"Age:{student_profile["age"]} ({'Adult' if is_adult else 'Minor'})")
print(f"GPA:{student_profile["gpa"]}")
print(f"courses:{student_profile["courses"]}")
print(f"# nun_courses:{student_profile["num_courses"]}")
print(f"Dean list:{'Yes' if on_Dean_list else 'No'}")
print(f"Age: converted type = {type(age)}")
print(f"GPA: converted type = {type(GPA)}")







            
                