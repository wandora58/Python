
import os
import string


# templates フォルダのパスを返す関数
def get_template_dir_path():
    template_dir_path = None
    try:
        # settings.py にパス情報が書いてあるならここで templates フォルダのパスを取得
        import settings
        if settings.TEMPLATE_PATH:
            template_dir_path = settings.TEMPLATE_PATH
    except ImportError:
        pass

    if not template_dir_path:
        # robot/views/console.py の robot までの絶対パスを取得
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # robot/templates が templates フォルダのパス
        template_dir_path = os.path.join(base_dir, 'templates')

    return template_dir_path


# template ファイルが見つからない時のエラー処理
class NoTemplateError(Exception):
    """No Template Error"""


# template ファイルのパスを見つける関数、引数はファイル名
def find_template(temp_file):

    # templates フォルダを取得
    template_dir_path = get_template_dir_path()

    # template ファイルのパスを取得
    temp_file_path = os.path.join(template_dir_path, temp_file)
    if not os.path.exists(temp_file_path):
        raise NoTemplateError('Could not find {}'.format(temp_file))

    return temp_file_path


# template ファイルの中身を返す関数
def get_template(template_file_path):

    # template ファイルのパスを取得
    template = find_template(template_file_path)

    with open(template, 'r', encoding='utf-8') as template_file:
        contents = template_file.read()

        # splitter: ====== の文字列をつける
        # sep: 改行
        # contents: コンテンツ
        contents = contents.rstrip(os.linesep)
        contents = '{splitter}{sep}{contents}{sep}{splitter}{sep}'.format(
            contents=contents, splitter="=" * 60, sep=os.linesep)

        return string.Template(contents)
