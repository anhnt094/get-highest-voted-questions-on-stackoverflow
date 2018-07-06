import argparse
import json
import requests


__doc__ = 'https://api.stackexchange.com/docs/'

api_url = 'https://api.stackexchange.com/2.2'


def get_highest_voted_questions_by_tag(N, tag):
    '''
    Return a dictionary contains N highest voted questions
    by tag on StackOverFlow

    :param N:   N questions to get
    :param tag: tag on Stack Over Flow
    :rtype: dict:
    '''
    url = api_url + '/questions?tagged={}&pagesize={}'\
                    '&order=desc&sort=votes&site=stackoverflow'.format(tag, N)
    response = requests.get(url)

    return json.loads(response.text)


def main():
    parser = argparse.ArgumentParser(description='Get highest voted questions'
                                                 'by tag on Stack Over Flow')
    parser.add_argument('N', type=int, help='number of questions')
    parser.add_argument('tag', help='tag of questions')
    args = parser.parse_args()

    questions = get_highest_voted_questions_by_tag(args.N, args.tag)

    for i, question in enumerate(questions['items']):
        print('{}. {}   -   Link: {}'.format(i+1, question['title'],
                                             question['link']))


if __name__ == '__main__':
    main()
