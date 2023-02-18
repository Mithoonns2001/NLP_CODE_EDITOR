import openai

# Set up API key
with open("files/api.txt") as f:
    openai.api_key = f.read().strip()

# Recursive function to generate code
def generate_code(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=3000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    generated_code = response.choices[0].text
    return generated_code

# # Read input text from file
# with open('files/p3.txt', 'r') as file:
#     input_text = file.read()

# # Set up GPT-3 prompt
# prompt = f"{input_text}. generate more code for each file."

# # Generate code and write to file
# generated_code = generate_code(prompt)
# with open('files/p4.txt', 'w') as file:
#     file.write(generated_code)
