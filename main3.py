from utils import number_generator, logger, multiplier, find_numbers, validate_email

# 🔥 Generator
print("Generator Output:")
for num in number_generator(5):
    print(num)

# 🔥 Closure
print("\nClosure Output:")
double = multiplier(2)
print("Double of 5:", double(5))

# 🔥 Decorator
@logger
def show_message():
    print("Hello from decorated function!")

print("\nDecorator Output:")
show_message()

# 🔥 Regex
print("\nRegex Output:")
text = "My numbers are 123 and 456"
print("Numbers found:", find_numbers(text))

email = "test@gmail.com"
print("Email valid:", validate_email(email))