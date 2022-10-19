import os

os.system('cls')

def main():
    while True:
        print("Welcome to the Riemann Zeta function summation tool.\n")
        print("The program performs a sum of (1/(n^k)).\n")
        kValue = input("Choose a 'k' value: ")
        numOfIterations = input("Choose an 'N' value: ")
        
        sumValue = 0
        count = 0
        while count < int(numOfIterations):
            count+=1
            #print("Sum Value:" + str(sumValue) + "| Count: " + str(count))
            sumValue = sumValue + (1/((count)**int(kValue)))
            #print("sumValue is " + str(sumValue)  + '\n')
        print("The value of the sum is: " + str(sumValue) + '\n')

if __name__ == "__main__":
    main()
