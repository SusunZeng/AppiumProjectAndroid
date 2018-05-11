# -*-encoding:utf-8-*-
import pytesseract
from PIL import Image
import os

def main(captcha_final_path='E:/AppiumProjectAndroid/config/captcha_final.png',
         txt_path='E:/AppiumProjectAndroid/config/output.txt'):
    img = Image.open("E:/AppiumProjectAndroid/jpg/1526000632(1).jpg")
    # img.show() #打开图片1.jpg
    # 转化到灰度图
    # img = image.convert('L')
    # 简单的，纯色的字符
    # text = ''
    # text = pytesseract.image_to_string(image, lang='chi_sim')  # 使用简体中文解析图片
    # # text = pytesseract.image_to_string(image)
    # print('text:', text)
    # with open("E:\AppiumProjectAndroid\config\output.txt", "w") as f:  # 将识别出来的文字存到本地
    #     print('text:', text)
    #     f.write(str(text))
    #     f.close()

    # 新建一张图片(大小和原图大小相同，背景颜色为255白色)
    print('img.size:', img.size)
    img_new = Image.new('P', img.size, 255)

    print('img.size[1]:', img.size[1])
    print('img.size[0]:', img.size[0])
    for x in range(img.size[1]):
        for y in range(img.size[0]):
            # 遍历图片的xy坐标像素点颜色
            pix = img.getpixel((y, x))
            # print('pix:', pix)
            #自己调色，r=0s，g=0，b>0为蓝色
            if (pix[0] > 200 and pix[1] < 150 and pix[2] < 140) or (pix[0] > 200 and pix[1] < 120 and pix[2] > 30):
                #  or (pix[0] > 200 and pix[1] < 120 and pix[2] > 30)
                #把遍历的结果放到新图片上，0为透明度，不透明
                img_new.putpixel((y, x), 0)
    img_new.save(captcha_final_path, format = 'png')
    img01 = Image.open(captcha_final_path)
    img01.show()
    #通过tesseract工具解析验证码图片，生成文本
    # cmd = 'tesseract '+captcha_final_path+' '+txt_path[0:-4]
    cmd = 'tesseract '+captcha_final_path+' '+txt_path[0:-4] + ' -psm 10 digits'
    print('cmd:', cmd)
    os.system(cmd)

    #读取txt文件里面的验证码
    with open(txt_path, 'r') as f:
        #去掉左右空格
        t = f.read().strip()
        print('t1:', t)
        #去掉中间空格
        if ' ' in t:
            t = t.replace(' ', '')
            print('t2:', t)
        #如果是数字且长度为4，就返回数字，如果不是就返回 fail
        if t.isdigit() and len(t) == 4:
            print('t3:', t)
            return t
        else:
            return 'fail'

if __name__ == '__main__':
    main_reslut = main()
    print('结果：', main_reslut)