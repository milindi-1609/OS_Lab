from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import numpy as np
import time
import matplotlib.pyplot as plt
from urllib.request import urlopen


def visualize_features(results, title):
    start, stop = np.array(results).T
    plt.barh(range(len(start)), stop, left=start)
    plt.grid(axis='x')
    plt.ylabel('Tasks')
    plt.xlabel('Seconds')
    plt.title(title)
    name = title+'.jpg'
    plt.savefig(name, dpi=300)
    print(name)
    plt.show()
    return stop[-1]-start[0]


def multithreading(func, args, workers):
    begin_time = time.time()
    with ThreadPoolExecutor(max_workers=workers) as executor:
        res = executor.map(func, args, [begin_time for i in range(len(args))])
    return list(res)


def multiprocessing(func, args, workers):
    begin_time = time.time()
    with ProcessPoolExecutor(max_workers=workers) as executor:
        res = executor.map(func, args, [begin_time for i in range(len(args))])
    return list(res)


def download(url, base):
    start = time.time()
    try:
        resp = urlopen(url)
    except Exception as e:
        print('Error %s' % e)
    stop = time.time() - base
    return start, stop


N = 16
URL = 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf'
urls = [URL for i in range(N)]


if __name__ == '__main__':
    visualize_features(multithreading(download, urls, 1), '1 Thread')
    visualize_features(multithreading(download, urls, 2), '2 Threads')
    visualize_features(multithreading(download, urls, 4), '4 Threads')
    visualize_features(multiprocessing(download, urls, 1), '1 Process')
    visualize_features(multiprocessing(download, urls, 2), '2 Processes')
    visualize_features(multiprocessing(download, urls, 4), '4 Processes')
