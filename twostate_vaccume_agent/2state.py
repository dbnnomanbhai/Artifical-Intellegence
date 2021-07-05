import random


class Object:

    def __repr__(self):
        return '<%s>' % getattr(self, '__name__', self.__class__.__name__)


class Agent(Object):

    def __init__(self):
        def program(percept): abstract

        self.program = program


loc_A, loc_B = 'A', 'B'


class vaccumEnvironment():

    def __init__(self):

        self.status = {loc_A: random.choice(['Clean', 'Dirty']), loc_B: random.choice(['Clean', 'Dirty']),



                       }

    def add_object(self, object, location=None):

        object.location = location or self.default_location(object)

    def default_location(self, object):

        return random.choice([loc_A, loc_B ])

    def percept(self, agent):

        return (agent.location, self.status[agent.location])

    def execute_action(self, agent, action):

        if action == 'Right':

            agent.location = loc_B

        elif action == 'Down':


            agent.location = loc_A

        elif action == 'Down':



            agent.location = loc_A

        elif action == 'Right':



            agent.location = loc_B

        elif action == 'Suck':

            # if self.status[agent.location]=='Dirty',

            self.status[agent.location] = 'Clean'


class tableDrivenAgent(Agent):

    def __init__(self, table):
        Agent.__init__(self)

        percepts = []

        def program(percept):
            percepts.append(percept)

            print(percepts)

            action = table.get(tuple(percepts))

            print('Agent perceives ', percept, ' and  action: ', action)

            return action

        self.program = program


def tableDrivenVaccumAgent():
    table = {

        ((loc_A, 'Clean'),): 'Right',

        ((loc_A, 'Dirty'),): 'Suck',

        ((loc_B, 'Clean'),): 'Left',

        ((loc_B, 'Dirty'),): 'Suck',

        ((loc_A, 'Clean'),): 'Down',





        (('B', 'Clean'), ('A', 'Dirty')): 'Suck',



        (('A', 'Clean'), ('B', 'Dirty')): 'Suck',


        (('B', 'Clean'), ('A', 'Clean')): 'Right',

        (('B', 'Clean'), ('A', 'Clean')): 'Down',

        ((loc_A, 'Clean'), (loc_A, 'Clean')): 'Right',

        ((loc_A, 'Clean'), (loc_B, 'Clean')): 'Left',

        ((loc_A, 'Clean'), (loc_B, 'Clean')): 'Down',

        ((loc_A, 'Clean'), (loc_B, 'Dirty')): 'Suck',

        ((loc_A, 'Clean'), (loc_A, 'Dirty')): 'Suck',

        ((loc_A, 'Clean'), (loc_B, 'Dirty')): 'Suck',

        ((loc_A, 'Clean'), (loc_A, 'Dirty')): 'Suck',

        ((loc_A, 'Dirty'), (loc_A, 'Clean')): 'Right',

        ((loc_A, 'Dirty'), (loc_B, 'Clean')): 'Left',

        ((loc_A, 'Dirty'), (loc_B, 'Dirty')): 'Right',

        ((loc_A, 'Dirty'), (loc_A, 'Dirty')): 'Suck',



        ((loc_B, 'Clean'), (loc_A, 'Clean')): 'Right',

        ((loc_B, 'Clean'), (loc_B, 'Clean')): 'Left',

        ((loc_B, 'Clean'), (loc_B, 'Dirty')): 'Right',

        ((loc_B, 'Clean'), (loc_A, 'Dirty')): 'Suck',



        ((loc_B, 'Dirty'), (loc_A, 'Clean')): 'Right',

        ((loc_B, 'Dirty'), (loc_B, 'Clean')): 'Left',

        ((loc_B, 'Dirty'), (loc_B, 'Dirty')): 'Right',

        ((loc_B, 'Dirty'), (loc_A, 'Dirty')): 'Suck',



        ((loc_A, 'Clean'), (loc_A, 'Clean'), (loc_A, 'Clean')): 'Right',

        ((loc_A, 'Clean'), (loc_A, 'Clean'), (loc_A, 'Dirty')): 'Suck',

        ((loc_A, 'Clean'), (loc_A, 'Clean'), (loc_A, 'Clean')): 'Down',

        ((loc_A, 'Clean'), (loc_A, 'Clean'), (loc_A, 'Dirty')): 'Suck',

        ((loc_B, 'Clean'), (loc_B, 'Clean'), (loc_B, 'Clean')): 'Left',





        ((loc_A, 'Clean'), (loc_A, 'Dirty'), (loc_A, 'Clean')): 'Right',

        ((loc_A, 'Clean'), (loc_A, 'Clean'), (loc_A, 'Dirty')): 'Suck',

        ((loc_A, 'Clean'), (loc_A, 'Dirty'), (loc_A, 'Clean')): 'Down',

        ((loc_A, 'Clean'), (loc_A, 'Clean'), (loc_A, 'Dirty')): 'Suck',

        ((loc_B, 'Clean'), (loc_B, 'Dirty'), (loc_B, 'Clean')): 'Left',

        ((loc_B, 'Clean'), (loc_B, 'Clean'), (loc_B, 'Dirty')): 'Suck',

        ((loc_B, 'Clean'), (loc_B, 'Dirty'), (loc_B, 'Clean')): 'Down',


        (('D', 'Clean'), ('A', 'Clean'), ('A', 'Clean')): 'Right',

        (('D', 'Clean'), ('A', 'Clean'), ('A', 'Clean')): 'Down',





        (('A', 'Dirty'), ('A', 'Clean'), ('B', 'Dirty')): 'Suck',



        (('B', 'Clean'), ('A', 'Dirty'), ('A', 'Clean')): 'Right',

        (('B', 'Clean'), ('A', 'Dirty'), ('A', 'Clean')): 'Down',

        (('B', 'Dirty'), ('B', 'Clean'), ('A', 'Dirty')): 'Suck',

        (('B', 'Dirty'), ('B', 'Clean'), ('B', 'Dirty')): 'Suck',








        (('A', 'Dirty'), ('A', 'Clean'), ('B', 'Dirty')): 'Suck',


        (('A', 'Clean'), ('C', 'Dirty'), ('C', 'Clean')): 'Right',


        (('B', 'Clean'), ('A', 'Clean'), ('B', 'Clean')): 'Left',

        (('B', 'Clean'), ('A', 'Clean'), ('B', 'Clean')): 'Down',

        (('D', 'Clean'), ('A', 'Clean'), ('C', 'Dirty')): 'Suck',

        (('A', 'Dirty'), ('A', 'Clean'), ('B', 'Clean')): 'Left',

        (('A', 'Dirty'), ('A', 'Clean'), ('B', 'Clean')): 'Down',

        (('B', 'Dirty'), ('B', 'Clean'), ('A', 'Clean')): 'Right',

        (('B', 'Dirty'), ('B', 'Clean'), ('A', 'Clean')): 'Down',












    }

    print("Table Driven Vaccum Agent\n")

    return tableDrivenAgent(table)


Tagent = tableDrivenVaccumAgent()

env = vaccumEnvironment()

env.add_object(Tagent)

for _ in range(4):
    action = Tagent.program(env.percept(Tagent))

    env.execute_action(Tagent, action)


class reflexVaccumAgent(Agent):

    def __init__(self):

        Agent.__init__(self)

        def program(percept):

            location = percept[0]

            status = percept[1]

            if status == 'Dirty':

                action = 'Suck'

            elif location == loc_A:

                action = 'Right'

            elif location == loc_B:

                action = 'Left'

            elif location == loc_B:

                action = 'Down'

            elif location == loc_A:

                action = 'Right'


            percept = (location, status)

            print('Agent perceives ', percept, ' and action: ', action)

            return action

        self.program = program


print("\nReflex Vaccum Agent\n")

Tagent = reflexVaccumAgent()

env = vaccumEnvironment()

env.add_object(Tagent)

for _ in range(4):
    action = Tagent.program(env.percept(Tagent))

    env.execute_action(Tagent, action)


class modelBasedVaccumAgent(Agent):

    def __init__(self):

        Agent.__init__(self)

        model = {loc_A: None, loc_B: None }

        def program(percept):

            location = percept[0]

            status = percept[1]

            model[location] = status

            if model[loc_A] == model[loc_B] :

                action = 'none'

            elif status == 'Dirty':

                action = 'Suck'

            elif location == loc_A:

                action = 'Right'

            elif location == loc_B:

                action = 'Left'

            elif location == loc_B:

                action = 'Down'

            elif location == loc_A:

                action = 'Right'



            percept = (location, status)

            print('Agent perceives ', percept, ' and action: ', action)

            return action

        self.program = program


print("\nModel Based Vaccum Agent\n")

Tagent = modelBasedVaccumAgent()

env = vaccumEnvironment()

env.add_object(Tagent)

for _ in range(4):
    action = Tagent.program(env.percept(Tagent))

    env.execute_action(Tagent, action)

