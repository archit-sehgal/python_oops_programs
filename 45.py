class computation:
    def __init__(self):
        pass

    def Factorial(self, n):
        x = 1
        for i in range(1, n):
            x += x*i
        print(x)

    def Sum(self, n):
        totalSum = 0
        for i in range(1, n+1):
            totalSum += i
        print(totalSum)

    def testPrim(self, n):
        x = 0
        for i in range(1, n+1):
            if (n % i == 0):
                x += 1
        if x == 2:
            return "prime"
        else:
            return "Not Prime"

    def coPrime(self, n1, n2):
        isCoPrime = 0
        for i in range(1, n1+1):
            if (n1 % i == 0) and (n2 % i == 0):
                isCoPrime += 1
        if isCoPrime == 1:
            print("The numbers are Co-Prime")
        else:
            print("The numbers are not Co-Primes")

    def tableMult(self, n):
        for i in range(1, 11):
            print(f"{n} * {i} = {n*i}")

    def allTablesMult(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in numbers:
            print("---------------")
            for j in range(1, 11):
                print(f"{i} * {j} = {i*j}")
            print()

    def listDiv(self, n):
        Ldiv = []
        for i in range(1, n+1):
            if (n % i == 0):
                Ldiv.append(i)
        print(Ldiv)

    def listDivPrim(self, n):
        Ldiv = []
        for i in range(1, n+1):
            if self.testPrim(i) == "prime":
                Ldiv.append(i)
        print(Ldiv)


call = computation()
