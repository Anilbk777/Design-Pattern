from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")

class ModelTrainer(ABC):
    def train_pipeline(self, data_path: str) -> None:
        try:
            self._load_data(data_path)
            self._preprocess_data()
            self.train_model()
            self.evaluate_model()
            self.save_model()
        except Exception as e:
            logging.error(f"[Error] Pipeline failed: {e}")
            raise

    # Common steps
    def _load_data(self, path: str) -> None:
        logging.info(f"[Common] Loading dataset from {path}")

    def _preprocess_data(self) -> None:
        logging.info("[Common] Splitting into train/test and normalizing")

    @abstractmethod
    def train_model(self) -> None:
        pass

    @abstractmethod
    def evaluate_model(self) -> None:
        pass

    def save_model(self) -> None:
        logging.info("[Common] Saving model to disk as default format")


class NeuralNetworkTrainer(ModelTrainer):
    def train_model(self) -> None:
        logging.info("[NeuralNet] Training Neural Network for 100 epochs")

    def evaluate_model(self) -> None:
        logging.info("[NeuralNet] Evaluating accuracy and loss")

    def save_model(self) -> None:
        logging.info("[NeuralNet] Saving weights to .h5 file")
