

class UndoService:
    def __init__(self):
        self._history = []
        self._index = -1

    @property
    def index(self):
        return self._index

    @property
    def history(self):
        return self._history

    def record(self, operation):
        self._history = self._history[0:self._index + 1]

        self._history.append(operation)
        self._index += 1

    def undo(self):

        self._history[self._index].undo()
        self._index -= 1

    def redo(self):

        self._index += 1
        self._history[self._index].redo()


class CascadedOperation:

    def __init__(self, undo_list, redo_list):
        self._undo_list = undo_list
        self._redo_list = redo_list

    def undo(self):
        for oper in self._undo_list:
            oper()

    def redo(self):
        for oper in self._redo_list:
            oper()


class Operation:

    def __init__(self, undo_function, redo_function):
        self._undo_function = undo_function
        self._redo_function = redo_function

    def undo(self):
        self._undo_function()

    def redo(self):
        self._redo_function()


class FunctionCall:

    def __init__(self, function_ref, *function_params):
        self._function_ref = function_ref
        self._function_params = function_params

    def call(self):
        return self._function_ref(*self._function_params)

    def __call__(self):
        return self.call()
