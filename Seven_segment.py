try:
    N = input('Enter a number:')
    Seven_segment = [['###','# #','# #','# #','###'], ['#','#','#','#','#'],
                     ['###','  #','###','#  ','###'], ['###','  #','###','  #','###'],
                     ['# #','# #','###','  #','  #'], ['###','#  ','###','  #','###'],
                     ['###','#  ','###','# #','###'], ['###','  #','  #','  #','  #'],
                     ['###','# #','###','# #','###'], ['###','# #','###','  #','###']]

    for i in range(5):
        for j in range(len(N)):
            print(Seven_segment[int(N[j])][i], end=' ')
        print()
except ValueError:
    print("Please enter a valid non negative and non decimal number")
    
        
