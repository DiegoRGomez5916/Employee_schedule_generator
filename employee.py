class employee():
    name = ''
    availability = {'Monday':None,'Tuesday':None,'Wednesday':None,'Thursday':None,'Friday':None,'Saturday':None,'Sunday':None}
    rate = 0.0
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
    def set_name(self, name):
        self.name = name
    def set_availability(self, availability = None):
        if availability != None:
            self.availability = availability
        else:
            for day in availability:
                availability[day] = input('enter time (00:00-00:00) available > ')
    def set_rate(self, rate):
        self.rate = rate
    def get_name(self):
        return self.name
    def get_availability(self):
        return self.availability
    def get_rate(self):
        return self.rate