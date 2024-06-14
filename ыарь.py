#1
def payment(account: str, customer: list[dict]) -> dict :
     ii_price = 0
     for item in customer:
         ii_price += item['price'] * item['count']

     diff = int(account) - ii_price
     if diff >= 0 :
         return {
             "status": "success",
             "comment": "Покупки оплачены"
         }
     return {
         "status": "fail",
         "comment": f"Недостаточно средств. Внесите {-diff} сумму денег"
      }
lidl = [
     {'name': 'a','count': 2,'price':99 },
     {'name': 'a','count': 30,'price':10 },
     {'name': 'a','count': 9,'price':0 },
     {'name': 'a','count': 2,'price':1 },
]
print(payment('1000',lidl))
#2
def phone(nums: list) -> str:
    return "+{}{}{}({}{}){}{}{}{}{}{}{}".format(*nums)
print(phone(list(range(12))))