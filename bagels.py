
import random


class Guess_Number():
    n_ofdigits = 3
    
    def __init__(self,name) -> None:
        self.name = name
        self.lst_answer, self.the_answer = self.number_generetor()
        self.life = 10
        self.right_answer = False
        self.intro()
        self.user_input()
    def number_generetor(self):
        a=[]
        while len(a)<=(self.n_ofdigits-1):
            ram_num = str(random.randint(0,9))
            if ram_num not in a:
                a.append(ram_num)
        print(a)
        return a,''.join(a)
    
    def intro(self):
        print(
        f'''Hi {self.name}!.
            I am thinking of a {self.n_ofdigits}-digit number with no repeated digits.
            Try to guess what it is. Here are some clues:
            When I say: That means:
            Pico        One digit is correct but in the wrong position.
            Fermi       One digit is correct and in the right position.
            Bagels      No digit is correct.''')
        input('Press enter to start')
        
    def user_input(self):
        print(f'You have {self.life} guesses to get it.')
        while True:
            for n in range(0,self.life):
                print(f'Guess #{n+1}:')
                user = input('> ')
                self.check_answer(user)
                if self.right_answer:
                    print('You Got it')
                    break
            again = input('Would you like to play again? Yes/No: ')
            if again.lower() == 'no':
                print('Thanks for playing!') 
                break
            else:
                self.lst_answer, self.the_answer = self.number_generetor()
                self.right_answer = False
                continue

    def check_answer(self,user_answer):
        hint=[]
        user_anwer_lst = ' '.join(user_answer).split()
        if user_anwer_lst == self.lst_answer:
            self.right_answer= True
            return

        for l in range(len(user_answer)):
            
            if user_anwer_lst[l] == self.lst_answer[l]:
                hint += ['Fermi']
                continue

            if user_anwer_lst[l] in self.lst_answer[l]:
                hint +=['Pico']

        if len(hint) < 1:
            hint += ['Bagels']
        print(', '.join(hint),'\n')


Guess_Number('maça')