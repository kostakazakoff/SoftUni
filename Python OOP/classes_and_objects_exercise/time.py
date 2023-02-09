class Time:
    max_hours, max_minutes, max_seconds = 23, 59, 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours, self.minutes, self.seconds = hours, minutes, seconds

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        self.seconds += 1
        
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
            
            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self.hours += 1

                if self.hours > Time.max_hours:
                    self.hours = 0

        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"        