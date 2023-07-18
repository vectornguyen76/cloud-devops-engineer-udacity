import pandas as pd
import pickle

class DataProcessor:
    @staticmethod
    def build_category_features(data, categorical_cols=None):
        if categorical_cols is None:
            categorical_cols = []
        category_index = {}
        if len(categorical_cols) == 0:
            return data, category_index
        
        df = data.copy()
        for col in categorical_cols:
            df[col] = df[col].astype("category")
            category_index[col] = df[col].cat.categories
            df[col] = df[col].cat.codes
        return df, category_index
    
    @staticmethod
    def apply_category_features(data, categorical_cols=None, category_index=None):
        if categorical_cols is None:
            return data
        
        df = data.copy()
        for col in categorical_cols:
            df[col] = df[col].astype("category")
            df[col] = pd.Categorical(df[col], categories=category_index[col]).codes
        return df
    
    @staticmethod
    def load_category_index(category_index_path: str):
        return pickle.load(open(category_index_path, "rb"))
    
class DataProcessorProblem1:
    @staticmethod
    def build_category_features(data, categorical_cols=None):
        category_index = {}
        if categorical_cols is None:
            return data, category_index
        
        df = data.copy()
        for col in categorical_cols:
            df[col] = df[col].astype("category")
            category_index[col] = df[col].cat.categories
            df[col] = df[col].cat.codes
        return df, category_index
    
    @staticmethod
    def apply_category_features(data, categorical_cols=None, category_index=None):
        if categorical_cols is None:
            return data
        
        df = data.copy()
        for col in categorical_cols:
            df[col] = df[col].astype("category")
            df[col] = pd.Categorical(df[col], categories=category_index[col]).codes
        return df
    
    @staticmethod
    def load_category_index(category_index_path: str):
        return pickle.load(open(category_index_path, "rb"))
    
    @staticmethod
    def save_category_index(category_index, category_index_path):
        pickle.dump(category_index, open(category_index_path, "wb"))

    @staticmethod
    def process_null_category_value(df, categorical_cols):
        for col in categorical_cols:
            most_frequent_value = df[col].mode()[0]
            df[col].fillna(most_frequent_value, inplace=True)
        return df
    
    @staticmethod
    def process_data(df, cfg):
        categorical_cols = cfg.feature_config["category_columns"]
        # df = DataProcessorProblem1.process_null_category_value(df, categorical_cols=categorical_cols)
        processed_df, category_index = DataProcessorProblem1.build_category_features(df, categorical_cols=categorical_cols)
        DataProcessorProblem1.save_category_index(category_index, cfg.category_index_path)
        feature_columns = cfg.feature_config["category_columns"] + cfg.feature_config["numeric_columns"]
        return processed_df, feature_columns

    @staticmethod
    def apply_process_data(df, cfg, category_index):
        categorical_cols = cfg.feature_config["category_columns"]
        # df = DataProcessorProblem1.process_null_category_value(df, categorical_cols)
        processed_df = DataProcessorProblem1.apply_category_features(df, categorical_cols, category_index)
        feature_columns = cfg.feature_config["category_columns"] + cfg.feature_config["numeric_columns"]
        return processed_df, feature_columns

    
class DataProcessorProblem2:
    @staticmethod
    def build_category_features(data, categorical_cols=None):
        category_index = {}
        if categorical_cols is None:
            return data, category_index
        
        df = data.copy()
        for col in categorical_cols:
            df[col] = df[col].astype("category")
            category_index[col] = df[col].cat.categories
            df[col] = df[col].cat.codes
        return df, category_index
    
    @staticmethod
    def apply_category_features(data, categorical_cols=None, category_index=None):
        if categorical_cols is None:
            return data
        
        df = data.copy()
        for col in categorical_cols:
            df[col] = df[col].astype("category")
            df[col] = pd.Categorical(df[col], categories=category_index[col]).codes
        return df
    
    @staticmethod
    def load_category_index(category_index_path: str):
        return pickle.load(open(category_index_path, "rb"))
    
    @staticmethod
    def save_category_index(category_index, category_index_path):
        pickle.dump(category_index, open(category_index_path, "wb"))

    @staticmethod
    def process_null_category_value(df, categorical_cols):
        for col in categorical_cols:
            most_frequent_value = df[col].mode()[0]
            df[col].fillna(most_frequent_value, inplace=True)
        return df
    
    @staticmethod
    def process_data(df, cfg):
        categorical_cols = cfg.feature_config["category_columns"]
        # df = DataProcessorProblem2.process_null_category_value(df, categorical_cols=categorical_cols)
        processed_df, category_index = DataProcessorProblem2.build_category_features(df, categorical_cols=categorical_cols)
        DataProcessorProblem2.save_category_index(category_index, cfg.category_index_path)
        feature_columns = cfg.feature_config["category_columns"] + cfg.feature_config["numeric_columns"]
        return processed_df, feature_columns
    
    @staticmethod
    def apply_process_data(df, cfg, category_index):
        categorical_cols = cfg.feature_config["category_columns"]
        # df = DataProcessorProblem2.process_null_category_value(df, categorical_cols)
        processed_df = DataProcessorProblem2.apply_category_features(df, categorical_cols, category_index)
        feature_columns = cfg.feature_config["category_columns"] + cfg.feature_config["numeric_columns"]
        return processed_df, feature_columns