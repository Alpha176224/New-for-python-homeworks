with open("sample.txt", "w+") as txt:
    txt.write(f'This is a simple file. This file, is for testing purposes. It is a test file.')
    txt.seek(0)
    data=txt.read()
cleaned_data_list=data.lower().replace('.', '').replace(',', '').split()
print(cleaned_data_list)
total_words=len(cleaned_data_list)
words_list=list(set(cleaned_data_list))
wordcount_list=list()
def word_counter(word,list):
    c=0
    while word in list:
        list.remove(word)
        c=c+1
    return c
for wrd in words_list:
    wordcount_list.append(word_counter(wrd,cleaned_data_list))
try:
    n=int(input("Enter how many top words do you want: "))
except ValueError:
    print('Value is not valid. Try to enter input correctly!')
print("Total words: ",total_words)
print(f"Top {n} common words:")
const=len(words_list)
words_list1=words_list.copy()
wordcount_list1=wordcount_list.copy()
k=1
while k <= min(n,const):
    m=max(set(wordcount_list))
    print(f'{words_list[wordcount_list.index(m)]} - {m} times')
    words_list.remove(words_list[wordcount_list.index(m)])
    wordcount_list.remove(m)
    k+=1
with open("word_count_report.txt",'w') as file:
    file.write(f"Word Count Report\nTotal Words: {total_words}\nTop {n} Words:")
with open("word_count_report.txt",'a') as file:
    k=1
    while k <= min(n,const):
        m=max(set(wordcount_list1))
        file.write(f'\n{words_list1[wordcount_list1.index(m)]} - {m}')
        words_list1.remove(words_list1[wordcount_list1.index(m)])
        wordcount_list1.remove(m)
        k+=1

                
