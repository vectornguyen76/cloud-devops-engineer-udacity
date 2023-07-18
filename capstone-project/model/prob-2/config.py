data_path = "./phase-1/prob-2/raw_train.parquet"
model_path = "./prob2/prob_2_model.pkl"
onnx_path = "./prob2/prob_2_onnx_model.onnx"
category_index_path = "./prob2/prob_2_category_index_path.pkl"
feature_config = {
    "numeric_columns": [
        "feature2",
        "feature5",
        "feature13",
        "feature18"
    ],
    "category_columns": [
        "feature1",
        "feature3",
        "feature4",
        "feature6",
        "feature7",
        "feature8",
        "feature9",
        "feature10",
        "feature11",
        "feature12",
        "feature14",
        "feature15",
        "feature16",
        "feature17",
        "feature19",
        "feature20"
    ],
    "target_column": "label",
    "ml_type": "classification"
}