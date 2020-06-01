''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

class Error(Exception):
   """Base class for other exceptions"""
   pass

class GRTMemberER(Error):
   """Raised when the team member numbers are less or more"""
   pass

class OTMemberER(Error):
   """Raised when the opponent member numbers are less or more"""
   pass

class TestCaseER(Error):
   """Raised when the input value for test cases is zero"""
   pass

def main():
    try:
        T = int(input())
        if T == 0:
            raise TestCaseER
        else:
            i = 1
            while i <= T:
                N = int(input())
                GRT = [int(x) for x in input().split()]
                OT = [int(y) for y in input().split()]
                if len(GRT) != N:
                    raise GRTMemberER
                elif len(OT) != N:
                    raise OTMemberER

                GRT.sort()
                OT.sort()
                counter = 0
                j = 0
                k = 0

                while j < N:
                    if GRT[j] > OT[k]:
                        counter += 1
                        j += 1
                        k += 1
                    else:
                        j += 1
                        
                print(counter)
                i = i+1

    except TestCaseER:
        print("Please use minimum 1 test case.")
    except GRTMemberER:
        print("Please provide proper GR team members.")
    except OTMemberER:
        print("Please provide proper opponent team members.")
    except ValueError:
        print("Please provide numeric values in each input")      

main()

