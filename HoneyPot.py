import socket
import threading,_thread
import time
from client_handler import *
#from command_simulation import switch_command
from colorama import Fore,Back,Style

#tail -f /proc/<pid>/fd/1

# ports- 20,21,22,23,25,53(U),67(u)68,69UDP,80,110,123(U),137-9(UDP),143,161-162(U),179,389(u),443,636(u),989,990

#Banner

banner='''
         _______ _       _______         _______ ________________
|\     /(  ___  ( (    /(  ____ |\     /(  ____ (  ___  \__   __/
| )   ( | (   ) |  \  ( | (    \( \   / | (    )| (   ) |  ) (   
| (___) | |   | |   \ | | (__    \ (_) /| (____)| |   | |  | |   
|  ___  | |   | | (\ \) |  __)    \   / |  _____| |   | |  | |   
| (   ) | |   | | | \   | (        ) (  | (     | |   | |  | |   
| )   ( | (___) | )  \  | (____/\  | |  | )     | (___) |  | |   
|/     \(_______|/    )_(_______/  \_/  |/      (_______)  )_(   
                                                                 '''


#print("\n")
print(Fore.LIGHTYELLOW_EX+banner)
print("\t\t\t\t\t\t\tVersion:1.0\n")
print(Style.RESET_ALL)
print(Fore.LIGHTRED_EX)
print("############  Help Manual  ############")
print("\nIf you want to log this session then please use script \ncommand below to record the entire session before running this script\n")
print("To Start recording:\nCommand: script -a session_log.txt\nAfter Exiting the honeypot please Exit the script first\nCommand: exit\n")
print("To exit the honeypot use Ctr+C command\n")
print("\n#####################################\n")
print(Style.RESET_ALL)
print(Fore.LIGHTGREEN_EX)
print("Now Starting the HoneyPot ! \n")
print("Please Wait...!\n")
time.sleep(4)

print("<-------- Below Services are started ----------->\n")
print(Style.RESET_ALL)
# --- main ---


# universal port opener

def Port25():
    port = 25

    sk = socket.socket()
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind(('127.0.0.1', port))
    print('SMTP started on port', port)
    sk.listen(5)

    try:
        while True:
            conn, addr = sk.accept()
            t = threading.Thread(target=client_handler25, args=(conn, addr,port))
            t.start()
    except KeyboardInterrupt as ex:
        print('KeyboardInterrupt')
        sk.close()
        print('Service closed on port', port)

########################

def Port53():
    port = 53

    sk = socket.socket()
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind(('127.0.0.1', port))
    print('Domain started on port', port)
    sk.listen(5)

    try:
        while True:
            conn, addr = sk.accept()
            t = threading.Thread(target=client_handler53, args=(conn, addr,port))
            t.start()
    except KeyboardInterrupt as ex:
        print('KeyboardInterrupt')
        sk.close()
        print('Service closed on port', port)






#########################


def Port80():
    port = 80

    sk = socket.socket()
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind(('127.0.0.1', port))
    print('http started on port', port)
    sk.listen(5)

    try:
        while True:
            conn, addr = sk.accept()
            t = threading.Thread(target=client_handler80, args=(conn, addr,port))
            t.start()
    except KeyboardInterrupt as ex:
        print('KeyboardInterrupt')
        sk.close()
        print('Service closed on port', port)



##########################


def Port110():
    port = 110

    sk = socket.socket()
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind(('127.0.0.1', port))
    print('POP3 started on port', port)
    sk.listen(5)

    try:
        while True:
            conn, addr = sk.accept()
            t = threading.Thread(target=client_handler110, args=(conn, addr,port))
            t.start()
    except KeyboardInterrupt as ex:
        print('KeyboardInterrupt')
        sk.close()
        print('Service closed on port', port)



############################


def Port111():
    port = 111

    sk = socket.socket()
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind(('127.0.0.1', port))
    print('RPC-Bind Service started on port', port)
    sk.listen(5)

    try:
        while True:
            conn, addr = sk.accept()
            t = threading.Thread(target=client_handler111, args=(conn, addr,port))
            t.start()
    except KeyboardInterrupt as ex:
        print('KeyboardInterrupt')
        sk.close()
        print('Service closed on port', port)





#########################

def Port135():
    port = 135

    sk = socket.socket()
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind(('127.0.0.1', port))
    print('MSRPC service started on port', port)
    sk.listen(5)

    try:
        while True:
            conn, addr = sk.accept()
            t = threading.Thread(target=client_handler135, args=(conn, addr,port))
            t.start()
    except KeyboardInterrupt as ex:
        print('KeyboardInterrupt')
        sk.close()
        print('Service closed on port', port)



#######################

def Port139():
    port = 139

    sk = socket.socket()
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind(('127.0.0.1', port))
    print('NetBios-ssn Service started on port', port)
    sk.listen(5)

    try:
        while True:
            conn, addr = sk.accept()
            t = threading.Thread(target=client_handler139, args=(conn, addr,port))
            t.start()
    except KeyboardInterrupt as ex:
        print('KeyboardInterrupt')
        sk.close()
        print('Service closed on port', port)




#########################

def Port143():
    port = 143

    sk = socket.socket()
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind(('127.0.0.1', port))
    print('imap Service started on port', port)
    sk.listen(5)

    try:
        while True:
            conn, addr = sk.accept()
            t = threading.Thread(target=client_handler143, args=(conn, addr,port))
            t.start()
    except KeyboardInterrupt as ex:
        print('KeyboardInterrupt')
        sk.close()
        print('Service closed on port', port)





####################


def Port443():
    port = 443

    sk = socket.socket()
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind(('127.0.0.1', port))
    print('https Service started on port', port)
    sk.listen(5)

    try:
        while True:
            conn, addr = sk.accept()
            t = threading.Thread(target=client_handler443, args=(conn, addr,port))
            t.start()
    except KeyboardInterrupt as ex:
        print('KeyboardInterrupt')
        sk.close()
        print('Service closed on port', port)




####################

def Port445():
    port = 445

    sk = socket.socket()
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind(('127.0.0.1', port))
    print('Microsoft-ds Service started on port', port)
    sk.listen(5)

    try:
        while True:
            conn, addr = sk.accept()
            t = threading.Thread(target=client_handler445, args=(conn, addr,port))
            t.start()
    except KeyboardInterrupt as ex:
        print('KeyboardInterrupt')
        sk.close()
        print('Service closed on port', port)




####################

def Port993():
    port = 993

    sk = socket.socket()
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind(('127.0.0.1', port))
    print('IMAPS Service started on port', port)
    sk.listen(5)

    try:
        while True:
            conn, addr = sk.accept()
            t = threading.Thread(target=client_handler993, args=(conn, addr,port))
            t.start()
    except KeyboardInterrupt as ex:
        print('KeyboardInterrupt')
        sk.close()
        print('Service closed on port', port)




###################

def Port995():
    port = 995

    sk = socket.socket()
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind(('127.0.0.1', port))
    print('POP3s Service started on port', port)
    sk.listen(5)

    try:
        while True:
            conn, addr = sk.accept()
            t = threading.Thread(target=client_handler995, args=(conn, addr,port))
            t.start()
    except KeyboardInterrupt as ex:
        print('KeyboardInterrupt')
        sk.close()
        print('Service closed on port', port)


############

def Port1723():
    port = 1723

    sk = socket.socket()
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind(('127.0.0.1', port))
    print('PPTP Service started on port', port)
    sk.listen(5)

    try:
        while True:
            conn, addr = sk.accept()
            t = threading.Thread(target=client_handler1723, args=(conn, addr,port))
            t.start()
    except KeyboardInterrupt as ex:
        print('KeyboardInterrupt')
        sk.close()
        print('Service closed on port', port)



##########################


def Port3306():
    port = 3306

    sk = socket.socket()
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind(('127.0.0.1', port))
    print('MYSQL Service started on port', port)
    sk.listen(5)

    try:
        while True:
            conn, addr = sk.accept()
            t = threading.Thread(target=client_handler3306, args=(conn, addr,port))
            t.start()
    except KeyboardInterrupt as ex:
        print('KeyboardInterrupt')
        sk.close()
        print('Service closed on port', port)



##########################

def Port3389():
    port = 3389

    sk = socket.socket()
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind(('127.0.0.1', port))
    print('MS-WBT Service started on port', port)
    sk.listen(5)

    try:
        while True:
            conn, addr = sk.accept()
            t = threading.Thread(target=client_handler3389, args=(conn, addr,port))
            t.start()
    except KeyboardInterrupt as ex:
        print('KeyboardInterrupt')
        sk.close()
        print('Service closed on port', port)



#####################

def Port5900():
    port = 5900

    sk = socket.socket()
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind(('127.0.0.1', port))
    print('VNC Service started on port', port)
    sk.listen(5)

    try:
        while True:
            conn, addr = sk.accept()
            t = threading.Thread(target=client_handler5900, args=(conn, addr,port))
            t.start()
    except KeyboardInterrupt as ex:
        print('KeyboardInterrupt')
        sk.close()
        print('Service closed on port', port)


##################

def Port8080():
    port = 8080

    sk = socket.socket()
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind(('127.0.0.1', port))
    print('HTTP-Proxy Service started on port', port)
    sk.listen(5)

    try:
        while True:
            conn, addr = sk.accept()
            t = threading.Thread(target=client_handler8080, args=(conn, addr,port))
            t.start()
    except KeyboardInterrupt as ex:
        print('KeyboardInterrupt')
        sk.close()
        print('Service closed on port', port)



##############



def Port23():
    port = 23

    sk = socket.socket()
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind(('127.0.0.1', port))
    print('Telnet Service started on port', port)
    sk.listen(5)

    try:
        while True:
            conn, addr = sk.accept()
            
            t = threading.Thread(target=client_handler23, args=(conn, addr,port))
            t.start()
    except KeyboardInterrupt as ex:
        print('KeyboardInterrupt')
        sk.close()
        print('Telnet Service closed on port', port)

def Port22():
    port = 22

    sk = socket.socket()
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind(('127.0.0.1', port))
    print('SSH Service started on port', port)
    sk.listen(5)

    try:
        while True:
            conn, addr = sk.accept()
            t = threading.Thread(target=client_handler22, args=(conn, addr,port))
            t.start()
    except KeyboardInterrupt as ex:
        print('KeyboardInterrupt')
        sk.close()
        print('SSH Service closed on port', port)


def Port21():
    port = 21

    sk = socket.socket()
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind(('127.0.0.1', port))
    print('FTP Service started on port', port)
    sk.listen(5)

    try:
        while True:
            conn, addr = sk.accept()
            t = threading.Thread(target=client_handler21, args=(conn, addr,port))
            t.start()
    except KeyboardInterrupt as ex:
        print('KeyboardInterrupt')
        sk.close()
        print('FTP Service closed on port', port)





try:
        _thread.start_new_thread(Port23,())
        _thread.start_new_thread(Port22,())
        _thread.start_new_thread(Port21,())
        _thread.start_new_thread(Port25,())
        _thread.start_new_thread(Port53,())
        _thread.start_new_thread(Port80,())
        _thread.start_new_thread(Port110,())
        _thread.start_new_thread(Port111,())
        _thread.start_new_thread(Port135,())
        _thread.start_new_thread(Port139,())
        _thread.start_new_thread(Port143,())
        _thread.start_new_thread(Port443,())
        _thread.start_new_thread(Port445,())
        _thread.start_new_thread(Port993,())
        _thread.start_new_thread(Port995,())
        _thread.start_new_thread(Port1723,())
        _thread.start_new_thread(Port3306,())
        _thread.start_new_thread(Port3389,())
        _thread.start_new_thread(Port5900,())
        _thread.start_new_thread(Port8080,())
        
       

except:
        pass
while 1:
        time.sleep(1)
        pass

