import glob, csv, jaconv, re

file_path = glob.glob("/Users/kebi/Desktop/analyzer/input/*.csv")
output_path = "/Users/kebi/Desktop/analyzer/output/anki_import.txt"

#https://stackoverflow.com/questions/46614526/how-to-import-a-csv-file-into-a-data-array
if (file_path[0]):
    with open(file_path[0], newline="") as csvfile:
        data = list(csv.reader(csvfile, delimiter='\t'))

    for x in data:
        #clear unneeded columns
        x.pop(0)
        x.pop(1)
        x.pop(1)
        x.pop(1)
        x.pop(1)
        x.pop(1)
        x.pop(1)
        x.pop(1)
        x.pop(1)
        x.pop(1)
        
        #convert reading to hiragana
        x[1] = jaconv.kata2hira(x[1])

        #remove readings from the example sentence except for the target word
        temp = ""
        bool = 0
        for c in x[2]:
            if (bool == 1):
                if (c == "["):
                    temp += "{"
                elif (c == "]"):
                    temp += "}"
                elif (c == "/"):
                    bool = 0
                    temp += c
                else:
                    temp += c
            elif (bool == 0):
                if (c == "<"):
                    bool = 1
                temp += c
        x[2] = temp
        x[2] = re.sub("\[.*?\]", "", x[2])
        x[2] = re.sub("{", "[", x[2])
        x[2] = re.sub("}", "]", x[2])

    #write to file
    f = open(output_path, "w")
    for x in data:
        f.write(x[0] + "[" + x[1] + "]," + x[2] + "\n")
    f.close()