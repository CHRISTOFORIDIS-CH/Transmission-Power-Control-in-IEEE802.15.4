import pandas as pd

# replace "input_file.txt" and "output_file.xlsx" with your actual file names
input_file = "data.txt"
output_file = "ML_Data.xlsx"

# create an empty list to store the data
data = []

# open the input file and read it line by line
with open(input_file, "r") as infile:
    for line in infile:
        # check if the line starts with "Prec"
        try:
            if line.startswith("Prec"):
                # extract the from_node, to_node, Prec, and RSSI values from the line
                from_node = line.split("from node: ")[1].split(" to node ")[0]
                to_node = line.split("to node ")[1].split(" is:")[0]
                Prec = line.split(": ")[-1].strip()
                # read the next line and extract the RSSI value from it
                next_line = next(infile)
                RSSI = next_line.split(": ")[-1].strip()
                # read the next line (the line afte next_line)and extract the PDR value from it
                # if it doesnt't exit give it the value 0
                next_next_line = next(infile)
                if "PDR" in next_next_line:
                    PDR = next_next_line.split(": ")[-1].strip()
                else:
                    PDR = 0
                # add the data to the list
                data.append([from_node, to_node, Prec, RSSI, PDR])
        except StopIteration:
            print("End of file reached")

# create a pandas DataFrame from the data and write it to an Excel file
df = pd.DataFrame(data, columns=["from_node", "to_node", "Prec", "RSSI", "PDR"])
df.to_excel(output_file, index=False)
