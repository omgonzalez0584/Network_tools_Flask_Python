from flask import Flask, flash, url_for, redirect, render_template, request
import subprocess
import requests as req


app = Flask(__name__)

def ping_test(ip,repeat):
    p1 = subprocess.Popen(['ping',repeat,ip],stdout=subprocess.PIPE)
    output = p1.communicate()[0]
    output = output.decode('utf-8')
    lista_output = output.split('\n')
    print(lista_output)
    return lista_output


def traceroute_test(ip):
    t1 = subprocess.Popen(['traceroute',ip],stdout=subprocess.PIPE)
    output = t1.communicate()[0]
    output = output.decode('utf-8')
    lista_output = output.split('\n')
    print(lista_output)
    return lista_output


def nslookup_test(ip):
    ns = subprocess.Popen(['nslookup',ip],stdout=subprocess.PIPE)
    output = ns.communicate()[0]
    output = output.decode('utf-8')
    lista_output = output.split('\n')
    print(lista_output)
    return lista_output

def mac_address_api(mac):
    url='http://macvendors.co/api/' + mac
    r = req.get(url)
    print(r)
    dict = r.json()
    repo_dict = dict['result']
    lista_output = []

    for i in repo_dict.keys():
        lista_output.append(repo_dict[i])

    print(lista_output)
    return lista_output


@app.route('/')
def prueba():
    return render_template('principal.html')

@app.route('/ping/',methods=['GET','POST'])
def ping():
    if request.method == 'POST':
        ip = request.form['ip']
        repeat = request.form['repeat']
        rep = '-c ' + repeat
        ping = ping_test(ip,rep)
        return render_template('principal.html',ping=ping)

@app.route('/traceroute/',methods=['GET','POST'])
def traceroute():
    if request.method == 'POST':
        ip = request.form['ip']
        traceroute = traceroute_test(ip)
        return render_template('principal.html',traceroute=traceroute)

@app.route('/nslookup/', methods=['GET','POST'])
def nslookup():
    if request.method == 'POST':
        ip = request.form['ip']
        nslook_up = nslookup_test(ip)
        return render_template('principal.html', nslook_up=nslook_up)

@app.route('/mac_lookup/', methods=['GET','POST'])
def mac_address():
    if request.method == 'POST':
        mac = request.form['ip']
        mac_address = mac_address_api(mac)
        return render_template('principal.html', mac_address=mac_address)

@app.route('/subnetting/', methods=['GET','POST'])
def subnetting():
    if request.method == 'POST':
        return render_template('subnetting.html')
    else:
        return  render_template('subnetting.html')

@app.route('/awifi/', methods=['GET','POST'])
def awifi():
    if request.method == 'POST':
        return render_template('awifi.html')
    else:
        return render_template('awifi.html')

@app.route('/contacto/', methods=['GET','POST'])
def contacto():
    if request.method == 'POST':
        return render_template('contacto.html')
    else:
        return render_template('contacto.html')
