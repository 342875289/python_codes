#!/usr/bin/env python     
# -*- coding: utf-8 -*-     
from win32com.client import Dispatch    
import win32com.client    

import os
class easyExcel:    
    """A utility to make it easier to get at Excel.    Remembering  
    to save the data is your problem, as is    error handling.  
    Operates on one workbook at a time."""    
    def __init__(self, filename=None):  #打开文件或者新建文件（如果不存在的话）  
        #启动一个excel进程
        self.xlApp = win32com.client.DispatchEx('Excel.Application')    
        if filename:#存在文件名则打开文件
            self.filename = filename    
            self.xlBook = self.xlApp.Workbooks.Open(filename)    
        else:       #不存在文件名则创建新文件
            self.xlBook = self.xlApp.Workbooks.Add()    
            self.filename = ''  
        self.xlApp.Visible = False#操作过程不可见
        #self.xlApp.DisplayAlerts = False#关闭错误提示
    def save(self, newfilename=None):  #保存文件  
        if newfilename:    
            self.filename = newfilename    
            self.xlBook.SaveAs(newfilename)    
        else:    
            self.xlBook.Save() 
    def close(self):  #关闭文件  
        self.xlBook.Close(SaveChanges=0)    
        del self.xlApp    
    def setSheet(self,sheet):
        self.sht = self.xlBook.Worksheets(sheet)  
        self.rows_conut = self.sht.usedrange.rows.count
        self.columns_conut = self.sht.usedrange.columns.count
    def getCell(self, row, col):  #获取单元格的数据  
        "Get value of one cell"    
        return self.sht.Cells(row, col).Value    
    def setCell(self, row, col, value):  #设置单元格的数据  
        "set value of one cell"       
        self.sht.Cells(row, col).Value = value  
    def setCellformat(self, row, col):  #设置单元格的数据  
        "set value of one cell"      
        self.sht.Cells(row, col).Font.Size = 15#字体大小  
        self.sht.Cells(row, col).Font.Bold = True#是否黑体  
        self.sht.Cells(row, col).Name = "Arial"#字体类型  
        self.sht.Cells(row, col).Interior.ColorIndex = 3#表格背景  
        #sht.Range("A1").Borders.LineStyle = xlDouble  
        self.sht.Cells(row, col).BorderAround(1,4)#表格边框  
        self.sht.Rows(3).RowHeight = 30#行高  
        self.sht.Cells(row, col).HorizontalAlignment = -4131 #水平居中xlCenter  
        self.sht.Cells(row, col).VerticalAlignment = -4160 #  
    def deleteRow(self, row):  
        self.sht.Rows(row).Delete()#删除行  
        self.sht.Columns(row).Delete()#删除列  
    def getRange(self, row1, col1, row2, col2):  #获得一块区域的数据，返回为一个二维元组  
        "return a 2d array (i.e. tuple of tuples)"    
        return self.sht.Range(self.sht.Cells(row1, col1), self.sht.Cells(row2, col2)).Value     
    def cpSheet(self, before):  #复制工作表  
        "copy sheet"     
        self.shts(1).Copy(None,shts(1))    
#下面是一些测试代码。    
if __name__ == "__main__":    
    #PNFILE = r'c:/screenshot.bmp'  
    try:
        filename_open = 'test.xlsx'
        filename_save = 'test2.xlsx'
        xls = easyExcel(os.getcwd()+'\\'+filename_open)
        xls.setSheet('宣讲会教室借用')
        #xls.setCell(2,'A',130)  
        print(xls.getCell(3,'C'))
        print(xls.getCell(3,'D'))
        print(xls.sht.Cells(3, 'D').Interior.ColorIndex)
        print(xls.sht.Cells(3, 'L').Interior.ColorIndex)
        xls.sht.Range('F3','F4').Merge()
        xls.sht.Cells(3, 'F').Interior.ColorIndex=1
        print(xls.sht.Range('C3','C4').MergeCells == True)
        print(xls.sht.Range('F3','F4').MergeCells == True)
        xls.save(os.getcwd()+'\\'+filename_save)    
        print("finish")
    finally:
        xls.close() 