import grequests, time


total_start_time = time.time()
total_pending_duration = 0
url = 'https://www.baidu.com'
req_list = [
    grequests.get(url),
    grequests.get(url),
    grequests.get(url),
]

start_time = time.time()
res_list = grequests.map(req_list)
end_time = time.time()
pending_duration = end_time-start_time
total_pending_duration += pending_duration
print(res_list, "耗时1：", pending_duration)

url = 'https://www.baidu.com'
req_list = [
    grequests.get(url),
    grequests.get(url),
    grequests.get(url),
]

start_time = time.time()
res_list = grequests.map(req_list)
end_time = time.time()
pending_duration = end_time-start_time
total_pending_duration += pending_duration
print(res_list, "耗时2：", pending_duration)

url = 'https://www.baidu.com'
req_list = [
    grequests.get(url),
    grequests.get(url),
    grequests.get(url),
]

start_time = time.time()
res_list = grequests.map(req_list)
end_time = time.time()
pending_duration = end_time-start_time
total_pending_duration += pending_duration
print(res_list, "耗时3：", pending_duration)

url = 'https://www.baidu.com'
req_list = [
    grequests.get(url),
    grequests.get(url),
    grequests.get(url),
]

start_time = time.time()
res_list = grequests.map(req_list)
end_time = time.time()
pending_duration = end_time-start_time
total_pending_duration += pending_duration
print(res_list, "耗时4：", pending_duration)

url = 'https://www.baidu.com'
req_list = [
    grequests.get(url),
    grequests.get(url),
    grequests.get(url),
]

start_time = time.time()
res_list = grequests.map(req_list)
end_time = time.time()
pending_duration = end_time-start_time
total_pending_duration += pending_duration
print(res_list, "耗时5：", pending_duration)

total_end_time = time.time()
# 可以得出结论：多个grequests.map互相是串行的
print("总耗时：", total_end_time-total_start_time, "累积耗时：", total_pending_duration)
