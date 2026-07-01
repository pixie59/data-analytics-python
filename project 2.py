import time
import random
sentences=["The quick brown fox jumps over the lazy dog.",
           "A journey of a thousand miles begins with a single step.",
           "I will dance till you ask me to dance"]

def typing_test():
    test_sentence=random.choice(sentences)
    print("Type the following sentence as fast as you can:")
    print(test_sentence)
    input("\n Press Enter when you are ready...")
    start_time=time.time()
    user_input=input("\nStart typing: ")
    end_time=time.time()
    time_taken=end_time-start_time
    word_count=len(user_input.split())
    accuracy=sum(1 for a, b in zip(user_input, test_sentence) if a == b) / len(test_sentence) * 100
    word_accuracy = sum(1 for a, b in zip(user_input.split(), test_sentence.split()) if a == b) / len(test_sentence.split()) * 100
    print("\n Results:")
    print(f"Time taken: {time_taken} seconds")
    print(f"Words typed: {word_count}")
    print(f"Typing speed: {word_count/(time_taken/60):.2f} words per minute")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Word Accuracy: {word_accuracy:.2f}%")
typing_test()
