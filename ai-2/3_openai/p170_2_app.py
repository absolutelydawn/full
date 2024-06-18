import openai
import json
def get_price_info_temp(product_name):
    price_info = {
        "product_name" : product_name,
        "price" : "10,000"
    }

def run_conversation_temp(user_query):
    messages = [
        {"role" : "user", "content" : user_query}
    ]

    functions = [
        {
            "name": "get_price_info_temp",
            "description":"Get price info",
            "parameters": {
                "type":"object",
                "properties": {
                    "product_name" : {
                        "type": "string",
                        "description" : "Product name for example 'keyboard', 'mouse', 'monitor'"
                    }
                },
                "required": ["product_name"]
            }
        }
    ]

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages,
        functions = functions,
        function_call = "auto"
    )

    response_messages = response.choices[0]["message"]

    return response_messages

user_query = "키보드의 가격은 얼마인가요?"
response_messages = run_conversation_temp(user_query) 
print(json.dumps(response_messages, ensure_ascii=False))
print(response_messages["function_call"])

user_query = "키보드의 가격은 얼마인가요?"
response_messages = run_conversation_temp(user_query) 
print(json.dumps(response_messages, ensure_ascii=False))
print(response_messages["function_call"])

            