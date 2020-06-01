'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

class Error(Exception):
   """Base class for other exceptions"""
   pass

class RAINtimesCT(Error):
   """Raised when the team member numbers are less or more"""
   pass

class CLOTHtimeCT(Error):
   """Raised when the opponent member numbers are less or more"""
   pass

def main():
    try:
        N = [int(x) for x in input().split()]
        RAIN = [int(y) for y in input().split()]
        CLOTH = [int(z) for z in input().split()]
        nc = 0
        diff = 0
        i = 0
        cloths = CLOTH
        rain_ls = []
        for a, b in zip(RAIN[0::], RAIN[1::]):
            rain_ls.append(abs(a-b))
        print(rain_ls)
        rain_ls.sort(reverse=True)
        if len(RAIN) != N[0]:
            raise RAINtimesCT
        elif len(CLOTH) != N[1]:
            raise CLOTHtimeCT

        while i < N[2]:
            diff = rain_ls[0]
            rain_ls.pop(0)
            print(rain_ls)
            print(cloths)
            print(diff)
            print(nc)
            nc += len([j for j in cloths if j <= diff])
            cloths = list(filter(lambda x: x >= diff, cloths))
            i +=1
            if nc == N[1] or len(rain_ls) == 0:
                break
            else:
                continue
        
        print(nc)

    except RAINtimesCT:
        print("Please provide proper rain times.")
    except CLOTHtimeCT:
        print("Please provide proper cloths numbers.")
    except ValueError:
        print("Please provide numeric values in each input")      

main()
