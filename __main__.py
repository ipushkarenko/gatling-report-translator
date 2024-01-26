from gtl_json_adapter import create_dtos_from_files
from single_sample_handler import create_dataframe_from_dtos

if __name__ == '__main__':
    create_dataframe_from_dtos(create_dtos_from_files(['stats.json']))
