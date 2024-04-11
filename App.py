# import libraries
#import joblib
import streamlit as st

#Define the functions and variables
with open('svc_model.pk1', 'rb') as model:
    classifier=joblib.load(model)

def predictor(sepal_Length, sepal_width, petal_Length,petal_width):
    global classifier
    prediction= classifier.predict([[sepal_Length, sepal_width, petal_Length,petal_width ]])
    if prediction == 0:
        return 'satosa'
    elif prediction ==1:
        return 'versicolor'
    else:
        return 'virginica'
    
def main():
    st.title('Iris classification app')
    # Body
    sepal_length=st.number_input('Sepal Length')
    sepal_width=st.number_input('Sepal Width')
    petal_length=st.number_input('Petal Length')
    petal_Width=st.number_input('petal Width')
# Predict
    if st.button('Predict'):
        prediction=predictor(sepal_length, sepal_width, petal_length, petal_Width)
        st.success(f'The flower is an iris {prediction}')

if __name__=="__main__":
    main()
   
         
