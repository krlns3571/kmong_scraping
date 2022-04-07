import datetime
import json

import requests

headers = {
    'authority': 'cdn-gql-prod2.class101.net',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'apollographql-client-name': 'web-prod',
    'x-auid': '2c06f0ef-ad28-459c-ae31-c95dd7a29092',
    'accept-language': 'ko',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'accept': '*/*',
    'environment': 'WEB',
    'x-transaction-id': 'b2697186-9ea1-4fb8-b6d4-815fe034f6da',
    'apollographql-operation-type': 'query',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://class101.net',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://class101.net/',
    'cookie': 'auid=2c06f0ef-ad28-459c-ae31-c95dd7a29092; _hackle_hid=64de051b-624c-46ef-a128-e35811a7cfee; ajs_anonymous_id=%223eb2f4b6-c59e-4879-8739-82e9b820ddd4%22; ab.storage.deviceId.2b3f474c-7aee-41a1-b6f9-c6be442dd067=%7B%22g%22%3A%22e2a7015b-4f2c-4c86-2424-031375ddaa3d%22%2C%22c%22%3A1646196232095%2C%22l%22%3A1646196232095%7D; _ga=GA1.2.2141157774.1646196232; _gid=GA1.2.1195301944.1646196232; ch-veil-id=09f6c9c3-d803-4a93-9bee-6001d5af468b; _gcl_au=1.1.324252291.1646196232; _gcl_aw=GCL.1646269009.CjwKCAiAyPyQBhB6EiwAFUuakt3bN_e5fICDFJ63uulHjPVBq8or_U0SetxNY7j38amMRTynyZXFVhoCBMIQAvD_BwE; _gac_UA-64561335-27=1.1646269010.CjwKCAiAyPyQBhB6EiwAFUuakt3bN_e5fICDFJ63uulHjPVBq8or_U0SetxNY7j38amMRTynyZXFVhoCBMIQAvD_BwE; cto_bundle=cOh8uF9YJTJGblBMN1hLJTJGWk90MVpLNnMzQW9kaHIxdFJ1QkVrbkk3JTJCcXBySCUyRiUyRnY5UnNBZGZUbkxrVFRLT3hYZll1RnV6c3dYTDBNaXlsNUdLVGtXaW5WRXJhbWF4JTJCOXhIMSUyRkslMkZucmVVTXpIWXdzcmZoU3ZBSXNBRDBxUWxob0xZM2FLWUVxQiUyQm8zJTJGNXNsNGFYVXAyeDRaM2d1dyUzRCUzRA; ch-session-4864=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZXMiLCJrZXkiOiI0ODY0LTYyMWVmNjA4MTZkYjY4NWY3NzliIiwiaWF0IjoxNjQ2Mjg5MTY5LCJleHAiOjE2NDg4ODExNjl9.-_HnZXIOSn0kTB34g54UU3bSdJPW8ixsnCF-fKJZOVk; ab.storage.sessionId.2b3f474c-7aee-41a1-b6f9-c6be442dd067=%7B%22g%22%3A%2280dafb6b-e7aa-c6df-9b8c-33f9bf324d86%22%2C%22e%22%3A1646290967294%2C%22c%22%3A1646287901302%2C%22l%22%3A1646289167294%7D',
}
product_id = 'kdQYceM6ZiZcoxtu3y5O'
json_data = [
    {
        'operationName': 'PostList',
        'variables': {
            'preFilter': {
                'productId': f'{product_id}',
                'excludeCheerMessages': True,
            },
            'offset': 0,
            'limit': 10,
        },
        'query': 'query PostList($preFilter: PrePostFilter!, $limit: Int, $offset: Int, $sort: [PrePostSorter!]) {\n  posts(prePostFilter: $preFilter, limit: $limit, offset: $offset, sort: $sort) {\n    ...PostSummary\n    __typename\n  }\n  postsCount(preFilter: $preFilter)\n}\n\nfragment PostSummary on Post {\n  _id\n  firestoreId\n  blindAt\n  createdAt\n  photoUrl\n  videoUUID\n  audioUUID\n  title\n  content\n  translatedContent\n  languageCode\n  userId\n  likedCount\n  type\n  important\n  missionId\n  disagreedCommentNotiUserIds\n  user {\n    _id\n    firestoreId\n    name\n    nickName\n    photoUrl\n    createdAt\n    __typename\n  }\n  files {\n    fileID\n    fileName\n    extension\n    __typename\n  }\n  __typename\n}\n',
    },
]

res = requests.post('https://cdn-gql-prod2.class101.net/graphql', headers=headers, json=json_data)

offset = json.loads(res.text)[0]['data']['postsCount'] -1

json_data = [
    {
        'operationName': 'PostList',
        'variables': {
            'preFilter': {
                'productId': f'{product_id}',
                'excludeCheerMessages': True,
            },
            'offset': int(f'{offset}'),
            'limit': 10,
        },
        'query': 'query PostList($preFilter: PrePostFilter!, $limit: Int, $offset: Int, $sort: [PrePostSorter!]) {\n  posts(prePostFilter: $preFilter, limit: $limit, offset: $offset, sort: $sort) {\n    ...PostSummary\n    __typename\n  }\n  postsCount(preFilter: $preFilter)\n}\n\nfragment PostSummary on Post {\n  _id\n  firestoreId\n  blindAt\n  createdAt\n  photoUrl\n  videoUUID\n  audioUUID\n  title\n  content\n  translatedContent\n  languageCode\n  userId\n  likedCount\n  type\n  important\n  missionId\n  disagreedCommentNotiUserIds\n  user {\n    _id\n    firestoreId\n    name\n    nickName\n    photoUrl\n    createdAt\n    __typename\n  }\n  files {\n    fileID\n    fileName\n    extension\n    __typename\n  }\n  __typename\n}\n',
    },
]

res = requests.post('https://cdn-gql-prod2.class101.net/graphql', headers=headers, json=json_data)
datetime.datetime.strptime(json.loads(res.text)[0]['data']['posts'][-1]['createdAt'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d %H:%M:%S')
