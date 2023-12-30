#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination"""
import csv
import math
from typing import List, Dict


class BabyNamesServer:
    """Server class for paginating a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def fetch_dataset(self) -> List[List]:
        """Fetch and cache the dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_dataset(self) -> Dict[int, List]:
        """Index the dataset by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.fetch_dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hypermedia_info_by_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Retrieve hypermedia information for a given index and page_size."""
        assert index is None or (isinstance(index, int) and index >= 0)
        assert isinstance(page_size, int) and page_size > 0

        indexed_data = self.index_dataset()

        if index is None:
            index = 0
        if index >= len(indexed_data):
            raise AssertionError("Index out of range")

        data_page = [indexed_data[i] for i in range(index, index + page_size) if i in indexed_data]

        next_index = index + page_size if index + page_size < len(indexed_data) else None
        hyper_data = {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data_page,
        }

        return hyper_data

