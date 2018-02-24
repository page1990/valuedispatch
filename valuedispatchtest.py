from valuedispatch import valuedispatch


def show_all():
    print('that is in all!')


@valuedispatch
def encode(encoding, *args, **kwargs):
    print('encoding in default utf-8', args, encoding)
    # show_all()


@encode.register('base32')
def encode_base32(encoding, *args, **kwargs):
    print('encoding in base32', args, encoding)
    # show_all()


@encode.register('gb2312')
def encode_gb2312(encoding, *args, **kwargs):
    # text_value = kwargs.get('text_value', 0)
    print('encoding in gb2312')
    # print('text_value is', text_value)
    # show_all()


@encode.register('xxx')
def encode_xxx(encoding, *args, **kwargs):
    print('encoding in xxx', args, encoding)
    # show_all()


def main():
    kwargs = {'text_value': 'ok'}
    encode('base32', 'processed by base32')
    encode('gb2312', 'processed by gb2312', **kwargs)
    # encode('xxx', 'processed by xxx', **kwargs)
    # encode('utf-8', 'processed by utf-8')


if __name__ == "__main__":
    main()
