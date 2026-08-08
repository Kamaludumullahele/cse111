import os


def main():
    # Read the contents of the provinces.txt file
    # into a list of provinces named 'provinces_list'
    file_path = os.path.join(os.path.dirname(__file__), "provinces.txt")
    provinces_list = read_provinces_file(file_path)

    # print the list of provinces to the console
    print("List of provinces:", provinces_list)
    print()
    print("The number of provinces in the list is:", len(provinces_list))
    print()
    provinces_list.pop(0)  # remove the first element of the list (the header line)
    print("List of provinces without the header line:", provinces_list)
    provinces_list.pop()  # remove the last element of the list (the footer line)
    print() 
    print("list without the first and last elements:", provinces_list)

    # replacing AB with Alberta in the list of provinces
    for i in range(len(provinces_list)):
        if provinces_list[i] == "AB":
            provinces_list[i] = "Alberta"
            # print("The list of provinces
            # after replacing AB with Alberta:", provinces_list
    count = provinces_list.count("Alberta")
    print()
    print("The number of times Alberta appears in the list is:", count)

def read_provinces_file(filename):
    # read the contents of the provinces.txt file into
    # a list of provinces and return the list
    provinces_list = []

    # Open the file for reading
    with open(filename, "rt") as provinces_file:
        next(provinces_file)  # Skip the header line

        # Read each line from the file
        for line in provinces_file:
            # strip the whitespace from the beginning and end
            # of the line and append to the end of the provinces_list
            provinces_list.append(line.strip())
    return provinces_list


    
if __name__ == "__main__":
    main()