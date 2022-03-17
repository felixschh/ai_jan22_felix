import numpy    as np
from numpy.testing._private.utils import decorate_methods
import pandas   as pd
import seaborn  as sb
import matplotlib.pyplot as plt
import sklearn  as skl
import time

from sklearn import pipeline      # Pipeline
from sklearn import preprocessing # OrdinalEncoder, LabelEncoder
from sklearn import impute
from sklearn import compose
from sklearn import model_selection # train_test_split
from sklearn import metrics         # accuracy_score, balanced_accuracy_score, plot_confusion_matrix
from sklearn import set_config

from sklearn.tree          import DecisionTreeRegressor
from sklearn.ensemble      import RandomForestRegressor
from sklearn.ensemble      import ExtraTreesRegressor
from sklearn.ensemble      import AdaBoostRegressor
from sklearn.ensemble      import GradientBoostingRegressor
from xgboost               import XGBRegressor
from lightgbm              import LGBMRegressor
from catboost              import CatBoostRegressor

data = pd.read_csv('data_enhancement.csv')
# print(data)

"""taking the days, months and years out of timestamp and dropping timestamp column"""
data['year'] = data['timestamp'].apply(lambda row: row[:4])
data['month'] = data['timestamp'].apply(lambda row: row.split('-')[2][:2])
data['hour'] = data['timestamp'].apply(lambda row: row.split(':')[0][-2:])
data.drop('timestamp', axis=1, inplace=True)

def feature_enhancement(data):
    #copy dataframe
    df = data

    for season in data['season'].unique():
        seasonal_data = df[df['season'] == season]
        hum_mean = seasonal_data['hum'].mean()
        wind_speed_mean = seasonal_data['wind_speed'].mean()
        t1_mean = seasonal_data['t1'].mean()
        t2_mean = seasonal_data['t2'].mean()
        
        for i in df[df['season'] == season].index:
            if np.random.randint(2) == 1:
                df['hum'].values[i] += hum_mean/10
            else:
                df['hum'].values[i] -= hum_mean/10
                
            if np.random.randint(2) == 1:
                df['wind_speed'].values[i] += wind_speed_mean/10
            else:
                df['wind_speed'].values[i] -= wind_speed_mean/10
                
            if np.random.randint(2) == 1:
                df['t1'].values[i] += t1_mean/10
            else:
                df['t1'].values[i] -= t1_mean/10
                
            if np.random.randint(2) == 1:
                df['t2'].values[i] += t2_mean/10
            else:
                df['t2'].values[i] -= t2_mean/10

    return df



print(data.head(3))
gen = feature_enhancement(data)
print(gen.head(3) )

#print(gen.shape)

#final_data = data
y = data['cnt']
x = data.drop(['cnt'], axis=1)



#print(data.shape)




cat_vars = ['season','is_weekend','is_holiday','year','month','weather_code']
num_vars = ['t1','t2','hum','wind_speed']


x_train, x_val, y_train, y_val = model_selection.train_test_split(x, y,
                                    test_size=0.2,
                                    random_state=0  # Recommended for reproducibility
                                )



extra_sample = gen.sample(gen.shape[0] // 3)
x_train = pd.concat([x_train, extra_sample.drop(['cnt'], axis=1 ) ])
y_train = pd.concat([y_train, extra_sample['cnt'] ])


transformer = preprocessing.PowerTransformer()
y_train = transformer.fit_transform(y_train.values.reshape(-1,1))
y_val = transformer.transform(y_val.values.reshape(-1,1))



rang = abs(y_train.max()) + abs(y_train.min())

num_4_treeModels = pipeline.Pipeline(steps=[
    ('imputer', impute.SimpleImputer(strategy='constant', fill_value=-9999)),
])

cat_4_treeModels = pipeline.Pipeline(steps=[
    ('imputer', impute.SimpleImputer(strategy='constant', fill_value='missing')),
    ('ordinal', preprocessing.OrdinalEncoder()) # handle_unknown='ignore' ONLY IN VERSION 0.24
])

tree_prepro = compose.ColumnTransformer(transformers=[
    ('num', num_4_treeModels, num_vars),
    ('cat', cat_4_treeModels, cat_vars),
], remainder='drop') # Drop other vars not specified in num_vars or cat_vars

tree_classifiers = {
  "Decision Tree": DecisionTreeRegressor(),
  "Extra Trees":   ExtraTreesRegressor(n_estimators=100),
  "Random Forest": RandomForestRegressor(n_estimators=100),
  "AdaBoost":      AdaBoostRegressor(n_estimators=100),
  "Skl GBM":       GradientBoostingRegressor(n_estimators=100),
  "XGBoost":       XGBRegressor(n_estimators=100),
  "LightGBM":      LGBMRegressor(n_estimators=100),
  "CatBoost":      CatBoostRegressor(n_estimators=100),
}
### END SOLUTIONv

tree_classifiers = {name: pipeline.make_pipeline(tree_prepro, model) for name, model in tree_classifiers.items()}

results = pd.DataFrame({'Model': [], 'MSE': [], 'MAB': [], " % error": [], 'Time': []})

for model_name, model in tree_classifiers.items():
    
    start_time = time.time()
    model.fit(x_train, y_train)
    total_time = time.time() - start_time
        
    pred = model.predict(x_val)
    
    results = results.append({"Model":    model_name,
                              "MSE": metrics.mean_squared_error(y_val, pred),
                              "MAB": metrics.mean_absolute_error(y_val, pred),
                              " % error": metrics.mean_squared_error(y_val, pred) / rang,
                              "Time":     total_time},
                              ignore_index=True)
### END SOLUTION


results_ord = results.sort_values(by=['MSE'], ascending=True, ignore_index=True)
results_ord.index += 1 
results_ord.style.bar(subset=['MSE', 'MAE'], vmin=0, vmax=100, color='#5fba7d')

print(results_ord)


print(y_train.max())
print(y_train.min())
print(y_val[3])
print(tree_classifiers['Random Forest'].predict(x_val)[3])