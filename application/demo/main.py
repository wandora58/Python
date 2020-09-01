from robot.controller import conversation

def main():

    conversation.talk_about_restaurant()

    # robot = restrantrobot()
    # robot.introduce()
    #
    # if not os.path.exists('demo.csv'):
    #     with open('demo.csv', 'w') as csv_file:
    #         fieldnames = ['Name', 'Count']
    #         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #         writer.writeheader()
    #
    # else:
    #     with open('demo.csv', 'r') as csv_file:
    #         reader = csv.DictReader(csv_file)
    #         dic = {}
    #         for row in reader:
    #             dic[row['Name']] = row['Count']
    #
    #         for key in dic.keys():
    #             if robot.reccomend(key):
    #                 break
    #
    #         restrant = robot.question().title()
    #
    #         if restrant in dic:
    #             cnt = int(dic[restrant])
    #             cnt += 1
    #             dic[restrant] = cnt
    #         else:
    #             dic[restrant] = 1
    #
    #         dic = dict(sorted(dic.items()), key = lambda x : x[1])
    #         del dic['key']
    #
    #         with open('demo.csv', 'w') as csv_file:
    #             fieldnames = ['Name', 'Count']
    #             writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #             writer.writeheader()
    #             for name, cnt in dic.items():
    #                 writer.writerow({'Name': name, 'Count': cnt})
    #
    #         robot.goodbye()

if __name__ == '__main__':
    main()
