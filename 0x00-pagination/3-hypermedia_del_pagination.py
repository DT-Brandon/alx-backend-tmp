#!/usr/bin/env python3

"""
This code defines the Server class and its methods to handle datasets.
"""

from typing import List, Dict
import csv


class Server:
    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Returns the dataset, loading it from the CSV file if necessary.
        """
        if self.__dataset is None:
            with open("Popular_Baby_Names.csv") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Returns the indexed dataset, truncating it to 1000 rows if necessary.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = \
                {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a subset of the indexed dataset based on the given index.
        """
        assert 0 <= index < len(self.indexed_dataset()), \
            "Index is out of range"

        dataset = self.indexed_dataset()
        data = [dataset[i] for i in range(index, index + page_size)]
        next_index = index + page_size

        return {'index': index, 'data': data,
                'page_size': page_size, 'next_index': next_index}
