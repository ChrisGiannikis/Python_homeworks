import random

lt=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

letters = []
for i in range(10000):
    r = random.choice(lt)
    letters.append(r)

print letters
done2="False"
while done2 == "False":
    done="False"
    print "Dwse mia lexi me kefalaious xarakthres:"
    print "Gia telos grapse 'STOP' "
    word = raw_input()
    if word == "STOP":
        done2 = "True"

    for i in range(10000):
        if len(word) == 1:
            x = letters[i]
            lexi = ''.join(x)
            x2 = x
            lexi2 = ''.join(x2)
        if len(word) == 2:
            x = letters[i-1] + letters[i]
            lexi = ''.join(x)
            if i < 9900:
                x2 = letters[i-100] + letters[i]
                lexi2 = ''.join(x2)
        if len(word) == 3:
            x = letters[i-2] + letters[i-1] + letters[i]
            lexi = ''.join(x)
            if i < 9800:
                x2 = letters[i-200] + letters[i-100] + letters[i]
                lexi2 = ''.join(x2)
        if len(word) == 4:
            x = letters[i-3] + letters[i-2] + letters[i-1] + letters[i]
            lexi = ''.join(x)
            if i < 9700:
                x2 = letters[i-300] + letters[i-200] + letters[i-100] + letters[i]
                lexi2 = ''.join(x2)
        if len(word) == 5:
            x = letters[i-4] + letters[i-3] + letters[i-2] + letters[i-1] + letters[i]
            lexi = ''.join(x)
            if i < 9600:
                x2 = letters[i-400] + letters[i-300] + letters[i-200] + letters[i-100] + letters[i]
                lexi2 = ''.join(x2)
        if len(word) == 6:
            x = letters[i-5] + letters[i-4] + letters[i-3] + letters[i-2] + letters[i-1] + letters[i]
            lexi = ''.join(x)
            if i <9500:
                x2 = letters[i-500] + letters[i-400] + letters[i-300] + letters[i-200] + letters[i-100] + letters[i]
                lexi2 = ''.join(x2)
        if len(word) == 7:
            x = letters[i-6] + letters[i-5] + letters[i-4] + letters[i-3] + letters[i-2] + letters[i-1] + letters[i]
            lexi = ''.join(x)
            if i < 9400:
                x2 = letters[i-600] + letters[i-500] + letters[i-400] + letters[i-300] + letters[i-200] + letters[i-100] + letters[i]
                lexi2 = ''.join(x2)
        if len(word) == 8:
            x = letters[i-7] + letters[i-6] + letters[i-5] + letters[i-4] + letters[i-3] + letters[i-2] + letters[i-1] + letters[i]
            lexi = ''.join(x)
            if i < 9300:
                x2 = letters[i-700] + letters[i-600] + letters[i-500] + letters[i-400] + letters[i-300] + letters[i-200] + letters[i-100] + letters[i]
                lexi2 = ''.join(x2)
        if len(word) == 9:
            x = letters[i-8] + letters[i-7] + letters[i-6] + letters[i-5] + letters[i-4] + letters[i-3] + letters[i-2] + letters[i-1] + letters[i]
            lexi = ''.join(x)
            if i < 9200:
                x2 = letters[i-800] + letters[i-700] + letters[i-600] + letters[i-500] + letters[i-400] + letters[i-300] + letters[i-200] + letters[i-100] + letters[i]
                lexi2 = ''.join(x2)
        if len(word) == 10:
            x = letters[i-9] + letters[i-8] + letters[i-7] + letters[i-6] + letters[i-5] + letters[i-4] + letters[i-3] + letters[i-2] + letters[i-1] + letters[i]
            lexi = ''.join(x)
            if i < 9100:
                x2 = letters[i-900] + letters[i-800] + letters[i-700] + letters[i-600] + letters[i-500] + letters[i-400] + letters[i-300] + letters[i-200] + letters[i-100] + letters[i]
                lexi2 = ''.join(x2)
        if len(word) == 11:
            x = letters[i-10] + letters[i-9] + letters[i-8] + letters[i-7] + letters[i-6] + letters[i-5] + letters[i-4] + letters[i-3] + letters[i-2] + letters[i-1] + letters[i]
            lexi = ''.join(x)
            if i < 9000:
                x2 =letters[i-1000] + letters[i-900] + letters[i-800] + letters[i-700] + letters[i-600] + letters[i-500] + letters[i-400] + letters[i-300] + letters[i-200] + letters[i-100] + letters[i]
                lexi2 = ''.join(x2)
        if len(word) == 12:
            x = letters[i-11] + letters[i-10] + letters[i-9] + letters[i-8] + letters[i-7] + letters[i-6] + letters[i-5] + letters[i-4] + letters[i-3] + letters[i-2] + letters[i-1] + letters[i]
            lexi = ''.join(x)
            if i < 8900:
                x2 = letters[i-1100] + letters[i-1000] + letters[i-900] + letters[i-800] + letters[i-700] + letters[i-600] + letters[i-500] + letters[i-400] + letters[i-300] + letters[i-200] + letters[i-100] + letters[i]
                lexi2 = ''.join(x2)
        if len(word) == 13:
            x = letters[i-12] + letters[i-11] + letters[i-10] + letters[i-9] + letters[i-8] + letters[i-7] + letters[i-6] + letters[i-5] + letters[i-4] + letters[i-3] + letters[i-2] + letters[i-1] + letters[i]
            lexi = ''.join(x)
            if i < 8800:
                x2 = letters[i-1200] + letters[i-1100] + letters[i-1000] + letters[i-900] + letters[i-800] + letters[i-700] + letters[i-600] + letters[i-500] + letters[i-400] + letters[i-300] + letters[i-200] + letters[i-100] + letters[i]
                lexi2 = ''.join(x2)
        if len(word) == 14:
            x = letters[i-13] + letters[i-12] + letters[i-11] + letters[i-10] + letters[i-9] + letters[i-8] + letters[i-7] + letters[i-6] + letters[i-5] + letters[i-4] + letters[i-3] + letters[i-2] + letters[i-1] + letters[i]
            lexi = ''.join(x)
            if i < 8700:
                x2 = letters[i-1300] + letters[i-1200] + letters[i-1100] + letters[i-1000] + letters[i-900] + letters[i-800] + letters[i-700] + letters[i-600] + letters[i-500] + letters[i-400] + letters[i-300] + letters[i-200] + letters[i-100] + letters[i]
                lexi2 = ''.join(x2)
        if len(word) == 15:
            x = letters[i-14] + letters[i-13] + letters[i-12] + letters[i-11] + letters[i-10] + letters[i-9] + letters[i-8] + letters[i-7] + letters[i-6] + letters[i-5] + letters[i-4] + letters[i-3] + letters[i-2] + letters[i-1] + letters[i]
            lexi = ''.join(x)
            if i < 8600:
                x2 = letters[i-1400] + letters[i-1300] + letters[i-1200] + letters[i-1100] + letters[i-1000] + letters[i-900] + letters[i-800] + letters[i-700] + letters[i-600] + letters[i-500] + letters[i-400] + letters[i-300] + letters[i-200] + letters[i-100] + letters[i]
                lexi2 = ''.join(x2)

        if lexi == word or lexi2 == word :
            done = "True"

    if word != "STOP":
        if done == "True":
            print word
        else:
            print ""
            print "Den yparxei tetoia lexi \n"
