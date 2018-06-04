import multiprocessing
import signal

from tqdm import tqdm


class TqdmBar:
    tqdm = tqdm
    total = None
    items = None
    desc = ''

    def process_item(self, item):
        """
        Operation to perform on a single item
        """
        raise NotImplementedError()

    def run(self, position=0):
        for item in self.tqdm(
                self.items,
                total=self.total,
                desc=self.desc,
                position=position):
            self.process_item(item)


class MultiBar:
    tqdm = tqdm

    def __init__(self, tqdmbar_list, threads, total=None, desc='Actions'):
        """
        :param tqdmpbar_list: list[TqdmBar]
        :param threads: int
        :param total: int
        """
        self.list = tqdmbar_list
        self.threads = threads
        self.total = total
        self.desc = desc

    def run(self):
            original_sigint_handler = signal.signal(signal.SIGINT, signal.SIG_IGN)
            pool = multiprocessing.Pool(processes=self.threads)
            signal.signal(signal.SIGINT, original_sigint_handler)

            try:
                pool_generator = pool.imap_unordered(self.worker, self.list)
                for response in self.tqdm(pool_generator,
                                          total=self.total,
                                          desc=self.desc, position=0):
                    pass
            except KeyboardInterrupt:
                pool.terminate()
            else:
                pool.close()
            pool.join()

    def worker(self, group_item):
        current = multiprocessing.current_process()
        position = current._identity[0]

        group_item.run(position=position)
