import openai

# Set up API key
with open("api.txt") as f:
    openai.api_key = f.read().strip()

# Recursive function to generate code
def generate_code(input_text):
    prompt = f"{input_text} generate code for each file"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=3000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    generated_code = response.choices[0].text
    return generated_code + generate_code(input_text)

# # Read input text from file
# with open('p3.txt', 'r') as file:
#     input_text = file.read()

# # Generate code using recursion
# generated_code = generate_code(input_text)

# # Write generated code to file
# with open('p4.txt', 'w') as file:
#     file.write(generated_code)


# import openai

# # Set up API key

# with open("api.txt") as f:
#     openai.api_key = f.read().strip()

# # Read input text from file
# with open('p3.txt', 'r') as file:
#     input_text = file.read()

# # Set up GPT-3 prompt
# prompt = f"{input_text}. generate code for each file"



# # Generate code using GPT-3 API
# response = openai.Completion.create(
#   engine="text-davinci-003",
#   prompt=prompt,
#   max_tokens=3000,
#   n=1,
#   stop=None,
#   temperature=0.5,
# )

# generated_code = response.choices[0].text

# # Write generated code to file
# with open('p4.txt', 'w') as file:
#     file.write(generated_code)
