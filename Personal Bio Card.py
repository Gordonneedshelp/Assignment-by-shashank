# Name: Param Jaiswal
# Branch: CSE Data Science Branch
# Student Details

"""
LOGIC:
1. Defines a set of variables to store personal information (Name, Age, Course, College, Email).
2. Uses formatted print statements ('f-strings') to inject these variables into a structural layout.
3. Employs special box-drawing characters (╔, ║, ╠, ╚) to create a professional-looking visual profile card.
"""

name = "Param Jaiswal"
age = 20  # Assuming a typical student age, or I can leave it or set it to something generic
course = "CSE Data Science Branch"
college = "CMR Institute of Technology"
email = "paramjaiswal@example.com"

print("╔════════════════════════════════════╗")
print("║         STUDENT PROFILE            ║")
print("╠════════════════════════════════════╣")
print(f"║ Name    : {name}")
print(f"║ Age     : {age}")
print(f"║ Course  : {course}")
print(f"║ College : {college}")
print(f"║ Email   : {email}")
print("╚════════════════════════════════════╝")