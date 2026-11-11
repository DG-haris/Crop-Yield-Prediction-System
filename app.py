import streamlit as st
import pandas as pd
import joblib


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Crop Yield Prediction System",
    page_icon="🌾",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>
        .main-title {
            font-size: 42px;
            font-weight: 700;
            text-align: center;
            margin-bottom: 5px;
        }

        .subtitle {
            text-align: center;
            font-size: 18px;
            margin-bottom: 30px;
        }

        .section-title {
            font-size: 24px;
            font-weight: 600;
            margin-top: 20px;
            margin-bottom: 10px;
        }

        .prediction-box {
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            margin-top: 20px;
            margin-bottom: 20px;
        }

        .prediction-value {
            font-size: 38px;
            font-weight: 700;
        }

        .prediction-label {
            font-size: 18px;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():
    return joblib.load("crop_yield_model.pkl")


model = load_model()


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🌾 Crop Yield Prediction System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Machine Learning based prediction of agricultural crop yield'
    '</div>',
    unsafe_allow_html=True
)

st.info(
    "Enter soil, weather, agricultural and crop information "
    "to estimate expected crop yield."
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("📊 Model Information")

    st.write("**Algorithm:** Gradient Boosting Regressor")

    st.write("**Prediction Target:**")
    st.write("Crop Yield (tonnes/hectare)")

    st.divider()

    st.write("**Validation Performance**")

    st.metric("R²", "0.686")
    st.metric("MAE", "0.516 t/ha")
    st.metric("RMSE", "0.641 t/ha")

    st.divider()

    st.caption(
        "Performance values are from the field-grouped "
        "validation set used during model development."
    )


# =========================================================
# CROP INFORMATION
# =========================================================

st.markdown(
    '<div class="section-title">🌱 Crop Information</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    crop_type = st.selectbox(
        "Crop Type",
        ["Wheat", "Barley", "Corn", "Rice", "Soybean"]
    )

with col2:
    region = st.selectbox(
        "Region",
        ["North", "South", "East", "West", "Central"]
    )

with col3:
    season = st.selectbox(
        "Season",
        ["Spring", "Summer", "Autumn"]
    )


# =========================================================
# SOIL CONDITIONS
# =========================================================

st.markdown(
    '<div class="section-title">🪴 Soil Conditions</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    soil_ph = st.number_input(
        "Soil pH",
        min_value=4.5,
        max_value=8.5,
        value=6.5,
        step=0.1
    )

with col2:
    soil_moisture = st.number_input(
        "Soil Moisture",
        min_value=10.0,
        max_value=50.0,
        value=30.0,
        step=0.1
    )

with col3:
    nitrogen_content = st.number_input(
        "Nitrogen Content",
        min_value=0.5,
        max_value=3.0,
        value=1.7,
        step=0.01
    )


col1, col2, col3 = st.columns(3)

with col1:
    phosphorus_content = st.number_input(
        "Phosphorus Content",
        min_value=0.2,
        max_value=1.5,
        value=0.85,
        step=0.01
    )

with col2:
    potassium_content = st.number_input(
        "Potassium Content",
        min_value=0.5,
        max_value=2.0,
        value=1.25,
        step=0.01
    )

with col3:
    irrigation_frequency = st.number_input(
        "Irrigation Frequency",
        min_value=1,
        max_value=6,
        value=4,
        step=1
    )


# =========================================================
# WEATHER CONDITIONS
# =========================================================

st.markdown(
    '<div class="section-title">🌦️ Weather Conditions</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    avg_temperature = st.number_input(
        "Average Temperature (°C)",
        min_value=10.0,
        max_value=35.0,
        value=22.5,
        step=0.1
    )

with col2:
    total_rainfall = st.number_input(
        "Total Rainfall",
        min_value=100.0,
        max_value=1200.0,
        value=650.0,
        step=1.0
    )

with col3:
    sunlight_hours = st.number_input(
        "Sunlight Hours",
        min_value=1000.0,
        max_value=3000.0,
        value=2000.0,
        step=1.0
    )


# =========================================================
# AGRICULTURAL INPUTS
# =========================================================

st.markdown(
    '<div class="section-title">🚜 Agricultural Inputs</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    fertilizer_amount = st.number_input(
        "Fertilizer Amount",
        min_value=50.0,
        max_value=300.0,
        value=175.0,
        step=1.0
    )

with col2:
    pesticide_usage = st.number_input(
        "Pesticide Usage",
        min_value=0.0,
        max_value=15.0,
        value=7.5,
        step=0.1
    )

with col3:

    month_names = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    harvest_month_name = st.selectbox(
        "Harvest Month",
        list(month_names.keys()),
        index=2
    )

    harvest_month = month_names[harvest_month_name]


# =========================================================
# PREDICTION BUTTON
# =========================================================

st.divider()

predict_button = st.button(
    "🌾 Predict Crop Yield",
    use_container_width=True
)


# =========================================================
# PREDICTION
# =========================================================

if predict_button:

    input_data = pd.DataFrame([{
        "soil_ph": soil_ph,
        "soil_moisture": soil_moisture,
        "avg_temperature": avg_temperature,
        "total_rainfall": total_rainfall,
        "fertilizer_amount": fertilizer_amount,
        "pesticide_usage": pesticide_usage,
        "sunlight_hours": sunlight_hours,
        "nitrogen_content": nitrogen_content,
        "phosphorus_content": phosphorus_content,
        "potassium_content": potassium_content,
        "irrigation_frequency": irrigation_frequency,
        "crop_type": crop_type,
        "region": region,
        "season": season,
        "harvest_month": harvest_month
    }])

    prediction = model.predict(input_data)[0]

    # -----------------------------------------------------
    # Prediction Result
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">🎯 Prediction Result</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="prediction-box">
            <div class="prediction-label">
                Estimated Crop Yield
            </div>
            <div class="prediction-value">
                {prediction:.2f} t/ha
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.success(
        f"The model estimates a crop yield of "
        f"**{prediction:.2f} tonnes per hectare**."
    )

    # -----------------------------------------------------
    # Input Summary
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">📋 Input Summary</div>',
        unsafe_allow_html=True
    )

    summary_data = pd.DataFrame({
        "Parameter": [
            "Crop Type",
            "Region",
            "Season",
            "Harvest Month",
            "Soil pH",
            "Soil Moisture",
            "Average Temperature",
            "Total Rainfall",
            "Fertilizer Amount",
            "Pesticide Usage",
            "Sunlight Hours",
            "Nitrogen Content",
            "Phosphorus Content",
            "Potassium Content",
            "Irrigation Frequency"
        ],
        "Value": [
            crop_type,
            region,
            season,
            harvest_month_name,
            f"{soil_ph:.2f}",
            f"{soil_moisture:.2f}",
            f"{avg_temperature:.2f} °C",
            f"{total_rainfall:.2f}",
            f"{fertilizer_amount:.2f}",
            f"{pesticide_usage:.2f}",
            f"{sunlight_hours:.2f}",
            f"{nitrogen_content:.2f}",
            f"{phosphorus_content:.2f}",
            f"{potassium_content:.2f}",
            irrigation_frequency
        ]
    })

    st.dataframe(
        summary_data,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Crop Yield Prediction System | Machine Learning College Project"
)