#import this

#====Variables and Some Arithmetic====
a = 961
b = 909
result = a*a + b*b
print(result)

#====Strings and Lists====
startpos1 = 82
endpos1 = 91
startpos2 = 152
endpos2 = 159

string = "qjfDvJnLZPcWTkfcdfYjXyrS5uq9ADzyWNBY8yRg78MgbPvlbt3VM0vHVbAkFJSptsK5GPNA6SnhcWFRTuThelodermaRKLJMchAcdS0tntPRqJ0uEQkx5CrIXdGgQj3c4PxOIeQiiGhivvc9TKgfdGWoenantheVl5OvERpz3Et."

print(f'{string[startpos1:endpos1+1]} {string[startpos2:endpos2+1]}')

#====Conditions and Loops====
x=4988
y=9228

summation = sum([x for x in range(x, y+1) if x % 2 != 0])

print(summation)

#====Working with Files====
outputFile = []

with open('input.txt', 'r') as f:
    outputFile = [line for pos, line in enumerate(
        f.readlines()) if pos % 2 != 0]
    
#print(outputFile)

with open('out.txt', 'w') as f:
    f.write(''.join([line for line in outputFile]))


#====Dictionaries====
txtStr = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

wordCountDict = {}

for word in txtStr.split(' '):
    if word in wordCountDict:
        wordCountDict[word] += 1
    else:
        wordCountDict[word] = 1

for key,value in wordCountDict.items():
    print(key, value)