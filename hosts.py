import sys
import os
from datetime import datetime

now = datetime.now()

def print_result(state, line):
    print('line "{}"'.format(line))
    print('[{}] '.format(now.strftime("%H:%M:%S")) + '\x1b[1;32;40m' + state + '\x1b[0m')
    print('Modified file: ' + '\x1b[1;34;40m' + '/etc/hosts' + '\x1b[0m')
    os.system('tail /etc/hosts')

def run(host):
    with open('/etc/hosts') as f:
        datas = f.readlines()
        count = -1
        lines = []
        for line in datas:
            count += 1
            lines.append( "{}".format(line.strip()) )
        
        for index, item in enumerate(lines):
            x = item.find(host)
            if( x != -1 ):
                y = item.find("#")
                if(y != -1):
                    tmp = item[:y] + item[y+1:]
                    item = "{}\n".format(tmp)
                    datas[index] = item
                    new_file = open('/etc/hosts', 'w')
                    new_file.writelines(datas)
                    new_file.close()
                    print_result("Uncommented", tmp)
                else:
                    tmp = item
                    item = "#{}\n".format(tmp)
                    datas[index] = item
                    new_file = open('/etc/hosts', 'w')
                    new_file.writelines(datas)
                    new_file.close()
                    print_result("Commented", tmp)

if __name__ == "__main__":
    host = sys.argv[1]
    run(host)
