from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def start():
  return render_template('index.html')


@app.route('/<cpf>')
def verification(cpf):
  try:
    cpf = cpf.replace(".", "").replace("-", "")
  except:
    pass
    
  contador = 0
  contador2 = 10
  total = 0
  while contador < 9:
      total += int(cpf[contador]) * contador2
      contador2 -= 1
      contador += 1
  cpf_digito = total * 10 % 11
  
  total = 0
  contador = 0
  contador2 = 11
  while contador < 10:
      total += int(cpf[contador]) * contador2
      contador2 -= 1
      contador += 1
  cpf_digito2 = total * 10 % 11
  
  if cpf_digito >= 10:
      cpf_digito = 0
  if cpf_digito2 >= 10:
      cpf_digito2 = 0
    
  if len(set(cpf)) == 1:  
    validation = 'YOUR CPF IS NOT VALID!'
  elif cpf[9] == str(cpf_digito) and cpf[10] == str(cpf_digito2):
    validation = 'YOUR CPF IS VALID!'
  else:
     validation = 'YOUR CPF IS NOT VALID!'

    
  return jsonify({'Validation': validation})

  
app.run(host='0.0.0.0')
