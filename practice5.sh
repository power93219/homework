cat /proc/cpuinfo
#cpuinfo 확인
cat /proc/cpuinfo > system_info
#system_info로 정보를 txt파일로 옮김
vi system_info
#system_info 파일에 옮겨졌는 지 확인
cat /proc/meminfo >> system_info
#meminfo를 system_info뒤에 연이어서 옮김
vi system_info
#뒤에 연속해서 기록됬는 지 확인
