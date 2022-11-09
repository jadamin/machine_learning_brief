import pandas as pd
from sklearn.model_selection import train_test_split
import streamlit as st
import pickle

pickle_in = open("modelRid.pkl", "rb")
model = pickle.load(pickle_in)



st.header("Bienvenue ")


dfcode = [
    "98001", "98002", "98003", "98004", "98005", "98006", "98007", "98008", "98010", "98011", "98014", "98019",
    "98022", "98023", "98024", "98027", "98028", "98029", "98030", "98031", "98032", "98033", "98034", "98038",
    "98039", "98040", "98042", "98045", "98052", "98053", "98055", "98056", "98058", "98059", "98065", "98070",
    "98072", "98074", "98075", "98077", "98092", "98102", "98103", "98105", "98106", "98107", "98108", "98109",
    "98112", "98115", "98116", "98117", "98118", "98119", "98122", "98125", "98126", "98133", "98136", "98144",
    "98146", "98148", "98155", "98166", "98168", "98177", "98178", "98188", "98198", "98199"]
    

zipcode = st.selectbox("Veuillez entrez le code pastale",dfcode)
bedrooms = st.number_input("nb des chambres",min_value=0,max_value=11)
bathrooms = st.number_input("baths",min_value=0.00,max_value=8.00)
floors = st.number_input("floors",min_value=1.,max_value=4.,step=0.5)
waterfront = st.radio("waterfront",("yes","no"))
if waterfront == "yes":
    waterfront =1
else:
    waterfront=0

view = st.number_input("view",min_value=0,max_value=4)
conditions = st.number_input("conditions",min_value=0,max_value=5)
grade = st.number_input("grade",min_value=3,max_value=13)
yr_built = st.number_input('year construction', min_value=1900, max_value=2015)
yr_renovated = st.number_input('year renovation', min_value=0, max_value=2015)
surface_lot = st.number_input("surface_lot",min_value=0.000000, max_value=1300.000000)
surface_base = st.number_input("surface_base",min_value=0.000000, max_value=1300.000000)
surface_above = st.number_input("surface_above",min_value=0.000000, max_value=1300.000000)
surface_liv = st.number_input("habitable surface",min_value=0.000000, max_value=1300.000000)

if st.button('valider'):
    point_en_cours = {
        "bedrooms": bedrooms,
        'bathrooms': bathrooms,
        "floors": floors,
        "waterfront": waterfront,
        "view": view,
        "conditions":conditions,
        "grade": grade,
        "yr_built": yr_built,
        "yr_renovated": yr_renovated,
        "surface_liv": surface_liv,
        'surface_above': surface_above,
        'surface_base': surface_base,
        'surface_lot': surface_lot,
        
        
    }
    for code in dfcode: 
        point_en_cours[code]=0

    point_en_cours[zipcode]=1
    point_en_cours = [point_en_cours[cle] for cle in point_en_cours]
    st.success(model.predict([point_en_cours]))