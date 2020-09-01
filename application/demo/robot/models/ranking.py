import csv
import collections
import os
import pathlib

RANKING_COLUMN_NAME = 'NAME'
RANKING_COLUMN_COUNT = 'COUNT'
RANKING_CSV_FILE_PATH = 'ranking.csv'

class CsvModel:
    def __init__(self, csv_file):
        self.csv_file = csv_file

        # csv ファイルが存在しないなら空のファイルを作る
        if not os.path.exists(self.csv_file):
            pathlib.Path(csv_file).touch()

class RankingModel(CsvModel):

    def __init__(self, csv_file=None, *args, **kargs):
        if not csv_file:
            csv_file = self.get_csv_file_path()
            super().__init__(csv_file)
            self.column = [RANKING_COLUMN_NAME, RANKING_COLUMN_COUNT]
            self.data = collections.defaultdict(int)
            self.load_data()


    # csv ファイルのパスを返す関数
    def get_csv_file_path(self):
        csv_file_path = None

        # settings.py にパス情報が書いてあるならここで templates フォルダのパスを取得
        try:
            import settings
            if settings.CSV_FILE_PATH:
                csv_file_path = settings.CSV_FILE_PATH
        except ImportError:
            pass

        # 書いていないなら RANKING_CSV_FILE_PATH のパスを取得
        if not csv_file_path:
            csv_file_path = RANKING_CSV_FILE_PATH
        return csv_file_path


    # データの読み込み
    def load_data(self):
        with open(self.csv_file, 'r+') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                self.data[row[RANKING_COLUMN_NAME]] = int(
                    row[RANKING_COLUMN_COUNT])
        return self.data


    # 一番人気な店の取得
    def get_most_popular(self, not_list=None):

        # リストが None ならリストの空配列を取得
        if not_list is None:
            not_list = []

        # データがない = csv に何も書き込まれていないときは None を返す
        if not self.data:
            return None

        # 辞書を値でソート(返り値はリスト)
        sorted_data = sorted(self.data, key=self.data.get, reverse=True)

        # not_list にない店を取得して返す
        for name in sorted_data:
            if name in not_list:
                continue
            return name


    # ユーザーの好きな店の Count をインクリメントする関数
    def increment(self, name):
        self.data[name.title()] += 1
        self.save()


    # csv ファイルに値を保存する関数
    def save(self):
        with open(self.csv_file, 'w+') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.column)
            writer.writeheader()

            for name, count in self.data.items():
                writer.writerow({
                    RANKING_COLUMN_NAME: name,
                    RANKING_COLUMN_COUNT: count
                })




