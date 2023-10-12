from mlProject.config.configuration import ConfigurationManager
from mlProject.entity.config_entity import DataTransformationConfig
from mlProject.components.data_transformation import DataTransformation
from mlProject import logger
from pathlib import Path


STAGE_NAME = "Data Transformation Stage"


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(slef):
        try:
            with open(Path("artifacts\data_validation\status.txt"), "r") as f:
                status = f.read().split(" ")[-1]
            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config = data_transformation_config)
                data_transformation.train_test_spliting()
            else:
                raise Exception("The data schema provided is not valid")
        except Exception as e:
            print(e)
                
if __name__=="__main__":
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>stage {STAGE_NAME} has completed \n\nx=================x")
        
    except Exception as e:
        raise e
    
        