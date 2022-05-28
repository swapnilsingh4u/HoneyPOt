
import socket
import threading,_thread
import time
#from colorama import Fore,Back,Style



# Commands

def switch_TelnetCommand(conn,command_input):
    if(command_input.strip() == 'ls'):
        conn.send(b"bin\tcdrom\tetc\tlib64\tmedia\topt\troot\tsbin\tsys\t\nusr\tboot\tdev\thome\tlib\tmnt\tproc\nvar\ttmp\n")
    elif (command_input.strip()=='ifconfig'):
        conn.send(b"eth0\tLink encap:Ethernet  HWaddr 00:5b:b0:40:2e:04\n\tinet addr:192.168.0.106  Bcast:192.168.0.255  Mask:255.255.255.0\n\tinet6 addr: fe80::44d4:cca1:3bc3:3621/64 Scope:Link\n\tUP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1\n\tRX packets:12479620 errors:0 dropped:0 overruns:0 frame:0\n\tTX packets:7361695 errors:0 dropped:0 overruns:0 carrier:0\n\tcollisions:0 txqueuelen:1000\n\tRX bytes:15862454952 (15.8 GB)  TX bytes:1542073590 (1.5 GB)\n")
    elif(command_input.strip() == 'id'):
        conn.send(b"uid=1000(root) gid=1000(root) groups=1000(root)\n")
    elif(command_input.strip() == 'uname -a'):
        conn.send(b"Linux rooted 4.10.0-38-generic #42~16.04.1-Ubuntu SMP Tue Oct 10 16:32:20 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux\n")
    elif(command_input.strip() == 'cat /etc/passwd'):
        conn.send(b"root:x:0:0:root:/root:/bin/bash\n")
    elif(command_input.strip() == 'ping localhost'):
        conn.send(b"PING localhost (127.0.0.1) 56(84) bytes of data.\n64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.042 ms\n64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.042 ms\n64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.042 ms\n64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.042 ms\n64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.042 ms\n\n--- localhost ping statistics ---\n5 packets transmitted, 5 received, 0% packet loss, time 4103ms\nrtt min/avg/max/mdev = 0.042/0.055/0.061/0.008 ms\n")
    elif(command_input.strip() == 'whoami'):
        conn.send(b"root\n")
    else:
        conn.send(b" Command Not found\n")


def switch_FtpCommand(conn,command_input):
    if(command_input.strip() == 'help'):
        conn.send(b"!\t\tdir(\tmdeleteqcsite\n$\t\tdisconnectmdirsendportsize\naccount\t\texitmgetputstatus\nappendformmkdirpwdstruct\nascii(\tgetattr(\tmlsquitsystem\nbellglobmodequotesunique\nbinaryhashmodtimerecvtenex\nbyehelpmputregettick\ncaseidlenewerrstatustrace\ncdimagenmaprhelptype\ncdupipanynlistrenameuser\nchmodipv4ntransresetumask\ncloseipv6openrestartverbose\ncredits(\tlcdpromptrmdir?\ndeletelspassiverunique\ndebugmacdefproxysend\n")
    else:
        conn.send(b" Command Not found\n")


########################################

def client_handler25(conn, addr,port):

    try:
        #print(Fore.LIGHTGREEN_EX)
        print('\n\n******* Service Accessed *********\n----------------------------------------------\nRemote Host IP: ',addr[0],'connected with us on Port:',port)
        #send the welcome msg to client
        #print(Style.RESET_ALL)
        conn.send(b"Welcome to the Server:\n\nUsername: ")
        count=0
        f.close()
        try:
            while count<3:
                data = conn.recv(100)
            
                if not data: 
                    print('Connection exit by the Host:', addr[0],"on Port", addr[1])
                    print("---------------------------------------------------------")
                    break
            
                #send the username dialog to client
                print("Username input: ",data.decode("utf-8"),end='')
                #data = conn.recv(100)
                conn.send(b"Password: ")
                data = conn.recv(100)
                print('Password input: ',data.decode("utf-8"),end='')
                count=count+1
                if count==2:
                    conn.send(b"Wrong Password Try again\n")
                else:
                    conn.send(b"Wrong Password Try again\nUsername: ")
                #count=count+1
                if(count==2):
                    print('Host ',addr[0],' Logged into the fake server')
                    conn.send(b"Welcome to the admin Server\n")
                    while True:
                        conn.send(b"root@Server~#: ")
                        #print('Command Input : ',data)
                        data=conn.recv(100)
                        ############################################################################
                        # Command controls --------
                        command = str(data.decode('utf-8'))
                        switch_TelnetCommand(conn,command)
                        # -------------------------
                        ############################################################################
                        #switch_command(conn,data)
                        print("System Command from ",addr[0],"@:Server# ",data.decode("utf-8"),end='')
                #print('Incoming Data: ',data,' From Host: ',addr[0],' on Port',port)
                #conn.send(b"Wrong Password Try again\n")
        except Exception as ex:
            #print('Exception:', addr[0], addr[1], ex)
            print("\nConnection reset by the Host: ",addr[0],addr[1])
            print("---------------------------------------------------------")
        finally:
            #print('close:', addr[0], addr[1])
            #print("\n\n****** Telnet Connection Closed by the Host: ",addr[0]," **********\n\n")
            conn.close()
    except Exception as ex:
        print("Connection reset by the Host: ",addr[0]," on Port",addr[1])
        print("----------------------------------------------------------")
        conn.close()


#######################################

def client_handler53(conn, addr,port):
    try:
        
        print('\n\n******* Service Accessed *********\n----------------------------------------------\nRemote Host IP: ',addr[0],'connected with us on Port:',port)
        #send the welcome msg to client
        conn.send(b"Welcome to the Server:\n\nUsername: ")
        count=0
        try:
            while count<3:
                data = conn.recv(100)
            
                if not data: 
                    print('Connection exit by the Host:', addr[0],"on Port", addr[1])
                    print("---------------------------------------------------------")
                    break
            
                #send the username dialog to client
                print("Username input: ",data.decode("utf-8"),end='')
                #data = conn.recv(100)
                conn.send(b"Password: ")
                data = conn.recv(100)
                print('Password input: ',data.decode("utf-8"),end='')
                count=count+1
                if count==2:
                    conn.send(b"Wrong Password Try again\n")
                else:
                    conn.send(b"Wrong Password Try again\nUsername: ")
                #count=count+1
                if(count==2):
                    print('Host ',addr[0],' Logged into the fake server')
                    conn.send(b"Welcome to the admin Server\n")
                    while True:
                        conn.send(b"root@Server~#: ")
                        #print('Command Input : ',data)
                        data=conn.recv(100)
                        ############################################################################
                        # Command controls --------
                        command = str(data.decode('utf-8'))
                        switch_TelnetCommand(conn,command)
                        # -------------------------
                        ############################################################################
                        #switch_command(conn,data)
                        print("System Command from ",addr[0],"@:Server# ",data.decode("utf-8"),end='')
                #print('Incoming Data: ',data,' From Host: ',addr[0],' on Port',port)
                #conn.send(b"Wrong Password Try again\n")
        except Exception as ex:
            #print('Exception:', addr[0], addr[1], ex)
            print("\nConnection reset by the Host: ",addr[0],addr[1])
            print("---------------------------------------------------------")
        finally:
            #print('close:', addr[0], addr[1])
            #print("\n\n****** Telnet Connection Closed by the Host: ",addr[0]," **********\n\n")
            conn.close()
    except Exception as ex:
        print("Connection reset by the Host: ",addr[0]," on Port",addr[1])
        print("----------------------------------------------------------")
        conn.close()



########################################


def client_handler80(conn, addr,port):
    try:
        print('\n\n******* Service Accessed *********\n----------------------------------------------\nRemote Host IP: ',addr[0],'connected with us on Port:',port)
        #send the welcome msg to client
        conn.send(b"Welcome to the Server:\n\nUsername: ")
        count=0
        try:
            while count<3:
                data = conn.recv(100)
            
                if not data: 
                    print('Connection exit by the Host:', addr[0],"on Port", addr[1])
                    print("---------------------------------------------------------")
                    break
            
                #send the username dialog to client
                print("Username input: ",data.decode("utf-8"),end='')
                #data = conn.recv(100)
                conn.send(b"Password: ")
                data = conn.recv(100)
                print('Password input: ',data.decode("utf-8"),end='')
                count=count+1
                if count==2:
                    conn.send(b"Wrong Password Try again\n")
                else:
                    conn.send(b"Wrong Password Try again\nUsername: ")
                #count=count+1
                if(count==2):
                    print('Host ',addr[0],' Logged into the fake server')
                    conn.send(b"Welcome to the admin Server\n")
                    while True:
                        conn.send(b"root@Server~#: ")
                        #print('Command Input : ',data)
                        data=conn.recv(100)
                        ############################################################################
                        # Command controls --------
                        command = str(data.decode('utf-8'))
                        switch_TelnetCommand(conn,command)
                        # -------------------------
                        ############################################################################
                        #switch_command(conn,data)
                        print("System Command from ",addr[0],"@:Server# ",data.decode("utf-8"),end='')
                #print('Incoming Data: ',data,' From Host: ',addr[0],' on Port',port)
                #conn.send(b"Wrong Password Try again\n")
        except Exception as ex:
            #print('Exception:', addr[0], addr[1], ex)
            print("\nConnection reset by the Host: ",addr[0],addr[1])
            print("---------------------------------------------------------")
        finally:
            #print('close:', addr[0], addr[1])
            #print("\n\n****** Telnet Connection Closed by the Host: ",addr[0]," **********\n\n")
            conn.close()
    except Exception as ex:
        print("Connection reset by the Host: ",addr[0]," on Port",addr[1])
        print("----------------------------------------------------------")
        conn.close()





########################################

def client_handler110(conn, addr,port):
    try:
        print('\n\n******* Service Accessed *********\n----------------------------------------------\nRemote Host IP: ',addr[0],'connected with us on Port:',port)
        #send the welcome msg to client
        conn.send(b"Welcome to the Server:\n\nUsername: ")
        count=0
        try:
            while count<3:
                data = conn.recv(100)
            
                if not data: 
                    print('Connection exit by the Host:', addr[0],"on Port", addr[1])
                    print("---------------------------------------------------------")
                    break
            
                #send the username dialog to client
                print("Username input: ",data.decode("utf-8"),end='')
                #data = conn.recv(100)
                conn.send(b"Password: ")
                data = conn.recv(100)
                print('Password input: ',data.decode("utf-8"),end='')
                count=count+1
                if count==2:
                    conn.send(b"Wrong Password Try again\n")
                else:
                    conn.send(b"Wrong Password Try again\nUsername: ")
                #count=count+1
                if(count==2):
                    print('Host ',addr[0],' Logged into the fake server')
                    conn.send(b"Welcome to the admin Server\n")
                    while True:
                        conn.send(b"root@Server~#: ")
                        #print('Command Input : ',data)
                        data=conn.recv(100)
                        ############################################################################
                        # Command controls --------
                        command = str(data.decode('utf-8'))
                        switch_TelnetCommand(conn,command)
                        # -------------------------
                        ############################################################################
                        #switch_command(conn,data)
                        print("System Command from ",addr[0],"@:Server# ",data.decode("utf-8"),end='')
                #print('Incoming Data: ',data,' From Host: ',addr[0],' on Port',port)
                #conn.send(b"Wrong Password Try again\n")
        except Exception as ex:
            #print('Exception:', addr[0], addr[1], ex)
            print("\nConnection reset by the Host: ",addr[0],addr[1])
            print("---------------------------------------------------------")
        finally:
            #print('close:', addr[0], addr[1])
            #print("\n\n****** Telnet Connection Closed by the Host: ",addr[0]," **********\n\n")
            conn.close()
    except Exception as ex:
        print("Connection reset by the Host: ",addr[0]," on Port",addr[1])
        print("----------------------------------------------------------")
        conn.close()





######################################


def client_handler111(conn, addr,port):
    try:
        print('\n\n******* Service Accessed *********\n----------------------------------------------\nRemote Host IP: ',addr[0],'connected with us on Port:',port)
        #send the welcome msg to client
        conn.send(b"Welcome to the Server:\n\nUsername: ")
        count=0
        try:
            while count<3:
                data = conn.recv(100)
            
                if not data: 
                    print('Connection exit by the Host:', addr[0],"on Port", addr[1])
                    print("---------------------------------------------------------")
                    break
            
                #send the username dialog to client
                print("Username input: ",data.decode("utf-8"),end='')
                #data = conn.recv(100)
                conn.send(b"Password: ")
                data = conn.recv(100)
                print('Password input: ',data.decode("utf-8"),end='')
                count=count+1
                if count==2:
                    conn.send(b"Wrong Password Try again\n")
                else:
                    conn.send(b"Wrong Password Try again\nUsername: ")
                #count=count+1
                if(count==2):
                    print('Host ',addr[0],' Logged into the fake server')
                    conn.send(b"Welcome to the admin Server\n")
                    while True:
                        conn.send(b"root@Server~#: ")
                        #print('Command Input : ',data)
                        data=conn.recv(100)
                        ############################################################################
                        # Command controls --------
                        command = str(data.decode('utf-8'))
                        switch_TelnetCommand(conn,command)
                        # -------------------------
                        ############################################################################
                        #switch_command(conn,data)
                        print("System Command from ",addr[0],"@:Server# ",data.decode("utf-8"),end='')
                #print('Incoming Data: ',data,' From Host: ',addr[0],' on Port',port)
                #conn.send(b"Wrong Password Try again\n")
        except Exception as ex:
            #print('Exception:', addr[0], addr[1], ex)
            print("\nConnection reset by the Host: ",addr[0],addr[1])
            print("---------------------------------------------------------")
        finally:
            #print('close:', addr[0], addr[1])
            #print("\n\n****** Telnet Connection Closed by the Host: ",addr[0]," **********\n\n")
            conn.close()
    except Exception as ex:
        print("Connection reset by the Host: ",addr[0]," on Port",addr[1])
        print("----------------------------------------------------------")
        conn.close()



######################################


def client_handler135(conn, addr,port):
    try:
        print('\n\n******* Service Accessed *********\n----------------------------------------------\nRemote Host IP: ',addr[0],'connected with us on Port:',port)
        #send the welcome msg to client
        conn.send(b"Welcome to the Server:\n\nUsername: ")
        count=0
        try:
            while count<3:
                data = conn.recv(100)
            
                if not data: 
                    print('Connection exit by the Host:', addr[0],"on Port", addr[1])
                    print("---------------------------------------------------------")
                    break
            
                #send the username dialog to client
                print("Username input: ",data.decode("utf-8"),end='')
                #data = conn.recv(100)
                conn.send(b"Password: ")
                data = conn.recv(100)
                print('Password input: ',data.decode("utf-8"),end='')
                count=count+1
                if count==2:
                    conn.send(b"Wrong Password Try again\n")
                else:
                    conn.send(b"Wrong Password Try again\nUsername: ")
                #count=count+1
                if(count==2):
                    print('Host ',addr[0],' Logged into the fake server')
                    conn.send(b"Welcome to the admin Server\n")
                    while True:
                        conn.send(b"root@Server~#: ")
                        #print('Command Input : ',data)
                        data=conn.recv(100)
                        ############################################################################
                        # Command controls --------
                        command = str(data.decode('utf-8'))
                        switch_TelnetCommand(conn,command)
                        # -------------------------
                        ############################################################################
                        #switch_command(conn,data)
                        print("System Command from ",addr[0],"@:Server# ",data.decode("utf-8"),end='')
                #print('Incoming Data: ',data,' From Host: ',addr[0],' on Port',port)
                #conn.send(b"Wrong Password Try again\n")
        except Exception as ex:
            #print('Exception:', addr[0], addr[1], ex)
            print("\nConnection reset by the Host: ",addr[0],addr[1])
            print("---------------------------------------------------------")
        finally:
            #print('close:', addr[0], addr[1])
            #print("\n\n****** Telnet Connection Closed by the Host: ",addr[0]," **********\n\n")
            conn.close()
    except Exception as ex:
        print("Connection reset by the Host: ",addr[0]," on Port",addr[1])
        print("----------------------------------------------------------")
        conn.close()




#####################################

def client_handler139(conn, addr,port):
    try:
        print('\n\n******* Service Accessed *********\n----------------------------------------------\nRemote Host IP: ',addr[0],'connected with us on Port:',port)
        #send the welcome msg to client
        conn.send(b"Welcome to the Server:\n\nUsername: ")
        count=0
        try:
            while count<3:
                data = conn.recv(100)
            
                if not data: 
                    print('Connection exit by the Host:', addr[0],"on Port", addr[1])
                    print("---------------------------------------------------------")
                    break
            
                #send the username dialog to client
                print("Username input: ",data.decode("utf-8"),end='')
                #data = conn.recv(100)
                conn.send(b"Password: ")
                data = conn.recv(100)
                print('Password input: ',data.decode("utf-8"),end='')
                count=count+1
                if count==2:
                    conn.send(b"Wrong Password Try again\n")
                else:
                    conn.send(b"Wrong Password Try again\nUsername: ")
                #count=count+1
                if(count==2):
                    print('Host ',addr[0],' Logged into the fake server')
                    conn.send(b"Welcome to the admin Server\n")
                    while True:
                        conn.send(b"root@Server~#: ")
                        #print('Command Input : ',data)
                        data=conn.recv(100)
                        ############################################################################
                        # Command controls --------
                        command = str(data.decode('utf-8'))
                        switch_TelnetCommand(conn,command)
                        # -------------------------
                        ############################################################################
                        #switch_command(conn,data)
                        print("System Command from ",addr[0],"@:Server# ",data.decode("utf-8"),end='')
                #print('Incoming Data: ',data,' From Host: ',addr[0],' on Port',port)
                #conn.send(b"Wrong Password Try again\n")
        except Exception as ex:
            #print('Exception:', addr[0], addr[1], ex)
            print("\nConnection reset by the Host: ",addr[0],addr[1])
            print("---------------------------------------------------------")
        finally:
            #print('close:', addr[0], addr[1])
            #print("\n\n****** Telnet Connection Closed by the Host: ",addr[0]," **********\n\n")
            conn.close()
    except Exception as ex:
        print("Connection reset by the Host: ",addr[0]," on Port",addr[1])
        print("----------------------------------------------------------")
        conn.close()



#####################################

def client_handler143(conn, addr,port):
    try:
        print('\n\n******* Service Accessed *********\n----------------------------------------------\nRemote Host IP: ',addr[0],'connected with us on Port:',port)
        #send the welcome msg to client
        conn.send(b"Welcome to the Server:\n\nUsername: ")
        count=0
        try:
            while count<3:
                data = conn.recv(100)
            
                if not data: 
                    print('Connection exit by the Host:', addr[0],"on Port", addr[1])
                    print("---------------------------------------------------------")
                    break
            
                #send the username dialog to client
                print("Username input: ",data.decode("utf-8"),end='')
                #data = conn.recv(100)
                conn.send(b"Password: ")
                data = conn.recv(100)
                print('Password input: ',data.decode("utf-8"),end='')
                count=count+1
                if count==2:
                    conn.send(b"Wrong Password Try again\n")
                else:
                    conn.send(b"Wrong Password Try again\nUsername: ")
                #count=count+1
                if(count==2):
                    print('Host ',addr[0],' Logged into the fake server')
                    conn.send(b"Welcome to the admin Server\n")
                    while True:
                        conn.send(b"root@Server~#: ")
                        #print('Command Input : ',data)
                        data=conn.recv(100)
                        ############################################################################
                        # Command controls --------
                        command = str(data.decode('utf-8'))
                        switch_TelnetCommand(conn,command)
                        # -------------------------
                        ############################################################################
                        #switch_command(conn,data)
                        print("System Command from ",addr[0],"@:Server# ",data.decode("utf-8"),end='')
                #print('Incoming Data: ',data,' From Host: ',addr[0],' on Port',port)
                #conn.send(b"Wrong Password Try again\n")
        except Exception as ex:
            #print('Exception:', addr[0], addr[1], ex)
            print("\nConnection reset by the Host: ",addr[0],addr[1])
            print("---------------------------------------------------------")
        finally:
            #print('close:', addr[0], addr[1])
            #print("\n\n****** Telnet Connection Closed by the Host: ",addr[0]," **********\n\n")
            conn.close()
    except Exception as ex:
        print("Connection reset by the Host: ",addr[0]," on Port",addr[1])
        print("----------------------------------------------------------")
        conn.close()






#####################################


def client_handler443(conn, addr,port):
    try:
        print('\n\n******* Service Accessed *********\n----------------------------------------------\nRemote Host IP: ',addr[0],'connected with us on Port:',port)
        #send the welcome msg to client
        conn.send(b"Welcome to the Server:\n\nUsername: ")
        count=0
        try:
            while count<3:
                data = conn.recv(100)
            
                if not data: 
                    print('Connection exit by the Host:', addr[0],"on Port", addr[1])
                    print("---------------------------------------------------------")
                    break
            
                #send the username dialog to client
                print("Username input: ",data.decode("utf-8"),end='')
                #data = conn.recv(100)
                conn.send(b"Password: ")
                data = conn.recv(100)
                print('Password input: ',data.decode("utf-8"),end='')
                count=count+1
                if count==2:
                    conn.send(b"Wrong Password Try again\n")
                else:
                    conn.send(b"Wrong Password Try again\nUsername: ")
                #count=count+1
                if(count==2):
                    print('Host ',addr[0],' Logged into the fake server')
                    conn.send(b"Welcome to the admin Server\n")
                    while True:
                        conn.send(b"root@Server~#: ")
                        #print('Command Input : ',data)
                        data=conn.recv(100)
                        ############################################################################
                        # Command controls --------
                        command = str(data.decode('utf-8'))
                        switch_TelnetCommand(conn,command)
                        # -------------------------
                        ############################################################################
                        #switch_command(conn,data)
                        print("System Command from ",addr[0],"@:Server# ",data.decode("utf-8"),end='')
                #print('Incoming Data: ',data,' From Host: ',addr[0],' on Port',port)
                #conn.send(b"Wrong Password Try again\n")
        except Exception as ex:
            #print('Exception:', addr[0], addr[1], ex)
            print("\nConnection reset by the Host: ",addr[0],addr[1])
            print("---------------------------------------------------------")
        finally:
            #print('close:', addr[0], addr[1])
            #print("\n\n****** Telnet Connection Closed by the Host: ",addr[0]," **********\n\n")
            conn.close()
    except Exception as ex:
        print("Connection reset by the Host: ",addr[0]," on Port",addr[1])
        print("----------------------------------------------------------")
        conn.close()




#####################################


def client_handler445(conn, addr,port):
    try:
        print('\n\n******* Service Accessed *********\n----------------------------------------------\nRemote Host IP: ',addr[0],'connected with us on Port:',port)
        #send the welcome msg to client
        conn.send(b"Welcome to the Server:\n\nUsername: ")
        count=0
        try:
            while count<3:
                data = conn.recv(100)
            
                if not data: 
                    print('Connection exit by the Host:', addr[0],"on Port", addr[1])
                    print("---------------------------------------------------------")
                    break
            
                #send the username dialog to client
                print("Username input: ",data.decode("utf-8"),end='')
                #data = conn.recv(100)
                conn.send(b"Password: ")
                data = conn.recv(100)
                print('Password input: ',data.decode("utf-8"),end='')
                count=count+1
                if count==2:
                    conn.send(b"Wrong Password Try again\n")
                else:
                    conn.send(b"Wrong Password Try again\nUsername: ")
                #count=count+1
                if(count==2):
                    print('Host ',addr[0],' Logged into the fake server')
                    conn.send(b"Welcome to the admin Server\n")
                    while True:
                        conn.send(b"root@Server~#: ")
                        #print('Command Input : ',data)
                        data=conn.recv(100)
                        ############################################################################
                        # Command controls --------
                        command = str(data.decode('utf-8'))
                        switch_TelnetCommand(conn,command)
                        # -------------------------
                        ############################################################################
                        #switch_command(conn,data)
                        print("System Command from ",addr[0],"@:Server# ",data.decode("utf-8"),end='')
                #print('Incoming Data: ',data,' From Host: ',addr[0],' on Port',port)
                #conn.send(b"Wrong Password Try again\n")
        except Exception as ex:
            #print('Exception:', addr[0], addr[1], ex)
            print("\nConnection reset by the Host: ",addr[0],addr[1])
            print("---------------------------------------------------------")
        finally:
            #print('close:', addr[0], addr[1])
            #print("\n\n****** Telnet Connection Closed by the Host: ",addr[0]," **********\n\n")
            conn.close()
    except Exception as ex:
        print("Connection reset by the Host: ",addr[0]," on Port",addr[1])
        print("----------------------------------------------------------")
        conn.close()







#####################################

def client_handler993(conn, addr,port):
    try:
        print('\n\n******* Service Accessed *********\n----------------------------------------------\nRemote Host IP: ',addr[0],'connected with us on Port:',port)
        #send the welcome msg to client
        conn.send(b"Welcome to the Server:\n\nUsername: ")
        count=0
        try:
            while count<3:
                data = conn.recv(100)
            
                if not data: 
                    print('Connection exit by the Host:', addr[0],"on Port", addr[1])
                    print("---------------------------------------------------------")
                    break
            
                #send the username dialog to client
                print("Username input: ",data.decode("utf-8"),end='')
                #data = conn.recv(100)
                conn.send(b"Password: ")
                data = conn.recv(100)
                print('Password input: ',data.decode("utf-8"),end='')
                count=count+1
                if count==2:
                    conn.send(b"Wrong Password Try again\n")
                else:
                    conn.send(b"Wrong Password Try again\nUsername: ")
                #count=count+1
                if(count==2):
                    print('Host ',addr[0],' Logged into the fake server')
                    conn.send(b"Welcome to the admin Server\n")
                    while True:
                        conn.send(b"root@Server~#: ")
                        #print('Command Input : ',data)
                        data=conn.recv(100)
                        ############################################################################
                        # Command controls --------
                        command = str(data.decode('utf-8'))
                        switch_TelnetCommand(conn,command)
                        # -------------------------
                        ############################################################################
                        #switch_command(conn,data)
                        print("System Command from ",addr[0],"@:Server# ",data.decode("utf-8"),end='')
                #print('Incoming Data: ',data,' From Host: ',addr[0],' on Port',port)
                #conn.send(b"Wrong Password Try again\n")
        except Exception as ex:
            #print('Exception:', addr[0], addr[1], ex)
            print("\nConnection reset by the Host: ",addr[0],addr[1])
            print("---------------------------------------------------------")
        finally:
            #print('close:', addr[0], addr[1])
            #print("\n\n****** Telnet Connection Closed by the Host: ",addr[0]," **********\n\n")
            conn.close()
    except Exception as ex:
        print("Connection reset by the Host: ",addr[0]," on Port",addr[1])
        print("----------------------------------------------------------")
        conn.close()






#######################################


def client_handler995(conn, addr,port):
    try:
        print('\n\n******* Service Accessed *********\n----------------------------------------------\nRemote Host IP: ',addr[0],'connected with us on Port:',port)
        #send the welcome msg to client
        conn.send(b"Welcome to the Server:\n\nUsername: ")
        count=0
        try:
            while count<3:
                data = conn.recv(100)
            
                if not data: 
                    print('Connection exit by the Host:', addr[0],"on Port", addr[1])
                    print("---------------------------------------------------------")
                    break
            
                #send the username dialog to client
                print("Username input: ",data.decode("utf-8"),end='')
                #data = conn.recv(100)
                conn.send(b"Password: ")
                data = conn.recv(100)
                print('Password input: ',data.decode("utf-8"),end='')
                count=count+1
                if count==2:
                    conn.send(b"Wrong Password Try again\n")
                else:
                    conn.send(b"Wrong Password Try again\nUsername: ")
                #count=count+1
                if(count==2):
                    print('Host ',addr[0],' Logged into the fake server')
                    conn.send(b"Welcome to the admin Server\n")
                    while True:
                        conn.send(b"root@Server~#: ")
                        #print('Command Input : ',data)
                        data=conn.recv(100)
                        ############################################################################
                        # Command controls --------
                        command = str(data.decode('utf-8'))
                        switch_TelnetCommand(conn,command)
                        # -------------------------
                        ############################################################################
                        #switch_command(conn,data)
                        print("System Command from ",addr[0],"@:Server# ",data.decode("utf-8"),end='')
                #print('Incoming Data: ',data,' From Host: ',addr[0],' on Port',port)
                #conn.send(b"Wrong Password Try again\n")
        except Exception as ex:
            #print('Exception:', addr[0], addr[1], ex)
            print("\nConnection reset by the Host: ",addr[0],addr[1])
            print("---------------------------------------------------------")
        finally:
            #print('close:', addr[0], addr[1])
            #print("\n\n****** Telnet Connection Closed by the Host: ",addr[0]," **********\n\n")
            conn.close()
    except Exception as ex:
        print("Connection reset by the Host: ",addr[0]," on Port",addr[1])
        print("----------------------------------------------------------")
        conn.close()





#######################################

def client_handler1723(conn, addr,port):
    try:
        print('\n\n******* Service Accessed *********\n----------------------------------------------\nRemote Host IP: ',addr[0],'connected with us on Port:',port)
        #send the welcome msg to client
        conn.send(b"Welcome to the Server:\n\nUsername: ")
        count=0
        try:
            while count<3:
                data = conn.recv(100)
            
                if not data: 
                    print('Connection exit by the Host:', addr[0],"on Port", addr[1])
                    print("---------------------------------------------------------")
                    break
            
                #send the username dialog to client
                print("Username input: ",data.decode("utf-8"),end='')
                #data = conn.recv(100)
                conn.send(b"Password: ")
                data = conn.recv(100)
                print('Password input: ',data.decode("utf-8"),end='')
                count=count+1
                if count==2:
                    conn.send(b"Wrong Password Try again\n")
                else:
                    conn.send(b"Wrong Password Try again\nUsername: ")
                #count=count+1
                if(count==2):
                    print('Host ',addr[0],' Logged into the fake server')
                    conn.send(b"Welcome to the admin Server\n")
                    while True:
                        conn.send(b"root@Server~#: ")
                        #print('Command Input : ',data)
                        data=conn.recv(100)
                        ############################################################################
                        # Command controls --------
                        command = str(data.decode('utf-8'))
                        switch_TelnetCommand(conn,command)
                        # -------------------------
                        ############################################################################
                        #switch_command(conn,data)
                        print("System Command from ",addr[0],"@:Server# ",data.decode("utf-8"),end='')
                #print('Incoming Data: ',data,' From Host: ',addr[0],' on Port',port)
                #conn.send(b"Wrong Password Try again\n")
        except Exception as ex:
            #print('Exception:', addr[0], addr[1], ex)
            print("\nConnection reset by the Host: ",addr[0],addr[1])
            print("---------------------------------------------------------")
        finally:
            #print('close:', addr[0], addr[1])
            #print("\n\n****** Telnet Connection Closed by the Host: ",addr[0]," **********\n\n")
            conn.close()
    except Exception as ex:
        print("Connection reset by the Host: ",addr[0]," on Port",addr[1])
        print("----------------------------------------------------------")
        conn.close()



######################################


def client_handler3306(conn, addr,port):
    try:
        print('\n\n******* Service Accessed *********\n----------------------------------------------\nRemote Host IP: ',addr[0],'connected with us on Port:',port)
        #send the welcome msg to client
        conn.send(b"Welcome to the Server:\n\nUsername: ")
        count=0
        try:
            while count<3:
                data = conn.recv(100)
            
                if not data: 
                    print('Connection exit by the Host:', addr[0],"on Port", addr[1])
                    print("---------------------------------------------------------")
                    break
            
                #send the username dialog to client
                print("Username input: ",data.decode("utf-8"),end='')
                #data = conn.recv(100)
                conn.send(b"Password: ")
                data = conn.recv(100)
                print('Password input: ',data.decode("utf-8"),end='')
                count=count+1
                if count==2:
                    conn.send(b"Wrong Password Try again\n")
                else:
                    conn.send(b"Wrong Password Try again\nUsername: ")
                #count=count+1
                if(count==2):
                    print('Host ',addr[0],' Logged into the fake server')
                    conn.send(b"Welcome to the admin Server\n")
                    while True:
                        conn.send(b"root@Server~#: ")
                        #print('Command Input : ',data)
                        data=conn.recv(100)
                        ############################################################################
                        # Command controls --------
                        command = str(data.decode('utf-8'))
                        switch_TelnetCommand(conn,command)
                        # -------------------------
                        ############################################################################
                        #switch_command(conn,data)
                        print("System Command from ",addr[0],"@:Server# ",data.decode("utf-8"),end='')
                #print('Incoming Data: ',data,' From Host: ',addr[0],' on Port',port)
                #conn.send(b"Wrong Password Try again\n")
        except Exception as ex:
            #print('Exception:', addr[0], addr[1], ex)
            print("\nConnection reset by the Host: ",addr[0],addr[1])
            print("---------------------------------------------------------")
        finally:
            #print('close:', addr[0], addr[1])
            #print("\n\n****** Telnet Connection Closed by the Host: ",addr[0]," **********\n\n")
            conn.close()
    except Exception as ex:
        print("Connection reset by the Host: ",addr[0]," on Port",addr[1])
        print("----------------------------------------------------------")
        conn.close()



##################################

def client_handler3389(conn, addr,port):
    try:
        print('\n\n******* Service Accessed *********\n----------------------------------------------\nRemote Host IP: ',addr[0],'connected with us on Port:',port)
        #send the welcome msg to client
        conn.send(b"Welcome to the Server:\n\nUsername: ")
        count=0
        try:
            while count<3:
                data = conn.recv(100)
            
                if not data: 
                    print('Connection exit by the Host:', addr[0],"on Port", addr[1])
                    print("---------------------------------------------------------")
                    break
            
                #send the username dialog to client
                print("Username input: ",data.decode("utf-8"),end='')
                #data = conn.recv(100)
                conn.send(b"Password: ")
                data = conn.recv(100)
                print('Password input: ',data.decode("utf-8"),end='')
                count=count+1
                if count==2:
                    conn.send(b"Wrong Password Try again\n")
                else:
                    conn.send(b"Wrong Password Try again\nUsername: ")
                #count=count+1
                if(count==2):
                    print('Host ',addr[0],' Logged into the fake server')
                    conn.send(b"Welcome to the admin Server\n")
                    while True:
                        conn.send(b"root@Server~#: ")
                        #print('Command Input : ',data)
                        data=conn.recv(100)
                        ############################################################################
                        # Command controls --------
                        command = str(data.decode('utf-8'))
                        switch_TelnetCommand(conn,command)
                        # -------------------------
                        ############################################################################
                        #switch_command(conn,data)
                        print("System Command from ",addr[0],"@:Server# ",data.decode("utf-8"),end='')
                #print('Incoming Data: ',data,' From Host: ',addr[0],' on Port',port)
                #conn.send(b"Wrong Password Try again\n")
        except Exception as ex:
            #print('Exception:', addr[0], addr[1], ex)
            print("\nConnection reset by the Host: ",addr[0],addr[1])
            print("---------------------------------------------------------")
        finally:
            #print('close:', addr[0], addr[1])
            #print("\n\n****** Telnet Connection Closed by the Host: ",addr[0]," **********\n\n")
            conn.close()
    except Exception as ex:
        print("Connection reset by the Host: ",addr[0]," on Port",addr[1])
        print("----------------------------------------------------------")
        conn.close()





####################################

def client_handler5900(conn, addr,port):
    try:
        print('\n\n******* Service Accessed *********\n----------------------------------------------\nRemote Host IP: ',addr[0],'connected with us on Port:',port)
        #send the welcome msg to client
        conn.send(b"Welcome to the Server:\n\nUsername: ")
        count=0
        try:
            while count<3:
                data = conn.recv(100)
            
                if not data: 
                    print('Connection exit by the Host:', addr[0],"on Port", addr[1])
                    print("---------------------------------------------------------")
                    break
            
                #send the username dialog to client
                print("Username input: ",data.decode("utf-8"),end='')
                #data = conn.recv(100)
                conn.send(b"Password: ")
                data = conn.recv(100)
                print('Password input: ',data.decode("utf-8"),end='')
                count=count+1
                if count==2:
                    conn.send(b"Wrong Password Try again\n")
                else:
                    conn.send(b"Wrong Password Try again\nUsername: ")
                #count=count+1
                if(count==2):
                    print('Host ',addr[0],' Logged into the fake server')
                    conn.send(b"Welcome to the admin Server\n")
                    while True:
                        conn.send(b"root@Server~#: ")
                        #print('Command Input : ',data)
                        data=conn.recv(100)
                        ############################################################################
                        # Command controls --------
                        command = str(data.decode('utf-8'))
                        switch_TelnetCommand(conn,command)
                        # -------------------------
                        ############################################################################
                        #switch_command(conn,data)
                        print("System Command from ",addr[0],"@:Server# ",data.decode("utf-8"),end='')
                #print('Incoming Data: ',data,' From Host: ',addr[0],' on Port',port)
                #conn.send(b"Wrong Password Try again\n")
        except Exception as ex:
            #print('Exception:', addr[0], addr[1], ex)
            print("\nConnection reset by the Host: ",addr[0],addr[1])
            print("---------------------------------------------------------")
        finally:
            #print('close:', addr[0], addr[1])
            #print("\n\n****** Telnet Connection Closed by the Host: ",addr[0]," **********\n\n")
            conn.close()
    except Exception as ex:
        print("Connection reset by the Host: ",addr[0]," on Port",addr[1])
        print("----------------------------------------------------------")
        conn.close()




##############################


def client_handler8080(conn, addr,port):
    try:
        print('\n\n******* Service Accessed *********\n----------------------------------------------\nRemote Host IP: ',addr[0],'connected with us on Port:',port)
        #send the welcome msg to client
        conn.send(b"Welcome to the Server:\n\nUsername: ")
        count=0
        try:
            while count<3:
                data = conn.recv(100)
            
                if not data: 
                    print('Connection exit by the Host:', addr[0],"on Port", addr[1])
                    print("---------------------------------------------------------")
                    break
            
                #send the username dialog to client
                print("Username input: ",data.decode("utf-8"),end='')
                #data = conn.recv(100)
                conn.send(b"Password: ")
                data = conn.recv(100)
                print('Password input: ',data.decode("utf-8"),end='')
                count=count+1
                if count==2:
                    conn.send(b"Wrong Password Try again\n")
                else:
                    conn.send(b"Wrong Password Try again\nUsername: ")
                #count=count+1
                if(count==2):
                    print('Host ',addr[0],' Logged into the fake server')
                    conn.send(b"Welcome to the admin Server\n")
                    while True:
                        conn.send(b"root@Server~#: ")
                        #print('Command Input : ',data)
                        data=conn.recv(100)
                        ############################################################################
                        # Command controls --------
                        command = str(data.decode('utf-8'))
                        switch_TelnetCommand(conn,command)
                        # -------------------------
                        ############################################################################
                        #switch_command(conn,data)
                        print("System Command from ",addr[0],"@:Server# ",data.decode("utf-8"),end='')
                #print('Incoming Data: ',data,' From Host: ',addr[0],' on Port',port)
                #conn.send(b"Wrong Password Try again\n")
        except Exception as ex:
            #print('Exception:', addr[0], addr[1], ex)
            print("\nConnection reset by the Host: ",addr[0],addr[1])
            print("---------------------------------------------------------")
        finally:
            #print('close:', addr[0], addr[1])
            #print("\n\n****** Telnet Connection Closed by the Host: ",addr[0]," **********\n\n")
            conn.close()
    except Exception as ex:
        print("Connection reset by the Host: ",addr[0]," on Port",addr[1])
        print("----------------------------------------------------------")
        conn.close()




###########################


def client_handler23(conn, addr,port):
    try:
        print('\n\n******* Telnet Service Accessed *********\n----------------------------------------------\nRemote Host IP: ',addr[0],'connected with us on Port:',port)
        #send the welcome msg to client
        conn.send(b"Welcome to the Telnet Server:\n\nUsername: ")
        count=0
        try:
            while count<3:
                data = conn.recv(100)
            
                if not data: 
                    print('Connection exit by the Host:', addr[0],"on Port", addr[1])
                    print("---------------------------------------------------------")
                    break
            
                #send the username dialog to client
                print("Username input: ",data.decode("utf-8"),end='')
                #data = conn.recv(100)
                conn.send(b"Password: ")
                data = conn.recv(100)
                print('Password input: ',data.decode("utf-8"),end='')
                count=count+1
                if count==2:
                    conn.send(b"Wrong Password Try again\n")
                else:
                    conn.send(b"Wrong Password Try again\nUsername: ")
                #count=count+1
                if(count==2):
                    print('Host ',addr[0],' Logged into the fake server')
                    conn.send(b"Welcome to the admin Server\n")
                    while True:
                        conn.send(b"root@Server~#: ")
                        #print('Command Input : ',data)
                        data=conn.recv(100)
                        ############################################################################
                        # Command controls --------
                        command = str(data.decode('utf-8'))
                        switch_TelnetCommand(conn,command)
                        # -------------------------
                        ############################################################################
                        #switch_command(conn,data)
                        print("System Command from ",addr[0],"@:Server# ",data.decode("utf-8"),end='')
                #print('Incoming Data: ',data,' From Host: ',addr[0],' on Port',port)
                #conn.send(b"Wrong Password Try again\n")
        except Exception as ex:
            #print('Exception:', addr[0], addr[1], ex)
            print("\nConnection reset by the Host: ",addr[0],addr[1])
            print("---------------------------------------------------------")
        finally:
            #print('close:', addr[0], addr[1])
            #print("\n\n****** Telnet Connection Closed by the Host: ",addr[0]," **********\n\n")
            conn.close()
    except Exception as ex:
        print("Connection reset by the Host: ",addr[0]," on Port",addr[1])
        print("----------------------------------------------------------")
        conn.close()


###################################################

######   FTP Client handler


def client_handler21(conn, addr,port):
    try:
        print('\n\n******* FTP Service Accessed *********\n----------------------------------------------\nRemote Host IP: ',addr[0],'connected with us on Port:',port)
        #send the welcome msg to client
        conn.send(b"Connected to FTP Server\n220 Service ready for new user.\nUsername:")
        count=0
        try:
            while count<3:
                data = conn.recv(100)
            
                if not data: 
                    print('Connection exit by the Host:', addr[0],"on Port", addr[1])
                    print("---------------------------------------------------------")
                    break
            
                #send the username dialog to client
                print("Username input: ",data.decode("utf-8"),end='')
                #data = conn.recv(100)
                conn.send(b"Password: ")
                data = conn.recv(100)
                print('Password input: ',data.decode("utf-8"),end='')
                count=count+1
                if count==2:
                    conn.send(b"Wrong Password Try again\n")
                else:
                    conn.send(b"Wrong Password Try again\nUsername: ")
                #count=count+1
                if(count==2):
                    print('Host ',addr[0],' Logged into the fake server')
                    conn.send(b"Welcome to the FTP Server\n")
                    while True:
                        conn.send(b"ftp> ")
                        #print('Command Input : ',data)
                        data=conn.recv(100)
                        ############################################################################
                        # Command controls --------
                        command = str(data.decode('utf-8'))
                        switch_FtpCommand(conn,command)
                        # -------------------------
                        ############################################################################
                        #switch_command(conn,data)
                        print("System Command from ",addr[0],"@:ftp> ",data.decode("utf-8"),end='')
                #print('Incoming Data: ',data,' From Host: ',addr[0],' on Port',port)
                #conn.send(b"Wrong Password Try again\n")
        except Exception as ex:
            #print('Exception:', addr[0], addr[1], ex)
            print("\nConnection reset by the Host: ",addr[0],addr[1])
            print("---------------------------------------------------------")
        finally:
            #print('close:', addr[0], addr[1])
            #print("\n\n****** Telnet Connection Closed by the Host: ",addr[0]," **********\n\n")
            conn.close()
    except Exception as ex:
        print("Connection reset by the Host: ",addr[0]," on Port",addr[1])
        print("----------------------------------------------------------")
        conn.close()

#####################




################# SSH client handler

def client_handler22(conn, addr,port):
    try:
        print('\n\n******* SSH Service Accessed *********\n----------------------------------------------\nRemote Host IP: ',addr[0],'connected with us on Port:',port)
        #send the welcome msg to client
        conn.send(b"Welcome to the SSH Server:\n\nUsername: ")
        count=0
        try:
            while True:
                data = conn.recv(255)
            
                if not data: 
                    print('Connection exit by the Host:', addr[0],"on Port", addr[1])
                    print("---------------------------------------------------------")
                    break
            
                #send the username dialog to client
                print("Username input: ",data.decode("utf-8"),end='')
                #data = conn.recv(100)
                conn.send(b"Password: ")
                data = conn.recv(255)
                print('Password input: ',data.decode("utf-8"),end='')
                conn.send(b"Wrong Password Try again\nUsername: ")
                #count=1
                #print('Incoming Data: ',data,' From Host: ',addr[0],' on Port',port)
                #conn.send(b"Wrong Password Try again\n")
        except Exception as ex:
            #print('Exception:', addr[0], addr[1], ex)
            print("Connection reset by the Host: ",addr[0],"on Port",addr[1])
            print("---------------------------------------------------------")
        finally:
            #print('close:', addr[0], addr[1])
            #print("\n****** SSH Connection Closed by the Host: ",addr[0]," **********\n\n")
            conn.close()
    except Exception as ex:
        print("Connection reset by the Host: ",addr[0]," on Port",addr[1])
        print("----------------------------------------------------------")
        conn.close()



###########################################################