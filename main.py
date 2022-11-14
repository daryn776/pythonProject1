import operator
import datetime

class MyError(Exception):
    def __init__(self,text):
        self.text = text

class Book:
    emp_count = 0
    id = 0

    def __init__(self, atau, dana, cena):

        self.nazvanie = atau
        self.dana =dana
        self.bagasy = cena
        Book.emp_count += 1
    id += 1
    def display_count(self):
        print('Всего сттудентов: %d' % Book.emp_count)

    def display(self):
        print(
              ' nazvanie: {} '
              ' avtory: {}'
              ' bet_sany: {}'
              ' bagasy:{} '.format(self.id,self.nazvanie,self.avtory,self.bet_sany,self.bagasy))

    def sort_choice(self,Data,choice):
        result = sorted(Data, key=operator.attrgetter(choice))
        for i in result:
            i.display()


s1 = Book("Abay joly", "Mukhtar Auezov", 500, 4000)
s2 = Book("45 kara soz", "Abai", 400, 3000)
s3 = Book("Python", "Daryn", 300, 10000)
s4 = Book("Sarar", "Tima", 350, 5000)
e = [s1, s2, s3, s4]



def sort_choice(Data, choice):
    result = sorted(Data, key=operator.attrgetter(choice))
    for i in result:
        i.display()

while True:
    print('\n1.список книг заданного автора')
    print('2.список книг багасы бойынша ')
    print('3.список книг, бет саны бойынша')

    print('4.exit ')
    n = input()

    try:
        n=int()
        if(n<0):
            raise MyError("Syz terys san engyndyn on engyz")
        if (n == 1):
            avtor = input("Enter Avtor")

            for i in e:
                if (avtor.upper()).strip() == i.avtor:
                    i.display()

        elif n == 2:
            avtor = input("Enter Avtor")
            cena = int(input("Enter Bagasy"))
            for i in e:
                if avtor == i.avtor and cena == i.cena:
                    i.display()
        elif n==3:
            k=int(input(("Sort time \n1. Nazvanie \n2. cenasy" )))
            if(k==1):
                result = sorted(e, key=operator.attrgetter('nazvanie'))
                for i in result:
                    i.display()
            elif k==2:
                sort_choice(e,'cena')
        elif n==4:
            break

        else:
            print("Syz suragan akparat zhok")
    except ValueError:
        print("Mandy durys berynyz")
    except MyError as mr:
        print(mr)
print("Всего книг: %d" % Book.emp_count)