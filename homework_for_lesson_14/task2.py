# Task 2

# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function

# '''

def stop_words(stop_words):
    def decorator(func):
        def wrapper(*args):
            wrong_words=func(*args)
            if wrong_words == None:
                return "well, nothing works"
            for word in stop_words:
                wrong_words = wrong_words.replace(word, "*")
            return wrong_words
        return wrapper
    return decorator

        

 

@stop_words(['drinks', "pepsi", "BMW"])
def create_slogan(name: str) -> str:
    return(f"{name} drinks pepsi in his brand new BMW!")

 
print(create_slogan("Wow"))

# assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

