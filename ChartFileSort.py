import os
import shutil
import time

path = r"G:\DLD\Output_NoBGA"
outPath = r"G:\DLD\out"
def ChartFileSort():
    for root,dirs,files in os.walk(path):
        if dirs == []:
            continue
        if root == "G:\DLD\Output_NoBGA":
            continue

        tPath = root
        for tRoot, tDirs, tFiles in os.walk(tPath):
            if tRoot == root:
                continue

            with open(f"{tRoot}/maidata.txt","r+",encoding='utf-8') as file:
                chartRaw = file.read()
                chartTitle = chartRaw[chartRaw.find("&title=")+7:chartRaw.find("&wholebpm=")-1].replace("'","").replace('"',"").replace('，',"").replace(',',"").replace('*',"").replace("?","").replace(":"," ").replace("<","《").replace(">","》")
                chartLv5 = chartRaw[chartRaw.find("&lv_5") + 6:chartRaw.find("&des_5")-1]
                chartLv6 = chartRaw[chartRaw.find("&lv_6")+6:chartRaw.find("&des_6")-1]

                chartLevel = chartLv6
                if chartLv6 == "":
                    chartLevel = chartLv5

                chartOutPath = f"{outPath}/{chartLevel}/{chartTitle}"

                if (os.path.exists(chartOutPath)) or ("宴" in chartTitle):
                    file.close()
                    continue


                os.makedirs(chartOutPath, exist_ok=True)
                for chartFile in tFiles:
                    shutil.copy2(f"{tRoot}/{chartFile}", f"{chartOutPath}/{chartFile}")
                print(chartTitle)
                file.close()
                time.sleep(1)
                # break

ChartFileSort()
