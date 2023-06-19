def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

def Multi_wordDic(alpha_dic):
    multi=1
    for i in alpha_dic:
        multi*= fact(alpha_dic[i])
    return multi
    

def calculate_rank(word):
    word = word.upper()
    
    word_dic = {}
    word_set=list(set(list(word)))
    word_set.sort()
    
    for i in word:
        if i not in word_dic:
            word_dic[i] = 1
        else:
            word_dic[i] += 1
    
    rank = 1
    l = len(word)
    for i in range(l):
        for j in range(word_set.index(word[i])):
            word_dic[word_set[j]]-=1
            
            rank= rank+ fact(l-i-1)//Multi_wordDic(word_dic) 
            word_dic[word_set[j]]+=1
        word_dic[word[i]]-=1
        if (word_dic[word[i]]==0):
            word_set.remove(word[i])
    print("Rank:",int(rank))

if __name__ == "__main__":
    n=int(input())
    for i in range(n):
        word = input()
        calculate_rank(word)
