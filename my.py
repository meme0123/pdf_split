import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QFileDialog, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon
import PyPDF2



# PyQt5
class my_win(QWidget):
    pdf_filename = ''
    my_dict =(
{'sp':38, 'ep':38, 'of':'글로벌융합공학부_연세대_학생부종합_활동우수형.pdf'},
{'sp':39, 'ep':39, 'of':'시스템반도체공학_연세대_학생부종합_시스템반도체특별전형.pdf'},
{'sp':40, 'ep':40, 'of':'아시아학전공_연세대_학생부종합_국제형(국내고).pdf'},
{'sp':41, 'ep':41, 'of':'언더우드학부(인문.사회)_연세대_특기자전형_특기자전형.pdf'},
{'sp':42, 'ep':42, 'of':'융합인문사회과학부(HASS)_연세대_학생부종합_국제형(국내고)1.pdf'},
{'sp':43, 'ep':43, 'of':'융합인문사회과학부(HASS)_연세대_학생부종합_국제형(국내고)2.pdf'},
{'sp':44, 'ep':45, 'of':'융합인문사회과학부(HASS)_연세대_학생부종합_국제형(국내고)3.pdf'},
{'sp':46, 'ep':46, 'of':'융합인문사회과학부(HASS)_연세대_학생부종합_국제형(국내고)4.pdf'},
{'sp':47, 'ep':47, 'of':'중어중문학과_연세대_학생부종합_면접형.pdf'},
{'sp':48, 'ep':49, 'of':'철학과_연세대_학생부종합_활동우수형.pdf'},
{'sp':50, 'ep':50, 'of':'컴퓨터과학과_연세대_학생부종합_면접형.pdf'},
{'sp':75, 'ep':75, 'of':'교육공학과_이화여대_학생부교과_고교추천전형.pdf'},
{'sp':76, 'ep':76, 'of':'교육학과_이화여대_학생부교과_고교추천전형.pdf'},
{'sp':77, 'ep':77, 'of':'사이버보안학과_이화여대_학생부종합_과학특기자전형.pdf'},
{'sp':78, 'ep':78, 'of':'사회과교육과 사회교육전공_이화여대_학생부교과_고교추천전형.pdf'},
{'sp':79, 'ep':79, 'of':'유아교육과_이화여대_학생부교과_교교추천전형.pdf'},
{'sp':80, 'ep':80, 'of':'화학생명분자과학부_이화여대_학생부교과_학교장추천.pdf'},
{'sp':82, 'ep':82, 'of':'건축학부_인하대학교_학생부종합_인하미래인재.pdf'},
{'sp':83, 'ep':84, 'of':'기계공학과_인하대학교_학생부종합_인하미래인재.pdf'},
{'sp':85, 'ep':85, 'of':'기계공학과_인하대학교_학생부종합_인하미래인재2.pdf'},
{'sp':86, 'ep':86, 'of':'사회인프라공학과_인하대학교_학생부종합_인하미래인재.pdf'},
{'sp':87, 'ep':87, 'of':'생명공학과_인하대학교_학생부종합_인하미래인재.pdf'},
{'sp':88, 'ep':88, 'of':'전자공학과_인하대학교_학생부종합_인하미래인재.pdf'},
{'sp':89, 'ep':89, 'of':'컴퓨터공학과_인하대학교_학생부종합_인하미래인재.pdf'},
{'sp':90, 'ep':90, 'of':'항공우주공학과_인하대학교_학생부종합_인하미래인재.pdf'},
{'sp':91, 'ep':91, 'of':'화학공학과_인하대학교_학생부종합_인하미래인재.pdf'},
{'sp':105, 'ep':105, 'of':'초등교육과_청주교육대학교_학생부종합_배움나눔인재전형1.pdf'},
{'sp':106, 'ep':106, 'of':'초등교육과_청주교육대학교_학생부종합_배움나눔인재전형2.pdf'},
{'sp':107, 'ep':107, 'of':'초등교육과_청주교육대학교_학생부종합_배움나눔인재전형3.pdf'},
{'sp':108, 'ep':108, 'of':'국어교육과_청주교육대학교_학생부교과_일반전형, 교과우수전형.pdf'},
{'sp':161, 'ep':161, 'of':'기계공학과_한국기술교육대학교_학생부종합_농어촌.pdf'},
{'sp':162, 'ep':162, 'of':'기계공학과_한국기술교육대학교_학생부종합_창의인재.pdf'},
{'sp':163, 'ep':163, 'of':'기계공학부_한국기술교육대학교_학생부종합_창의인재.pdf'},
{'sp':164, 'ep':164, 'of':'기계공학부_한국기술교육대학교_학생부종합_지역인재1.pdf'},
{'sp':165, 'ep':165, 'of':'기계공학부_한국기술교육대학교_학생부종합_지역인재2.pdf'},
{'sp':166, 'ep':167, 'of':'디자인공학부_한국기술교육대학교_학생부종합_창의인재.pdf'},
{'sp':168, 'ep':168, 'of':'에너지신소재화학공학부_한국기술교육대학교_학생부종합_지역인재.pdf'},
{'sp':169, 'ep':170, 'of':'전기전자통신공학부_한국기술교육대학교_학생부종합_지역인재.pdf'},
{'sp':171, 'ep':172, 'of':'컴퓨터공학과_한국기술교육대학교_학생부종합_지역인재1.pdf'},
{'sp':173, 'ep':173, 'of':'컴퓨터공학과_한국기술교육대학교_학생부종합_지역인재2.pdf'},
{'sp':174, 'ep':174, 'of':'컴퓨터공학과_한국기술교육대학교_학생부종합_창의인재.pdf'})

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('DongTan Sparta - PDF Split')
        self.setGeometry(300,300,500,300)

        self.Lgrid = QGridLayout()
        self.setLayout(self.Lgrid)

        self.label1 = QLabel('Open PDF file:', self)
        my_button1 = QPushButton('Open PDF File', self)
        my_button2 = QPushButton('Run', self)
        self.label2 = QLabel('Starting Page:', self)
        self.line_edit = QLineEdit(self)

        self.Lgrid.addWidget(self.label1, 1, 1)
        self.Lgrid.addWidget(my_button1, 2, 1)
        self.Lgrid.addWidget(my_button2, 3, 1)
        self.Lgrid.addWidget(self.label2, 4, 1)
        self.Lgrid.addWidget(self.line_edit, 5, 1)

        my_button1.clicked.connect(self.my_open_file)
        my_button2.clicked.connect(self.pdf_split)

        self.show()

    def my_open_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Open pdf file', './')
        if fname[0]:
            self.label1.setText('Open PDF file:' + fname[0])
            self.pdf_filename = fname[0]

    # based PyPDF2 3.0.0
    def pdf_split(self):
        read_pdf = PyPDF2.PdfReader(open(self.pdf_filename, 'rb'))

        for j in self.my_dict:
            write_pdf = PyPDF2.PdfWriter()

            my_page = read_pdf.pages[j['sp']-1]
            write_pdf.add_page(my_page)
            print(j['sp'])

            for i in range(j['sp'], j['ep']):
                my_page = read_pdf.pages[i-1]
                write_pdf.add_page(my_page)
                print('i:' + str(i))

            print(j['of'])
            write_pdf.write(open('C:/Users/meme0/Downloads/' + j['of'], 'wb'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = my_win()
    sys.exit(app.exec())