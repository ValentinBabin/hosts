import sys

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
                    print('line "{}"'.format(tmp))
                    print('\x1b[1;32;40m' + 'Uncommented' + '\x1b[0m')
                else:
                    tmp = item
                    item = "#{}\n".format(tmp)
                    datas[index] = item
                    new_file = open('/etc/hosts', 'w')
                    new_file.writelines(datas)
                    new_file.close()
                    print('line "{}"'.format(tmp))
                    print('\x1b[1;32;40m' + 'Commented' + '\x1b[0m')

if __name__ == "__main__":
    host = sys.argv[1]
    run(host)
