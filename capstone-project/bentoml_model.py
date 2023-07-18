from skl2onnx import update_registered_converter
from lightgbm import LGBMClassifier
from skl2onnx.common.shape_calculator import calculate_linear_classifier_output_shapes
from onnxmltools.convert.lightgbm.operator_converters.LightGbm import convert_lightgbm
from skl2onnx.common.data_types import FloatTensorType
from sklearn.pipeline import Pipeline
import pickle
import bentoml
from skl2onnx import convert_sklearn

update_registered_converter(
    LGBMClassifier, "LightGbmLGBMClassifier",
    calculate_linear_classifier_output_shapes, convert_lightgbm,
    options={'nocl': [True, False], 'zipmap': [True, False, 'columns']}
)

# Load model pkl
model1 = pickle.load(open("./model/prob_1/prob_1_model.pkl", "rb"))
model2 = pickle.load(open("./model/prob_2/prob_2_model.pkl", "rb"))

# Load pineline
pipeline1 = Pipeline([('lgbm', model1)])
pipeline2 = Pipeline([('lgbm', model2)])

# Convert model to onnx
model_onnx1 = convert_sklearn(
    pipeline1, 'pipeline_lightgbm',
    [('input', FloatTensorType([None, 16]))],
    target_opset={'': 12, 'ai.onnx.ml': 2}
)
model_onnx2 = convert_sklearn(
    pipeline2, 'pipeline_lightgbm',
    [('input', FloatTensorType([None, 20]))],
    target_opset={'': 12, 'ai.onnx.ml': 2}
)

# Create signatures
signatures = {
    "run": {"batchable": True},
    
}

# Save model onnx to bentoml model
onnx_bentoml_model_1 = bentoml.onnx.save_model("onnx_bentoml_model_1", model_onnx1, signatures=signatures)
print(f"Model onnx_bentoml_model_1 saved: {onnx_bentoml_model_1}")

onnx_bentoml_model_2 = bentoml.onnx.save_model("onnx_bentoml_model_2", model_onnx2, signatures=signatures)
print(f"Model onnx_bentoml_model_2 saved: {onnx_bentoml_model_2}")