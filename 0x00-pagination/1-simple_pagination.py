#!/usr/bin/env python3
"""server class to paginate a database
"""

import csv
from typing import List
from math import ceil


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
        """Returns a specific page from the dataset.
        Args:
            page: The page number to retrieve.
            page_size: The number of rows per page.
        Returns:
            List of rows representing the requested page.
        """
        assert isinstance(page, int) and isinstance(page_size, int), \
            "Page and page_size must be integers"
        assert page > 0 and page_size > 0, \
            "Page and page_size must be greater than 0"

        def index_range(page, page_size):
            start_index = (page - 1) * page_size
            end_index = page * page_size

            return start_index, end_index

        dataset = self.dataset()
        total_rows = len(dataset)
        total_pages = ceil(total_rows / page_size)

        start_index, end_index = index_range(page, page_size)

        if start_index > total_rows or page > total_pages:
            return []

        return dataset[start_index:end_index]
