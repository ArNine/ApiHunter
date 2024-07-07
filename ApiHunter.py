import requests
import queue
import threading

class ApiHunter:

    def __int__(self, request_pool_size, thread_num, func):
        self.request_pool_size = request_pool_size
        self.thread_num = thread_num
        self.request_pool = queue.Queue(request_pool_size)
        self.func = func
        self.thread_pool = {}

    def produce(self, body):
        self.request_pool.put(body)

    def _request(self) -> requests.models.Response:
        body = self.request_pool.get()
        # TODO 根据请求的body判断是否在缓存数据库中

        # TODO 如果在缓存数据库中，直接返回结果，如果不在，发起http请求, 返回response
        res = requests.get(url='')

        # TODO 将获取的结果存入到数据库中
        extracted_data = self.func(res)

        # TODO 保存到buffer缓冲区，批量写入数据库

        return extracted_data

    def start(self):
        for i in range(self.thread_num):
            thread = threading.Thread(target=self._request, args=(self, ))
            thread.start()
            self.thread_pool[thread.name] = thread





