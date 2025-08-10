class TODOListModel:
    def __init__(self):
        self._tasks = []

    @property
    def tasks(self):
        return self._tasks

    def create_task(self, task: str):
        new_tasks = {"title": task, "is_completed": False}
        self.tasks.append(new_tasks)

    def complete_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["is_completed"] = True

    def remove_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)


class TODOListView:
    def display_tasks(self, tasks:list):
        print("ToDoList\n")
        if not tasks:
            print("Empty list")
        else:
            for task in tasks:
                # ️️] | [ ] | Title of task
                if task["is_completed"]:
                    status = "[✔️]"
                else:
                    status = "[ ]"
                print(f"{status} | {task["title"]}", end="\n===========================\n")
            print("===========================")

    def display_message(self, message:str):
        print(f"Message: {message}")


class TODOListController:
    def __init__(self, model:TODOListModel, view:TODOListView):
        self._model = model
        self._view = view

    def update_view(self):
        self._view.display_tasks(self._model.tasks)

    def add_new_task(self, task_name:str):
        self._model.create_task(task_name)
        self._view.display_message("Added task")
        self.update_view()

    def complete_existing_task(self, task_index):
        self._model.complete_task(task_index-1)
        self._view.display_message(f"Completed task {task_index}.")
        self.update_view()

    def remove_existing_task(self, task_index):
        self._model.remove_task(task_index-1)
        self._view.display_message(f"Removed task {task_index}.")
        self.update_view()

if __name__ == "__main__":
    todo_model = TODOListModel()
    todo_view = TODOListView()
    todo_controller = TODOListController(todo_model, todo_view)
    todo_controller.update_view()
    todo_controller.add_new_task("Buy bread")
    todo_controller.add_new_task("Have rest")
    todo_controller.complete_existing_task(2)
    todo_controller.remove_existing_task(1)