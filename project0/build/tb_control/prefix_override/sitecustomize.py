import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/siddhant/Desktop/enpm662/enpm662_fall2024/project0/install/tb_control'
