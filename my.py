import PyPDF2

pdf_filename = 'C:/Users/meme0/Downloads/aaa.pdf'
#my_dict = ({'sp':5, 'ep':6, 'of':'bbb_005_006'},
#           {'sp':100, 'ep':102, 'of':'bbb_100_102'})
my_dict =(
{'sp':7, 'ep':7, 'of':'경영학부_가천대학교_가천바람개비1.pdf'},
{'sp':8, 'ep':8, 'of':'법학과_가천대학교_가천바람개비1.pdf'},
{'sp':9, 'ep':9, 'of':'심리학과_가천대학교_가천바람개비2.pdf'},
{'sp':10, 'ep':10, 'of':'유아교육학과_가천대학교_사회기여자.pdf'},
{'sp':11, 'ep':12, 'of':'자율전공학과_가천대학교_가천바람개비2.pdf'},
{'sp':13, 'ep':13, 'of':'전기공학과_가천대학교_가천바람개비1.pdf'},
{'sp':14, 'ep':14, 'of':'전자공학과_가천대학교_학석사통합.pdf'},
{'sp':15, 'ep':15, 'of':'패션디지안학과_가천대학교_가천바람개비1.pdf'})


# based PyPDF2 3.0.0 
read_pdf = PyPDF2.PdfReader(open(pdf_filename, 'rb'))

for j in my_dict:
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
