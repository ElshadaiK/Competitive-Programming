class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            log_splited = log.split()
            if log_splited[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log_splited)
        letter_logs.sort(key = lambda x: (x[1:], x[0]))
        letter_logs = [" ".join(log) for log in letter_logs] 
        return letter_logs + digit_logs