#  Understanding inner function and wrapper function
# function is a first class object
# function bitor theke fun return korte pari, abr function e parameter hisebee function pass korte pari.

def double_decker():
    print('starting the double decker')
    def inner_fun():
        print('inside the inner')
        return 3000
    return inner_fun #Note: function er bitor fun return korechi.

# print(double_decker())
# print(double_decker()()) 






def do_something(work1, work2):
    print('work started')
    #print(work1)
    work1() #Note: parameter hisebe function ashle, ei function e er bitor take call korte hole curley bracket dite hbe.
    work2()
    print('work ended')

# do_something(2)
# do_something('ami busy')
def coding():
    print('coding in python')

# do_something(coding)
def sleeping():
    print('sleeping and dreaming in python')

do_something(sleeping, coding) #Note: Parameter hisebe function pathaisi.