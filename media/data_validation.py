data_valid = False;

#treatment grade1
while (data_valid == False):
    grade1 = input("Insert your first grade: ");

    try:
        grade1 = float(grade1);
        validation = True;
    except:
        print("Insert numbers");
        continue;

    if (grade1 < 0 or grade1 > 10):
        print("Digit a number between 0 and 10");
        continue;
    else:
        data_valid = True;

data_valid = False;

#----------------
#treatment grade2
while (data_valid == False):
    grade2 = input("Insert your second grade: ");

    try:
        grade2 = float(grade2);
        validation = True;
    except:
        print("Insert numbers");
        continue;

    if (grade2 < 0 or grade2 > 10):
        print("Digit a number between 0 and 10");
        continue;
    else:
        data_valid = True;

data_valid = False;

#----------------
#treatment total_classes
while (data_valid == False):
    total_classes = input("Type the total classes: ");

    try:
        total_classes = int(total_classes);
        validation = True;
    except:
        print("Insert numbers");
        continue;

    if (total_classes <= 0):
        print("The number of classes can't be 0 or less");
        continue;
    else:
        data_valid = True;

data_valid = False;

#----------------
#treatment absences
while (data_valid == False):
    absences = input("Insert the number of your absences: ");

    try:
        absences = int(absences);
    except:
        print("Insert numbers");
        continue;

    if (absences < 0 or absences > total_classes):
        print("The number of absences can't be 0 or higher than total classes");
        continue;
    else:
        data_valid = True;


ava_grade = (grade1 + grade2) / 2;
attendance = (total_classes - absences) / total_classes;

print("Average grade: ", round(ava_grade, 2));
print("Attendance rate: ", str(round((attendance * 100), 2)) + "%");

if (ava_grade >= 6 and attendance >= 0.8):
    print("The student has been approved");
elif (ava_grade < 6 and attendance < 0.8):
    print("The student has failed in his grade and attendance");
elif (attendance >= 0.8):
    print("The student grade is lower, but his passed on attendance");
else:
    print("The student grade is great, but he failed in his attendance");
