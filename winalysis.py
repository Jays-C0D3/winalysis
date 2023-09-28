###########################################
# GitHub : https://github.com/n000b-n000b #
###########################################
import os as a
import subprocess as b
from datetime import date,datetime

def main():
    def stream():
        b.run(['powershell','tasklist','/FO','csv','>>', date.today().strftime('%Y%m%d') + '_masterrec.csv'])
    def trace_f():
        keydate = open('keydate.txt','w')
        keydate.write(date.today().strftime('%Y%m%d'))
    def analysis():
        
    a.chdir('C:\winalysis')
    if 'keydate.txt' in a.listdir():
        tmp_subproc = b.run(['powershell', 'Get-content', 'keydate.txt'], capture_output=True)
        if len(str(tmp_subproc.stdout))==3:
            trace_f()
        with open('keydate.txt','r') as keydate_ref:
            if int(date.today().strftime('%Y%m%d'))>=int(keydate_ref.readline())+7:
                print("7 day stream complete.")
                print("Relocating data and creating logs.")
    else:
        trace_f()
    indx = 0
    while indx<=1440:
        for x in range(1,61):
            stream()
        indx+=1
main()
