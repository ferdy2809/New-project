class car:
    def __init__(self, speed, color):
        print(speed)
        print(color)
        print('the __init__is called')
        
        
ford = car(200, 'RED')
honda = car(220, 'BLUE')
audi = car(250, 'GREEN')

# ford.speed = 200
# honda.speed = 220
# audi.speed = 250

# ford.color = 'red'
# honda.color = 'blue'
# audi.color = 'black'

# print(ford.speed)
#print(ford.color)