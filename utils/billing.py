from models.list import model_list
from config import balance, default_money

class billing:
    async def cost(model, input_token, output_token):
        input_cost = float(model_list[model]["cost"]["input"])
        output_cost = float(model_list[model]["cost"]["output"])

        final_cost = (input_cost * input_token + output_cost * output_token)/1000000 * 33
    
        return final_cost
    
    class balance:
        async def get(user):
            if user not in balance:
                balance[user] = default_money
                return default_money
            return balance[user]
        
        async def set(user, amount):
            if user == "*":
                for user in balance:
                    balance[user] = amount
                    return "OK"
            if user not in balance:
                balance[user] = amount
            else:
                balance[user] = amount
            return balance[user]
        
        async def add(user, amount):
            if user == "*":
                for user in balance:
                    balance[user] += amount
                    return "OK"
            if user not in balance:
                balance[user] = amount
            else:
                balance[user] += amount
            return balance[user]