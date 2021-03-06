__author__ = 'xskylarx'
# -*- coding: utf-8 -*-

# Python + PyQt4 By Skylar
#
# Creado: 29 - sep - 2013
#      Por: xskylarx
# xskyofx@gmail.com
# Por favor si modificas algo haz referencia al autor.
from pafy import  Pafy # esta es la libreria para leer la informacion
from PyQt4 import QtGui, QtCore
from inicio import Ui_Form
import urllib.request
import os
import sys
import subprocess


class v_skytube(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.vskytube = Ui_Form()
        self.vskytube.setupUi(self)
        self.connect(self.vskytube.btn_valida,QtCore.SIGNAL('clicked()'), self.valida)
        self.resize(579,66)
        self.vskytube.label_7.setStyleSheet("color:grey;")
        self.setWindowTitle('SkyTube Download v.1.1')
        self.setMaximumSize(579,250)
        self.setMinimumSize(579,66)
        self.vskytube.groupBox.setVisible(False)
        self.connect(self.vskytube.btn_valida_2,QtCore.SIGNAL('clicked()'), self.descarga)
        self.connect(self.vskytube.btn_vlc,QtCore.SIGNAL('clicked()'), self.AbreVLC)
        self.connect(self.vskytube.btn_otro,QtCore.SIGNAL('clicked()'), self.muestra)
        self.vskytube.lbl_desc.setVisible(False)
        self.vskytube.btn_vlc.setVisible(False)
        self.vskytube.btn_otro.setVisible(False)
        self.connect(self.vskytube.btn_folder,QtCore.SIGNAL('clicked()'), self.folder)

    def folder(self):
        perfil = (os.path.join (os.environ['USERPROFILE'],'videos'))
        subprocess.Popen('explorer ' + str(perfil))

    def descarga(self):
        try:

            self.vskytube.lineEdit.setVisible(False)
            self.vskytube.btn_valida.setVisible(False)
            self.vskytube.label_7.setVisible(False)
            self.vskytube.lbl_desc.setStyleSheet("color:red;")
            self.vskytube.lbl_desc.setText('Tu video se esta descargado, puede tardar varios minutos ...')
            self.vskytube.lbl_desc.setVisible(True)
            self.resize(579,66)
            QtGui.QMessageBox.about(self,'Empezando Descarga ... ','La descarga puede tardar varios minutos, dependiendo de tu conexion ...')
            global url
            os.system('skytubec.exe ' + url)
            self.vskytube.lbl_desc.setStyleSheet("color:green;")
            self.vskytube.lbl_desc.setText('Tu video se descargo correctamente ...')
            self.vskytube.btn_vlc.setVisible(True)
            self.vskytube.btn_otro.setVisible(True)
            if os.path.isfile('c:\progra~1\VideoLAN\VLC\\vlc.exe') or os.path.isfile('c:\progra~2\VideoLAN\VLC\\vlc.exe'):
                self.vskytube.btn_vlc.setEnabled(True)
            else:
                self.vskytube.btn_vlc.setEnabled(False)

        except Exception as e:
            QtGui.QMessageBox.about(self,'Error Descarga', str(e))



    def muestra(self):
        self.vskytube.lineEdit.setVisible(True)
        self.vskytube.btn_valida.setVisible(True)
        self.vskytube.label_7.setVisible(True)
        self.vskytube.lbl_desc.setVisible(False)
        self.vskytube.btn_vlc.setVisible(False)
        self.vskytube.btn_otro.setVisible(False)
        self.vskytube.groupBox.setVisible(False)
        self.vskytube.lineEdit.clear()

    def AbreVLC(self):

        best = video.getbest(preftype="mp4")
        titulo = best.title
        titulo = str(titulo).replace('"','')
        perfil = (os.path.join (os.environ['USERPROFILE'],'videos'))
        #QtGui.QMessageBox.about(self,'ff','"' + os.path.abspath(os.path.dirname(__file__)) + '\\videos\\' + best.title + '.' + best.extension + '"' )
        if os.path.isfile('c:\progra~1\VideoLAN\VLC\\vlc.exe'):
            subprocess.Popen('c:\progra~1\VideoLAN\VLC\\vlc.exe "' +str(perfil) + '\\' + titulo + '.' + best.extension + '"' )
        else:
             subprocess.Popen('c:\progra~2\VideoLAN\VLC\\vlc.exe "' + str(perfil) + '\\' + titulo + '.' + best.extension + '"' )


    def valida(self):
        try:
            self.vskytube.groupBox.setVisible(False)
            self.resize(579,66)
            self.vskytube.lbl_imagen.setText('sin imagen')
            if os.path.isfile(os.path.dirname(sys.executable)+ '\\skytube.jpg'):
                os.remove(os.path.dirname(sys.executable) + '\\skytube.jpg')

            self.vskytube.groupBox.setVisible(True)
            video_id = self.vskytube.lineEdit.text()

            if video_id.split('?v=') == 1:
                video_id = video_id.split('?v=')

            if len(video_id) == 1:
                global url
                url= 'http://www.youtube.com/watch?v=' + video_id[1]
            else:
                global url
                url= 'http://www.youtube.com/watch?v=' + video_id



            global video

            video = Pafy(url)
            best = video.getbest(preftype="mp4")
            self.vskytube.lbl_calidad.setText(best.resolution + ' Extencion: ' + best.extension)

            self.vskytube.groupBox.setStyleSheet("color:green;")
            self.vskytube.groupBox.setTitle(video.title)
            self.vskytube.lbl_autor.setText(video.author)
            self.vskytube.lbl_duracion.setText(video.duration)
            self.vskytube.lbl_id.setText(video.videoid)
            self.vskytube.lbl_rating.setText(str(video.rating))
            self.vskytube.lbl_visto.setText(str(video.viewcount))
            self.resize(579,250)


            #os.chdir(os.path.dirname(sys.executable))
            url = video.thumb
            file = ('skytube.jpg')
            urllib.request.urlretrieve(url, file)
            img = (os.path.dirname(sys.executable) + '\skytube.jpg')
            #img = (video.thumb)
            #self.vskytube.lbl_imagen.setText('<img src="'+ img +'" />')
            self.vskytube.lbl_imagen.setPixmap(QtGui.QPixmap(img))
        except Exception as e:
            QtGui.QMessageBox.about(self,'Error SkyTube ',' No existe el video favor de verificar.')
            QtGui.QMessageBox.about(self,'Error SkyTube ',str(e))

def main():
    app = QtGui.QApplication(sys.argv)
    vskytube = v_skytube()
    vskytube.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


