#!/usr/bin/env python3
"""Simple Pagination"""
import csv
from typing import List, Tuple


def calculate_index_range(page, page_size):
    """Calculate the start and end index for a specified page and page size."""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class BabyNamesServer:
    """Server class to handle pagination for a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def fetch_dataset(self) -> List[List]:
        """Fetch and cache the dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve the specified page of baby names """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = calculate_index_range(page, page_size)

        dataset = self.fetch_dataset()
        return dataset[start_index:end_index]

