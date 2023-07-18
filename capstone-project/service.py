from pydantic import BaseModel
from data_processor import DataProcessorProblem1, DataProcessorProblem2
from model.prob_1 import config as cfg1
from model.prob_2 import config as cfg2
from bentoml.io import JSON
import bentoml
import pandas as pd
from typing import Optional

# Declare input
class DataInput(BaseModel):
    id: str
    rows: list
    columns: list
    
class DataOutput(BaseModel):
    id: Optional[str]
    predictions: Optional[list]
    drift: Optional[int]

def process_data1(data: DataInput):
    raw_df = pd.DataFrame(data.rows, columns=data.columns)
    category_index1 = DataProcessorProblem1.load_category_index(cfg1.category_index_path)
    feature_df, feature_columns = DataProcessorProblem1.apply_process_data(raw_df, cfg1, category_index1)
    features = feature_df[feature_columns]
    return features

def process_data2(data: DataInput):
    raw_df = pd.DataFrame(data.rows, columns=data.columns)
    category_index2 = DataProcessorProblem2.load_category_index(cfg2.category_index_path)
    feature_df, feature_columns = DataProcessorProblem2.apply_process_data(raw_df, cfg2, category_index2)
    features = feature_df[feature_columns]
    return features

# Load model bentoml
runner1 = bentoml.onnx.get("onnx_bentoml_model_1:latest").to_runner(max_batch_size=150000)
runner2 = bentoml.onnx.get("onnx_bentoml_model_2:latest").to_runner(max_batch_size=150000)

bentoml_service = bentoml.Service("bentoml_service", runners= [runner1, runner2])

# API model 1
@bentoml_service.api(
    input=JSON(pydantic_model=DataInput),
    output=JSON(pydantic_model=DataOutput)
)
async def classify1(data_input: DataInput):
    onnx_predictions = await runner1.run.async_run(process_data1(data_input))
    preds = [pred_proba[1] for pred_proba in list(onnx_predictions)[1]]
    
    return DataOutput(
        id=data_input.id,
        predictions=preds,
        drift=0
    )

# API model 2
@bentoml_service.api(
    input=JSON(pydantic_model=DataInput),
    output=JSON(pydantic_model=DataOutput)
)
async def classify2(data_input: DataInput):
    onnx_predictions = await runner2.run.async_run(process_data2(data_input))
    preds = [pred_proba[1] for pred_proba in list(onnx_predictions)[1]]
    
    return DataOutput(
        id=data_input.id,
        predictions=preds,
        drift=0
    )