Python automation creation to help switching NAT from One ISP (Telkom) To another ISP (CBN) using python paramiko to access SSH to the router's public IP.
By configuring the relevant public ip to each databases: DatabaseNAT-TelkoToCBN.csv, and DatabaseNAT-cbnToTelko.csv
Selecting 111 will execute the telko (ISP1) to cbn (ISP2) database meanwhile 222 will execute the cbn (ISP2) to telko (ISP1) database hardcoded, the csv name shouldn't be changed.
The algorithm is: extracting csv by using loop. Inside the loop: do /ip firewall nat enable/disable find comments=enable/disable in the csv.

Another way to do this is through using Netwatch, scheduler and script, but it is prohibited by my org.
