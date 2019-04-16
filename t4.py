import pickle

a = 99
b = '99'


with open('ser.text','wb') as f:
    pickle.dump(a,f)
    # pickle.dump(b,f)