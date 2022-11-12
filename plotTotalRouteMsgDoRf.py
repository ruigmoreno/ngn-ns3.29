import os
import numpy as np
import matplotlib.pyplot as plt

os.chdir('./scriptResults-all-do-rf-001/')
cwd = os.getcwd()
phy = '80211a'
nb_nodes='81'
packetInterval = '0.01'
parameter='PreqTotal' # 'PreqTotal', 'PrepTotal', 'PerrTotal', 
                        # txPreqTotal, txPrepTotal, txPerrTotal, totalDropped, totalQueued
listModes=['R','RP']
listFlags=['d0-r0', 'd0-r1', 'd1-r0', 'd1-r1']
# listPacketSize=['32','256','1024']
packetSize='1024'
listFlows=['1','10','30','50','70']
# title = 'Modes with packet interval of '+packetInterval+' s'
#title = 'Modos com intervalo de pacote de '+packetInterval+' s'
# for parameter in listParameter:

plt.axis([0, 71, 0, 500])
plt.ylabel('Total de mensagens PREQ Iniciadas')
# plt.ylabel('Total de mensagens PREP Iniciadas')
# plt.ylabel('Total de mensagens PERR Iniciadas')
# plt.ylabel('Total de mensagens PREQ na rede')
# plt.ylabel('Total de mensagens PREP na rede')
# plt.ylabel('Total de mensagens PERR na rede')

for mode in listModes:
    if mode == 'R':
        color='black'
    elif mode == 'RP':
        color='red'
    # for packetSize in listPacketSize:
    for flag in listFlags:
        x = np.array([])
        y = np.array([])
        error = np.array([])
        for nb_flows in listFlows:
            load_y = np.loadtxt('./'+mode+'/'+flag+'/nb_nodes-'+nb_nodes+'-packetInterval-'+packetInterval+'-'+phy+'-'+nb_flows+'-flows/'+parameter+'-packetSize-'+packetSize, usecols=1)
            y = np.append(y, load_y)

            load_x = np.loadtxt('./'+mode+'/'+flag+'/nb_nodes-'+nb_nodes+'-packetInterval-'+packetInterval+'-'+phy+'-'+nb_flows+'-flows/'+parameter+'-packetSize-'+packetSize, usecols=0)
            x = np.append(x, load_x)

            load_error=np.loadtxt('./'+mode+'/'+flag+'/nb_nodes-'+nb_nodes+'-packetInterval-'+packetInterval+'-'+phy+'-'+nb_flows+'-flows/'+parameter+'-packetSize-'+packetSize, usecols=2)
            error = np.append(error, load_error)
        if flag == 'd0-r0':
            markerStyle='.'
        elif flag == 'd0-r1':
            markerStyle='s'
        elif flag == 'd1-r0':
            markerStyle='x'
        elif flag == 'd1-r1':
            markerStyle='*'
        # plt.xlabel('flows number')
        plt.xlabel('Número de fluxos')
        plt.errorbar(x, y, yerr=error, marker=markerStyle, color=color, label=mode+' '+flag+' '+packetSize+' bytes', capsize=6)
        plt.legend(bbox_to_anchor=(0.1, -.36, .8, .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0)
        plt.grid(True)
#plt.suptitle(title, y=0.925)
# plt.savefig('./plot-'+parameter+'-route-msgs-per-node.pdf', bbox_inches="tight")
plt.savefig('./plot-'+parameter+'-route-msgs-per-node-PT.pdf', bbox_inches="tight")
plt.clf() # clear the entire current figure with all its axes
