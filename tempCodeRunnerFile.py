
prompt = ChatPromptTemplate.from_template("Translate this from English to French:\n{input}")

# Define a Runnable (Chain) to connect prompt + LLM
translation_chain = prompt | model
