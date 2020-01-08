from random import randint

class ArrayUtil:
    def generateSequenceArray(self, n):
        result = []
        for i in range(n):
            result.append(i)
        return result

    def generateRandomArray(self, n):
        result = self.generateSequenceArray(n)
        for i in range(n):
            r = randint(i,n-1)
            t = result[r]
            result[r] = result[i]
            result[i] = t
        return result

    def printList(self, list):
        print(list)

if __name__ == "__main__":
    util = ArrayUtil()
    list = util.generateSequenceArray(10)
    util.printList(list)
 
    list = util.generateRandomArray(10)
    util.printList(list)
