data_path = "./data/prob_1/raw_train.parquet"
model_path = "./model/prob_1/prob_1_model.pkl"
onnx_path = "./model/prob_1/prob_1_onnx_model.onnx"
category_index_path = "./model/prob_1/prob_1_category_index_path.pkl"
feature_config = {
    "numeric_columns": [
        "feature3",
        "feature4",
        "feature5",
        "feature6",
        "feature7",
        "feature8",
        "feature9",
        "feature10",
        "feature11",
        "feature12",
        "feature13",
        "feature14",
        "feature15",
        "feature16"
    ],
    "category_columns": [
        "feature2",
        "feature1"
    ],
    "target_column": "label",
    "ml_type": "classification"
}