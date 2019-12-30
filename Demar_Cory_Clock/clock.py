# Programmer: Cory DeMar
# ComSc 20
# Assognment #16
# Objects
# 5-15-17

def to_minutes(obj):
    return obj.hour * 60 + obj.minute

def from_military(s):
    #Create Clock object from military-format time string
    hr = int(s[0:2])
    minute = int(s[2:4])
    return Clock (hr, minute)

##def from_am_to_pm_method_1(s):
##    #Creat Clock object from string in form hh:mm AM/MP
##    pos = s.find(':')
##    if pos >= 0:
##        hour = int(s[:pos]) % 12
##        minute = int(s[pos + 1] : pos + 3]) % 60
##        pos = pos + 3
##        while s[pos] not in 'AaPp':
##            pos = pos + 1
##        if s[pos] in 'pP':
##            hour = hour + 12
##        else:
##            hour = 0
##            minute = 0
##    return Clock(hour, minute)

def from_am_pm(s):
    #create clock object from string in form hh:mm AM/PM
    [h, m] = s.split(':')
    hour = int(h) % 12
    minute = int(m[0:2]) % 60
    suffix = m[2:]
    suffix = suffix.strip().upper()
    if suffix[0] == 'P':
        hour = hour + 12
    return Clock(hour, minute)


class Clock:
    def __init__(self, hour, minute):
        self.hour = abs(hour) % 24
        self.minute = abs(minute) % 60

    def __str__(self):
        return format(self.hour, '02d') + format(self.minute, '02d')

    def add(self, other):
        self_min = to_minutes(self)
        other_min = to_minutes(other)
        total = self_min + other_min
        return Clock(total // 60, total % 60)

    def subtract(self, other):
        self_min = to_minutes(self)
        other_min = to_minutes(other)
        total = self_min - other_min
        return Clock(total // 60, total % 60)