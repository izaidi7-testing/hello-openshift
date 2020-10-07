import os
import subprocess
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
	p = subprocess.Popen("/bin/bash -c 'source /opt/intel/openvino/bin/setupvars.sh; cd /opt/pneumonia-classification/application/; python3 pneumonia_classification.py -m ../resources/FP32/model.xml -o /opt/output'", shell=True) 
	p.wait()
	output = subprocess.check_output("cat /opt/output/stats.txt")
	return "Inference ran successfully "+ output

@app.route('/dont run')
def hello():
	return 'Inference is not running'

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080)
