x = "incrível"

def myFunc():
  global x
  x = "inacreditável"
  y = "fantástico"
  global z
  z = "Seja Bem-Vindo"
  print("Python é " + x + " e " + y)

myFunc()

print("=" * 20)
print("Você é " + x)
print(z)
