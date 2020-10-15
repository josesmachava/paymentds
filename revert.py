from paymentsds.mpesa import Client

client = Client(
   api_key='<REPLACE>',                # API Key
   public_key='<REPLACE>',             # Public Key
   service_provider_code='<REPLACE>',  # input_ServiceProviderCode
   initiatorIdentifier='<REPLACE>',    # input_InitiatorIdentifier,
   securityIdentifier='<REPLACE>'      # input_SecurityCredential
)

try:
   reversion_data = {
      'reference': '11114',      # input_ThirdPartyReference
      'transaction': 'T12344CC', # input_TransactionReference
      'amount': '10'             # input_ReversalAmount
   }

   result = client.revert(reversion_data)
except:
   # Handle success scenario