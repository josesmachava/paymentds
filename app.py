from flask import Flask
from flask import render_template
from flask import request

from paymentsds.mpesa import Client


app = Flask(__name__)





@app.route('/', methods=["GET", "POST"])
def index():
   if request.method == "POST":

      number = request.form["number"]
      amount = request.form["amount"]
      #print(amount, number)
      client = Client(
         api_key='fv9209jesuwbxhneoithqo6us7rukpu4',              # API Key
         public_key='MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAmptSWqV7cGUUJJhUBxsMLonux24u+FoTlrb+4Kgc6092JIszmI1QUoMohaDDXSVueXx6IXwYGsjjWY32HGXj1iQhkALXfObJ4DqXn5h6E8y5/xQYNAyd5bpN5Z8r892B6toGzZQVB7qtebH4apDjmvTi5FGZVjVYxalyyQkj4uQbbRQjgCkubSi45Xl4CGtLqZztsKssWz3mcKncgTnq3DHGYYEYiKq0xIj100LGbnvNz20Sgqmw/cH+Bua4GJsWYLEqf/h/yiMgiBbxFxsnwZl0im5vXDlwKPw+QnO2fscDhxZFAwV06bgG0oEoWm9FnjMsfvwm0rUNYFlZ+TOtCEhmhtFp+Tsx9jPCuOd5h2emGdSKD8A6jtwhNa7oQ8RtLEEqwAn44orENa1ibOkxMiiiFpmmJkwgZPOG/zMCjXIrrhDWTDUOZaPx/lEQoInJoE2i43VN/HTGCCw8dKQAwg0jsEXau5ixD0GUothqvuX3B9taoeoFAIvUPEq35YulprMM7ThdKodSHvhnwKG82dCsodRwY428kg2xM/UjiTENog4B6zzZfPhMxFlOSFX4MnrqkAS+8Jamhy1GgoHkEMrsT5+/ofjCx0HjKbT5NuA2V/lmzgJLl3jIERadLzuTYnKGWxVJcGLkWXlEPYLbiaKzbJb2sYxt+Kt5OxQqC1MCAwEAAQ==',           # Public Key
         service_provider_code='171717' # input_ServiceProviderCode
      )
      try:
         payment_data = {
            'to': number,         # input_CustomerMSISDN
            'reference': '111PA2D',      # input_ThirdPartyReference
            'transaction': 'T12344CC', # input_TransactionReference
            'amount': amount             # input_Amount
         }

         result = client.send(payment_data)
      except:
         print('Operation failed')
         
  
   return render_template('index.html')

