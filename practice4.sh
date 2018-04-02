cat /proc/cpuinfo
#cpu정보
cat /proc/cpuinfo | grep processor
#processor만 뽑아서 보여줌
cat /proc/meminfo
#memory정보
cat /procmeminfo | grep memtotal
#memtotal만 뽑아서 보여줌
getconf LONG_BIT
64
#64비트확인
uname -m
x86_64
