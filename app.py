from graph import app

product = input("Enter Product Name: ")
audience = input("Enter Target Audience: ")
tone = input("Enter Writing Tone: ")

user_data = {
    "product": product,
    "audience": audience,
    "tone": tone,
    "content": "",
    "keywords": "",
    "hashtags": "",
    "image_prompt": "",
    "final_content": ""
}

# Running the workflow
result = app.invoke(user_data)

print("\nGenerated LinkedIn Post:\n")
print(result["content"])

print("\nSEO Keywords & Hashtags:\n")
print(result["keywords"])

print("\nImage Prompt:\n")
print(result["image_prompt"])

print("\nFinal Reviewed Campaign:\n")
print(result["final_content"])