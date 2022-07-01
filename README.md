# pix2pix_Generate_oracle-bone-script
项目描述：用基于gan的pix2pix模型训练现有的甲骨文图片，实现自动生成甲骨文
# 使用方法：
在demo.py中输入对应汉字
eg: text = u"{0}".format('诺')
即可在output目录下生成对应的原汉字和生成的甲骨文
![image](https://user-images.githubusercontent.com/85725490/176805092-2cc9e737-d508-4e66-96d4-a76faaea90bf.png)
# 模型描述：
 分为生成器和判断器两部分
 当输入了一个汉字，生成器就会努力生成一个“像甲骨文”的图片，判别器则负责判断生成器中生成的图片是生成的“fake”还是真是存在的“real”
 训练的关键在于，如果生成图像通过判别器的检验，我们奖励生成器；如果伪造的图像被识破，我们惩罚生成器。
# 一些训练过程截图：
 ![IMG_0942](https://user-images.githubusercontent.com/85725490/176806561-e37bd0b5-9df0-47a7-a3bd-28573f22fb6d.PNG)

 ![IMG_0941](https://user-images.githubusercontent.com/85725490/176806579-e2fa988f-764a-400e-a311-d4dd13e3dba6.PNG)

  ![IMG_0943](https://user-images.githubusercontent.com/85725490/176806593-902aa661-1e81-4248-83dc-0d8e7d5256b7.PNG)
