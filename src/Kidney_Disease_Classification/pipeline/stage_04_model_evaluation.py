from src.Kidney_Disease_Classification.config.configuration import ConfigurationManager
from src.Kidney_Disease_Classification.components.model_evaluation import Evaluation
from src.Kidney_Disease_Classification import logger



STAGE_NAME = "Evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass



    def main(self):
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            evaluation = Evaluation(config = model_evaluation_config)
            evaluation.evaluation()
            evaluation.save_score()
            evaluation.log_into_mlfow()


if __name__ == "__main__":
     
    try :
        logger.info("f>>>>>>>>>{STAGE_NAME} is started<<<<<<<<<<<<")

        model_evaliuation_pipeline = ModelEvaluationPipeline()
        model_evaliuation_pipeline.main()

        logger.info(f">>>>>>>>>>{STAGE_NAME} is completed /n/n X===========================X")

    except Exception as e:
        logger.info(e)
        raise e
    