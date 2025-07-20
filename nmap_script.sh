# /bin/bash
# this script is for scanning stuff with nmap

if [ $# -lt 2 ]; then
  echo "pls give IP and script"
  echo "example: ./nmap_script.sh 127.0.0.1 ftp-anon"
  exit
fi

ip=$1
script=$2

echo "Scanning $ip using $script script..."
nmap --script $script -sV $ip
