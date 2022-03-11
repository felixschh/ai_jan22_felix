import data_handler as dh

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor

x_train, x_test, y_train, y_test = dh.get_data("insurance.csv")

def train_models(x_train, y_train):
    
    dt = DecisionTreeRegressor(max_depth=5, random_state=42)
    dt = dt.fit(x_train, y_train)

    rf = RandomForestRegressor(n_estimators=50, random_state=42)
    rf = rf.fit(x_train, y_train)

    gbt = GradientBoostingRegressor(random_state=42)
    gbt = gbt.fit(x_train, y_train)

    return dt, rf, gbt

