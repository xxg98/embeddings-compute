import grequests


contents = ["阿Sa是谁？", "武林外传中的无双是什么样的性格？", "《功夫》讲了什么？", "《红豆》这首歌好听吗？", "坤坤会打篮球吗？"]
req_list = []
req_size = 2

req_headers = {
    'Content-Type': 'application/json',
}
new_contents = []
for i, content in enumerate(contents):
    req_body = {
        'model': 'gpt-3.5-turbo',
        'messages': [{
            "role": "user",
            "content": content
        }],
        'temperature': 0.95,
        'stream': "false"
    }
    req_list.append(grequests.post('http://117.50.180.37:6006/v1/chat/completions',
                                   json=req_body, headers=req_headers))
    if len(req_list) == req_size:
        res_list = grequests.map(req_list)
        print("响应结果：")
        for res_index, res in enumerate(res_list):
            if res.status_code == 200:
                res_dict = res.json()
                answer = res_dict.get("choices")[0].get("message").get("content")
                print(answer)
                new_contents.append(answer)
            else:
                # 出现异常时存入原文
                new_contents.append(contents(i - (req_size - res_index - 1)))

        req_list = []
        print("req_list长度：", len(req_list))

if req_list:
    res_list = grequests.map(req_list)
    print("响应结果：")
    for res in res_list:
        if res.status_code == 200:
            res_dict = res.json()
            answer = res_dict.get("choices")[0].get("message").get("content")
            print(answer)
            new_contents.append(answer)
        else:
            # 出现异常时存入原文
            new_contents.append(contents(i - (req_size - res_index - 1)))
print("订正后的内容：", new_contents)
