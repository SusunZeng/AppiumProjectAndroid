# -*-encoding:utf-8-*-
import pytesseract
from PIL import Image
import os

def main(captcha_final_path='E:/AppiumProjectAndroid/config/captcha_final.png',
         txt_path='E:/AppiumProjectAndroid/config/output.txt'):
    img = Image.open("E:/AppiumProjectAndroid/jpg/1526000632(1).jpg")
    # img.show() #��ͼƬ1.jpg
    # ת�����Ҷ�ͼ
    # img = image.convert('L')
    # �򵥵ģ���ɫ���ַ�
    # text = ''
    # text = pytesseract.image_to_string(image, lang='chi_sim')  # ʹ�ü������Ľ���ͼƬ
    # # text = pytesseract.image_to_string(image)
    # print('text:', text)
    # with open("E:\AppiumProjectAndroid\config\output.txt", "w") as f:  # ��ʶ����������ִ浽����
    #     print('text:', text)
    #     f.write(str(text))
    #     f.close()

    # �½�һ��ͼƬ(��С��ԭͼ��С��ͬ��������ɫΪ255��ɫ)
    print('img.size:', img.size)
    img_new = Image.new('P', img.size, 255)

    print('img.size[1]:', img.size[1])
    print('img.size[0]:', img.size[0])
    for x in range(img.size[1]):
        for y in range(img.size[0]):
            # ����ͼƬ��xy�������ص���ɫ
            pix = img.getpixel((y, x))
            # print('pix:', pix)
            #�Լ���ɫ��r=0s��g=0��b>0Ϊ��ɫ
            if (pix[0] > 200 and pix[1] < 150 and pix[2] < 140) or (pix[0] > 200 and pix[1] < 120 and pix[2] > 30):
                #  or (pix[0] > 200 and pix[1] < 120 and pix[2] > 30)
                #�ѱ����Ľ���ŵ���ͼƬ�ϣ�0Ϊ͸���ȣ���͸��
                img_new.putpixel((y, x), 0)
    img_new.save(captcha_final_path, format = 'png')
    img01 = Image.open(captcha_final_path)
    img01.show()
    #ͨ��tesseract���߽�����֤��ͼƬ�������ı�
    # cmd = 'tesseract '+captcha_final_path+' '+txt_path[0:-4]
    cmd = 'tesseract '+captcha_final_path+' '+txt_path[0:-4] + ' -psm 10 digits'
    print('cmd:', cmd)
    os.system(cmd)

    #��ȡtxt�ļ��������֤��
    with open(txt_path, 'r') as f:
        #ȥ�����ҿո�
        t = f.read().strip()
        print('t1:', t)
        #ȥ���м�ո�
        if ' ' in t:
            t = t.replace(' ', '')
            print('t2:', t)
        #����������ҳ���Ϊ4���ͷ������֣�������Ǿͷ��� fail
        if t.isdigit() and len(t) == 4:
            print('t3:', t)
            return t
        else:
            return 'fail'

if __name__ == '__main__':
    main_reslut = main()
    print('�����', main_reslut)