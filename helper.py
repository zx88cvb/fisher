def is_isbn_or_key(word):
    """
    是否为isbn或key
    :param word: 输入查询字符
    :return: 返回key or isbn
    """

    # isbn isbn13 13个0到9数组组成
    # isbn13 10个数字 含有一些 '-'

    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'

    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'

    return isbn_or_key