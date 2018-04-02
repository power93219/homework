ifconfig(in Linux)
#ip확인
apt-get install openssh-server
#openssh-server를 설치
cat /etc/ssh/sshd_config | egrep ^\#?Port
#Port번호 확인
sudo vi /etc/ssh/sshd_config
#Port번호 10022로 바꿈
service sshd restart
#재시작
cat /etc/ssh/sshd_config | egrep ^\#?Port
#바뀐 Port번호 확인
