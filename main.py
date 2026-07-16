from LLM import generate_response

prompt = """
You are an expert digital marketing assistant.

Create a marketing campaign for the following product.

Product Name: Organic Green Tea

Return:

1. Product Description
2. Target Audience
3. Marketing Tagline
4. Social Media Caption
5. Email Marketing Subject
6. Call to Action
"""

response = generate_response(prompt)

print(response)