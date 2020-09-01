
class restrantrobot:

    def introduce(self):
        print('---------------------------------------------')
        print('Hello, I am Hanako. What is your name?')
        print('---------------------------------------------')
        self.name = input()

    def question(self):
        print('---------------------------------------------')
        print('{}, which restrant do you like?'.format(self.name))
        print('---------------------------------------------')
        self.restrant = input()
        return self.restrant

    def reccomend(self, restrant):
        print('---------------------------------------------')
        print('I reccomend {} restrantrobot'.format(restrant))
        print('Do you like it? [y/n]')
        print('---------------------------------------------')
        response = input()
        if response == 'y':
            return True
        else:
            return False

    def goodbye(self):
        print('---------------------------------------------')
        print('Thank you so much, {}!'.format(self.name))
        print('---------------------------------------------')
