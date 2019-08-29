import hashlib

def looking_for_leading_zeros(text, zeros = 1):
  """

  Proof of Work concept.
  Iterating from NONCE 0, one by one until TEXT + str(NONCE) will hash to a specified
  number of zeros.
  """
  text = text + '0'
  zeros_str = '0'*zeros
  hash = hashlib.sha256(str.encode(text)).hexdigest()
  
  nonce = 1
  while hash[:zeros] != zeros_str:
    length = len(str(nonce - 1))
    text = text[:-length] + str(nonce)
    print(text)
    hash = hashlib.sha256(str.encode(text)).hexdigest()
    print('trying hash: %s' %hash)
    nonce = nonce + 1
  
  print('\ntook %d nonce \nto get the hash:%s\nwith %d leading zeros' %(nonce , hash, zeros))

looking_for_leading_zeros('abc', 1)
