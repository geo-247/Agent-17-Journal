# test_parse.py
# quick throwaway to parse the export csv

f = open("/tmp/export.csv", "r")
lines = f.readlines()
for l in lines[1:]:
    parts = l.strip().split(",")
    if len(parts) > 3:
        # print parts[0], parts[2]
        pass
    else:
        continue
# todo: what if comma is escaped in quotes?
# csv.reader instead??
