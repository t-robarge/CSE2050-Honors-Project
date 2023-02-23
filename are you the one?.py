import random
import name_list as ns


class Contestant:
    def __init__(self):
        self.name = random.choice(ns.nameset)
        self.age = random.choice(range(18,50))

    pass
    def __repr__(self):
        return f'{self.name}, {self.age}'

class PerfectMatches:
    def __init__(self, contestants):
        self.contestants = contestants
        self.list = []
        
        for i in range(len(self.contestants)//2):
            x = random.Random(500).choice(self.contestants[:len(self.contestants)//2])
            y = random.Random(500).choice(self.contestants[len(self.contestants)//2:])
            self.list.append((x,y))
            self.contestants.remove(x)
            self.contestants.remove(y)



     
class Simulation:
    def __init__(self, num_of_contestants=16):
        self.num_of_contestants = num_of_contestants
        self.play_game()
       
        self.perfect_matches = PerfectMatches(self.contestants).list
        
   
    def get_perfect_matches(self):
        list = []
        
        for i in range(len(self.contestants)//2):
            x = random.Random(500).choice(self.contestants[:len(self.contestants)//2])
            y = random.Random(500).choice(self.contestants[len(self.contestants)//2:])
            list.append((x,y))
            self.contestants.remove(x)
            self.contestants.remove(y)

        return list


    def play_game(self):
        
        self.contestants = []
        for i in range(self.num_of_contestants):
            self.contestants.append(Contestant())
        
       

       




    #Perfect Match Algorithms
    def algoritm_1(contestant_1, contestant_2):
        pass

    def algoritm_2(contestant_1, contestant_2):
        pass

    def algoritm_3(contestant_1, contestant_2):
        pass



    




if __name__ == '__main__':
    #Simulated Game
    S1 = Simulation()
    print(S1.perfect_matches)
    print(S1.perfect_matches)

    

        
