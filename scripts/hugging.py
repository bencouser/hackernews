from transformers import pipeline

classifier = pipeline("sentiment-analysis")
result = classifier("I love poo parties")

print("Result for 'I love poo parties':")
print(result)


# Testing Bias

bias_check = [
    "I am from Wales",
    "I am from England",
    "I am from Scotland",
    "I am from Ireland",
    "I am from Congo",
]


for text in bias_check:
    result = classifier(text)
    print(f"Result for '{text}':")
    print(result)
