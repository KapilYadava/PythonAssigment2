class First:

    def method1(self):
        print('First')


class Second:

    def method1(self):
        print('Second')


class Third(First):

    def method1(self):
        print('Third')


class Fourth(Second, Third):

    def method1(self):
        print('Fourth')

    fourth = Third()
    fourth.method1()
