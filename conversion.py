# This Python file uses the following encoding: utf-8
import os, sys
from pathlib import Path
from dbm import dBm
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QShortcut
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QKeySequence
from functools import partial

class Conversion(QWidget):

    def __init__(self):
        super(Conversion, self).__init__()
        self.setWindowTitle("dBm conv")
        self.load_ui()
        self.dbm = dBm()       
        d = self.dbm      
        self.s=""
        u = self.ui
        self.EDITS = { u.edt_dbm : d.set_dbm, 
            u.edt_volt_p : d.set_v_p, 
            u.edt_volt_rms : d.set_v_rms, 
            u.edt_watts : d.set_w, 
            u.edt_volt_pp : d.set_v_pp }        
        self.connect_widgets()
        self.ui.edt_dbm.setText('0')
        self.update_widgets()  
        QShortcut(QKeySequence('Ctrl+s'), self, self.save)
    
    def connect_widgets(self):
        for edt in self.EDITS:
            edt.editingFinished.connect(partial(self.set_edt, \
                edt, self.EDITS[edt]))
        
    def save(self):
        fn, pattern = QFileDialog.getSaveFileName(self)
        if len(fn) == 0:
            return
        open(fn, "w").write('%s' % self.dbm)
    
    def set_edt(self, edt, f):
        f(float(edt.text()))
        self.update_widgets()
        
    def update_widgets(self):
        d = dict(zip(self.EDITS.keys(), self.dbm.get_values()))
        for k in d:
            k.setText("%.3g" % d[k])
        
    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

if __name__ == "__main__":
    app = QApplication([])
    widget = Conversion()
    widget.show()
    sys.exit(app.exec_())
