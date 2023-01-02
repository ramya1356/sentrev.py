import time
import psutil
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns',10)
la_rcd_bytes=psutil.net_io_counters().bytes_recv
la_snt_bytes=psutil.net_io_counters().bytes_sent
total_bytes=la_rcd_bytes+la_snt_bytes
data=[]
#print(la_rcd_bytes)
#print(la_snt_bytes)
#print(total_bytes)
#print(f"{la_snt_bytes/1024/1024:.2f}MB and {la_rcd_bytes/1024/1024:.2f}MB then {total_bytes/1024/1024:.2f}MB")
#io_bytes=psutil.net_io_counters(pernic=True)
io_bytes=psutil.net_io_counters()
#print(io_bytes)
#print(io_bytes1)
#df=pd.DataFrame(io_bytes)
#df1=pd.DataFrame(io_bytes1)
#print(df)
#print(df1)
while True:
    byte_recd=psutil.net_io_counters().bytes_recv
    byte_sent=psutil.net_io_counters().bytes_sent
    total_new_bytes=byte_recd+byte_sent
    new_recvd=byte_recd-la_rcd_bytes
    new_sent=byte_sent-la_snt_bytes
    new_total=total_new_bytes-total_bytes
    mb_new_recvd=new_recvd/1024/1024
    mb_new_sent = new_sent / 1024 / 1024
    mb_new_total = new_total / 1024 / 1024
    print(f"{mb_new_recvd:.2f}MB and {mb_new_sent:.2f}MB then {mb_new_total:.2f}MB")
    data.append({'Byte_sent':io_bytes.bytes_sent,
                 'Byte_recvd':io_bytes.bytes_recv,
                 'pkt_sent':io_bytes.packets_sent,
                 'pkt_rcvd':io_bytes.packets_recv,
                 'pkt_drop_in':io_bytes.dropin,
                 'pkt_drop_out':io_bytes.dropout,
                 'error_in':io_bytes.errin,
                 'error_out':io_bytes.errout})
    df=pd.DataFrame(data)
    time.sleep(1)
    #sns.lineplot(data=df)
    #plt.show()
    print(df)
