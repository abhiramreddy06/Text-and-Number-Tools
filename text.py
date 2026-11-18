import string

def count_words(sentence):
    words = sentence.split()
    return len(words)

def find_longest_word(sentence):
    # Remove basic punctuation so it doesn't inflate word length
    cleaned = sentence.translate(str.maketrans('', '', string.punctuation))
    words = cleaned.split()
    if not words:
        return "None"
    return max(words, key=len)

def reverse_sentence(sentence):
    return sentence[::-1]

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    print("--- Text and Number Tools ---")
    
    # Text input and processing
    user_sentence = input("Enter a sentence: ")
    print("\n--- Text Results ---")
    print(f"Word Count: {count_words(user_sentence)}")
    print(f"Longest Word: {find_longest_word(user_sentence)}")
    print(f"Reversed Sentence: {reverse_sentence(user_sentence)}")
    
    # Number input and processing
    print("\n--- Number Results ---")
    try:
        user_number = int(input("Enter an integer to check if it is prime: "))
        prime_status = "Yes, it is prime." if is_prime(user_number) else "No, it is not prime."
        print(f"Prime Check ({user_number}): {prime_status}")
    except ValueError:
        print("Invalid input: Please enter a whole number.")

if __name__ == "__main__":
    main()
