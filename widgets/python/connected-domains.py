import subprocess
import socket

def run_netstat():
    try:
        # Run netstat -an and capture the output
        netstat_output = subprocess.check_output(['netstat', '-an'], universal_newlines=True)
        return netstat_output
    except subprocess.CalledProcessError as e:
        print(f"Error running netstat: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def extract_ips(netstat_output):
    ips = []
    lines = netstat_output.splitlines()
    for line in lines:
        parts = line.split()
        if len(parts) >= 4 and parts[0] == "TCP" and ":" in parts[1] and ":" in parts[2]:
            local_ip, local_port = parts[1].rsplit(':', 1)
            remote_ip, remote_port = parts[2].rsplit(':', 1)
            ips.append((local_ip, remote_ip))
    return ips

def nslookup_ips(ips):
    domain_names = []
    for local_ip, remote_ip in ips:
        try:
            # Perform DNS lookup on the remote IP
            host = socket.gethostbyaddr(remote_ip)
            if len(host) >= 2:
                # The second entry in the host tuple is the domain name
                domain_names.append(host[0])
        except socket.herror as e:
            domain_names.append("N/A")
    return domain_names

if __name__ == "__main__":
    netstat_output = run_netstat()
    
    if netstat_output:
        ips = extract_ips(netstat_output)
        domain_names = nslookup_ips(ips)
        
        for (local_ip, remote_ip), domain in zip(ips, domain_names):
            if not '/' in domain and not 'jedi' in domain.lower():
                print(f"Remote IP: {remote_ip}, Domain: {domain}")
                # print(f"Local IP: {local_ip}, Remote IP: {remote_ip}, Domain: {domain}")
