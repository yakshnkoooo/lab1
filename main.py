def knn_predict(X_train, y_train, X_test, k=5):
    predictions = []
    for test_point in X_test:
        distances = []
        for i, train_point in enumerate(X_train):
            dist = np.sqrt(np.sum((test_point - train_point) ** 2))
            distances.append((dist, y_train[i]))

        distances.sort(key=lambda x: x[0])
        k_nearest = distances[:k]
        # Голосование большинством
        k_labels = [label for _, label in k_nearest]
        most_common = Counter(k_labels).most_common(1)[0][0]
        predictions.append(most_common)

    return predictions
