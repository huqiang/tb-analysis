import requests
import json
import time
import simplejson

headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0'
}

startingPage = 252
pageSize = 20
counter = (startingPage - 1)*pageSize
totalPage = 1000
outputFile = open("reviews.txt", "a")

base_url = 'https://rate.taobao.com/feedRateList.htm?auctionNumId=574183760823&pageSize=' + str(pageSize)

for i in range(startingPage, totalPage+1, 1):
    print('Page: {}'.format(i))
    url = base_url + '&currentPageNum=%s' % str(i)
    # print(url)
    tb_req = requests.get(url, headers=headers).text[3:-2]
    print(tb_req)

    tb_dict = simplejson.loads(tb_req)
    # print(tb_dict)
    print(tb_dict['comments'][0]['auction']['sku'].encode('utf-8'))

    tb_json = json.dumps(tb_dict)
    #print(type(tb_json))

    # print(tb_json)
    review_j = json.loads(tb_json)
    for p in range(0, pageSize, 1):
      counter += 1
      print('{}\t{}\t{}\n'.format(counter, review_j['comments'][p]['auction']['sku'].encode('utf-8'), review_j['comments'][p]['content'].encode('utf-8')))
      outputFile.write('{}\t{}\t{}\n'.format(counter, review_j['comments'][p]['auction']['sku'].encode('utf-8'), review_j['comments'][p]['content'].encode('utf-8')))
      print('Added: {}'.format(counter))

    time.sleep(60)

outputFile.close()