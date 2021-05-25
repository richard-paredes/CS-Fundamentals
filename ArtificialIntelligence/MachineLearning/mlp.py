from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.model_selection import cross_validate
from sklearn import datasets
from pandas import read_csv
from statistics import mean

def print_metrics(model_name, cv_metrics):
    print("***************************************\n")
    print(f"Metrics for {model_name}")
    for key in sorted(cv_metrics.keys()):
        print(f"{key}: {cv_metrics[key]}")
    print("***************************************\n")

def main():
    
    data = read_csv("heart_failure_clinical_records_dataset.csv", header=0)
    x = data[['age', 'anaemia', 'creatinine_phosphokinase', 'diabetes', 'ejection_fraction', 'high_blood_pressure', 'platelets', 'serum_creatinine', 'serum_sodium', 'sex', 'smoking', 'time']]
    y = data['DEATH_EVENT']
    
    svc_linear = SVC(kernel='linear')
    svc_rbf = SVC(kernel='rbf')
    mlp_relu = MLPClassifier(activation='relu')
    mlp_tanh = MLPClassifier(activation='tanh')

    svc_linear_cv = cross_validate(svc_linear, x, y, cv=10, return_train_score=True, return_estimator=True, verbose=1, n_jobs=-1)
    print_metrics("Support Vector Machine Classifier with Linear Kernel", svc_linear_cv)
    svc_rbf_cv = cross_validate(svc_rbf, x, y, cv=10, return_train_score=True, return_estimator=True, verbose=1, n_jobs=-1)
    print_metrics("Support Vector Machine Classifier with Radial Basis Function Kernel", svc_rbf_cv)
    mlp_relu_cv = cross_validate(mlp_relu, x, y, cv=10, return_train_score=True, return_estimator=True, verbose=1, n_jobs=-1)
    print_metrics("Multi-layer Perceptron Classifier with Rectified Linear Unit Activation Function", mlp_relu_cv)
    mlp_tanh_cv = cross_validate(mlp_tanh, x, y, cv=10, return_train_score=True, return_estimator=True, verbose=1, n_jobs=-1)
    print_metrics("Multi-layer Perceptron Classifier with Hyperbolic Tangent Activation Function", mlp_tanh_cv)

main()