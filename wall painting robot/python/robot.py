import sys
import serial
import serial.tools.list_ports
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtCore import Qt

class serialThreadClass(QtCore.QThread):  # Seri Porttan veri okuma işlemi için QThread Kullanıldı.

    message = QtCore.pyqtSignal(str)
    def __init__(self,parent = None):

        super(serialThreadClass,self).__init__(parent)
        self.serialPort = serial.Serial()
        self.stopflag = False
    def stop(self):
        self.stopflag = True
    def run(self):
        while True:
            if (self.stopflag):
                self.stopflag = False
                break
            elif(self.serialPort.isOpen()): # eğer seri Port bağlı değil iken veri okumayı denersek hata verir.
                try:                        # bu hatayı yakalayabilmek için "try" bloğu kullanıldı.
                    self.data = self.serialPort.readline()
                except:
                    print("HATA\n")
                self.message.emit(str(self.data.decode()))

class Pencere(QtWidgets.QWidget):  
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.com_portlar=QtWidgets.QComboBox()
        self.ports = serial.tools.list_ports.comports()
        for i in self.ports:
            self.com_portlar.addItem(str(i))
        self.baudComboBox =QtWidgets.QComboBox()
        baud= ["2400", "4800", "9600", "19200", "38400"]
        for i in baud:
            self.baudComboBox.addItem(i)
        self.baglan =QtWidgets.QPushButton("Bağlan")
        self.baglantiKes =QtWidgets.QPushButton("Bağlantıyı Kes")
        self.home =QtWidgets.QPushButton("Home Pozisyonu")
        self.b_yukari =QtWidgets.QPushButton("Yukarı")
        self.b_asagi =QtWidgets.QPushButton("Aşağı")
        self.b_dur = QtWidgets.QPushButton("Durdur")
        self.r_saga = QtWidgets.QPushButton("Sağa")
        self.r_sola = QtWidgets.QPushButton("Sola")
        self.r_dur = QtWidgets.QPushButton("Durdur")
        self.acil_stop=QtWidgets.QPushButton("Acil Stop!")
        self.label1=QtWidgets.QLabel("COM PORT:")
        self.label2=QtWidgets.QLabel("BoudRate:")
        self.label3=QtWidgets.QLabel('<font color=red>Bağlı Değil</font>')
        self.label3.setAlignment(Qt.AlignCenter)
        self.label4=QtWidgets.QLabel("Boya Tabancası:")
        self.label5=QtWidgets.QLabel("Boya Tabancası:")
        self.label6=QtWidgets.QLabel("Boya Tabancası:")
        self.group1=QtWidgets.QButtonGroup()
        self.r1=QtWidgets.QRadioButton("Çalıştır")
        self.r2=QtWidgets.QRadioButton("Durdur")
        self.r2.setChecked(True)
        self.group1.addButton(self.r1)
        self.group1.addButton(self.r2)
        
        self.message = QtWidgets.QTextEdit()
        self.message.setReadOnly(True)
        self.messageTitle = QtWidgets.QLabel("Gelen Mesaj")
        ##########COM PORT BAUDRATE KISMI##################
        self.form=QtWidgets.QFormLayout()
        self.hbox1=QtWidgets.QHBoxLayout()
        self.hbox1.addWidget(self.label1)
        self.hbox1.addWidget(self.com_portlar)
        self.hbox1.addWidget(self.label2)
        self.hbox1.addWidget(self.baudComboBox)
        self.form.addRow(self.hbox1)
        ###### Bağlı - Bağlı Değil Labeli###########
        self.form.addRow(self.label3)
        ###### Bağlan - Bağlantıyı Kes Butonları######
        self.hbox6=QtWidgets.QHBoxLayout()
        self.hbox6.addWidget(self.baglan)
        self.hbox6.addWidget(self.baglantiKes)
        self.form.addRow(self.hbox6)
        ###### Home Pozisyonu Butonu###################
        self.hbox8=QtWidgets.QHBoxLayout()
        self.hbox8.addWidget(self.home)
        self.form.addRow(self.hbox8)
        ###### Boya Püskürtme Radio Butonları##########
        self.hbox2=QtWidgets.QHBoxLayout()
        self.hbox2.addWidget(self.label4)
        self.hbox2.addWidget(self.r1)
        self.hbox2.addWidget(self.r2)
        self.form.addRow(self.hbox2)
        ###### Boya Tabancası Yukarı -Dur - Aşağı Butonları#######
        self.hbox3=QtWidgets.QHBoxLayout()
        self.hbox3.addWidget(self.label5)
        self.hbox3.addWidget(self.b_yukari)
        self.hbox3.addWidget(self.b_dur)
        self.hbox3.addWidget(self.b_asagi)
        self.form.addRow(self.hbox3)
        ###### Boya Tabancası Sola - Dur - Sağa Butınları#########
        self.hbox4=QtWidgets.QHBoxLayout()
        self.hbox4.addWidget(self.label6)
        self.hbox4.addWidget(self.r_sola)
        self.hbox4.addWidget(self.r_dur)
        self.hbox4.addWidget(self.r_saga)
        self.form.addRow(self.hbox4)
        ###### Acil Stop#####################
        self.hbox5=QtWidgets.QHBoxLayout()
        self.hbox5.addWidget(self.acil_stop)
        self.form.addRow(self.hbox5)
        
        self.hbox7=QtWidgets.QHBoxLayout()
        self.hbox7.addWidget(self.message)
        self.form.addRow(self.hbox7)
        
        self.resim = QtWidgets.QLabel(self)
        self.resim.setPixmap(QtGui.QPixmap("klu.jpg"))
        self.vbox=QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.resim)
        self.form.addRow(self.vbox)
        self.resim.setAlignment(Qt.AlignCenter)
        self.resim.move(70,100)
        self.setGeometry(100,100,500,500)
        self.setLayout(self.form)
        
       
        
        self.mySerial = serialThreadClass()  # pencere sınıfının içerisinde serialThreadClass nesnesi oluşturuldu.
        self.mySerial.message.connect(self.messageTextEdit)  # seri porttan mesaj geldiğinde messageTextEdit fonksiyonuna dallan.
        self.mySerial.start() 
        
        self.baglan.clicked.connect(self.serialConnect) # Butona tıklandığında serialConnection isimli fonksiyona dallan.
        self.baglantiKes.clicked.connect(self.serialDisconnect)
        self.home.clicked.connect(lambda: self.calis(self.home))
        self.b_yukari.clicked.connect(lambda: self.calis(self.b_yukari))   # Bu yüzden leds fonksiyonunun içine buton parametresi
        self.b_dur.clicked.connect(lambda: self.calis(self.b_dur)) # yazıldı.
        self.b_asagi.clicked.connect(lambda: self.calis(self.b_asagi))
        self.r_sola.clicked.connect(lambda: self.calis(self.r_sola))
        self.r_dur.clicked.connect(lambda: self.calis(self.r_dur))
        self.r_saga.clicked.connect(lambda: self.calis(self.r_saga))
        self.acil_stop.clicked.connect(lambda: self.calis(self.acil_stop))
        self.r1.toggled.connect(lambda:self.calis(self.r1))
        self.r2.toggled.connect(lambda:self.calis(self.r2))
        
        self.setWindowTitle("Duvar Boyama Robotu")
        self.show()
    
    def serialConnect(self): # "Bağlan" butonuna tıklandığında bu fonksiyona dallanacak.
        self.portText = self.com_portlar.currentText() # port combobox'ın içinde hangi değer varsa çekildi.
        self.port = self.portText.split() # combo box'ın içerisinde bize lazım olan sadece "COM13" kısmı. Bu yüzden split ile kelimeler ayrıldı.
        self.baudrate = self.baudComboBox.currentText()# comboBox'ın içindeki baudrate değeri çekildi.
        self.mySerial.serialPort.baudrate = int(self.baudrate) # seriport baudrate ayarı tanımlandı.
        self.mySerial.serialPort.port = self.port[0]
        try:
            self.mySerial.serialPort.open() # seri porta bağlanma komutu verildi.
        except:
            self.message.append("Bağlantı Hatası!!")
        if(self.mySerial.serialPort.isOpen()):
            self.label3.setText('<font color=green>Bağlandı</font>') # bağlantı sağlandıysa label1 yeşile dönsün.
            self.baglan.setEnabled(False)       # Bağlantı varken tekrar bağlan butonuna tıklanmasın diye butonu pasif ediyoruz.
            self.com_portlar.setEnabled(False) # Bağlantı varken port ve baudrate seçimi yapılmasın diye
            self.baudComboBox.setEnabled(False) # kullanıcının seçim yapmasını engelliyoruz.

    def serialDisconnect(self): # "Bağlantı Kes" butonuna tıklandığında bu fonksiyona dallanacak.
        if self.mySerial.serialPort.isOpen():
            self.mySerial.serialPort.write("7".encode())
            self.mySerial.serialPort.close()
            if self.mySerial.serialPort.isOpen()== False:
                self.label3.setText('<font color=red>Bağlantı Kesildi</font>')
                self.baglan.setEnabled(True)
                self.com_portlar.setEnabled(True)
                self.baudComboBox.setEnabled(True)
        else:
            self.message.append("Seriport Zaten Kapalı.")
    def messageTextEdit(self):  # seri porttan mesaj geldiğinde bu fonksiyon çalıştırılacak.
        self.incomingMessage = str(self.mySerial.data.decode())
        self.message.append(self.incomingMessage)
    
    def calis(self,secim):
        if secim == self.r1:
            if self.mySerial.serialPort.isOpen():
                self.mySerial.serialPort.write("8".encode())  # seri porttan Arduino'ya 1 karakteri gönderildi.
            else:
                self.message.append("Seri Port Bağlı Değil.")
        elif secim == self.r2:
            if self.mySerial.serialPort.isOpen():
                self.mySerial.serialPort.write("9".encode())  # seri porttan Arduino'ya 1 karakteri gönderildi.
            else:
                self.message.append("Seri Port Bağlı Değil.")
        if secim == self.b_yukari:
            if self.mySerial.serialPort.isOpen():
                self.mySerial.serialPort.write("1".encode())  # seri porttan Arduino'ya 1 karakteri gönderildi.
            else:
                self.message.append("Seri Port Bağlı Değil.")
        elif secim == self.b_dur:
            if self.mySerial.serialPort.isOpen():
                self.mySerial.serialPort.write("2".encode())
            else:
                self.message.append("Seri Port Bağlı Değil.")
        elif secim == self.b_asagi:
            if self.mySerial.serialPort.isOpen():
                self.mySerial.serialPort.write("3".encode())
            else:
                self.message.append("Seri Port Bağlı Değil.")
        elif secim == self.r_sola:
            if self.mySerial.serialPort.isOpen():
                self.mySerial.serialPort.write("4".encode())
            else:
                self.message.append("Seri Port Bağlı Değil.")
        elif secim == self.r_dur:
            if self.mySerial.serialPort.isOpen():
                self.mySerial.serialPort.write("5".encode())
            else:
                self.message.append("Seri Port Bağlı Değil.")
        elif secim == self.r_saga:
            if self.mySerial.serialPort.isOpen():
                self.mySerial.serialPort.write("6".encode())
            else:
                self.message.append("Seri Port Bağlı Değil.")
        elif secim == self.acil_stop:
            if self.mySerial.serialPort.isOpen():
                self.mySerial.serialPort.write("7".encode())
            else:
                self.message.append("Seri Port Bağlı Değil.")
        elif secim == self.home:
            if self.mySerial.serialPort.isOpen():
                self.mySerial.serialPort.write("h".encode())
            else:
                self.message.append("Seri Port Bağlı Değil.")
    
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    pen = Pencere()
    sys.exit(app.exec_())
