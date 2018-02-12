import random

class Data:
    def __init__(self, filename, count=1000):
        self.labels = []
        self.features = []
        file = open(filename, "r")
        for i in range(count):
            line = file.readline().strip()
            #print(line)
            parts = line.split("\t")
            #print(parts)
            if len(parts) == 2:
                label = parts[0]
                features_str = parts[1].split(" ")
                features = [int(item) for item in features_str]
                self.labels.append(int(label))
                self.features.append(features)
        file.close()
    
    def get_sample(self, count = 10):
        sample_labels = []
        sample_features = []
        for i in range(count):
            index = random.randint(0, len(self.labels)-1)
            sample_labels.append(self.labels[index])
            sample_features.append(self.features[index])
        return sample_labels, sample_features
    
    def get_all(self):
        return self.labels, self.features

if __name__ == "__main__":
    data = Data("data/toy_problem_2_test.txt")
    labels, features = data.get_sample()
    print(str(labels))
    print(str(features))