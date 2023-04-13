import random
import name_list as ns

class Contestant:
    def __init__(self):
        self.name = random.choice(ns.nameset)
        self.age = random.choice(range(18,50))
    def __repr__(self):
        return f'{self.name}: {self.age}'

class Match:
    def __init__(self, contestant1, contestant2):
        self.contestant1 = contestant1
        self.contestant2 = contestant2
        self.match = set((contestant1, contestant2))


class Simulation:
    def __init__(self, num_of_contestants=16):
        self.num_of_contestants = num_of_contestants
        #Create list of contestants
        self.contestants = []
        for i in range(self.num_of_contestants):
            self.contestants.append(Contestant())
        #Randomly select perfect matches from contestant lis
        self.perfect_matches = self.get_perfect_matches()
        
    def get_perfect_matches(self):
        perfect_match_list = []
        contestants_copied = self.contestants[:]
        
        for i in range(len(self.contestants)//2):
            x = random.choice(contestants_copied[:len(contestants_copied)//2])
            y = random.choice(contestants_copied[len(contestants_copied)//2:])
            match_set = set()
            for contestant in (x,y):
                match_set.add(contestant)
        
            perfect_match_list.append(match_set)
            contestants_copied.remove(x)
            contestants_copied.remove(y)

        return perfect_match_list
    def meet_contestants(self):
        meet_contestants = []
        for cont in self.contestants:
            meet_contestants.append(cont.__repr__())
        return meet_contestants
    
    def truth_booth(self, matchup):
        if matchup in self.perfect_matches: return True
        return False
        
    #Perfect Match Algorithms
    def get_possible_answers(self):
        possible_couples = []
        for i in range(len(self.contestants)):
            for j in range(len(self.contestants)-1):
                match_set = set()
                first, second = self.contestants[i], self.contestants[j+1]
                match_set.add(first), match_set.add(second)
                if match_set in possible_couples:
                    continue
                elif first == second:
                    continue
                elif (second, first) in possible_couples:
                    continue
                else:
                    possible_couples.append(match_set)
        return possible_couples
    def track_match_probability(self, guess, perfect_matches):
        #make func that takes the guess and returns the list of non-perfect 
        #match guesses, as well as the probability of one being correct
        #represented as amt_correct_at_round / amt of non perfect matches
        #store the variable and when the prob is good draw (amt_correct_at_round)
        #matches at random from the list, this should optimize the function
        new_guess = []
        amt_correct = 0
        probability = 0
        for match in guess:
            if match not in perfect_matches:
                new_guess.append(match)
                if self.truth_booth(match) is True: amt_correct += 1
        if len(new_guess) > 0:
            probability = amt_correct / len(new_guess)
        return new_guess, probability
    def random_algorithm(self, matches_remaining):
        'randomly selects couples from match possibilities'
        guess = []
        
        #Truth Booth
        truth_booth_choice = random.choice(matches_remaining)
        result = self.truth_booth(truth_booth_choice)
        if result is True:
            guess.append(truth_booth_choice)
        else:
            matches_remaining.remove(truth_booth_choice)
        #random guesses
        while len(guess) < 8:
            match = random.choice(matches_remaining)
            if match not in guess:
                guess.append(match)
        
        #determine amt correct
        amount_correct = 0
        for couple in guess:
            if self.truth_booth(couple) is True: amount_correct += 1
        return amount_correct, matches_remaining


    def algorithm_1(self, perfect_matches, matches_remaining, truth_booth_couples):
        #Send couple to truth booth
        if len(truth_booth_couples) > 0:
            selected_couple = random.choice(truth_booth_couples)
            truth_booth_couples.remove(selected_couple)
        else:
            selected_couple = random.choice(matches_remaining)
            matches_remaining.remove(selected_couple)
        #Determine if they are a perfect match
        result = self.truth_booth(selected_couple)
        #add to perfect_match list if true
        #remove possible couples with both individuals in them
        if result is True:
            for contestant in selected_couple:
                for other in matches_remaining:
                    if contestant in other:
                        matches_remaining.remove(other)
            perfect_matches.append(selected_couple)
        
        #select 8 couples
        guess = []
        for i in range(len(perfect_matches)):
                guess.append(perfect_matches[i])
        while len(guess) < 8:
            choice = random.choice(matches_remaining)
            if choice not in guess:
                guess.append(choice)
        #check how many are correct
        amount_correct = 0
        for couple in guess:
            if self.truth_booth(couple) is True: amount_correct += 1 
        #if none are correct remove all couples from possibilities
        if amount_correct == perfect_matches:
            for couple in guess:
                if couple in matches_remaining:
                    matches_remaining.remove(couple)
        elif amount_correct > len(perfect_matches):
            truth_booth_couples = [i for i in guess if i not in perfect_matches]
        #quick test to make sure guess is the same as perfect match list
        if amount_correct == 8:
            for couple in guess:

                assert(couple in self.perfect_matches)

        return amount_correct, perfect_matches, matches_remaining, truth_booth_couples
    def optimized_algorithm(self,perfect_matches,matches_remaining, score_data):
        #Send couple to truth booth
        if score_data[1] >= .1:
            selected_couple = random.choice(score_data[0])
            if selected_couple in matches_remaining:
                matches_remaining.remove(selected_couple)
        else:
            selected_couple = random.choice(matches_remaining)
            matches_remaining.remove(selected_couple)
        #Determine if they are a perfect match
        result = self.truth_booth(selected_couple)
        #add to perfect_match list if true
        #remove possible couples with both individuals in them
        if result is True:
            for contestant in selected_couple:
                for other in matches_remaining:
                    if contestant in other:
                        matches_remaining.remove(other)
            perfect_matches.append(selected_couple)
        
        #select 8 couples
        guess = []
        for i in range(len(perfect_matches)):
                guess.append(perfect_matches[i])
        while len(guess) < 8:
            if score_data[1] > .75:
                for i in range((len(score_data[0])//2)):
                    choice = random.choice(score_data[0])
                    if choice not in guess:
                        guess.append(choice)
            
            choice = random.choice(matches_remaining)
            if choice not in guess:
                guess.append(choice)
        #check how many are correct
        amount_correct = 0
        for couple in guess:
            if self.truth_booth(couple) is True: amount_correct += 1 
        #if none are correct remove all couples from possibilities
        if amount_correct == len(perfect_matches):
            for couple in guess:
                if couple in matches_remaining:
                    matches_remaining.remove(couple)
            score_data = [],0
        else:
            score_data = self.track_match_probability(guess, perfect_matches)
        return amount_correct, perfect_matches, matches_remaining, score_data
    def play_game(self, algorithm=None):
        round = 1
        if algorithm is None:
            algorithm = input('Select algorithm: Random, Naive, Optimized\n')
        while round < 1000:
            print(f'Round {round}:')
            if algorithm == 'Naive':
                if round == 1:
                    comp_perfect_matches = []
                    matches_remaining = self.get_possible_answers()
                    truth_booth_couples = []
                else:
                    comp_perfect_matches = results[1]
                    matches_remaining = results[2]
                    truth_booth_couples = results[3]
                results = self.algorithm_1(comp_perfect_matches, matches_remaining,truth_booth_couples)
            elif algorithm == 'Random':
                if round == 1:
                    matches_remaining = self.get_possible_answers()
                else:
                    matches_remaining = results[1]
                results = self.random_algorithm(matches_remaining)
            elif algorithm == 'Optimized':
                if round == 1:
                    comp_perfect_matches = []
                    matches_remaining = self.get_possible_answers()
                    score_data = ([],0)
                else:
                    comp_perfect_matches = results[1]
                    matches_remaining = results[2]
                    score_data = results[3]
                results = self.optimized_algorithm(comp_perfect_matches, matches_remaining, score_data)
            print(f'You got {results[0]} correct this round!')
            if results[0] == 8:
                print(f"You won in {round} rounds!")
                print(f'The perfect matches are: {self.perfect_matches}')
                break
                
            round += 1
        #for data analyzing - return amount of rounds
        return round
if __name__ == '__main__':
    #Simulated Game
    s1 = Simulation()
    #print(s1.perfect_matches)
    #assert(s1.truth_booth(s1.contestants[1],s1.contestants[9]))
    s1.play_game()
    #print(s1.algorithm_1())
    #print(s1.get_possible_answers()) 