import csv
import os
print(os.getcwd())

def main():
    
    #index of the students' id number index of the csv file
    INUMBER_INDEX = 0
    # Using the id number as the key read the contents of the
    # csv file into a compound dictionary called students_dict
    file_path = os.path.join(os.path.dirname(__file__), "students.csv")
    students_dict = read_dictionary(file_path, INUMBER_INDEX)
    print(students_dict)
    print()
    INUMBER = input("Enter a student's I-Number: ")
    INUMBER = INUMBER.replace("-", "")
    if not INUMBER.isdigit():
        print("This is not a valid I-Number")

    elif len(INUMBER) != 9:
         print("The I-Number should be a 9 digit number")
         
    else:
        if INUMBER in students_dict:
                        name = students_dict[INUMBER][1]
                        print(f"Student {INUMBER} is {name}.")
        else:
            print("No such student")
        

def read_dictionary(filename, key_column_index):
    # Open the csv file to read and store the reference
    # to the file name csv_file.
    dictionary = {}
    with open (filename, "rt") as csv_file:
        #use the csv module to create reader module
        #that can read the opened csv file
        reader = csv.reader(csv_file)
        # Skip the first line, header
        next(reader)
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list
    return dictionary

if __name__ == "__main__":
  main()
