import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtSql import *
 
# My function for assembling SQL queries for my 'transactions' table. I'll share the code another time.
from dq_sql import *
 
app = QApplication(sys.argv)
 
class DqTableForm(QWidget):
    def __init__(self, parent = None):
        super(DqTableForm,self).__init__(parent)
 
        self.setWindowTitle('Transactions')
        self.setMinimumWidth(950)
        self.setMinimumHeight(300)
 
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("dataq.db")
        db.open()
 
        self.DqModel = QSqlQueryModel()
 
# My TransQry function takes parameters and returns a SQL query using the parameters as criteria for filtering my 'transactions' table.     
 
self.DqModel.setQuery(TransQry("2014-03-01","2014-03-31","DESC","","","202",""), db)
 
           self.DqTable = QTableView()
           self.DqTable.setModel(self.DqModel)
           self.DqTable.hideColumn(0)
           self.DqTable.resizeColumnsToContents()
           self.DqTable.resizeRowsToContents()
 
           grid = QGridLayout()
           grid.addWidget(self.DqTable,0,0)
           self.setLayout(grid)
form = DqTableForm()
form.show()
app.exec_()
