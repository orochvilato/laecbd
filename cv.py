from PIL import Image
for i in range(59):
    #img = Image.open("img/jlm_%02d.jpg" % i)
    img = Image.open('pages/{p}-large.jpg'.format(p=i+1))
    img.save('pages/{p}.jpg'.format(p=i+1),'jpeg')
    img.thumbnail((50,100),Image.ANTIALIAS)
    img.save('pages/{p}-thumb.jpg'.format(p=i+1),'jpeg')
