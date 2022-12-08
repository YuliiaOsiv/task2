import sys

file_with_data = sys.argv[1]
medals = sys.argv[2]
country = sys.argv[3]
code_number = sys.argv[4]
year = sys.argv[5]
year_set = set()

#print("country = ", country, "medals = ", medals)

with open(file_with_data, "r") as file: #умовне відображення файлу в нашій програмі
    line = file.readline() #ID
    line = file.readline() #rerr
    while line != "":
        line_splitted = line.split("\t")
        #if country == line_splitted[7]:
            #print(line_splitted)
        year = int(line_splitted[9])
        year_set.add(year)
        line = file.readline()

year_list = sorted(year_set)
print(year_set)

for i, y in enumerate(year_list[:10], 1):
    print(i, "\t", y)



