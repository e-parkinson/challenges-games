#27/08/15

def horizontalHistogram(alphabet, arrayOfScores):
    for i in range(0,len(arrayOfScores)):
        print(alphabet[i], end = " ")
        workingValue = arrayOfScores[i]
        #print(workingValue)
        workingValue = int(float(workingValue))
        print(workingValue * '*')

#main method
'''
print("Enter list of values in format [a,b,c,..]")
arrayOfScores[] = input()
'''
testArrayOfScores = [4,7,5,1]
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#based on relative frequency % from wikipedia
typicalEnglishLetterDistribution = [8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.056,2.758,0.978,2.361,0.150,1.974,0.074]
horizontalHistogram(alphabet, typicalEnglishLetterDistribution)
