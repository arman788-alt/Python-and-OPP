# # Class Composition. inheritance vs composition


# # inheritance vs composition
class CPU:
    def __init__(self, cores) -> None:
        self.cores = cores

class RAM:
    def __init__(self, size) -> None:
        self.size = size

class HardDrive:
    def __init__(self, capacity) -> None:
        self.capacity = capacity

# computer has a cpu
# computer has a ram
# computer has a hard drive
class Computer:
    def __init__(self, cores, ram_size, hd_capacity) -> None:
        self.cpu = CPU(cores)
        self.ram = RAM(ram_size)
        self.hard_disc = HardDrive(hd_capacity)
     

mac = Computer(8, 16, 512)
#print(mac.cpu) #error : <__main__.CPU object at 0x0000026532FD68A0>
# print(mac.cpu.cores)
# print(mac.ram.size)
# print(mac.hard_disc.capacity)





class CPU:
    def __init__(self, cores) -> None:
        self.cores = cores
    
    def __repr__(self) -> str:
        return f"CPU(cores={self.cores})"

class RAM:
    def __init__(self, size) -> None:
        self.size = size
    
    def __repr__(self) -> str:
        return f"RAM(size={self.size}GB)"

class HardDrive:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
    
    def __repr__(self) -> str:
        return f"HardDrive(capacity={self.capacity}GB)"

class Computer:
    def __init__(self, cores, ram_size, hd_capacity) -> None:
        self.cpu = CPU(cores)
        self.ram = RAM(ram_size)
        self.hard_disc = HardDrive(hd_capacity)
    
    def __repr__(self) -> str:
        return f"Computer(cpu={self.cpu}, ram={self.ram}, hard_disc={self.hard_disc})"

mac = Computer(8, 16, 512)

print(mac.ram)
print(mac)
