import abc

class SortingStrategy(abc.ABC):
    @abc.abstractmethod
    def sort(self, data):
        pass

class BubbleSortStrategy(SortingStrategy):
    def sort(self, data):
        print("Sorted data with bubble sort")
        return sorted(data)

class QuickSortStrategy(SortingStrategy):
    def sort(self, data):
        print("Sorted data with quick sort")
        return sorted(data)

class Context:
    def __init__(self, strategy:SortingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy:SortingStrategy):
        self.strategy = strategy

    def do_smth_wih_strategy(self, data):
        self.strategy.sort(data)

data_to_sort = [1, 2, 3, 5, 4, 56, 8, 9, 7]

context = Context(QuickSortStrategy())
print(context.do_smth_wih_strategy(data_to_sort))

print(f"Change strategy to Bubble")
context.set_strategy(BubbleSortStrategy())
print(context.do_smth_wih_strategy(data_to_sort))