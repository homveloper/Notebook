from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
data = ["a", "a", "b", "c", "c"]
#encoder.fit(data)
#encoded_data = encoder.transform(data)
encoded_data = encoder.fit_transform(data)
print(encoded_data)
labeled_data = encoder.inverse_transform(encoded_data)
print(labeled_data)


import sklearn.preprocessing as prp
import numpy as np

encoder = prp.LabelEncoder()
data = [1,1,2,2,3]
encoded_data = encoder.fit_transform(data)
encoder = prp.OneHotEncoder()
onehot_encoded_data = encoder.fit_transform(encoded_data.reshape(-1,1))
print(onehot_encoded_data.toarray())
