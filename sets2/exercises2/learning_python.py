#class Suitor:
#def __init__(self, id, preference_list):
#self.preference_list = preference_list
#self.index_to_propose_to = 0
#self.id = id
#def preference(self):
#return self.preference_list[self.index_to_propose_to]
#def post_rejection(self):
#self.index_to_propose_to += 1

class Suitor:
    # caio.__init__(0,[2,3]) actually works. So the self means that the obj can call that function.
    def __init__(self, id, preference_list):
        self.id = id
        self.preference_list = preference_list 
        #Can think of self as the obj, the same as in this means the obj instance in js.
        # caio.id workd but Suitor doesnt, because self is the obj instance, not the class.
        self.index_to_propose_to = 0

    def preference(self):
        # caio.preference_list[caio.index... = 0]
        return self.preference_list[self.index_to_propose_to]

    def post_rejection(self):
        self.index_to_propose_to += 1

    def abstract(self):
        if(self.id == 0):
            return set([1,1,5,8,8,7,7,7])
            #{8,1,5,7}
        else:
            return "Awesome!"

    #The below function works if we do print(Suitor.summation(3,4)) = 7
    #But caio.summation(3,4) doenst, it says 3 arguments were passed in. So
    #whenever I want an instance of a class to call a fucntion, the instance will be self in the arguments.

    #def summation(a, b):
    #    return a + b

class Suited:
    def __init__(self, id, preference_list):
        self.id = id
        self.preference_list = preference_list
        self.held = None 
        self.current_suitors = set()

    def reject(self):
        if len(self.current_suitors) == 0:
            return set()
        
        self.held = min(
            self.current_suitors,
            key=lambda suitor: self.preference_list.index(suitor.id)
        )
        rejected = self.current_suitors - set([self.held])
        self.current_suitors = set([self.held])

        return rejected

    def add_suitor(self, suitor):
        self.current_suitors.add(suitor)

def stable_marriage(suitors, suiteds):
    """ Construct a stable marriage between Suitors and Suiteds. """
    unassigned = set(suitors)
    print(unassigned)
    while len(unassigned) > 0:
        for suitor in unassigned:
            next_to_propose_to = suiteds[suitor.preference()]
            next_to_propose_to.add_suitor(suitor)
        unassigned = set()
  
        for suited in suiteds:
            unassigned |= suited.reject() # python set union operator
  
        for suitor in unassigned:
            suitor.post_rejection() # have some ice cream
    
    return dict([(suited.held, suited) for suited in suiteds])

caio = Suitor(0, [3, 5, 4, 2, 1, 0])
joao = Suitor(1, [2, 3, 1, 0, 4, 5])
abru = Suitor(2, [5, 2, 1, 0, 3, 4])
juio = Suitor(3, [0, 1, 2, 3, 4, 5])
vito = Suitor(4, [4, 5, 1, 2, 0, 3])
rede = Suitor(5, [0, 1, 2, 3, 4, 5])

print(caio.preference())

suitors = [
caio,
joao,
abru,
juio,
vito,
rede
]

juli = Suited(0, [3, 5, 4, 2, 1, 0])
fran = Suited(1, [2, 3, 1, 0, 4, 5])
lina = Suited(2, [5, 2, 1, 0, 3, 4])
moni = Suited(3, [0, 1, 2, 3, 4, 5])
lana = Suited(4, [4, 5, 1, 2, 0, 3])
anna = Suited(5, [0, 1, 2, 3, 4, 5])


suiteds = [
juli,
fran,
lina,
moni,
lana,
anna
]

stable_marriage(suitors, suiteds)