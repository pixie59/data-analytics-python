import time
import random
sentences=["The quick brown fox jumps over the lazy dog.",
           "A journey of a thousand miles begins with a single step.",
           "I will dance till you ask me to dance"]

def typing_test():
    test_sentence=random.choice(sentences)
    print("Type the following sentence as fast as you can:")
    print(test_sentence)
    input("Press Enter when you are ready...")
    start_time=time.time()
    user_input=input("\Start typing: ")
    end_time=time.time()
    time_taken=end_time-start_time
    time_taken_in_minutes=time_taken/60
    word_count=len(user_input.split())
typing_test()
