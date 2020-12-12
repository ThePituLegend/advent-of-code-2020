class Console:
    def __init__(self, RAM):
        self.__RAM = RAM
        self.RESET(0)
    
    def __str__(self):
        return f"PC: {self.__PC} | ACC: {self.__ACC}"

    def nop(self, _):
        self.__PC += 1

    def acc(self, i):
        self.__ACC += int(i)
        self.__PC += 1
    
    def jmp(self, rel):
        self.__PC += int(rel)

    def RESET(self, addr):
        self.__PC = int(addr)
        self.__ACC = 0
        self.__history = []

    def __execute_PC(self):
        instr = getattr(self, self.__RAM[self.__PC][0])
        self.__history.append(self.__PC)
        instr(self.__RAM[self.__PC][1])

    def execute_RAM(self, addr=0):
        self.RESET(addr)
        while self.__PC not in self.__history:
            self.__execute_PC()
