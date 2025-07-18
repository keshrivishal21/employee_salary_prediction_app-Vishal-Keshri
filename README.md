
# 💼 Employee Salary Classification App

This is a Machine Learning-based web application built using **Streamlit** that predicts whether an employee earns more than $50K/year or not based on input attributes like age, education, occupation, and more.

---

## 🚀 Features

- Predict salary class: `<=50K` or `>50K`
- Modern and user-friendly UI
- Takes input via sliders and dropdowns
- Built using:
  - Scikit-learn (for training models)
  - Streamlit (for interactive web UI)
  - Pandas and Joblib (for data handling & saving model)

---

## 📦 Dependencies

Install the necessary packages:

```bash
pip install -r requirements.txt
```

---

## 🧠 Model Training

The machine learning models are trained using:

- Logistic Regression
- Random Forest
- Gradient Boosting

The best model is selected based on accuracy and saved using:

```python
joblib.dump(best_model, "best_model.pkl")
```

---

## 📂 File Structure

```
employee_salary_prediction/
│
├── app.py                  # Streamlit web app
├── best_model.pkl          # Trained ML model
├── requirements.txt        # Python dependencies
├── README.md               # Project description
└── data/                   # (Optional) Raw or processed dataset
```

---

## ▶️ Running the App

To start the web app locally:

```bash
streamlit run app.py
```

Open your browser and go to: [http://localhost:8501](http://localhost:8501)

---

## ☁️ Deployment (Streamlit Cloud)

1. Push this project to a GitHub repo.
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your GitHub and deploy the repo.
4. Set `app.py` as the main entry point.

---

## 👨‍💻 Author

- **Vishal Keshri**  
  MCA Student | Web & ML Enthusiast

---

## 📝 License

This project is open source and free to use.
