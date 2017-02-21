def geoPic(file='tree.jpg'):

    import PIL.Image
    img = PIL.Image.open(file)
    exif_data = img._getexif()
    # 详细标签信息，参考http://stackoverflow.com/questions/4764932/in-python-how-do-i-read-the-exif-data-for-an-image
    # import PIL.ExifTags
    # exif = {
    #   PIL.ExifTags.TAGS[k]: v
    #   for k, v in img._getexif().items()
    #   if k in PIL.ExifTags.TAGS
    # }
    DataTime_ = exif_data[306]
    data_, time_ = DataTime_.split(' ')
    data_ = u'{0}年{1}月{2}日'.format(*data_.split(':'))
    time_ = u'{0}时{1}分{2}秒'.format(*time_.split(':'))

    GPSInfo = exif_data[34853]
    # 'GPSInfo': {
    #     1: 'N',
    #     2: ((34, 1), (1, 1), (374844, 10000)),
    #     3: 'E',
    #     4: ((108, 1), (47, 1), (152088, 10000)),
    #     5: (200, 100),
    #     6: (0, 1000),
    #     7: ((2, 1), (51, 1), (7, 1)),
    #     27: 'ASCII\x00\x00\x00NETWORK',
    #     29: '2015:11:19'
    # }
    # http://www.exiv2.org/tags.html 末尾有信息注解

    def dms2de(dms):
        # ((34, 1), (1, 1), (374844, 10000)) -> 34.027079
        # (degrees, minutes, seconds) -> decimal
        de = dms[0][0] / dms[0][1] \
            + dms[1][0] / dms[1][1] / 60 \
            + dms[2][0] / dms[2][1] / 3600
        if GPSInfo[1] in ('W', 'S'):
            de *= -1
        return de
    try:
        lat, lng = dms2de(GPSInfo[2]), dms2de(GPSInfo[4])
        return data_, time_, lat, lng
    except:
        return None

if __name__ == '__main__':
    import os
    os.chdir(r'E:\python\2017_2_15')
    print(geoPic())
