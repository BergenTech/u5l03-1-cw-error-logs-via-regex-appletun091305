import re, json, csv

with open("logs.json","r") as file:
    with open("error_logs.csv","w") as write_file:
        writer = csv.writer(write_file)
        writer.writerow(["timestamp","level","message"])
        data = json.load(file)
        for line in data:
            if re.search(r"ERROR",line["level"],re.IGNORECASE):
                line["level"] = "ERROR"
                writer.writerow(line.values())