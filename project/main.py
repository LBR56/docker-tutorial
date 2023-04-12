from data.iris_dataloader import IrisDataLoader
from model.dense_model import DenseModel
from trainer.dense_trainer import DenseTrainer
from sklearn.metrics import classification_report

def main():

    print('setting data loader ...')
    data_loader = IrisDataLoader()
    
    print('setting model ...')
    model = DenseModel()
    
    print('setting trainer ...')
    trainer = DenseTrainer(data_loader.get_train(), model.model)

    print('training model ...')
    trainer.fit()

    print('predict data ...')
    y_pred = model.model.predict(data_loader.get_test()[0])

    print(classification_report(data_loader.get_test()[1], y_pred.argmax(axis=1)))

if __name__ == '__main__':
    main()