

def main():
    # Read the contents of the provinces.txt file
    # into a list of provinces named 'provinces_list'
    provinces_list = read_provinces_file("provinces.txt")

    # print the list of provinces to the console
    print("List of provinces:", provinces_list)

def read_provinces_file(filename):
    # read the contents of the provinces.txt file into 
    # a list of provinces and return the list
    provinces_list = []
    # Open the file for reading
    with open(filename, "rt") as provinces_file:
        # Read each line from the file
        for line in provinces_file:
            # strip the whitespace from the beginning and end
            # of the lind and append to the end of the provinces_list
            provinces_list.append(line.strip())
    return provinces_list


    
if __name__ == "__main__":
    main()