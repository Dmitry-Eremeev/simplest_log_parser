# Example response:
# NOKs number in every minute: {'2018-04-11 03:13': 0, '2018-04-11 03:14': 1}

from os import linesep


class Parser:
    def __init__(self):
        self.records = dict()

    def parse_log(self, log_file):
        with open(log_file, encoding="utf-8") as raw_data:
            while True:
                line = raw_data.readline()
                if not line:
                    break
                if line != "\n":
                    date, _, status = line.rstrip(linesep).rpartition(" ")
                    date, _, _ = date.strip("[]").rpartition(":")
                    self.records.setdefault(date, 0)
                    if status == "NOK":
                        self.records[date] += 1


if __name__ == "__main__":
    parser = Parser()
    parser.parse_log("events.log")
    print("NOKs number in every minute: %s" % parser.records)
