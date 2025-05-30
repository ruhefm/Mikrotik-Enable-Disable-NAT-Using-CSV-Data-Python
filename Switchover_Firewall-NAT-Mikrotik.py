import csv
import paramiko

def switchJaringan(csvdb):

    with open(csvdb, mode='r', newline='') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for row in csv_reader:
            clientName = row['client']
            ipPub = row['ipPub']
            ipPort = row['ipPort']
            username = row['username']
            password = row['password']
            enableComment = row['enable']
            disableComment = row['disable']


            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            try:
                client.connect(ipPub, ipPort, username, password)
                print(f"Sudah konek ke {clientName}")
                disableCMD=disableComment
                enableCMD=enableComment
                stdin, stdout, stderr = client.exec_command(f"""
                /ip firewall nat disable [find where comment="{disableCMD}"]
                /ip firewall nat enable [find where comment="{enableCMD}"]
                /ip firewall nat print where comment~"{disableCMD}"
                /ip firewall nat print where comment~"{enableCMD}"
                                                            """)
                output = stdout.read().decode()
                print("Output:")
                print(output)

            except Exception as e:
                print(f"Error: {e}")
            finally:
                client.close()
menu = input(f"""
             111. Switch Jaringan TELKOM to CBN
             222. Switch Jaringan CBN to TELKOM
             """)

if menu == "111":
    switchJaringan("DatabaseNAT-TelkoToCBN.csv")
if menu == "222":
    switchJaringan("DatabaseNAT-cbnToTelko.csv")