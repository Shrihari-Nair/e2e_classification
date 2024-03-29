from generic_classifier import logger
from generic_classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from generic_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from generic_classifier.pipeline.stage_03_training import ModelTrainingPipeline
from generic_classifier.pipeline.stage_04_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Prepare base model"
try:
   logger.info("*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   obj = PrepareBaseModelTrainingPipeline()
   obj.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
   logger.exception(e)
   raise e


STAGE_NAME = "Training"
try:
   logger.info("*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   obj = ModelTrainingPipeline()
   obj.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
   logger.exception(e)
   raise e


STAGE_NAME = "Evaluation stage"
try:
   logger.info("*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   obj = EvaluationPipeline()
   obj.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
   logger.exception(e)
   raise e
