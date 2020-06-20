import csv

sub_set = [0, 3]
# Pure functions


class Patient:
    def __init__(self, data):
        self.personal_data = []
        for index, value in enumerate(data):
            if index not in sub_set:
                self.personal_data.append(value)

    def get_risk(self):
        return self.personal_data[0]

    def get_age(self):
        return self.personal_data[1]

    def get_weight(self):
        return self.personal_data[2]

    def printData(self):
        print(self.personal_data)

    def set_risk(self, risk):
        self.personal_data[0] = risk


class Treatment:
    def __init__(self, patient):

        self.patient = patient
        self.feed_rate = 1

        self.current_hour = 0
        self.end_hour = self.current_hour + 1

        self.current_day = 0

        self.week_len = 5

        self.week_feeding_data = []
        self.daily_feeding_data = []
        self.hourly_feeding_data = []

        self.pause_feeding = False


    def feed(self):
        while self.current_day <= self.week_len:
            self.handle_daily_feed()
            while self.current_hour < 24:
                self.handle_hourly_feed()
                self.current_hour = self.current_hour + 1
            if self.current_hour == 24:
                self.current_hour = 0
                self.current_day+=1
            

    
    def handle_daily_feed(self):
        
        print('handling daily feed (current Day): ' + str(self.current_day))


    def handle_hourly_feed(self):
        # Push data into hour array
        bound_data = self.hourly_feeding_data
    def treat_low_risk(self):
        print("treating low risk")

with open("pData1.csv", newline='') as csvfile:
    inputItems = list(csv.reader(csvfile))
    p = Patient(inputItems[0])
    Treatment(p).feed()
