import openai

openai.api_key = ""

def retriever_info(query):
    # Dummy implementation for example purposes
    return "about prime minister of india"

def rag_query(query):
    retrieved_info = retriever_info(query)  # Call to the retriever_info function
    augmented_prompt = f"User query: {query}. Retrieved information: {retrieved_info}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4o",  # Use the correct model
        messages=[
            {"role": "user", "content": augmented_prompt}
        ],
        max_tokens=150,
        temperature=0.7,
    )
    
    return response.choices[0].message['content'].strip()

# Example usage
query = "Tell me about the prime minister of india"
response = rag_query(query)
print(response)

