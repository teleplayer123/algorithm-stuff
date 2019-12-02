from random import randrange

class Tree(object):

    def __init__(self, data, max_depth=1, min_size=1, n_folds=1):
        self.data = data
        self.max_depth = max_depth
        self.min_size = min_size
        self.n_folds = n_folds

    def partition(self, index, value, data):
        left, right = [], []
        for row in data:
            if row[index] < value:
                left.append(row)
            else:
                right.append(row)
        return left, right

    def split_var(self, data):
        classes = set([row[-1] for row in data])
        index, value, score, groups = 0, 0, max(max(self.data))**2, None
        for i in range(len(data[0])-1):
            for row in data:
                gs = self.partition(i, row[i], data)
                gini = self.gini_index(gs, classes)
                if gini < score:
                    index, value, score, groups = i, row[i], gini, gs
        return {"index": index, "value": value, "groups": groups}

    def gini_index(self, groups, classes):
        gini = 0
        nstances = sum([len(group) for group in groups])
        for group in groups:
            size = len(group)
            if size == 0:
                continue
            score = 0
            for val in classes:
                p = [row[-1] for row in group].count(val) / size
                score += p**2
            gini += (1 - score) * (size / nstances)
        return gini

    def terminal_node(self, data):
        res = [row[-1] for row in data]
        return max(set(res), key=res.count)

    def split(self, node, max_depth, min_size, depth):
        left, right = node["groups"]
        del(node["groups"])
        if not left or not right:
            node["left"] = node["right"] = self.terminal_node(left + right)
            return
        if depth >= max_depth:
            node["left"], node["right"] = self.terminal_node(left), self.terminal_node(right)
            return
        if len(left) < min_size:
            node["left"] = self.terminal_node(left)
        else:
            node["left"] = self.split_var(left)
            self.split(node["left"], max_depth, min_size, depth+1)
        if len(right) <= min_size:
            node["right"] = self.terminal_node(right)
        else:
            node["right"] = self.split_var(right)
            self.split(node["right"], max_depth, min_size, depth+1)

    def build_tree(self, data):
        root = self.split_var(data)
        self.split(root, self.max_depth, self.min_size, 1)
        return root

    def print_tree(self, node, depth=0):
        if isinstance(node, dict):
            print(depth * " ", f"[{node['index'] + 1}]", f"[{node['value']}]")
            self.print_tree(node["left"], depth+1)
            self.print_tree(node["right"], depth+1)
        else:
            print(depth * " ", f"[{node}]")

    def predict(self, node, row):
        if row[node["index"]] < node["value"]:
            if isinstance(node["left"], dict):
                return self.predict(node["left"], row)
            else:
                return node["left"]
        else:
            if isinstance(node["right"], dict):
                return self.predict(node["right"], row)
            else:
                return node["right"]

    def accuracy_percentage(self, actual, predicted):
        score = 0.0
        for i in range(len(actual)):
            if actual[i] == predicted[i]:
                score += 1
        accuracy = score / float(len(actual)) * 100.0
        return accuracy

    def cross_validation(self, data, n_folds):
        assert self.n_folds < len(data), "amount of folds must be less than or equal to sum of rows in data"
        split_set = []
        data_copy = list(data)
        fold_size = int(len(data) / n_folds)
        for _ in range(n_folds):
            fold = []
            while len(fold) < fold_size:
                index = randrange(len(data_copy))
                i = data_copy.pop(index)
                fold.append(i)
            split_set.append(fold)
        return split_set

    def decision_tree(self, train, test):
        predictions = []
        node = self.build_tree(train)
        for row in test:
            predicted = self.predict(node, row)
            predictions.append(predicted)
        return predictions    

    def train(self):
        folds = self.cross_validation(self.data, self.n_folds)
        scores = []
        for fold in folds:
            train = list(folds)
            train.remove(fold)
            train = sum(train, [])
            test = []
            for row in fold:
                row_copy = list(row)
                row_copy[-1] = None
                test.append(row_copy)
            predicted = self.decision_tree(train, test)
            actual = [row[-1] for row in fold]
            score = self.accuracy_percentage(actual, predicted)
            scores.append(score)
        return scores