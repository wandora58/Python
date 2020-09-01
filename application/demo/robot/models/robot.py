
from robot.models import ranking
from robot.views import console


DEFAULT_ROBOT_NAME = 'Roboko'


class Robot(object):

    def __init__(self, name=DEFAULT_ROBOT_NAME, user_name=''):
        self.name = name
        self.user_name = user_name

    def hello(self):

        # hello.txt をテンプレートとして user_name を標準出力する
        while True:
            template = console.get_template('hello.txt')
            user_name = input(template.substitute({
                'robot_name': self.name}))

            if user_name:
                self.user_name = user_name
                break


class RestaurantRobot(Robot):

    def __init__(self):

        # 親クラスの __init__ 関数を実行
        super().__init__()
        self.ranking_model = ranking.RankingModel()


    # hello 関数を実行していない場合のデコレータ
    def _hello_decorator(func):
        def wrapper(self):
            if not self.user_name:
                self.hello()
            return func(self)
        return wrapper


    # 店を推薦する関数
    @_hello_decorator
    def recommend_restaurant(self):

        # 一番人気な店を取得
        new_recommend_restaurant = self.ranking_model.get_most_popular()

        # 一番人気な店がない = まだ csv に何も書き込まれいない場合は None を返す
        if not new_recommend_restaurant:
            return None

        # 推薦する店を will_recommend_restaurants と置く
        will_recommend_restaurants = [new_recommend_restaurant]

        # reccomend.txt をテンプレートとして is_yes を標準出力する
        while True:
            template = console.get_template('recommend.txt')
            is_yes = input(template.substitute({
                'restaurant': new_recommend_restaurant
            }))

            # 標準出力が y or yes ならループ終了
            if is_yes.lower() == 'y' or is_yes.lower() == 'yes':
                break

            # 標準出力が n or no なら次に人気の店を取得
            # すでに推薦した店は not_list に置いて次は推薦しない
            if is_yes.lower() == 'n' or is_yes.lower() == 'no':
                new_recommend_restaurant = self.ranking_model.get_most_popular(
                    not_list=will_recommend_restaurants)
                if not new_recommend_restaurant:
                    break
                will_recommend_restaurants.append(new_recommend_restaurant)


    # 好きな店を聞く関数
    @_hello_decorator
    def ask_user_favorite(self):
        # question.txt をテンプレートとして restrant を標準出力する
        while True:
            template = console.get_template('question.txt')
            restaurant = input(template.substitute({
                'user_name': self.user_name,
            }))

            # 店の Count をインクリメントする
            if restaurant:
                self.ranking_model.increment(restaurant)
                break


    @_hello_decorator
    def thank_you(self):
        template = console.get_template('goodbye.txt')
        print(template.substitute({
            'robot_name': self.name,
            'user_name': self.user_name,
        }))










