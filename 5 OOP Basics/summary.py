class Book: 
    def __init__(self, name) -> None:
        self.name = name
    def read(self):
        raise NotImplementedError

class Physics(Book):
    def __init__(self, name, lab) -> None:
        self.lab = lab
        super().__init__(name) 
    def read(self):
        print('reading physics vector chapter')

topon = Physics('topon', True)

print(issubclass(Physics, Book)) #check korbo.. physics(child class) er parent class book kinaaa...sotti hole true dibee...mithaa bole false dibee
print(isinstance(topon, Physics)) #cheeck korbo topon ki physics class er instence kinaa ..orthat physics class theke toiri hoisee kina? hoile true dibe
print(isinstance(topon, Book)) 

topon.read()