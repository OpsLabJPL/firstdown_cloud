
from email.utils import parsedate_tz

class ASPLog:

    """
    Return a JSON object from the ASP auto_processed.log file data.
    """
    def parselog(self, filename):
        lines = []
        with open(filename, "r") as logfile:
            for line in logfile:
                status = SequenceStatus()
                fields = line.split()
                if len(fields) < 10:
                    continue
                status.duration = fields[5]
                status.name = fields[6]
                status.scid = fields[7]
                status.seqid = fields[8]
                if status.duration: # if string is not empty
                    dateTimeString = "{0} {1} {2} {3} Z".format(fields[2], fields[1], fields[4], fields[3])
                    status.timestamp = parsedate_tz(dateTimeString)
                for word in fields[9:]:
                    status.statusMessage += word + " "
                status.statusMessage = status.statusMessage.rstrip()
                lines.append(line)
        return lines

class SequenceStatus:

    def __init__(self):
        self.duration = 0
        self.name = ""
        self.scid = ""
        self.seqid = ""
        self.timestamp = ""
        self.statusMessage = ""

    def __str__(self):
        """Return a readable string description of an instance of Overflight"""
        return "Status name: {0} scid: {1} seqid: {2} duration: {3} timestamp: {4}".format(self.name, self.scid,
                                                                                           self.seqid,
                                                                                           str(self.duration),
                                                                                           self.timestamp)


