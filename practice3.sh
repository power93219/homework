cat /etc/passwd | grep jylee
# jylee 계정이 있나 확인 -> 없음
sudo useradd jylee -m -s /bin/bash
# jylee 계정 생성
echo 'embedded' | passwd --stdin jylee
# jylee 계정의 패스워드를 embedded로 설정

