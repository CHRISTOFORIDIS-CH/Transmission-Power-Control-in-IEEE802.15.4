# replace "certain phrase" with the actual phrase you want to match
phrase1 = "Prec  from"
phrase2 = "Total RSSI"
phrase3 = "PDR for"

# replace "input_file.txt" and "output_file.txt" with your actual file names
with open("RawData.txt", "r") as infile, open("CleanData.txt", "w") as outfile:
    for line in infile:
        if line.startswith(phrase1) or line.startswith(phrase2) or line.startswith(phrase3):
            outfile.write(line)
        else:
            continue