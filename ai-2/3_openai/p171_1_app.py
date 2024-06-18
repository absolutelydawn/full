import openai
import json


def get_price_info(product_name):
  product_price = {"키보드":"3만원", "마우스":"2만원","모니터":"30만원"}


  price = product_price.get(product_name)
  if price == None:
    price = "해당 상품은 가격 정보가 없습니다."
 
  price_info = {
    "product_name":product_name,
    "price":price
  }


  return json.dumps(price_info)


def run_conversation(user_query):
  messages = [
    {"role": "user", "content": user_query}
  ]


  functions = [
    {
      "name": "get_price_info",
      "description": "Get price info",
      "parameters": {
        "type": "object",
        "properties": {
          "product_name": {
              "type": "string",
              "description": "Product name. for example 'keyboard', 'mouse'"
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


  response_messages = response["choices"][0]["message"]


  if response_messages.get("function_call"):
    function_args = json.loads(response_messages["function_call"]["arguments"])


    function_response = get_price_info(
      product_name = function_args.get("product_name")
    )


    messages.append(response_messages)
    messages.append(
      {
        "role": "function",
        "name": "get_price_info",
        "content": function_response
      }
    )


    second_response = openai.ChatCompletion.create(
      model = "gpt-3.5-turbo",
      messages = messages
    )
    return second_response


  return response_messages


user_query = "마우스의 가격은 얼마인가요?"
response_messages = run_conversation(user_query)
print(json.dumps(response_messages, ensure_ascii=False))
