#!/usr/bin/env python3
"""
"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Takes 2 integer arguments and returns a tuple of size two
    containing the start and end index corresponding to the range of
    indexes to return in a list for those pagination parameters
    Args:
        page (int): page number to return (pages are 1-indexed)
        page_size (int): number of items per page
    Return:
        tuple(start_index, end_index)
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Takes 2 integer arguments and returns requested page from the dataset
        Args:
            page (int): required page number. must be a positive integer
            page_size (int): number of records per page. must be a +ve integer
        Return:
            list of lists containing required data from the dataset
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        dataset = self.dataset()
        try:
            index = index_range(page, page_size)
            return dataset[index[0]:index[1]]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Take 2 int argumetns and returns a dictionary containing the following
        key-value pairs:
            page_size: the length of the returned dataset
            page: the current page number
            data: the dataset page
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: total number of pages in the dataset as an integer

        Args:
            page(int): requested page
            page_size(int): number of records per page
        """
        dataset = self.dataset()
        data_length = len(dataset)
        data = self.get_page(page, page_size)
        response = {}
        response['page_size'] = len(data)
        response['page'] = page
        response['data'] = data
        total_pages = math.ceil(data_length / page_size)
        if page + 1 < total_pages:
            response['next_page'] = page + 1
        else:
            response['next_page'] = None
        if page - 1 > 1:
            response['prev_page'] = page - 1
        else:
            response['prev_page'] = None
        response['total_pages'] = total_pages

        return response
