from enum import Enum
from dataclasses import dataclass
from datetime import datetime, timedelta
from random import choice

class LogLevel(Enum):
    ERROR = 0
    WARN = 1
    INFO = 2
    
@dataclass
class LogEntry:
    level: LogLevel
    time: datetime
    text: str

class LogGenerator:
    #region data
    _infos = ["all quiet", "*yawn*", "so bored", "does anyone read these?"]
    _warns = ["what was that?", "did you hear something?", "anyone there?", "uh oh. . ."]
    _errors = ["help help!", "fire! burning!", "danger danger!", "oh god!"]
    _starttime = datetime.now() - timedelta(days=1)
    _hour = 0
    #endregion
    
    def _get_time(self):
        ret = self._starttime + timedelta(hours=self._hour)
        self._hour += 1
        return ret
    
    def _goodlog(self):
        return LogEntry(
            LogLevel.INFO,
            self._get_time(),
            choice(self._infos)
        )
    
    def _medlog(self):
        return LogEntry(
            LogLevel.WARN,
            self._get_time(),
            choice(self._warns)
        )
    
    def _badlog(self):
        return LogEntry(
            LogLevel.ERROR,
            self._get_time(),
            choice(self._errors)
        )

    def generate_entries(self):
        log: list[LogEntry] = []
        for _ in range(0, 8):
            log.append(self._goodlog())
        for _ in range(0, 8):
            log.append(self._medlog())
        for _ in range(0, 8):
            log.append(self._badlog())
        return log


# def find_start_of_errors(log: list[LogEntry]) -> LogEntry:
#     left = 0
#     right = len(log) - 1

#     while left <= right:
#         mid = (left + right) // 2
#         if log[mid].level == LogLevel.ERROR:
#             if log[mid - 1].level == LogLevel.WARN:
#                 return log[mid - 1]
#             else:
#                 right = mid - 1
#         elif log[mid].level == LogLevel.WARN:
#             left = mid + 1
#         elif log[mid].level == LogLevel.INFO:
#             left = mid + 1
    
#     return -1

def find_start_of_errors(log: list[LogEntry]) -> LogEntry:
    if len(log) <= 1:
        return log[0]
    
    mid = len(log) // 2

    if log[mid].level == LogLevel.INFO:
        find_start_of_errors(log[mid:])
    else:
        find_start_of_errors(log[:mid])



if __name__ == "__main__":

    log = LogGenerator().generate_entries()

    print("=====log=====")
    for l in log:
        print(l)
    print()
    print("=====search result=====")   
    start = find_start_of_errors(log)
    print(f"found: {start}")

    print   