# pirmer upotrebe:
# kao sudo/ ili sudo su

# kreira usera undp1, home folder mu je /home/undp1/
# sudo ./skripta-za-usere.sh 1       
# kreira usera undp2019, home folder mu je /home/undp2019/            
# sudo ./skripta-za-usere.sh 2019
username=undp$1
password="KulSifra2021#1"
useradd $username -d /home/$username -m ;
echo $username:$password | chpasswd
echo "the account is setup"

