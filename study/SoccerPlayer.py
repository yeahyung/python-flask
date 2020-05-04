class SoccerPlayer(object):
    def __init__(self, name, position, backNumber):
        self.name = name
        self.position = position
        self.backNumber = backNumber


    def __str__(self):
        return "Hi, my name is %s. I play in %s in center" % (self.name, self.position)

    def change_back_number(self, newNumber):
        print("change back number: From %d to %d" %(self.backNumber, newNumber))
        self.backNumber = newNumber
