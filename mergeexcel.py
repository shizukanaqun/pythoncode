import xlrd  #读取Excel文件的包
import xlsxwriter   #将文件写入Excel的包
import os

#打开一个excel文件
def open_xls(file):
    f = xlrd.open_workbook(file)
    return f


#获取excel中所有的sheet表
def getsheet(f):
    return f.sheets()


#获取sheet表的行数
def get_Allrows(f,sheet):
    table=f.sheets()[sheet]
    return table.nrows


#读取文件内容并返回行内容
def getFile(file,shnum):
    f=open_xls(file)
    table=f.sheets()[shnum]
    num=table.nrows
    for row in range(num):
        rdata=table.row_values(row)
        datavalue.append(rdata)
    return datavalue

#获取sheet表的个数
def getshnum(f):
    x=0
    sh=getsheet(f)
    for sheet in sh:
        x+=1
    return x

#函数入口
if __name__=='__main__':
    #定义要合并的excel文件列表
    # allxls=['D:\workspace\excel\新建 Microsoft Excel 2007 工作表 - 副本 (2).xlsx',
    #         'D:/workspace/excel/新建 Microsoft Excel 2007 工作表 - 副本 (3).xlsx',
    #         'D:/workspace/excel/新建 Microsoft Excel 2007 工作表 - 副本 (4).xlsx',
    #         'D:/workspace/excel/新建 Microsoft Excel 2007 工作表 - 副本 (5).xlsx',
    #         'D:/workspace/excel/新建 Microsoft Excel 2007 工作表 - 副本.xlsx',
    #         'D:/workspace/excel/新建 Microsoft Excel 2007 工作表.xlsx'] #列表中的为要读取文件的路径
    #存储所有读取的结果
    datavalue=[]
    rootDir = "D:\workspace\excel"

    for parent,dirnames,filenames in os.walk(rootDir):       
            for filename in filenames :
                fileDir = os.path.join(parent,filename)
                print(fileDir)
                f=open_xls(fileDir)
                x=getshnum(f)
                for shnum in range(x):
                    print("正在读取文件："+str(fileDir)+"的第"+str(shnum)+"个sheet表的内容...")
                    rvalue=getFile(fileDir,shnum)

    for fl in allxls:
        f=open_xls(fl)
        x=getshnum(f)
        for shnum in range(x):
            print("正在读取文件："+str(fl)+"的第"+str(shnum)+"个sheet表的内容...")
            rvalue=getFile(fl,shnum)

    #定义最终合并后生成的新文件
    endfile='D:/workspace/all.xlsx'
    wb=xlsxwriter.Workbook(endfile)
    #创建一个sheet工作对象
    ws=wb.add_worksheet()
    for a in range(len(rvalue)):
        for b in range(len(rvalue[a])):
            c=rvalue[a][b]
            ws.write(a,b,c)
    wb.close()

    print("文件合并完成")