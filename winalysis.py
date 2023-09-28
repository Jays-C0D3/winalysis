###########################################
# GitHub : https://github.com/n000b-n000b #
###########################################
import os as a
import subprocess as b
import pandas as c
from datetime import date,datetime
from time import sleep

def main():
    def stream():
        b.run(['powershell','tasklist','/FO','csv','>>', date.today().strftime('%Y%m%d') + '_masterrec.csv'])
    def trace_f():
        keydate = open('keydate.txt','w')
        keydate.write(date.today().strftime('%Y%m%d'))
    def ingest():
        harvest_len = str(input("How many days would you like to collect?: "))
        if harvest_len.isdigit():
            max_harv=open('winset.txt','w')
            max_harv.write(harvest_len)
            max_harv.close()
            next
        else:
            print("Please enter a number value")
            harvest_len = str(input("How many days would you like to collect?: "))
            if harvest_len.isdigit():
                next
            else:
                print("Human error. Good Bye!")
                exit(0)
    a.chdir('C:\winalysis')
    if 'keydate.txt' in a.listdir() and 'winset.txt' in a.listdir():
        tmp_subproc = b.run(['powershell', 'Get-content', 'keydate.txt'], capture_output=True)
        tmp_subproc1 = b.run(['powershell', 'Get-content', 'winset.txt'], capture_output=True)
        if len(str(tmp_subproc.stdout))==3:
            trace_f()
        if len(str(tmp_subproc1.stdout))==3:
            ingest()
        tmp_subproc = tmp_subproc.stdout.strip()
        tmp_subproc1 = tmp_subproc1.stdout.strip()
        if int(date.today().strftime('%Y%m%d'))>=int(str(tmp_subproc).replace('b','').replace("'",''))+int(str(tmp_subproc1).replace('b','').replace("'",'')):
            print("Data ingestion complete.")
            print("CSV files in Winalysis directory are ready to be imported into your DataViz tool of choice. \n \nHappy Analyzing :)")
            exit()
    else:
        trace_f()
        ingest()
    indx = 0
    while indx<=1440:
        for x in range(1,61):
            stream()
        indx+=1
main()
